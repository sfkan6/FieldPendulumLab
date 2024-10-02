import { getAmplitudeAndFrequencyByRecords } from '@/shared/libs/amplitudeFrequency'
import { getDataSample } from '@/entities/DataSample/api'


export const getAmplitudeAndFrequencyByName = async (name) => {
  const {records} = await getDataSample('amplitude', name)
  return getAmplitudeAndFrequencyByRecords(records)
}

export const getAmplitudeFrequencies = async (names) => {
  let amplitudeFrequencies = []
  names.forEach(async name => {
    amplitudeFrequencies.push(await getAmplitudeAndFrequencyByName(name))
  })
  return amplitudeFrequencies;
}


