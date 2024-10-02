<script setup>
import { Notification } from '@/shared/ui/notification'
 
</script>


<template>
  <div class='notifications'>
    <Notification color="#0f5132" background="#d1e7dd" id='success-notification'>
      <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
        <path d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0"/>
      </svg>
      Успешно
    </Notification>
    <Notification color="#842029" background="#f8d7da" id='failure-notification'>
      <svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 16 16">
        <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z"/>
      </svg>
      Ошибка
    </Notification>
  </div>
</template>


<style scoped lang="sass">

.notifications
  position: absolute
  left: calc((100% - 155px) / 2)
  
  > *
    display: none


.show_and_hide
  animation: fadeinout 2s linear forwards
  display: flex

@keyframes fadeinout
  0%,100%
    opacity: 0
    display: none

  33%,66%
    opacity: 1

</style>
