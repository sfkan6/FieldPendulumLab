
const host = `http://${import.meta.env.VITE_BACKEND_HOST}/stream/threshing_test/`


export const getThresholdImage = async (base64_image, hsv_ranges) => {
  const url = host + 'threshold'
  let response = await fetch(url, {
    method: "POST",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({base64_image, hsv_ranges}),
  })
  return await response.json()
}

export const getFinishedImage = async (base64_image, hsv_ranges, options) => {
  const url = host + 'finished'
  let response = await fetch(url, {
    method: "POST",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({base64_image, hsv_ranges, options}),
  })
  return await response.json()
}
