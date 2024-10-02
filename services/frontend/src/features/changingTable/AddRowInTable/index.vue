<script setup>
import { Button } from '@/shared/ui'
import { stringWithFunction } from '../stringWithFunction'
import { ref } from 'vue'


let { records, numberOfColumns, placeholder } = defineProps({
  records: {
    type: Array,
    required: true,
  },
  numberOfColumns: {
    type: Number,
    default: 0,
  },
  placeholder: {
    type: String,
    default: 'line number'
  },
})


let newLineId = ref(0)

const getLineId = (lineNumber, numberOfLines) => {
  if (lineNumber < 1) {
    return 0
  }
  else if (lineNumber > numberOfLines) {
    return numberOfLines;
  }
  else {
    return lineNumber - 1
  }
}

const addLine = () => {
  const lineId = getLineId(newLineId.value, records.length)
  records.splice(lineId, 0, new Array(numberOfColumns).fill(0))
}

</script>

<template>
  <stringWithFunction>
    <template v-slot:label>
      Добавить строку:
    </template>

    <template v-slot:function>
      <input type="text" :placeholder="placeholder" v-model="newLineId"/>
      <Button color='#6c757d' @click='addLine'>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M8 2a.5.5 0 0 1 .5.5v5h5a.5.5 0 0 1 0 1h-5v5a.5.5 0 0 1-1 0v-5h-5a.5.5 0 0 1 0-1h5v-5A.5.5 0 0 1 8 2"/>
        </svg>
        "Insert"
      </Button>
    </template>
  </stringWithFunction>
</template>

<style scoped lang="sass">

input
  width: 100px !important

</style>
