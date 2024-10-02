<script setup>
import { ref } from 'vue'

let { HSVRange } = defineProps({
  HSVRange: {
    type: Array,
    required: true,
  },
})

</script>

<template>
  <div>
    <div>
    </div>
    <div class="coordinate">
      Hue:
      <div class="setting-coordinate">
        <input type="range" min="0" max="255" step="1" v-model="HSVRange[0][0]"/>
        <input type="range" min="0" max="255" step="1" v-model="HSVRange[1][0]"/>
      </div>
    </div>

    <div class="coordinate">
      Saturation:
      <div class="setting-coordinate">
        <input type="range" min="0" max="255" step="1" v-model="HSVRange[0][1]"/>
        <input type="range" min="0" max="255" step="1" v-model="HSVRange[1][1]"/>
      </div>
    </div>
    <div class="coordinate">
      Value:
      <div class="setting-coordinate">
        <input type="range" min="0" max="255" step="1" v-model="HSVRange[0][2]"/>
        <input type="range" min="0" max="255" step="1" v-model="HSVRange[1][2]"/>
      </div>
    </div>
  </div>
</template>

<style scoped lang="sass">

.coordinate, .setting-coordinate
  display: flex
  flex-direction: row
  flex-wrap: wrap
  align-items: center
  justify-content: space-between

.coordinate
  margin-bottom: 10px
  &:last-child
    margin-bottom: 0 !important

.setting-coordinate
  max-width: 290px


input[type=range]
  max-width: 130px
</style>
