<script setup>
const props = defineProps({
  background: {
    type: String,
    default: "#fafafa",
  },
})
</script>

<template>
  <div class="wrapper">
    <slot/>
  </div>
</template>

<style scoped lang='sass'>
$background: v-bind('props.background')

.wrapper
  width: 100%
  min-height: 700px 

  background-color: $background
  border-radius: 15px
  padding: max(10px, 3%) max(10px, 4%)
  box-sizing: border-box

</style>
