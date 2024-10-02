import { getFrequencyByLists } from '@/shared/libs'
import { getDataSample } from '@/entities/DataSample/api'



export const getFrequencyByNames = async (names) => {
  let listsOfRecords = []
  for (const name of names) {
    const dataSample = await getDataSample("amplitude", name)
    listsOfRecords.push(dataSample.records)
  }
  return getFrequencyByLists(listsOfRecords)
}

