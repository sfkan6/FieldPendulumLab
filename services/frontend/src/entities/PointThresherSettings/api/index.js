import { getPointThresherHSVRanges, getPointThresherOptions, setPointThresherHSVRanges, setPointThresherOptions } from '@/shared/api'
import { PointThresherSettings } from '../model'

export const getPointThresherSettings = async (pointName) => {
  const HSVRanges = await getPointThresherHSVRanges(pointName)
  const options = await getPointThresherOptions(pointName)
  return new PointThresherSettings(HSVRanges, options)
}


export const setPointThresherSettings = async (pointThresherSettings, pointName) => {
  await setPointThresherHSVRanges(pointThresherSettings.HSVRanges, pointName)
  await setPointThresherOptions(pointThresherSettings.options, pointName)
  return await getPointThresherSettings(pointName)
}
