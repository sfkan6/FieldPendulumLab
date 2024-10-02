<script setup>
import { Calculation } from '../Calculation'
import { DropdownListWithSelection } from '@/shared/ui'
import { getAllNames } from '@/shared/api'
import { getFrequenciesByName } from '@/features/creatingData'
import { ref } from 'vue'


const dataNames = await getAllNames('amplitude_frequency')

const selectedName = ref(null)
const setSelectedName = (names) => {
  selectedName.value = (names.length === 0) ? null : names[0]
}


const leftFrequency = ref([0, 0])
const rightFrequency = ref([0, 0])
const resonantFrequency = ref([0, 0])


const defineFrequencies = async () => {
  if (selectedName.value) {
    const frequencies = await getFrequenciesByName(selectedName.value, 6)
    leftFrequency.value = frequencies[0]
    rightFrequency.value = frequencies[1]
    resonantFrequency.value = frequencies[2]
  }
}

</script>

<template>
  <Calculation :calculate="defineFrequencies" maxHeight='500px'>
    <div class='values'>
      <div>Частота 1, рад/с: {{ leftFrequency[0] }} ± {{ leftFrequency[1] }}</div>
      <div>Частота 2, рад/с: {{ rightFrequency[0] }} ± {{ rightFrequency[1] }}</div>
      <div>Резонансная частота, рад/с: {{ resonantFrequency[0] }} ± {{ resonantFrequency[1] }}</div>
    </div>

    <div>
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

</style>
