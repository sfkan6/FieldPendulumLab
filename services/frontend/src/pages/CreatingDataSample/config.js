import { CreatingAmplitudeSample, CreatingAmplitudeFrequencySample, 
  CreatingFrequencyPhaseShiftSample, CreatingSampleFromFile } from '@/widgets/CreatingDataSample'


export const dataTypeAndCreatingComponent = {
  'from_file': CreatingSampleFromFile,
  'amplitude': CreatingAmplitudeSample,
  'amplitude_frequency': CreatingAmplitudeFrequencySample,
  'frequency_phase_shift': CreatingFrequencyPhaseShiftSample,
}

export const getCreatingComponentByDataType = (dataType) => dataTypeAndCreatingComponent[dataType]
