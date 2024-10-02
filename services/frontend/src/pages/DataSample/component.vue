<script setup>
import { Button, Table, Form } from '@/shared/ui'
import { DataSample } from '@/entities/DataSample/ui'
import { createDataSample, updateDataSample, getDataSample } from '@/entities/DataSample/api'

import { AddRowInTable, ShiftColumnValues } from '@/features/changingTable'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import { getTableHeaderByDataType } from '@/shared/config'



const { dataType, currentName } = defineProps({
  dataType: {
    type: String,
    required: true,
  },
  currentName: {
    type: String,
    required: true,
  },
})


const tableHeader = getTableHeaderByDataType(dataType)

const dataSample = ref(await getDataSample(dataType, currentName))
const deleteRecordById = (lineId) => dataSample.value.records.splice(lineId, 1)


const router = useRouter()

const redirectToDataSample = (response) => {
  if (response.status == 200) {
    response.json()
      .then(newDataSample => router.push({ name: "dataSample", params: {dataType, name: newDataSample.name}}))
  }
}

const saveDataSample = async () => {
  const response = await updateDataSample(dataType, currentName, dataSample.value)
  redirectToDataSample(response)
}

const createCopyDataSample = async () => {
  let copyDataSample = dataSample.value
  copyDataSample.name = "copy-" + copyDataSample.name
  const response = await createDataSample(dataType, copyDataSample)
  redirectToDataSample(response)
}


</script>

<template>
  <container class='editable-data-sample'>
    <Form class='data-sample'>

      <div>
        <div>Название:</div>
        <input type='text' placeholder='name' v-model="dataSample.name" class='name'/>
      </div>

      <div>
        <div>Время создания: </div>
        <div>{{ dataSample.timestamp }}</div>
      </div>

      <div>
        <div>Описание:</div>
        <textarea type="text" placeholder="description" v-model="dataSample.description" class='description'/>
      </div>

      <div class='middle-slot' :key="dataSample.records">
        <hr>
        <AddRowInTable :records="dataSample.records" :numberOfColumns="2"/>
        <ShiftColumnValues :columnIndex="0" :records="dataSample.records">
          Сдвинуть значения первого столбца:
        </ShiftColumnValues>
        <ShiftColumnValues :columnIndex="1" :records="dataSample.records" :fractionalPartLength="4">
          Сдвинуть значения второго столбца:
        </ShiftColumnValues>
        <hr>
      </div>
    
      <Table class='data-table not-field'>
        <thead>
          <tr>
            <th>#</th>
            <th v-for="heading in tableHeader">{{ heading }}</th>
            <th></th>
          </tr>
        </thead>
        <tbody :key="dataSample.records">
          <tr v-for="(record, index) in dataSample.records">
            <td></td>
            <td><input type='text' v-model="dataSample.records[index][0]"></td>
            <td><input type='text' v-model="dataSample.records[index][1]"></td>
            <td>
              <Button color='#dc3545' @click="deleteRecordById(index)" class='delete-row-button'>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
                  <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                  <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708"/>
                </svg>
              </Button>
            </td>
          </tr>
        </tbody>
      </Table>

      <div class='lower-slot'>
        <Button color='#6c757d' @click='createCopyDataSample'>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/>
          </svg>
          Создать копию
        </Button>
        <Button color='#198754' @click='saveDataSample'>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
            <path d="M2 1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H9.5a1 1 0 0 0-1 1v7.293l2.646-2.647a.5.5 0 0 1 .708.708l-3.5 3.5a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L7.5 9.293V2a2 2 0 0 1 2-2H14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h2.5a.5.5 0 0 1 0 1z"/>
          </svg>
          Сохранить
        </Button>
      </div>

    </Form>
  </container>
</template>

<style scoped lang="sass">

.editable-data-sample
  width: 500px


.description
  width: 100%
  resize: vertical
  max-height: 400px
  min-height: 100px

.description, .name
  margin-top: 10px



.middle-slot > *
  margin-bottom: 20px

.lower-slot
  margin-top: 25px
  margin-bottom: 10px

  display: flex
  align-items: center
  justify-content: space-around
  flex-direction: row
  flex-wrap: wrap

  button
    margin: 0 !important

    :deep(svg)
      margin-right: 7px
      width: 18px


.delete-row-button
  padding: 6px 5px !important
  margin: 0 !important


</style>
