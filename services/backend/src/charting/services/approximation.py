from scipy.optimize import curve_fit
import numpy as np


class Approximator:
    
    def __init__(self, func) -> None:
        self.func = func

    def get_by_x_y(self, x, y, step=0.01):
        popt, _ = self._get_popt_and_pcov(x, y)
        x_fitted = np.arange(min(x), max(x), step)
        y_fitted = self.func(x_fitted, *popt)
        return x_fitted.tolist(), y_fitted.tolist()
 
    def get_values(self, x, y):
        popt, _ = self._get_popt_and_pcov(x, y)
        return popt.tolist()

    def get_errors_by_x_y(self, x, y):
        _, pcov = self._get_popt_and_pcov(x, y)
        return np.sqrt(np.diag(pcov)).tolist()
    
    def _get_popt_and_pcov(self, x, y):
        return curve_fit(self.func, x, y, method="lm")[:2]

