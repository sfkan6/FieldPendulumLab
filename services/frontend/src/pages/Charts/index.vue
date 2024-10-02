<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'


const chartTypes = [
  'points', 
  'amplitude_versus_time', 
  'amplitude_resonance_curve', 
  'phase_resonance_curve'
]

</script>

<template>
  <PageContentWrapper class='wrapper'>
    <RouterLink v-for="chartType in chartTypes" :to="'/charts/' + chartType">
      <container class='chart-type'>
        <div class='img-wrapper'>
          <img :src="'chart-types/' + chartType + '.png'">
        </div>
      </container>
    </RouterLink>
  </PageContentWrapper>
</template>

<style scoped lang="sass">
$resizer-color: #4020fe

.wrapper
  display: flex
  flex-direction: row
  flex-wrap: wrap
  align-items: stretch
  justify-content: space-around

.chart-type
  height: min-content

  &:hover 
    box-shadow: 0px 10px 16px 4px #DBDBDB
    transition-duration: 0.1s
    transition-timing-function: linear
    transform: scale(1.005)
    cursor: pointer
 
  .img-wrapper
    max-width: 350px
    width: 100%

</style>
