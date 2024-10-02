<script setup>

</script>

<template>
  <Suspense>
    <template #default>
      <slot/>
    </template>
    <template #fallback>
      <div>Loading...</div>
    </template>
  </Suspense>
</template>

<style scoped lang="sass">

.wrapper
  display: flex
  flex-direction: column
  flex-wrap: wrap
  align-items: center

</style>
