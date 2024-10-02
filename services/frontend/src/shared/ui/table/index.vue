<script setup>
const props = defineProps({
  color: {
    type: String,
    default: "#212529",
  },
  background: {
    type: String,
    default: "#f1f1f1",
  },
  maxHeight: {
    type: String,
    default: "auto",
  },
})
</script>

<template>
  <div class="table_container">
    <table>
      <slot/>
    </table>
  </div>
</template>

<style scoped lang='sass'>
$maxHeight: v-bind('props.maxHeight')

.table_container
  max-height: $maxHeight
  width: 100%
  overflow-y: scroll

table
  width: 100%
  counter-reset: recordCount
  border-collapse: collapse

:deep(thead)
  position: sticky
  top: 0
  background: white
  border-bottom: 1px solid black

  tr
    text-align: left

  th
    padding: 10px
    
    &:first-child
      text-align: center


:deep(tbody tr)
  counter-increment: recordCount
  border-bottom: 1px solid #dee2e6

  &:hover
    background: #ededed

  td
    padding: 10px

    &:first-child::before 
      content: counter(recordCount)

    &:first-child
      text-align: center


::-webkit-scrollbar
  width: 10px
  background-color: transparent

::-webkit-scrollbar-thumb
  background-color: #c5c5c5
  border-radius: 10px


</style>
