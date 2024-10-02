import { getAbsAverage, getAverageArray } from './general'
import { getColumns } from './splitColumns'


export const getFrequencyByLists = (listsOfRecords) => {
  const listsOfTimes = []
  for (const records of listsOfRecords) {
    const columns = getColumns(records, 2)
    listsOfTimes.push(columns[1])
  }
  const averageTimes = getAverageArray(listsOfTimes)
  return getAbsAverage(averageTimes)
}


export const getNaturalFrequency = (frequency, attenuationCoefficient) => Math.sqrt(frequency**2 + attenuationCoefficient**2)

export const getNaturalFrequencyByResonant = (resonantFrequency, attenuationCoefficient) => Math.sqrt(resonantFrequency**2 + 2 * attenuationCoefficient**2)

