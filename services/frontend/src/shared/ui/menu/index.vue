<script setup>
import { ref, watch } from 'vue'

let { values, selectedValue, setSelectedValue, color, hover_color } = defineProps({
  values: {
    type: Array,
    required: true
  },
  selectedValue: {
    type: String,
    required: true
  },
  setSelectedValue: {
    type: Function,
    default: (newValue) => {}
  },
  color: {
    type: String,
    default: "#4e23ab",
  },
  hover_color: {
    type: String,
    default: "#8059d4",
  },
})

setSelectedValue(selectedValue ? selectedValue : values[0])

</script>


<template>
  <div class="menu">
    <div v-for="value in values" class="value" :class="{ selected: selectedValue == value}" @click="setSelectedValue(value)">
      {{ value }}
    </div>
  </div>
</template>

<style scoped lang='sass'>
$color: v-bind('color')
$hover_color: v-bind('hover_color')


.menu
  border-radius: 10px
  display: flex
  flex-direction: row
  flex-wrap: wrap
  align-items: center
  justify-content: space-around
  background-color: #fff

.selected
  color: $color

.value
  word-break: break-all

  padding: 7px 12px
  border-radius: 7px
  margin: 5px

  display: flex
  align-items: center
  flex-direction: row

  border: 1px solid transparent
  background-color: fff
  
  &:hover
    cursor: pointer
    color: $hover_color

</style>
