<script setup>

const props = defineProps({
  color: {
    type: String,
    default: "#0f5132",
  },
  background: {
    type: String,
    default: "#d1e7dd",
  },
})

</script>


<template>
  <div class='notification'>
    <slot/>
  </div>
</template>


<style scoped lang="sass">
$color: v-bind('props.color')
$background: v-bind('props.background')

.notification
  position: absolute
  padding: 15px 20px
  margin: 0 auto

  border-radius: 8px
  background-color: $background
  color: $color

  display: flex
  justify-content: space-evenly
  align-items: center
  opacity: 0

  :deep(svg)
    fill: $color
    width: 24px
    margin-right: 10px

</style>
