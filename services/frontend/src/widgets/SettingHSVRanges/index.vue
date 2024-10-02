<script setup>
import { Button, CollapsibleContent, ResizableImage, HSVCustomization } from '@/shared/ui'
import { computed, ref } from "vue"


let { HSVRanges } = defineProps({
  HSVRanges: {
    type: Array,
    default: [],
  },
})

const emptyHSVRange = [[0, 0, 0], [0, 0, 0]]


const HSVRangeIndex = ref(0)
const setHSVRangeIndex = (index, event=null) => {
  if (event && ['path', 'svg', 'BUTTON'].includes(event.target.tagName)) {
    return
  }
  HSVRangeIndex.value = index
}


const addHSVRange = () => HSVRanges.push(structuredClone(emptyHSVRange))

const deleteHSVRange = (index) => {
  if (HSVRangeIndex.value > index) {
    setHSVRangeIndex(HSVRangeIndex.value - 1)
  }
  else if (HSVRangeIndex.value == index) {
    if (HSVRanges.length == 1) {
      addHSVRange()
    }
    setHSVRangeIndex(0)
  }
  HSVRanges.splice(index, 1)
}

</script>

<template>
  <container>
    <div>
      Выбранные диапазоны:
      <table>
        <tbody>
          <tr v-for="(HSVRange, index) in HSVRanges"
            @click="setHSVRangeIndex(index, $event)"
            :class="{ selected_hsv_range: index == HSVRangeIndex }"
          >
            <td>{{ index + 1}}. </td>
            <td>({{ HSVRange[0][0] }}, {{ HSVRange[0][1] }}, {{ HSVRange[0][2] }})</td>
            <td>({{ HSVRange[1][0] }}, {{ HSVRange[1][1] }}, {{ HSVRange[1][2] }})</td>
            <td>
              <Button color='#dc3545' @click="deleteHSVRange(index)" class='delete-row-button'>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
                  <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                  <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708"/>
                </svg>
              </Button>
            </td>
          </tr>
        </tbody>
      </table>

      <div class="add-row-button" @click="addHSVRange">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
          <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2z"/>
          <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
        </svg>
      </div>
    </div>
  </container>

  <container>
    <HSVCustomization :HSVRange="HSVRanges[HSVRangeIndex]"/>
    <CollapsibleContent value="Подсказка по HSV" class="HSVHint">
      <ResizableImage path="/search-hsv-range.png" class="HSVHint-image"/>
    </CollapsibleContent>
  </container>

</template>

<style scoped lang="sass">

.HSVHint
  margin-top: 20px

  .HSVHint-image
    min-height: 200px
    min-width: 200px
    max-width: 470px
    max-height: 350px

table
  font-size: 22px
  border-collapse: separate
  border-spacing: 0 10px

  width: 100%
  margin-top: 15px

  td
    padding: 10px
    text-align: center

    &:first-child
      border-radius: 10px 0 0 10px

    &:last-child
      border-radius: 0 10px 10px 0


tr, .add-row-button

  &:hover
    cursor: pointer

  &:hover:not(.selected_hsv_range)
    background-color: #f1f1f1

.selected_hsv_range
  background-color: #e3e3e3


.add-row-button
  display: flex
  align-items: center
  flex-direction: column

  border-radius: 10px
  padding: 10px
  margin: 0 !important

  svg
    width: 24px

.delete-row-button
  margin: 0 !important

</style>
