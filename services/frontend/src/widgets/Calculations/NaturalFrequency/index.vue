<script setup>
import { Calculation } from '../Calculation'
import { DropdownListWithSelection } from '@/shared/ui'
import { getNaturalFrequency } from '@/shared/libs'
import { getAllNames } from '@/shared/api'
import { getAttenuationCoefficientByNames } from '@/features/creatingData/attenuationCoefficient'
import { getFrequencyByNames } from '@/features/creatingData/naturalFrequency'
import { ref } from 'vue'


const dataNames = await getAllNames('amplitude')

const selectedNames = ref([])
const setSelectedNames = (names) => selectedNames.value = names


const frequency = ref(0)
const attenuationCoefficient = ref(0)
const naturalFrequency = ref(0)


const defineAttenuationCoefficient = async () => {
  if (selectedNames.value.length > 0) { 
    frequency.value = (await getFrequencyByNames(selectedNames.value)).toFixed(4)
    attenuationCoefficient.value = (await getAttenuationCoefficientByNames(selectedNames.value)).toFixed(4)
    naturalFrequency.value = (getNaturalFrequency(frequency.value, attenuationCoefficient.value)).toFixed(4)
  }
}


</script>

<template>
  <Calculation :calculate="defineAttenuationCoefficient" maxHeight='500px'>
    <div class="values">
      <div>Частота, рад/с: {{ frequency }}</div>
      <div>Коэффициент затухания: {{ attenuationCoefficient }}</div>
      <div>Собственная частота, рад/с: {{ naturalFrequency }}</div>
    </div>

    <div>
      <DropdownListWithSelection value="Данные затухающих колебаний" :items="dataNames" 
        :setSelectedItems="setSelectedNames" maxHeight="250px" width="270px"
      />
      <div class="selectedNames">
        <div v-for="name in selectedNames">
          <div class="selectedName">{{ name }}</div>
        </div>
      </div>
    </div>
  </Calculation>
</template>

<style scoped lang="sass">

.values

  > *
    font-size: 20px
    font-weight: bold
    margin-bottom: 10px

</style>
