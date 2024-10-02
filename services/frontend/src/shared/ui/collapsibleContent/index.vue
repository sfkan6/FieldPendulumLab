<script setup>
import { ref } from "vue"

const { value } = defineProps({
  value: {
    type: String,
    required: true
  },
})


const isShow = ref(false)
const toggleShow = () => isShow.value = !isShow.value

</script>


<template>
  <div class="collapsible-content">
    <div class='label'>
      {{ value }}

      <div class="collapse-buttons" @click='toggleShow'>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16" v-show="isShow">
          <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707z"/>
        </svg>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16" v-show="!isShow">
          <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.5 4.5a.5.5 0 0 0-1 0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293z"/>
        </svg>
      </div>
    </div>

    <transition name="fade">
      <div v-show="isShow" class="content">
        <slot/>
      </div>
    </transition>
  </div>
</template>


<style scoped lang='sass'>

.fade-enter-active, .fade-leave-active
  transition: opacity 0.3s ease

.fade-enter-from, .fade-leave-to
  opacity: 0


.collapsible-content
  display: flex
  align-items: flex-start
  flex-direction: column

  .content
    margin-top: 15px

  .label
    display: flex
    flex-direction: row

    .collapse-buttons
      display: flex
      align-items: center
      margin-left: 10px

      &:hover
        cursor: pointer

      svg
        width: 22px

</style>
