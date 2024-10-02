
const host = `http://${import.meta.env.VITE_BACKEND_HOST}/charting/`


export const getChart = async (chartType, chartData) => {
  const url = host + chartType
  let response = await fetch(url, {
    method: "POST",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(chartData)
  })
  return await response.json()
}

export const getApproximation = async (chartType, data) => {
  const url = host + 'approximation/'+ chartType
  let response = await fetch(url, {
    method: "POST",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  return await response.json()
}
