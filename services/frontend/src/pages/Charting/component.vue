<script setup>
import { Button, DropdownListWithSelection, ResizableImage } from '@/shared/ui'
import { setBase64Image, downloadByHref } from '@/shared/libs'
import { getAllNames, getChart } from '@/shared/api'
import { getDataSample } from '@/entities/DataSample/api'
import { ref } from 'vue'


const { chartType, chartConfigData } = defineProps({
  chartType: {
    type: String,
    required: true,
  },
  chartConfigData: {
    type: Object,
    required: true,
  },
})


let title = ref(chartConfigData.title)
let xLabel = ref(chartConfigData.xLabel)
let yLabel = ref(chartConfigData.yLabel)


const dataNames = await getAllNames(chartConfigData.dataType)

const selectedNames = ref([])
const setSelectedNames = (names) => {
  selectedNames.value = names
}

const colorsOfNames = ref(Object.fromEntries(dataNames.map(name => [name, "#000000"])));


const chartImageSrc = ref("/empty_graph.png")
const setChart = (base64Image) => setBase64Image(base64Image, chartImageSrc)



const getPointData = async (dataType, getXdataAndYdata) => {
  let pointData = {}
  for (let name of selectedNames.value) {
    const dataSample = await getDataSample(dataType, name)
    const { xdata, ydata } = getXdataAndYdata(dataSample.records)
    pointData[name] = {xdata, ydata, color: colorsOfNames.value[name]}
  }
  return pointData
}


const getChartData = async () => {
  const pointData = await getPointData(chartConfigData.dataType, chartConfigData.getXdataAndYdata)
  return {title: title.value, xlabel: xLabel.value, ylabel: yLabel.value, pointData}
}


const createChart = async () => {
  const base64Image = await getChart(chartType, await getChartData());
  setChart(base64Image)
}

const downloadChart = async () => downloadByHref(chartImageSrc.value, chartType)


</script>

<template>
  <container class='chart-settings'>
    <div>
      <div>Title: </div>
      <textarea v-model="title">{{ title }}</textarea>
    </div>
    <div>
      <div>X-label: </div>
      <textarea v-model="xLabel">{{ xLabel }}</textarea>
    </div>

    <div>
      <div>Y-label: </div>
      <textarea v-model="yLabel">{{ yLabel }}</textarea>
    </div>
  
    <div>
      <DropdownListWithSelection value="Данные" :items="dataNames" :setSelectedItems="setSelectedNames" maxHeight="230px" width="350px"/>

      <div class="selectedNames" :key="selectedNames">
        <template v-for="(name, index) in dataNames">
          <div v-if="selectedNames.includes(name)" class="selectedName">
            <div class="label" :style="{ color: colorsOfNames[name]}">{{ name }}</div>
            <input type="color" v-model="colorsOfNames[name]"/>
          </div>
        </template>
      </div>
    </div>

    <div class="control-buttons">
      <Button color='#6c757d' @click="downloadChart">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
          <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5"/>
          <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708z"/>
        </svg>
        Скачать
      </Button>
      <Button color='#198754' @click='createChart'>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0M4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5z"/>
        </svg>
        Создать
      </Button>
    </div>
  </container>

  <container class='chart-container'>
    <ResizableImage :path="chartImageSrc" class="chart"/>
  </container>

</template>

<style scoped lang="sass">

.chart-settings
  width: 400px

  display: flex
  flex-direction: column
  align-items: stretch
  text-align: left

  padding: 25px max(10px, 3%) !important

  > *:not(.control-buttons)
    margin-bottom: 10px

    input, textarea
      margin-top: 5px

    textarea
      width: 100%
      max-height: 400px
      resize: vertical

  .control-buttons
    margin-top: 5px

    display: flex
    flex-wrap: wrap
    align-items: center
    justify-content: space-around

    button
      margin: 0 !important

      svg
        margin-right: 7px


.selectedNames
  display: flex
  flex-direction: row
  flex-wrap: wrap
  justify-content: space-around


.selectedName
  word-break: break-all
  display: flex
  align-items: center
  flex-direction: row

  padding: 7px 12px
  margin: 5px
  
  border-radius: 7px
  border: 1px solid transparent
  background-color: #f1f1f1
  
  .label
    margin-right: 10px

  &:hover
    border: 1px solid #ddd
    background-color: #fff


input[type=color]
  width: 25px
  height: 25px

  padding: 0 !important
  margin: 0 !important

  border-radius: 50%
  border: none

  &::-webkit-color-swatch-wrapper, 
  &::-webkit-color-swatch
    margin: 0 
    padding: 0

    border-radius: 50%
    border: none

  max-height: 600px
  max-width: 700px

.chart
  max-width: 600px
  max-height: 450px

.dropdown-content
  max-height: 300px
  bottom: 50px

</style>
