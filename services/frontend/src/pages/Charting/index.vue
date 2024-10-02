<script setup>
import Page from "./component.vue"
import { chartsConfigData } from "./config.js"

const { chartType } = defineProps({
  chartType: {
    type: String,
    required: true,
  },
})

</script>

<template>
  <PageContentWrapper class='wrapper'>
    <AsyncWrapper>
      <Page :chartConfigData="chartsConfigData[chartType]" :chartType="chartType"/>
    </AsyncWrapper>
  </PageContentWrapper>
</template>


<style scoped lang="sass">

.wrapper
  display: flex
  flex-direction: row
  flex-wrap: wrap
  align-items: flex-start
  justify-content: space-around

</style>
