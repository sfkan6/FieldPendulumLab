import { createDataSample } from '@/entities/DataSample/api'
import { showSuccessNotification, showFailureNotification } from '@/widgets/SuccessOrError'



export const createDataSampleAndNotify = async (dataType, dataSample) => {
  const response = await createDataSample(dataType, dataSample)
  if (response.status == 200) {
    showSuccessNotification()
  }
  else {
    showFailureNotification()
  }
}
