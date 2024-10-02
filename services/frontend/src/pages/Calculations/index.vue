<script setup>
import { 
  AttenuationCoefficient, NaturalFrequency, NaturalFrequencyByResonant,
  ARCErrors, Frequencies, QualityFactor 
  } from '@/widgets/Calculations'

</script>

<template>
  <PageContentWrapper class='wrapper'>
    <div class='title'>Вычисления</div>
    <div class='calculators'>
      <AsyncWrapper>
        <QualityFactor/>
        <NaturalFrequencyByResonant/>
        <Frequencies/>
        <NaturalFrequency/>
        <AttenuationCoefficient/>
        <ARCErrors/>
      </AsyncWrapper>
    </div>
  </PageContentWrapper>
</template>


<style scoped lang="sass">

.title
  text-align: center
  font-size: 26px
  font-weight: bold
  margin-bottom: 25px


.wrapper
  display: flex
  flex-direction: column
  flex-wrap: wrap
  align-items: center
  justify-content: space-around


.calculators
  display: flex
  flex-direction: row
  flex-wrap: wrap
  justify-content: space-around
  align-items: flex-start

</style>
