import { getColumns, getAbsMaxValue, getFrequencyByAmplitude, getFrequencyErrorByAmplitude, getQualityFactor, getQualityFactorError } from '@/shared/libs'
import { getApproximation } from '@/shared/api'
import { getDataSample } from '@/entities/DataSample/api'



export const getFrequenciesByName = async (name, k=6) => {
  const {records} = await getDataSample('amplitude_frequency', name)
  const columns = getColumns(records, 1)
  const {xdata, ydata, values, errors} = await getApproximation('amplitude_resonance_curve', {xdata: columns[1], ydata: columns[0]})
  
  const yMax = getAbsMaxValue(ydata)
  const result = ydata.filter(y => y >= yMax * 0.7)
 
  const selectedY = [result.at(0), result.at(-1), yMax]
  return selectedY.map(y => [
    getFrequencyByAmplitude(y, xdata, ydata, k), 
    getFrequencyErrorByAmplitude(y, values, errors, k),
  ])
}



export const getQualityFactorByName = async (name, k=6) => {
  const frequencies = await getFrequenciesByName(name, k)
  const columns = getColumns(frequencies, 1)

  return [
    getQualityFactor(...columns[0]).toFixed(k),
    getQualityFactorError(...columns[0], columns[1]).toFixed(6)
  ]
}
