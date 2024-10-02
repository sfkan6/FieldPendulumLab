<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import { NavBar } from '@/widgets/NavBar'
</script>

<template>
  <header>
    <NavBar color='#4e23ab' hover_color='#8059d4'/>
  </header>
  <main>
    <RouterView />
  </main>
</template>

<style lang="sass">
@import '@/app/assets/style.sass'

header 
  padding: 2% 5%

main
  display: flex
  padding: 2% 5%
  padding-top: 10px

</style>
