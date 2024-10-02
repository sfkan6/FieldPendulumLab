<script setup>
import { Calculation } from '../Calculation'
import { DropdownListWithSelection } from '@/shared/ui'
import { getAllNames, getChart, getApproximation } from '@/shared/api'
import { getColumns } from '@/shared/libs'
import { getDataSample } from '@/entities/DataSample/api'
import { ref } from 'vue'


const dataType = 'amplitude_frequency'
const chartType = 'amplitude_resonance_curve'

const dataNames = await getAllNames(dataType)

const selectedName = ref(null)
const setSelectedName = (names) => {
  selectedName.value = (names.length === 0) ? null : names[0]
}


const acceleration = ref([0, 0])
const naturalFrequency = ref([0, 0])
const attenuationCoefficient = ref([0, 0])


const defineErrors = async () => {
  if (selectedName.value) { 
    const {records} = await getDataSample(dataType, selectedName.value)
    const columns = getColumns(records, 1)
    const {values, errors} = await getApproximation(chartType, {xdata: columns[1], ydata: columns[0]})

    const k = 6
    acceleration.value = [values[0], errors[0]].map(e => e.toFixed(k))
    naturalFrequency.value = [values[1], errors[1]].map(e => e.toFixed(k))
    attenuationCoefficient.value = [values[2], errors[2]].map(e => e.toFixed(k))
  }
}


</script>

<template>
  <Calculation :calculate="defineErrors" maxHeight='500px'>
    <div class="title">
      Аппроксимация амплитудно-резонансной кривой
    </div>
    <div class="values">
      <div>Ускорение, м/с²: {{ acceleration[0] }} ± {{ acceleration[1] }}</div>
      <div>Собственная частота, рад/с: {{ naturalFrequency[0] }} ± {{ naturalFrequency[1] }}</div>
      <div>Коэффициент затухания: {{ attenuationCoefficient[0] }} ± {{ attenuationCoefficient[1] }}</div>
    </div>

    <div class='selecting-data'>
      <DropdownListWithSelection value="Амплитудные частоты" :items="dataNames" :maxLen="1"
        :setSelectedItems="setSelectedName" maxHeight="250px" width="270px"
      />
      <div class="selectedNames">
        <div class="selectedName" v-if="selectedName">{{ selectedName }}</div>
      </div>
    </div>
  </Calculation>

</template>

<style scoped lang="sass">

.title
  font-size: 22px
  margin-bottom: 15px

.values
  margin-top: 5px

  > *
    font-weight: bold
    margin-bottom: 15px

.selecting-data
  width: 100%

</style>
