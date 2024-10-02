from .services import Approximator
import numpy as np


class AmplitudeResonanceCurveApproximator(Approximator):

    def get_amplitude_resonance_curve(self, om, a, om0, beta):
        return a / np.sqrt((om0**2 - om**2)**2 + (2 * beta * om)**2)
    
    def __init__(self):
        super().__init__(self.get_amplitude_resonance_curve)


class ExponentialApproximator(Approximator):

    def get_exponential_curve(self, x, a, b, c):
        return a * np.exp(-b * x) + c
    
    def __init__(self):
        super().__init__(self.get_exponential_curve)


class PhaseResonanceCurveApproximator(Approximator):
 
    def get_phase_resonance_curve(self, om, om0, beta):
        psi = np.arctan(-2 * beta * om / (om0**2 - om**2))
        return psi - np.pi * (psi > 0)
    
    def __init__(self):
        super().__init__(self.get_phase_resonance_curve)
    

class FadingFluctuationsApproximator(Approximator):
    
    def get_angle(self, t, a0, b, w, f):
        return a0 * np.exp(-b * t) * np.sin(w * t + f)

    def __init__(self):
        super().__init__(self.get_angle)


class ForcedFluctuationsApproximator(Approximator):
    
    def get_angle(self, t, a0, am, b, w0, w, f, p):
        return a0 * np.exp(-b * t) * np.cos(np.sqrt(w0**2 - b**2) * t + f) + am * np.cos(w * t + p)

    def __init__(self):
        super().__init__(self.get_angle)
 
