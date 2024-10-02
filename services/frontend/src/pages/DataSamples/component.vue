<script setup>
import { Button, Card } from '@/shared/ui'
import { downloadByHref } from '@/shared/libs'
import { getDataSamples, deleteDataSamples, loadTestData } from '@/shared/api'
import { deleteDataSample, downloadDataSample } from '@/entities/DataSample/api'
import { DataSample } from '@/entities/DataSample/ui'


const { title, dataType } = defineProps({
  title: String,
  dataType: String,
})

const dataSamples = await getDataSamples(dataType)

const reload = () => location.reload()

const downloadDataSampleFile = async (name) => {
  let blob = await downloadDataSample(dataType, name);
  blob = new Blob([JSON.stringify(JSON.parse(await blob.text()), null, 2)], {type: blob.type});
  downloadByHref(URL.createObjectURL(blob), name)
}

const deleteDataSampleHandler = async (event, name) => {
  const dataSample = event.target.closest('.data-sample-card');
  const time = 0.35
  dataSample.style.transitionDuration = `${time}s`;
  dataSample.style.opacity = 0
  dataSample.style.transform = 'scale(0)'
  setTimeout(() => {
    dataSample.remove()
    deleteDataSample(dataType, name)
  }, time * 1000);
}
</script>

<template>
  <h3 class='title'>{{ title }}</h3>

  <div class='main-control-buttons'>
    <Button color='#dc3545' @click='deleteDataSamples(dataType); reload();'>
      <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
        <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
        <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
      </svg>
      Delete All
    </Button>
    <Button color='#6c757d' @click='loadTestData(dataType); reload();'>
      <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
        <path d="M4.406 1.342A5.53 5.53 0 0 1 8 0c2.69 0 4.923 2 5.166 4.579C14.758 4.804 16 6.137 16 7.773 16 9.569 14.502 11 12.687 11H10a.5.5 0 0 1 0-1h2.688C13.979 10 15 8.988 15 7.773c0-1.216-1.02-2.228-2.313-2.228h-.5v-.5C12.188 2.825 10.328 1 8 1a4.53 4.53 0 0 0-2.941 1.1c-.757.652-1.153 1.438-1.153 2.055v.448l-.445.049C2.064 4.805 1 5.952 1 7.318 1 8.785 2.23 10 3.781 10H6a.5.5 0 0 1 0 1H3.781C1.708 11 0 9.366 0 7.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383"/>
        <path d="M7.646 15.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 14.293V5.5a.5.5 0 0 0-1 0v8.793l-2.146-2.147a.5.5 0 0 0-.708.708z"/>
      </svg>
      Test data load
    </Button>
    <RouterLink :to="`/data_samples/${dataType}/create`">
      <Button color='#417eff'>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
          <path d="M8.5 6a.5.5 0 0 0-1 0v1.5H6a.5.5 0 0 0 0 1h1.5V10a.5.5 0 0 0 1 0V8.5H10a.5.5 0 0 0 0-1H8.5z"/>
          <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2zm10-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1"/>
        </svg>
      </Button>
    </RouterLink>
  </div>

  <div class='data-samples'>
    <Card v-for="(dataSample, index) in dataSamples" class="data-sample-card" :key="index">
      <div class='control-buttons'>
        <RouterLink :to="`/data_samples/${dataType}/${dataSample.name}`">
          <Button color='#417eff'>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
              <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
              <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
            </svg>
          </Button>
        </RouterLink>
        <Button color='#6c757d' @click='downloadDataSampleFile(dataSample.name)'>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
            <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5"/>
            <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708z"/>
          </svg>
        </Button>
        <Button color='#dc3545' @click='deleteDataSampleHandler($event, dataSample.name)'>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
            <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
            <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
          </svg>
        </Button>
      </div>
      <DataSample  :dataType="dataType" :dataSample='dataSample' tableHeight="300px"/>
    </Card>
  </div>
</template>

<style scoped lang="sass">

.title
  text-align: center
  margin: 20px 0 25px
  font-size: 28px

.main-control-buttons button
  margin: 10px 5px !important

.control-buttons 
  margin-bottom: 15px

  button
    padding: 7px 6px !important
    margin: 3px 5px !important

    :deep(svg)
      width: 18px

  button:first-child
    margin-left: 0 !important

.data-samples
  display: flex
  flex-direction: row
  flex-wrap: wrap
  justify-content: space-around
  align-items: flex-start

.data-sample-card
  width: 350px
  opacity: 1

</style>
