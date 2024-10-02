<script setup>
import { Button, DropdownListWithSelection, Form } from '@/shared/ui'
import { getAllNames } from '@/shared/api'
import { getDataSample } from '@/entities/DataSample/api'
import { getAmplitudeAndFrequencyByName } from '@/features/creatingData/amplitudeFrequency'
import { ref } from 'vue'



const { setDataSample } = defineProps({
  setDataSample: {
    type: Function,
    required: true,
  },
})

const originalDataType = "amplitude"
const dataType = "amplitude_frequency"


const dataNames = await getAllNames(originalDataType)

const selectedNames = ref([])
const setSelectedNames = (names) => selectedNames.value = names


const getNamesAndRecords = async (names) => {
  let namesAndRecords = {}
  for (const name of names) {
    namesAndRecords[name] = await getAmplitudeAndFrequencyByName(name)
  }
  return namesAndRecords
}


const getRecords = async () => {
  const namesAndRecords = await getNamesAndRecords(selectedNames.value)
  const records = Object.values(namesAndRecords)
  records.sort((a, b) => parseFloat(a[1]) - parseFloat(b[1]))
  return records
}

const dataSample = ref({name: "", description: "", records: []})

const showDataSample = async () => {
  dataSample.value.records = await getRecords()
  setDataSample(dataSample.value)
}

</script>

<template>
  <Form class='Form'>
    <div>
      <div class='label'>Название:</div>
      <input type='text' placeholder='name' v-model="dataSample.name"/>
    </div>

    <div>
      <div class='label'>Описание:</div>
      <textarea type="text" placeholder="description" v-model="dataSample.description"/>
    </div>

    <div>
      <DropdownListWithSelection value="Амплитудные данные" :items="dataNames" :setSelectedItems="setSelectedNames" maxHeight="250px" width="270px"/>

      <div class="selectedNames">
        <RouterLink v-for="(name, index) in selectedNames" :to="'/data_samples/amplitude/' + name">
          <div class="selectedName">{{ name }}</div>
        </RouterLink>
      </div>
    </div>

    <div class="control-buttons">
      <Button color='#198754' @click='showDataSample'>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
          <path d="M6.804 8 1 4.633v6.734zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C.713 12.69 0 12.345 0 11.692V4.308c0-.653.713-.998 1.233-.696z"/>
          <path d="M14.804 8 9 4.633v6.734zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C8.713 12.69 8 12.345 8 11.692V4.308c0-.653.713-.998 1.233-.696z"/>
        </svg>
        Create
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
  
  .label
    margin-right: 10px

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
  margin-top: 20px
  margin-bottom: 0
  display: flex
  align-items: center
  justify-content: space-around

  button
    margin: 0 !important
    svg
      margin-right: 7px

.data-sample-link
  color: #4e23ab


.dropdown-content
  max-height: 300px


input[type=checkbox]
  margin-right: 10px
</style>
