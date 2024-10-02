<script setup>
import { Button, DropdownListWithSelection } from '@/shared/ui'
import { getAllNames } from '@/shared/api'
import { getFrequenciesByName } from '@/features/creatingData'
import { ref } from 'vue'


const { calculate, maxHeight } = defineProps({
  calculate: {
    type: Function,
    default: () => {},
  },
  maxHeight: {
    type: String,
    default: "500px",
  },
})

</script>

<template>
  <container class='container'>

    <slot/>

    <Button color='#6c757d' @click="calculate">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
        <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5"/>
        <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708z"/>
      </svg>
      Вычислить
    </Button>

  </container>

</template>

<style scoped lang="sass">
$maxHeight: v-bind('maxHeight')

.container
  width: $maxHeight
  display: flex
  flex-direction: column
  align-items: flex-start


button
  margin-top: 15px !important


:slotted(.selectedNames)
  display: flex
  flex-direction: row
  flex-wrap: wrap
  justify-content: space-around


:slotted(.selectedName)
  display: flex
  align-items: center
  flex-direction: row

  padding: 7px 12px
  margin: 5px
  
  border-radius: 7px
  border: 1px solid transparent
  background-color: #f1f1f1
  
  .label
    margin-right: 10px

  &:hover
    border: 1px solid #ddd
    background-color: #fff

</style>
