<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import Page from "./component.vue";


let { dataType, name } = defineProps({
  dataType: String,
  name: String,
})

const route = useRoute()

watch(route, async (newRoute, oldRoute) => {
  dataType = newRoute.params.dataType
  name = newRoute.params.name
})


</script>

<template>
  <PageContentWrapper class='wrapper'>
    <AsyncWrapper>
      <Page :dataType="dataType" :currentName="name" :key="dataType + name"/>
    </AsyncWrapper>
  </PageContentWrapper>
</template>

<style scoped lang="sass">

.wrapper
  display: flex
  flex-direction: column
  flex-wrap: wrap
  align-items: center

</style>
