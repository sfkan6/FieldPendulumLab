<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  value: {
    type: String,
    default: "Dropdown",
  },
  background: {
    type: String,
    default: "#f1f1f1",
  },
  hover: {
    type: String,
    default: "#ddd",
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

</script>


<template>
  <div class="dropdown">
    <div class='label'>
      {{ value }}
      <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
        <path d="M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"/>
      </svg>
    </div>
    <div class="content-wrapper">
      <slot/>
    </div>
  </div>
</template>

<style scoped lang='sass'>
$background: v-bind('props.background')
$hover: v-bind('props.hover')
$maxHeight: v-bind('props.maxHeight')
$width: v-bind('props.width')
$verticalShift: v-bind('props.verticalShift')

.dropdown
  position: relative
  display: inline-block
  padding: 0
  height: 100%

  &:hover .content-wrapper > *
    display: flex

.label
  padding: 13px 24px

svg
  margin-left: 10px

.content-wrapper > *
  bottom: $verticalShift
  max-height: $maxHeight
  overflow-y: scroll

  color: red
  position: absolute
  overflow-y: auto

  display: none
  flex-direction: column
  align-items: center

  background-color: $background
  width: $width

  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2)
  border-radius: 6px
  border: 1px solid rgba(0,0,0,.15)

  padding: 7px
  box-sizing: border-box

  > *
    color: black
    display: block
    width: 100%

    padding: 10px 20px
    box-sizing: border-box

    border-radius: inherit
    word-break: break-word
    
    &:hover
      background-color: $hover


::-webkit-scrollbar
  width: 10px
  background-color: transparent

::-webkit-scrollbar-thumb
  background-color: #c5c5c5
  border-radius: 10px


</style>
