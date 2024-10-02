<script setup>
import { Button, Menu, CollapsibleContent, ResizableImage } from '@/shared/ui'
import { getThresholdImage, getFinishedImage, WebSocketClient } from '@/shared/api'
import { setBase64Image } from '@/shared/libs'
import { SettingHSVRanges, ImageStreaming, SuccessOrError } from '@/widgets'
import { getPointThresherSettings, PointThresherSettings } from '@/entities/PointThresherSettings'
import { pointsAndNames, defaultPointsAndSettings, setPointThresherSettingsByPoint } from "./config"
import { reactive, ref } from 'vue'


const getPointsAndSettings = async () => {
  let pointsAndSettings = {}

  for (const point of Object.keys(pointsAndNames)) {
    const {HSVRanges, options} = await getPointThresherSettings(pointsAndNames[point])
    pointsAndSettings[point] = new PointThresherSettings(HSVRanges, options)

  }
  return pointsAndSettings
}

const pointsAndSettings = reactive(await getPointsAndSettings())

const points = Object.keys(pointsAndSettings)
const selectedPoint = ref(points[0])
const setSelectedPoint = (newPoint) => selectedPoint.value = newPoint



const imageSrc = ref('/pendulum_of_field.jpg')
const setImage = (base64Image) => setBase64Image(base64Image, imageSrc)
const getBase64Image = () => imageSrc.value.replace('data:image/png;base64,','')

let video_client = new WebSocketClient('pendulum_of_field/image')
const startVideo = () => video_client.run(setImage);
const stopVideo = () => video_client.close()



const thresholdImageSrc = ref('/pendulum_of_field.jpg')
const setThresholdImage = (base64Image) => setBase64Image(base64Image, thresholdImageSrc)

const updateThresholdImage = async () => {
  const base64Image = getBase64Image()
  const settings = pointsAndSettings[selectedPoint.value]
  const base64ThresholdImage = await getThresholdImage(base64Image, settings.HSVRanges)
  setThresholdImage(base64ThresholdImage)
}

const updateThresholdImageWithParameters = async () => {
  const base64Image = getBase64Image()
  const settings = pointsAndSettings[selectedPoint.value]
  const base64ThresholdImage = await getFinishedImage(base64Image, settings.HSVRanges, settings.options)
  setThresholdImage(base64ThresholdImage)
}


const setDefaultSettings = () => pointsAndSettings[selectedPoint.value].setSettings(defaultPointsAndSettings[selectedPoint.value])
const savePointSettings = async () => setPointThresherSettingsByPoint(pointsAndSettings[selectedPoint.value], selectedPoint.value)

</script>

<template>
  <div class="left-part">
    <container class='stream-container'>
      <ImageStreaming :imageSrc="imageSrc">
        <div class='video-buttons'>
          <Button color='#198754' @click='startVideo'>
            Start
            <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
              <path d="M10.804 8 5 4.633v6.734zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C4.713 12.69 4 12.345 4 11.692V4.308c0-.653.713-.998 1.233-.696z"/>
            </svg>
          </Button>
          <Button color='#dc3545' @click="stopVideo">
            Stop
            <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
              <path d="M6 3.5a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-1 0V4a.5.5 0 0 1 .5-.5m4 0a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-1 0V4a.5.5 0 0 1 .5-.5"/>
            </svg>
          </Button>
        </div>
      </ImageStreaming>
    </container>

    <container class='stream-container'>
      <ImageStreaming :imageSrc="thresholdImageSrc">
        <div class='video-buttons'>
          <Button color='#5d5d5d' @click='updateThresholdImage'>
            Threshold
            <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
              <path d="M10.804 8 5 4.633v6.734zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C4.713 12.69 4 12.345 4 11.692V4.308c0-.653.713-.998 1.233-.696z"/>
            </svg>
          </Button>
          <Button color='#5d5d5d' @click="updateThresholdImageWithParameters">
            With parameters
            <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
              <path d="M8 4a.5.5 0 0 1 .5.5V6H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V7H6a.5.5 0 0 1 0-1h1.5V4.5A.5.5 0 0 1 8 4zm-2.5 6.5A.5.5 0 0 1 6 10h4a.5.5 0 0 1 0 1H6a.5.5 0 0 1-.5-.5z"/>
              <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2zm10-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1z"/>
            </svg>
          </Button>
        </div>
      </ImageStreaming>
    </container>
  </div>

  <div class="right-part">
    <container class="menu-container">
      <Menu :values="points" :selectedValue="selectedPoint" :setSelectedValue="setSelectedPoint"/>
    </container>

    <SettingHSVRanges :HSVRanges="pointsAndSettings[selectedPoint]._HSVRanges" :key="selectedPoint"/>

    <container>
      <CollapsibleContent value="Параметры улучшения изображения" class="image-enhancement-options">
        <div class="options" :key="selectedPoint">
          <div>Открытие: <input type="text" v-model="pointsAndSettings[selectedPoint]._options.open_iters"></div>
          <div>Расширение: <input type="text" v-model="pointsAndSettings[selectedPoint]._options.dilate_iters"></div>
          <div>Закрытие: <input type="text" v-model="pointsAndSettings[selectedPoint]._options.close_iters"></div>
        </div>
      </CollapsibleContent>

      <div class='buttons'>
        <Button color='#6c757d' @click='setDefaultSettings'>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M15 2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2zM0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm8.5 9.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707V11.5z"/>
          </svg>
          By default
        </Button>
        <Button color='#198754' @click='savePointSettings'>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
            <path d="M2 1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H9.5a1 1 0 0 0-1 1v7.293l2.646-2.647a.5.5 0 0 1 .708.708l-3.5 3.5a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L7.5 9.293V2a2 2 0 0 1 2-2H14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h2.5a.5.5 0 0 1 0 1z"/>
          </svg>
          Сохранить
        </Button>
      </div>
    </container>

  </div>

</template>

<style scoped lang="sass">

.video-buttons 
  margin-top: 20px
  display: flex
  flex-direction: row
  align-items: center
  justify-content: center
  flex-wrap: wrap

  button
    margin-bottom: 0 !important
    margin-top: 0 !important
  
    svg
      width: 22px !important
      margin-left: 5px


.left-part
  min-width: 450px
  max-width: calc(100% - 600px)
  display: flex
  flex-wrap: wrap
  flex-direction: row
  align-items: flex-start

  > *
    max-width: calc(100% - 80px)

.right-part
  width: 550px
  display: flex
  flex-direction: column
  flex-wrap: wrap
  align-items: stretch


.stream-container
  padding: 20px !important


.menu-container
  padding: 5px !important


.buttons 
  display: flex
  align-items: center
  justify-content: space-around
  flex-direction: row
  flex-wrap: wrap

  button
    :deep(svg)
      margin-right: 7px
      width: 18px


.image-enhancement-options
  margin-bottom: 10px

  .options
    margin-left: 20px

  .options > *
    display: flex
    flex-direction: row
    align-items: center
    flex-wrap: wrap
    justify-content: space-between
  
    width: 250px
    margin-bottom: 15px

    input
      width: 100px



</style>
