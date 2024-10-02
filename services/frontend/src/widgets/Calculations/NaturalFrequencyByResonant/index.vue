<script setup>
import { Calculation } from '../Calculation'
import { Button } from '@/shared/ui'
import { getNaturalFrequencyByResonant } from '@/shared/libs'
import { ref } from 'vue'


const naturalFrequency = ref(0)
const resonantFrequency = ref(0)
const attenuationCoefficient = ref(0)


const defineNaturalFrequency = async () => {
  const a = parseFloat(resonantFrequency.value), b = parseFloat(attenuationCoefficient.value)
  naturalFrequency.value = (getNaturalFrequencyByResonant(a, b)).toFixed(6)
}


</script>

<template>
  <Calculation :calculate="defineNaturalFrequency" maxHeight='500px'>
    <div class="value">Собственная частота, рад/с: {{ naturalFrequency }}</div>
    <div class="data">Резонансная частота, рад/с: <input type="text" v-model="resonantFrequency"></div>
    <div class="data">Коэффициент затухания: <input type="text" v-model="attenuationCoefficient"></div>
  </Calculation>
</template>

<style scoped lang="sass">

.value
  margin-bottom: 20px
  font-weight: bold

.data
  margin-bottom: 10px
  display: flex
  flex-direction: row
  justify-content: space-between
  align-items: center
  width: 100%

  input
    width: 150px

</style>
