import { getColumns } from '@/shared/libs'


const getXdataAndYdata = (records, step=1) => {
  const columns = getColumns(records, step=step)
  const xdata = columns[1], ydata = columns[0]
  return {xdata, ydata}
}

const getXdataAndYdataForAmplitudeCurve = (records) => getXdataAndYdata(records, 2)


export const chartsConfigData = {
  points: {
    title: "title",
    xLabel: "xlabel",
    yLabel: "ylabel",
    dataType: "angle",
    getXdataAndYdata,
  },
  amplitude_versus_time: {
    title: "Зависимость амплитуды от времени",
    xLabel: "Время, с",
    yLabel: "Амплитуда, °",
    dataType: "amplitude",
    getXdataAndYdata: getXdataAndYdataForAmplitudeCurve,
  },
  amplitude_resonance_curve: {
    title: "Амплитудно-резонансная кривая",
    xLabel: "Циклическая частота, $рад/с$",
    yLabel: "Амплитуда, °",
    dataType: "amplitude_frequency",
    getXdataAndYdata,
  },
  phase_resonance_curve: {
    title: "Фазовая резонансная кривая",
    xLabel: "Циклическая частота, $рад/с$",
    yLabel: "Сдвиг фаз, $рад$",
    dataType: "frequency_phase_shift",
    getXdataAndYdata,
  },
}


export const chartsTitles = {
  points: 'Точки',
  fading_fluctuations: 'Затухающие колебания',
  amplitude_versus_time: 'Амплитуда затухающих колебаний',
  amplitude_resonance_curve: 'Aмплитудная резонансная кривая',
  phase_resonance_curve: 'Фазовая резонансная кривая',
}


