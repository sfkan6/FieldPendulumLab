<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { getCreatingComponentByDataType } from './config'
import Page from "./component.vue";


let { dataType } = defineProps({
  dataType: String,
})


const route = useRoute()

watch(route, async (newRoute, oldRoute) => {
  dataType = newRoute.params.dataType
})

const CreatingComponent = getCreatingComponentByDataType(dataType)
</script>

<template>
  <PageContentWrapper class='wrapper'>
    <Page :dataType="dataType" :creatingComponent="CreatingComponent" :key="dataType"/>
  </PageContentWrapper>
</template>

<style scoped lang="sass">

.wrapper
  display: inline-flex
  flex-direction: row
  justify-content: space-evenly
  flex-wrap: wrap
  align-items: flex-start

</style>
