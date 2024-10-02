<script setup>
import { Button, Table } from '@/shared/ui'
import { WebSocketClient } from '@/shared/api'
import { getTableHeaderByDataType } from '@/shared/config'
import { createDataSampleAndNotify } from '@/features'
import { ref } from "vue"


const { setDataSample } = defineProps({
  setDataSample: {
    type: Function,
    required: true,
  },
})


const dataType = "angle"

const dataSample = ref({name: "", description: "", records: []})
const tableHeader = getTableHeaderByDataType(dataType)


const saveData = async () => await createDataSampleAndNotify(dataType, dataSample.value)
const deleteData = () => dataSample.value.records = []

const showData = (data) => {
  const values = Object.values(JSON.parse(data))
  dataSample.value.records.push(values)
  setDataSample(dataSample.value)
};



let data_client = new WebSocketClient('pendulum_of_field/angle')
const sleepTime = ref(1)



const isInitialStep = ref(true)
const isMainStep = ref(false)
const isFinalStep = ref(false)


const toggle = (isButtonShow) => {
  isButtonShow.value = !isButtonShow.value
}

const runToggle = () => {
  toggle(isInitialStep)
  toggle(isMainStep)

  data_client.run(showData, {sleep_time: parseFloat(sleepTime.value)})
}
const finishToggle = () => {
  toggle(isMainStep)
  toggle(isFinalStep)

  data_client.close()
}
const repeatToggle = () => {
  toggle(isFinalStep)
  toggle(isInitialStep)

  deleteData()
}
const saveToggle = () => {
  saveData()
}

</script>

<template>
  <container class="control-panel">
    <input type="range" id="sleep_time" min="0" max="3" step="0.1" v-model="sleepTime"/>
    <div class="label">Интервал измерений, s: {{ sleepTime }}</div>

    <div class="buttons">
      <Button color='#198754' @click='runToggle' v-show='isInitialStep'>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
          <path d="M10.804 8 5 4.633v6.734zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C4.713 12.69 4 12.345 4 11.692V4.308c0-.653.713-.998 1.233-.696z"/>
        </svg>
        Run
      </Button>
      <Button color='#dc3545' @click="finishToggle" v-show='isMainStep'>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
          <path d="M6 3.5a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-1 0V4a.5.5 0 0 1 .5-.5m4 0a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-1 0V4a.5.5 0 0 1 .5-.5"/>
        </svg>
        Finish
      </Button>
      <Button color='#417eff' @click='repeatToggle' v-show='isFinalStep'>
        <svg xmlns="http://www.w3.org/2000/svg" width="16"  viewBox="0 0 16 16">
          <path d="M11.534 7h3.932a.25.25 0 0 1 .192.41l-1.966 2.36a.25.25 0 0 1-.384 0l-1.966-2.36a.25.25 0 0 1 .192-.41m-11 2h3.932a.25.25 0 0 0 .192-.41L2.692 6.23a.25.25 0 0 0-.384 0L.342 8.59A.25.25 0 0 0 .534 9"/>
          <path fill-rule="evenodd" d="M8 3c-1.552 0-2.94.707-3.857 1.818a.5.5 0 1 1-.771-.636A6.002 6.002 0 0 1 13.917 7H12.9A5 5 0 0 0 8 3M3.1 9a5.002 5.002 0 0 0 8.757 2.182.5.5 0 1 1 .771.636A6.002 6.002 0 0 1 2.083 9z"/>
        </svg>
        Repeat
      </Button>
      <Button color='#6c757d' @click='saveToggle' v-show='isFinalStep'>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
          <path d="M2 1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H9.5a1 1 0 0 0-1 1v7.293l2.646-2.647a.5.5 0 0 1 .708.708l-3.5 3.5a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L7.5 9.293V2a2 2 0 0 1 2-2H14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h2.5a.5.5 0 0 1 0 1z"/>
        </svg>
       Save 
      </Button>
    </div>
  </container>

  <container class="data-sample">
    <input type="text" placeholder="name" v-model="dataSample.name"></input>
    <textarea type="text" placeholder="description" v-model="dataSample.description"></textarea>
    <Table maxHeight="450px">
      <thead>
        <tr>
          <th>#</th>
          <th v-for="heading in tableHeader">{{ heading }}</th>
        </tr>
      </thead>
      <tbody :key="dataSample.records">
        <tr v-for="record in dataSample.records">
          <td></td>
          <td>{{ record[0] }}</td>
          <td>{{ record[1] }}</td>
        </tr>
      </tbody>
    </Table>
  </container>
</template>

<style scoped lang="sass">

.control-panel

  > *
    width: 100%

  .label
    margin-top: 10px
    margin-bottom: 15px

  .buttons
    display: flex
    flex-direction: row
    flex-wrap: wrap
    align-items: center
    justify-content: space-around

    button
      margin-bottom: 0
      margin-top: 0

.data-sample
  > *:not(:last-child)
    margin-bottom: 15px

</style>
