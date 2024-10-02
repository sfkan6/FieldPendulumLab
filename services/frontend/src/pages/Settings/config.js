import { SettingHSV } from './HSV'

export const settingsTitles = {
  hsv: 'Настройка HSV диапазонов',
}

export const pathAndComponent = {
  hsv: SettingHSV,
}

export const getComponentByPath = (path) => pathAndComponent[path]
