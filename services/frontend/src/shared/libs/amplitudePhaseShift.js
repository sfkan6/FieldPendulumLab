
export const getPhaseShift = (frequency, naturalFrequency, attenuationCoefficient) => {
  const psi = Math.atan(-2 * attenuationCoefficient * frequency / (naturalFrequency**2 - frequency**2))
  if (psi > 0) {
    return psi - Math.PI
  }
  return psi
}

export const getPhaseShiftsByFrequencies = (frequencies, naturalFrequency, attenuationCoefficient) => {
  return frequencies.map(frequency => getPhaseShift(frequency, naturalFrequency, attenuationCoefficient))
}

export const getAmplitudePhaseShifts = async (records, naturalFrequency, attenuationCoefficient, n=4) => {
  return records.map(record => [getPhaseShift(record[1], naturalFrequency, attenuationCoefficient).toFixed(n), record[1]])
}


