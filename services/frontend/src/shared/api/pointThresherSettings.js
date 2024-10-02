const host = `http://${import.meta.env.VITE_BACKEND_HOST}/stream/`


export const getRequest = async (path) => {
  const url = host + path
  let response = await fetch(url, {method: "GET"})
  return await response.json()
}

export const getPointThresherHSVRanges = async (pointName) => await getRequest(`${pointName}_point_thresher/hsv_ranges`)
export const getPointThresherOptions = async (pointName) => await getRequest(`${pointName}_point_thresher/options`)


export const putRequest = async (body, path) => {
  const url = host + path
  let response = await fetch(url, {
    method: "PUT",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body),
  })
  return await response.json()
}

export const setPointThresherHSVRanges = async (hsv_ranges, pointName) => await putRequest({hsv_ranges}, `${pointName}_point_thresher/hsv_ranges`)
export const setPointThresherOptions = async (options, pointName) => await putRequest({options}, `${pointName}_point_thresher/options`)

