<script setup>
import { Calculation } from '../Calculation'
import { DropdownListWithSelection } from '@/shared/ui'
import { getAllNames } from '@/shared/api'
import { getQualityFactorByName } from '@/features/creatingData'
import { ref } from 'vue'


const dataNames = await getAllNames('amplitude_frequency')

const selectedName = ref(null)
const setSelectedName = (names) => {
  selectedName.value = (names.length === 0) ? null : names[0]
}

const qualityFactor = ref([0, 0])

const defineQualityFactor = async () => {
  if (selectedName.value) { 
    qualityFactor.value = await getQualityFactorByName(selectedName.value)
  }
}


</script>

<template>
  <Calculation :calculate="defineQualityFactor" maxHeight='500px'>
    <div class='value'>Добротность: {{ qualityFactor[0] }} ± {{ qualityFactor[1] }}</div>

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

.value
  font-weight: bold
  margin-bottom: 10px

.selecting-data
  width: 100%

</style>
