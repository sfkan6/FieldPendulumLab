

export const setBase64Image = (base64Image, imageSrc) => {
  imageSrc.value = "data:image/png;base64," + base64Image
}


export const getSum = (array) => array.reduce((b, a) => b + a, 0);

export const getAbsAverage = (array) => array.reduce((a, b) => Math.abs(a) + Math.abs(b)) / array.length;

export const getAbsMaxValue = (values) => Math.max.apply(null, values.map(Math.abs))

export const getAverageArray = (arrays) => {
let averageArray = []
  for (let i = 0; i < arrays[0].length; i++) {
    let array = []
    for (let j = 0; j < arrays.length; j++) {
      array.push(arrays[j][i])
    }
    averageArray.push(getAbsAverage(array))
  }
  return averageArray
}
