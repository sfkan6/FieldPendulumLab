import { getFrequencyError } from './errors'



export const getAmplitude = (w, a, w0, b) => {
  return a / Math.sqrt((w0**2 - w**2)**2 + (2 * b * w)**2)
}

export const getFrequency = (A, a, w0, b, k=1) => {
  return Math.sqrt(-2 * b**2 + w0**2 + k * Math.sqrt(Math.abs(4 * b**2 * (b**2 - w0**2) - (a / A)**2)))
}

const getXByY = (xdata, ydata, y) => xdata.at(ydata.indexOf(y))

export const getFrequencyByAmplitude = (amplitude, frequencies, amplitudes, k=6) => parseFloat(getXByY(frequencies, amplitudes, amplitude).toFixed(k))

export const getFrequencyErrorByAmplitude = (amplitude, values, errors, k=6) => parseFloat(getFrequencyError(amplitude, ...values, [1, ...errors]).toFixed(k))


export const getQualityFactor = (leftFrequency, rightFrequency, resonantFrequency, k=6) => {
  return parseFloat((resonantFrequency / (rightFrequency - leftFrequency)).toFixed(k))
}
