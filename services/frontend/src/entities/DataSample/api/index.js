

const host = `http://${import.meta.env.VITE_BACKEND_HOST}/data_samples/`


export const createDataSample = async (dataType, dataSample) => {
  let params = {
    method: "POST",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(dataSample)
  }
  const url = host + `${dataType}/create`
  return await fetch(url, params)
}

export const getDataSample = async (dataType, name) => {
  const url = host + `${dataType}/${name}`
  let response = await fetch(url, {method: "GET"})
  return await response.json()
}

export const updateDataSample = async (dataType, name, dataSample) => {
  const url = host + `${dataType}/${name}`
  const params = {
    method: "PUT",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(dataSample)
  }
  let response = await fetch(url, params)
  return await response.json()
}

export const deleteDataSample = async (dataType, name) => {
  const url = host + `${dataType}/${name}`
  let response = await fetch(url, {method: "DELETE"})
  return await response.json()
}

export const downloadDataSample = async (dataType, name) => {
  const url = host + `${dataType}/${name}`
  let response = await fetch(url, {method: "GET"})
  return await response.blob()
}

