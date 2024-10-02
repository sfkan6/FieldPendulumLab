<script setup>
import { ref } from 'vue'

let { path, resizer_color } = defineProps({
  path: {
    type: String,
    required: true,
  },
  resizer_color: {
    type: String,
    default: "#4020fe",
  },

})

</script>

<template>
  <div class='img-wrapper'>
    <img :src="path">
  </div>
</template>


<style scoped lang='sass'>
$resizer-color: v-bind('resizer_color')

.img-wrapper
  line-height: 0
  resize: both
  overflow: hidden

  min-height: 200px
  min-width: 200px
  max-width: 100%
  max-height: 100%

  img
    height: 100%
    object-fit: cover
 
  &::-webkit-resizer
    border-width: 20px
    border-style: solid
    border-color: transparent $resizer-color $resizer-color transparent 


</style>
