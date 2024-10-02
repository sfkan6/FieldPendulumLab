<template>
  <div class="container">
    <slot/>
  </div>
</template>

<script setup>
const props = defineProps({
  background: {
    type: String,
    default: "#fafafa",
  },
})
</script>

<style scoped lang='sass'>
$background: v-bind('props.background')

.container
  padding: 25px 20px
  margin: 15px 20px
  border-radius: 10px
  box-shadow: 0 1px 8px rgb(0 0 0 / 10%)
  background-color: white

</style>
