<script setup>
import { getComponentByPath } from './config'
import { useRoute } from 'vue-router'
import { ref, watch } from 'vue'


let { path } = defineProps({
  path: String,
})

const route = useRoute()

watch(route, async (newRoute, oldRoute) => {
  path = newRoute.params.path
})

const Component = getComponentByPath(path)

</script>

<template>
  <PageContentWrapper class='wrapper'>
    <AsyncWrapper>
      <component :is="Component"/>
    </AsyncWrapper>
  </PageContentWrapper>
</template>

<style scoped lang="sass">
.wrapper
  display: flex
  flex-wrap: wrap
  flex-direction: row
  align-items: flex-start
  justify-content: space-between


@media screen and (max-width: 800px)
  .wrapper
    align-items: center !important
    flex-direction: column !important


</style>
