<script setup>
import { Dropdown } from '@/shared/ui'
import { getSum } from '@/shared/libs'
import { ref } from 'vue'

let { value, items, setSelectedItems, maxLen, maxHeight, width, verticalShift } = defineProps({
  value: {
    type: String,
    required: true,
  },
  items: {
    type: Array,
    required: true,
  },
  setSelectedItems: {
    type: Function,
    default: () => {},
  },
  maxLen: {
    type: Number,
    default: 100,
  },
  maxHeight: {
    type: String,
    default: "auto",
  },
  width: {
    type: String,
    default: "100%",
  },
  verticalShift: {
    type: String,
    default: "auto",
  }
})

const checkboxs = ref(new Array(items.length).fill(false))
const toggleCheckbox = (index) => {
  checkboxs.value[index] = !checkboxs.value[index]
}


const getSelectedItems = () => {
  let selectedItems = []
  checkboxs.value.forEach((value, index) => {
    if (value) {
      selectedItems.push(items[index])
    }
  })
  return selectedItems
}


const toggle = (index) => {
  if ((getSum(checkboxs.value) < maxLen) || (checkboxs.value[index])) {
    toggleCheckbox(index)
    setSelectedItems(getSelectedItems())
  }
}

</script>


<template>
  <Dropdown :value="value" class='dropdown' :maxHeight="maxHeight" :width="width" :verticalShift="verticalShift">
    <div class="dropdown-content">
      <div v-for="(item, index) in items" @click="toggle(index)">
        <input type="checkbox" v-model="checkboxs[index]" @change=""/>
        {{ item }}
      </div>
    </div>
  </Dropdown>
</template>

<style scoped lang="sass">

</style>
