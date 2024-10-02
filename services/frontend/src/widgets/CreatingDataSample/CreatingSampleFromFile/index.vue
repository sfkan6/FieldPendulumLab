<script setup>
import { Button, CollapsibleContent, DropdownListWithSelection, Form, ResizableImage } from '@/shared/ui'
import { dataTypeAndName, getTypeByName } from '@/shared/config'
import { getContentByFile } from '@/shared/libs'
import { getAllNames, getChart } from '@/shared/api'
import { getDataSample } from '@/entities/DataSample/api'
import { ref } from 'vue'


const { setDataSample, setDataType } = defineProps({
  setDataSample: {
    type: Function,
    required: true,
  },
  setDataType: {
    type: Function,
    required: true,
  },
})


setDataType('angle')

const typeNames = Object.values(dataTypeAndName)

const selectedName = ref(null)
const setSelectedName = (names) => {
  selectedName.value = (names.length === 0) ? null : names[0]
}

const dataSample = ref(null)

const onFileChange = async (e) => {
  dataSample.value = JSON.parse(await getContentByFile(e.target.files[0]))
}

const showDataSample = () => {
  if (selectedName.value && dataSample.value) {
    setDataType(getTypeByName(selectedName.value))
    setDataSample(dataSample.value)
  }
}

const dataTemplate = {
  "name": "damped",
  "timestamp": "2024-05-20 02:55:02",
  "description": "Damped oscillation",
  "records": [
    [90.12, 0.27],
    ...
    [25.41, 7.57],
  ]
}

</script>

<template>
  <Form class='form'>
    <input id="files" type="file" @change="onFileChange">

    <CollapsibleContent value="Шаблон файла" class="data-template">
      <pre class='template'>{{ JSON.stringify(dataTemplate, null, 2) }}</pre>
    </CollapsibleContent>

    <div class='selecting-data-type'>
      <DropdownListWithSelection value="Тип данных" :items="typeNames" :maxLen="1"
        :setSelectedItems="setSelectedName" maxHeight="250px" width="270px"
      />
      <div class="selectedNames">
        <div class="selectedName" v-if="selectedName">{{ selectedName }}</div>
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
  width: 550px

  input
    margin-top: 10px

.data-template
  flex-direction: column !important
  margin-top: 20px
  margin-bottom: 10px !important
  cursor: pointer

  .label
    padding: 10px 10px
    width: fit-content

  .template
    width: 100%
    box-sizing: border-box
    padding: 10px
    border: 1px solid black
    border-radius: 10px


.selectedNames
  width: 100%
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

input[type=file]
  font-size: 16px
  
  &::-webkit-file-upload-button
    padding: 8px 12px
    border-radius: 5px
    border: 1px solid black
    background-color: #fff
    
    &:hover
      cursor: pointer
      background-color: #f1f1f1

.control-buttons, .selecting-data-type
  margin-bottom: 0 !important


</style>
