<script setup>
const props = defineProps({
  color: {
    type: String,
    default: "#212529",
  },
})
</script>

<template>
  <button class="btn">
    <slot/>
  </button>
</template>


<style scoped lang='sass'>
$color: v-bind('props.color')

.transition-style
  transition-property: fill, color, background-color, border-color, box-shadow
  transition-duration: .15s
  transition-timing-function: ease-in-out

.btn
  @extend .transition-style

  font-size: 16px
  line-height: 1.5
  padding: 6px 7px
  margin: 10px

  color: $color
  background-color: transparent
  border: 1px solid $color
  border-radius: 4px

  display: inline-flex
  align-items: center

  &:hover 
    cursor: pointer
    color: white
    background-color: $color

  &:hover :deep(svg)
    fill: #ffffff

  :deep(svg)
    @extend .transition-style
    width: 20px
    margin: 0 3px
    fill: $color

</style>
