<script setup>
import { Button } from '@/shared/ui'
import { ref } from 'vue'

</script>

<template>
  <div class='string-with-function'>
    <div class="label">
      <slot name="label"/>
    </div>
    <div class='function-block'>
      <slot name="function"/>
    </div>
  </div>
</template>

<style scoped lang="sass">

.string-with-function
  width: 100%
  display: flex
  justify-content: space-between
  align-items: center


.function-block
  width: 250px
  display: flex
  justify-content: space-between
  align-items: center
  flex-direction: row
  flex-wrap: wrap

.label
  width: calc(100% - 250px)
  word-break: break-word


</style>
