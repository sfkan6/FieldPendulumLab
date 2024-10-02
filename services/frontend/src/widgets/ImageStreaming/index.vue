<script setup>
import { ResizableImage } from '@/shared/ui'
import { WebSocketClient } from '@/shared/api'
import { ref } from 'vue'

const { imageSrc, maxHeight} = defineProps({
  imageSrc: {
    type: String, 
    required: true,
  },
  maxHeight: {
    type: String,
    default: '500px',
  },

})

</script>

<template>
  <div class='streaming-video'>
    <ResizableImage :path="imageSrc" class="video"/>

    <slot/>
  </div>
</template>

<style scoped lang="sass">
$maxHeight: v-bind('maxHeight')

.streaming-video
  max-width: 100%

  .video
    max-height: $maxHeight

</style>
