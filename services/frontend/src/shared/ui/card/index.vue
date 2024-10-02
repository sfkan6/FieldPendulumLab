<script setup>
</script>

<template>
  <container class='card'>
    <slot/>
  </container>
</template>

<style scoped lang="sass">

.card
  margin: 20px !important

  &:hover 
    box-shadow: 0px 10px 16px 4px #DBDBDB
    transition-duration: 0.1s
    transition-timing-function: linear
    /*transform: scale(1.005)*/

</style>
