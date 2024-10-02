import { getAbsAverage, getAbsMaxValue } from './general'

export const getPeriodsByTimes = (times) => {
  let periods = []
  for (let i = 0; i < times.length - 1; i++) {
    periods.push(times[i + 1] - times[i])
  }
  return periods;
}

export const getFrequencyByTimes = (times, n=2) => {
  const periods = getPeriodsByTimes(times)
  return (Math.PI / getAbsAverage(periods)).toFixed(n)
}


export const getAmplitudeAndFrequencyByRecords = async (records) => {
  const amplitude = getAbsMaxValue(records.map(record => record[0]))
  const frequency = getFrequencyByTimes(records.map(record => record[1]))
  return [amplitude, frequency]
}

