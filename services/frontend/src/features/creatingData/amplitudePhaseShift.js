import { getDataSample } from '@/entities/DataSample/api'
import { getAmplitudePhaseShifts } from '@/shared/libs/amplitudePhaseShift'


export const getAmplitudePhaseShiftsByName = async (name, naturalFrequency, attenuationCoefficient, n=4) => {
  const {records} = await getDataSample("amplitude_frequency", name)
  return getAmplitudePhaseShifts(records, naturalFrequency, attenuationCoefficient, n)
}


