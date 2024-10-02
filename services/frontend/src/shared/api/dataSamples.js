
const host = `http://${import.meta.env.VITE_BACKEND_HOST}/data_samples/`


export const getAllNames = async (dataType) => {
  const url = host + `${dataType}/names`
  let response = await fetch(url, {method: "GET"})
  return await response.json()
}

export const getDataSamples = async (dataType) => {
  const url = host + `${dataType}/`
  let response = await fetch(url, {method: "GET"})
  return await response.json()
}

export const deleteDataSamples = async (dataType) => {
  const url = host + `${dataType}/`
  let response = await fetch(url, {method: "DELETE"})
  return await response.json()
}


export const loadTestData = async (dataType) => {
  const url = host + `${dataType}/test_data/load`
  let response = await fetch(url, {method: "PUT"})
  return await response.json()
}

export const addToTestData = async (dataType, name) => {
  const url = host + `${dataType}/test_data/${name}`
  let response = await fetch(url, {method: "POST"})
  return await response.json()
}

export const deleteFromTestData = async (dataType, name) => {
  const url = host + `${dataType}/test_data/${name}`
  let response = await fetch(url, {method: "DELETE"})
  return await response.json()
}





