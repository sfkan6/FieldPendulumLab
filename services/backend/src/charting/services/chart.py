from abc import abstractmethod
from copy import deepcopy
from typing import Self
from .charting import ChartBuilder
from .approximation import Approximator
import base64



class Chart:

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def set_config(self, title: str = 'title', xlabel: str = 'xlabel', ylabel: str = 'ylabel', **kwargs) -> None:
        pass

    @abstractmethod
    def make_all_data(self, point_data: dict) -> None:
        pass

    @abstractmethod
    def make_data(self, xdata: list, ydata: list, color: str, label: str) -> None:
        pass

    @abstractmethod
    def get_base64_chart(self) -> str:
        pass
 
    @abstractmethod
    def get_clean(self) -> Self:
        pass


class DefaultChart(Chart):

    def __init__(self, chart_builder: ChartBuilder) -> None:
        self.chart_builder = chart_builder
        self.reset()

    def reset(self) -> None:
        self.chart_builder.reset()

    def set_config(self, title: str = 'title', xlabel: str = 'xlabel', ylabel: str = 'ylabel', **kwargs) -> None:
        self.chart_builder.display_labels(title, xlabel, ylabel)

    def make_all_data(self, point_data: dict) -> None:
        for label, data in point_data.items():
            xdata, ydata = self.get_float_list(data['xdata']), self.get_float_list(data['ydata'])
            self.make_data(xdata, ydata, data['color'], label)
   
    def make_data(self, xdata: list, ydata: list, color: str, label: str) -> None:
        pass
    
    def get_float_list(self, data):
        return list(map(float, data))
    
    def get_base64_chart(self) -> str:
        return base64.b64encode(self.chart_builder.get_byte_chart()).decode()

    def get_clean(self) -> Self:
        chart = deepcopy(self)
        chart.reset()
        return chart


class PointsChart(DefaultChart):
 
    def make_data(self, xdata: list, ydata: list, color: str, label: str) -> None:
        self.chart_builder.build_points(xdata, ydata, color=color, label=label)


class ApproximationChart(DefaultChart):
    
    def __init__(self, chart_builder: ChartBuilder, approximator: Approximator) -> None:
        self.approximator = approximator
        super().__init__(chart_builder)

    def make_data(self, xdata: list, ydata: list, color: str, label: str) -> None:
        self.chart_builder.build_points(xdata, ydata, color=color, label=label)
        xx, yy = self.approximator.get_by_x_y(xdata, ydata)
        self.chart_builder.build_line(list(xx), yy, color=color)
