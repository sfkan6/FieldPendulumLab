<script setup>
import { Button, Dropdown } from '@/shared/ui'
import { getAllNames } from '@/shared/api'
import { DataSample } from '@/entities/DataSample/ui'
import { createDataSampleAndNotify } from '@/features'
import { SuccessOrError } from '@/widgets/SuccessOrError'
import { ref } from 'vue'


const { dataType, creatingComponent } = defineProps({
  dataType: {
    type: String,
    required: true,
  },
  creatingComponent: {
    type: Object,
  }
})


const dataSampleType = ref(dataType)
const setDataSampleType = async (newDataType) => dataSampleType.value = newDataType

const dataSample = ref({name: "Название", timestamp: "", description: "Описание", records: []})
const setDataSample = async (newDataSample) => dataSample.value = newDataSample

const saveDataSample = async () => createDataSampleAndNotify(dataSampleType.value, dataSample.value)
</script>

<template>
  <SuccessOrError/>

  <container class='creating'>
    <AsyncWrapper>
      <component :is="creatingComponent" :setDataType="setDataSampleType" :setDataSample="setDataSample"/>
    </AsyncWrapper>
  </container>

  <container class='static-data-sample'>
    <DataSample :dataType="dataSampleType" :dataSample='dataSample' tableHeight="400px" :key='dataSample'/>
    <div class='control-buttons'>
      <Button color='#6c757d' @click='saveDataSample'>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
          <path d="M2 1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H9.5a1 1 0 0 0-1 1v7.293l2.646-2.647a.5.5 0 0 1 .708.708l-3.5 3.5a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L7.5 9.293V2a2 2 0 0 1 2-2H14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h2.5a.5.5 0 0 1 0 1z"/>
        </svg>
        Сохранить
      </Button>
    </div>
  </container>

</template>

<style scoped lang="sass">

.static-data-sample
  min-width: 300px
  max-width: 500px

  .control-buttons
    display: flex
    justify-content: flex-end
    margin-top: 10px

    button
      margin-bottom: 0

</style>
