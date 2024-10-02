<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import Page from "./component.vue";


let { dataType } = defineProps({
  dataType: String,
})

const route = useRoute()
let title = route.meta.title

watch(route, async (newRoute, oldRoute) => {
  dataType = newRoute.params.dataType
  title = newRoute.meta.title
})

</script>

<template>
  <PageContentWrapper class='wrapper'>
    <AsyncWrapper>
      <Page :dataType="dataType" :title="title" :key="dataType"/>
    </AsyncWrapper>
  </PageContentWrapper>
</template>

<style scoped lang="sass">

.wrapper
  display: flex
  flex-direction: column
  flex-wrap: wrap
  align-items: stretch

</style>
