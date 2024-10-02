<script setup>
import { Calculation } from '../Calculation'
import { DropdownListWithSelection } from '@/shared/ui'
import { getAllNames, getChart } from '@/shared/api'
import { ref } from 'vue'
import { getAttenuationCoefficientByNames } from '@/features/creatingData/attenuationCoefficient'


const dataNames = await getAllNames('amplitude')

const selectedNames = ref([])
const setSelectedNames = (names) => selectedNames.value = names


const attenuationCoefficient = ref(0)

const calculateAttenuationCoefficient = async () => {
  if (selectedNames.value.length > 0) { 
    attenuationCoefficient.value = (await getAttenuationCoefficientByNames(selectedNames.value)).toFixed(4)
  }
}


</script>

<template>
  <Calculation :calculate="calculateAttenuationCoefficient" maxHeight='500px'>
    <div class="value">
      Коэффициент затухания: {{ attenuationCoefficient }}
    </div>

    <div class='selecting-data'>
      <DropdownListWithSelection value="Данные затухающих колебаний" :items="dataNames" 
        :setSelectedItems="setSelectedNames" maxHeight="250px" width="270px"
      />
      <div class="selectedNames">
        <div class="selectedName" v-for="name in selectedNames">{{ name }}</div>
      </div>
    </div>

  </Calculation>
</template>

<style scoped lang="sass">

.value
  font-weight: bold
  margin-bottom: 15px

.selecting-data
  width: 100%

</style>
