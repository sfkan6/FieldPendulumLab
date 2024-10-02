import { getAbsMaxValue, getAverageArray } from './general'
import { getColumns } from './splitColumns'


export const getAttenuationCoefficient = (amplitudes, times, maxAmplitude=0) => {
  maxAmplitude = maxAmplitude == 0 ? amplitudes[0] : maxAmplitude

  let sum1 = 0, sum2 = 0
  for (let i = 0; i < amplitudes.length; i++) {
    sum1 += times[i] * Math.log(amplitudes[i] / maxAmplitude)
    sum2 += times[i]**2
  }
  return -sum1 / sum2
}


export const getMaxAmplitude = (listsOfAmplitudes) => {
  const maxAmplitudes = []
  for (const amplitudes of listsOfAmplitudes) {
    maxAmplitudes.push(amplitudes[0])
  }
  return getAbsMaxValue(maxAmplitudes)
}

export const getAttenuationCoefficientByLists = (listsOfRecords) => {
  const listsOfAmplitudes = []
  const listsOfTimes = []

  for (const records of listsOfRecords) {
    const columns = getColumns(records, 2)
    listsOfAmplitudes.push(columns[0])
    listsOfTimes.push(columns[1])
  }
  const maxAmplitude = getMaxAmplitude(listsOfAmplitudes) 

  const averageAmplitudes = getAverageArray(listsOfAmplitudes), averageTimes = getAverageArray(listsOfTimes)
  return getAttenuationCoefficient(averageAmplitudes, averageTimes, maxAmplitude)
}


