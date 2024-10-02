<script setup>
import { Button, DropdownListWithSelection, Form, ResizableImage } from '@/shared/ui'
import { getAllNames, getChart } from '@/shared/api'
import { setBase64Image } from '@/shared/libs'
import { getDataSample } from '@/entities/DataSample/api'
import { ref } from 'vue'


const { setDataSample } = defineProps({
  setDataSample: {
    type: Function,
    required: true,
  },
})


const originalDataType = "angle"
const dataType = "amplitude"


const dataNames = await getAllNames(originalDataType)

const selectedName = ref(null)
const setSelectedName = (names) => {
  selectedName.value = (names.length === 0) ? null : names[0]
}


const angleRecords = ref([])
const updateAngleRecords = async (name) => {
  const {records} = await getDataSample(originalDataType, name)
  angleRecords.value = records
}


const indexesOfRecords = ref(Array.from(Array(angleRecords.value.length).keys()))
const updateIndexesOfRecords = () => {
  indexesOfRecords.value = Array.from(Array(angleRecords.value.length).keys())
}

const selectedIndexes = ref([])
const setSelectedIndexes = (newSelectedIndexes) => selectedIndexes.value = newSelectedIndexes




const initialChartData = {
  title: "Зависимость угла от времени",
  xlabel: "Время, с",
  ylabel: "Угол, °",
}

const getChartData = (name, records) => {
  const pointData = {
    [name]: {
      xdata: records.map(record => record[1]),
      ydata: records.map(record => record[0]),
      color: 'blue'
    }
  }
  return {...initialChartData, pointData}
}


const chartImageSrc = ref("/empty_graph.png")
const setChart = (base64Image) => setBase64Image(base64Image, chartImageSrc)


const updateChart = async (name, records) => {
  const chartData = getChartData(name, records)
  const base64Image = await getChart("angle_points", chartData);
  setChart(base64Image)
}




const setNameAndShowChart = async (names) => {
  setSelectedName(names)
  if (selectedName.value) {
    await updateAngleRecords(selectedName.value)
    await updateChart(selectedName.value, angleRecords.value)
    updateIndexesOfRecords()
    setSelectedIndexes([])
  }
}


const dataSample = ref({name: "", description: "", records: []})
const getAmplitudeRecords = () => selectedIndexes.value.map(index => angleRecords.value[index])

const showDataSample = async () => {
  dataSample.value.records = getAmplitudeRecords()
  setDataSample(dataSample.value)
}
</script>

<template>
  <Form class='form'>
    <div>
      <div class='label'>Название:</div>
      <input type='text' placeholder='name' v-model="dataSample.name"/>
    </div>

    <div>
      <div class='label'>Описание:</div>
      <textarea type="text" placeholder="description" v-model="dataSample.description"/>
    </div>

    <div class='not-field'>
      <DropdownListWithSelection value="Угловые данные" :items="dataNames" :setSelectedItems="setNameAndShowChart" :maxLen="1" maxHeight="250px" width="270px"/>

      <div class="selectedNames">
        <RouterLink v-if="selectedName !== null" :to="`/data_samples/${originalDataType}/${selectedName}`" :key="selectedName">
          <div class="selectedName">{{ selectedName }}</div>
        </RouterLink>
      </div>
    </div>

    <ResizableImage :path="chartImageSrc" class="video"/>

    <div class='not-field'>
      <DropdownListWithSelection value="Точки" :items="indexesOfRecords" verticalShift="50px"
        :setSelectedItems="setSelectedIndexes" maxHeight="200px" width="200px" :key="indexesOfRecords"/>
      <div class="selectedNames" :key="selectedIndexes">
        <div v-for="value in selectedIndexes" class="selectedName">
          {{ value }}
        </div>
      </div>
    </div>

    <div class="control-buttons not-field">
      <Button color='#198754' @click='showDataSample'>
        Create
        <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
          <path d="M6.804 8 1 4.633v6.734zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C.713 12.69 0 12.345 0 11.692V4.308c0-.653.713-.998 1.233-.696z"/>
          <path d="M14.804 8 9 4.633v6.734zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C8.713 12.69 8 12.345 8 11.692V4.308c0-.653.713-.998 1.233-.696z"/>
        </svg>
      </Button>
    </div>
  </Form>
</template>

<style scoped lang="sass">

.form
  width: 400px
  
  .label
    margin-bottom: 5px
    

.selectedNames
  display: flex
  flex-direction: row
  flex-wrap: wrap
  justify-content: space-around


.selectedName
  display: flex
  align-items: center
  flex-direction: row

  padding: 7px 12px
  margin: 5px
  
  border-radius: 7px
  border: 1px solid transparent
  background-color: #f1f1f1
  color: black
  
  &:hover
    border: 1px solid #ddd
    background-color: #fff



.panel-for-creating-data-sample
  width: 400px

.data-sample
  max-width: 370px

  .description
    max-height: 100px
    text-overflow: ellipsis


  textarea
    max-width: 100%
    max-height: 300px

  > *
    margin-bottom: 15px

    > input, textarea
      margin-top: 10px


.control-buttons
  margin-top: 10px
  margin-bottom: 0

  display: flex
  align-items: center
  justify-content: flex-end

  button
    margin: 0 !important
    svg
      width: 22px
      margin-left: 7px

.data-sample-link
  color: #4e23ab

</style>
