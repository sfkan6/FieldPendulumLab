

export const dataTypeAndName = {
  angle: 'Углы',
  amplitude: 'Амплитуды',
  amplitude_frequency: 'Амплитудные частоты',
  frequency_phase_shift: 'Фазовые сдвиги частот',
}


export const getNameByType = (dataType) => dataTypeAndName[dataType]

export const getTypeByName = (dataName) => Object.keys(dataTypeAndName).find(key => dataTypeAndName[key] == dataName)
