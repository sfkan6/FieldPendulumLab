from fastapi import APIRouter
from .custom_charts import PointsChart, SignedPointsChart, ForcedFluctuationsChart, FadingFluctuationsChart, AmplitudeChart, PRCChart, ARCChartWithText
from .custom_approximation import AmplitudeResonanceCurveApproximator
from .services import MatplotlibChartBuilder
from .controller import ChartController, ApproximatorController


matplot_chart_builder = MatplotlibChartBuilder("", "", "", 10)

router = APIRouter(prefix="/charting")

routes = [
    ChartController("points", PointsChart(matplot_chart_builder)),
    ChartController("angle_points", SignedPointsChart(matplot_chart_builder)),
    ChartController("forced_fluctuations", ForcedFluctuationsChart(matplot_chart_builder)),
    ChartController("fading_fluctuations", FadingFluctuationsChart(matplot_chart_builder)),
    ChartController("amplitude_versus_time", AmplitudeChart(matplot_chart_builder)),
    ChartController("amplitude_resonance_curve", ARCChartWithText(matplot_chart_builder)),
    ChartController("phase_resonance_curve", PRCChart(matplot_chart_builder)),

    ApproximatorController("approximation/amplitude_resonance_curve", AmplitudeResonanceCurveApproximator()),
]

for route in routes:
    router.include_router(route.router)

