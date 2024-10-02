import { setPointThresherSettings, PointThresherSettings } from '@/entities/PointThresherSettings'


export const pointsAndNames = {
  'Центральная': 'center',
  'Угловая': 'corner',
}

export const defaultOptions = {open_iters: 3, dilate_iters: 4, close_iters: 3}

export const defaultPointsAndSettings = {
  'Центральная': new PointThresherSettings(
    [
      [
        [40, 40, 40], 
        [90, 255, 255]
      ],
    ], structuredClone(defaultOptions)),
  'Угловая': new PointThresherSettings(
    [
      [
        [0, 150, 150], 
        [10, 255, 255],
      ],
      [
        [175, 0, 150], 
        [180, 255, 255],
      ],
    ], structuredClone(defaultOptions)),
}


export const setPointThresherSettingsByPoint = async (pointThresherSettings, point) => await setPointThresherSettings(pointThresherSettings, pointsAndNames[point])
