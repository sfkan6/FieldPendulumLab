<script setup>
import { Button, ResizableImage } from '@/shared/ui'
import { setBase64Image, getColumns } from '@/shared/libs'
import { getChart, WebSocketClient } from '@/shared/api'
import { ImageStreaming, SuccessOrError } from '@/widgets'
import { CreatingAngleSample } from '@/widgets/CreatingDataSample'
import { onMounted, ref } from "vue"



const dataSample = ref({})
const setDataSample = (newDataSample) => dataSample.value = newDataSample


const chartImageSrc = ref("/empty_graph.png")
const setChart = (base64Image) => setBase64Image(base64Image, chartImageSrc)


const createChart = async () => {
  const columns = getColumns(dataSample.value.records, 1)
  const pointData = {
    [dataSample.value.name]: {xdata: columns[1], ydata: columns[0], color: "blue"}
  }

  const chartData = {
    title: "Зависимость угла от времени",
    xlabel: "Время, с",
    ylabel: "Угол, °",
    pointData
  }

  const base64Image = await getChart("points", chartData);
  setChart(base64Image)
}


const imageSrc = ref('/pendulum_of_field.jpg')
const setImage = (base64Image) => setBase64Image(base64Image, imageSrc)

let video_client = new WebSocketClient('pendulum_of_field/image')
const startVideo = () => video_client.run(setImage);
const stopVideo = () => video_client.close()
</script>

<template>
  <PageContentWrapper class='wrapper'>

    <SuccessOrError/>
  
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
            <RouterLink to="/settings/hsv">
              <Button color='#6c757d' class='button-link'>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
                  <path fill-rule="evenodd" d="M8.636 3.5a.5.5 0 0 0-.5-.5H1.5A1.5 1.5 0 0 0 0 4.5v10A1.5 1.5 0 0 0 1.5 16h10a1.5 1.5 0 0 0 1.5-1.5V7.864a.5.5 0 0 0-1 0V14.5a.5.5 0 0 1-.5.5h-10a.5.5 0 0 1-.5-.5v-10a.5.5 0 0 1 .5-.5h6.636a.5.5 0 0 0 .5-.5"/>
                  <path fill-rule="evenodd" d="M16 .5a.5.5 0 0 0-.5-.5h-5a.5.5 0 0 0 0 1h3.793L6.146 9.146a.5.5 0 1 0 .708.708L15 1.707V5.5a.5.5 0 0 0 1 0z"/>
                </svg>
              </Button>
            </RouterLink>
          </div>
        </ImageStreaming>

      </container>

      <container class='chart-container'>
        <ResizableImage :path="chartImageSrc" class="chart"/>
        <div class='buttons'>
          <Button color='#198754' @click='createChart'>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0M4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5z"/>
            </svg>
            Создать
          </Button>
        </div>
      </container>
    </div>
  
    <div class="right-part">
      <CreatingAngleSample :setDataSample="setDataSample"/>
    </div>

  </PageContentWrapper>
</template>

<style scoped lang="sass">

@media screen and (max-width: 900px)
  .wrapper
    align-items: center !important
    flex-direction: column !important

  .left-part
    max-width: max-content !important

.wrapper
  display: flex
  flex-direction: row
  flex-wrap: wrap
  align-items: flex-start
  justify-content: space-between

.left-part
  max-width: calc(100% - 400px)
  display: flex
  flex-wrap: wrap
  flex-direction: row
  align-items: flex-start

  > *
    max-width: calc(100% - 80px)

.right-part
  width: 400px
  display: flex
  flex-direction: column
  flex-wrap: wrap
  align-items: stretch



.stream-container
  padding: 20px !important


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

  .button-link svg
    margin-right: 2px
    margin-bottom: 3px

</style>
