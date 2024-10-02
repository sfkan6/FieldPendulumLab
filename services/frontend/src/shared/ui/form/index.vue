<script setup>
</script>

<template>
  <div class="form">
    <slot/>
  </div>
</template>


<style scoped lang='sass'>

.from
  text-align: left

  display: flex
  flex-direction: column
  align-items: stretch


.form > *:not(.not-field)
  display: flex
  flex-direction: row
  flex-wrap: wrap
  justify-content: space-between
  align-items: flex-start

  letter-spacing: 1px
  word-break: break-all
  margin-bottom: 10px

  div:first-child
    margin-right: 20px

</style>
