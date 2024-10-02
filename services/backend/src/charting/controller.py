from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse
from .services import Chart, Approximator


class ChartController:

    def __init__(self, name_of_chart_type: str, prototype_chart: Chart):
        self.name_of_chart_type = name_of_chart_type
        self.prototype_chart = prototype_chart

        self.router = APIRouter()
        self.router.add_api_route(f"/{self.name_of_chart_type}", self.get_chart, methods=["POST"])

    def get_chart(self, body=Body()):
        point_data = body.get('pointData', None)

        if not(point_data):
            return
        
        try:
            chart = self.prototype_chart.get_clean()
            chart.set_config(**body)
            chart.make_all_data(point_data)
        except:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='Unprocessable data',
            )
        return chart.get_base64_chart()


class ApproximatorController:

    def __init__(self, name_of_chart_type: str, approximator: Approximator):
        self.name_of_chart_type = name_of_chart_type
        self.approximator = approximator

        self.router = APIRouter()
        self.router.add_api_route(f"/{self.name_of_chart_type}", self.get_chart, methods=["POST"])

    def get_chart(self, body=Body()):
        xdata = self.get_float_list(body.get('xdata', []))
        ydata = self.get_float_list(body.get('ydata', []))
        
        try:
            xx, yy = self.approximator.get_by_x_y(xdata, ydata, step=0.001)
            values = self.approximator.get_values(xdata, ydata)
            errors = self.approximator.get_errors_by_x_y(xdata, ydata)
            return JSONResponse({'xdata': xx, 'ydata': yy, 'values': values, 'errors': errors})
        except:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='Unprocessable data',
            )
 
    def get_float_list(self, data):
        return list(map(float, data))

