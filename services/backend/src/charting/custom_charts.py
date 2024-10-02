from math import pi
from .custom_approximation import (
    ForcedFluctuationsApproximator, 
    FadingFluctuationsApproximator, 
    ExponentialApproximator, 
    AmplitudeResonanceCurveApproximator, 
    PhaseResonanceCurveApproximator
)
from .services import ApproximationChart, PointsChart, ChartBuilder


class SignedPointsChart(PointsChart):
    
    def make_data(self, xdata: list, ydata: list, color: str, label: str) -> None:
        super().make_data(xdata, ydata, color, label)

        zx = -(max(xdata) - min(xdata)) * 0.01
        zy = (max(ydata) - min(ydata)) * 0.025
        for index in range(len(xdata)):
            self.chart_builder.build_text(xdata[index] + zx, ydata[index] + zy, str(index), color="black")


class FadingFluctuationsChart(ApproximationChart):
    
    def __init__(self, chart_builder: ChartBuilder) -> None:
        super().__init__(chart_builder, FadingFluctuationsApproximator())


class ForcedFluctuationsChart(ApproximationChart):

    def __init__(self, chart_builder: ChartBuilder) -> None:
        super().__init__(chart_builder, ForcedFluctuationsApproximator())


class AmplitudeChart(ApproximationChart):

    def __init__(self, chart_builder: ChartBuilder) -> None:
        super().__init__(chart_builder, ExponentialApproximator())


class ARCChart(ApproximationChart):

    def __init__(self, chart_builder: ChartBuilder) -> None:
        super().__init__(chart_builder, AmplitudeResonanceCurveApproximator())


class ARCChartWithText(ARCChart):
 
    def make_data(self, xdata: list, ydata: list, color: str, label: str) -> None:
        super().make_data(xdata, ydata, color, label)
        y, xf_left, xf_right, yy_max, x_yy_max = self._get_approximation_values(xdata, ydata, 0.7)
        self._make_lines(y, xf_left, xf_right, yy_max, x_yy_max, xdata[-1])
        # self._make_text(xdata[0], y, xf_left, x_yy_max, xf_right)
  
    def _get_approximation_values(self, xdata, ydata, k = 0.7):
        xx, yy = self.approximator.get_by_x_y(xdata, ydata, step=0.001)
        values = self.approximator.get_values(xdata, ydata)

        yy_max = max(yy)
        x_yy_max = xx[yy.index(yy_max)]

        yfs = [y for y in yy if y / yy_max >= k]
        xf_left, xf_right = xx[yy.index(yfs[0])], xx[yy.index(yfs[-1])]

        y = self.approximator.func(xf_left, *values)

        return y, xf_left, xf_right, yy_max, x_yy_max

    def _make_lines(self, y, xf_left, xf_right, yy_max, x_yy_max, xmax):
        self.chart_builder.vline(x=xf_left, ymin=0, ymax=y, linestyle='dashed', color='black')
        self.chart_builder.vline(x=xf_right, ymin=0, ymax=y, linestyle='dashed', color='black')
        self.chart_builder.vline(x=x_yy_max, ymin=0, ymax=yy_max, linestyle='dashed', color='black')
        self.chart_builder.hline(y=y, xmin=xf_left, xmax=xmax, linestyle='dashed', color='black', linewidth=1.25)
 
    def _make_text(self, x_text, y_text, xf_left, x_yy_max, xf_right, rounding=6, y_shift=20):
        self.chart_builder.build_text(x_text, y_text + y_shift, rf"$\omega_1 = {round(xf_left, rounding)}$", color='black', fontsize=14)
        self.chart_builder.build_text(x_text, y_text, rf"$\omega_р = {round(x_yy_max, rounding)}$", color='black', fontsize=14)
        self.chart_builder.build_text(x_text, y_text - y_shift, rf"$\omega_2 = {round(xf_right, rounding)}$", color='black', fontsize=14)


class PRCChart(ApproximationChart):

    def __init__(self, chart_builder: ChartBuilder) -> None:
        super().__init__(chart_builder, PhaseResonanceCurveApproximator())
