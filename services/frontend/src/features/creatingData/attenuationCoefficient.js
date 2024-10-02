import { getAttenuationCoefficientByLists } from '@/shared/libs/attenuationCoefficient'
import { getDataSample } from '@/entities/DataSample/api'


export const getAttenuationCoefficientByNames = async (names) => {
  let listsOfRecords = []
  for (const name of names) {
    const dataSample = await getDataSample("amplitude", name)
    listsOfRecords.push(dataSample.records)
  }
  return getAttenuationCoefficientByLists(listsOfRecords)
}




