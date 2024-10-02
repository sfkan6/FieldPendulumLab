

const toggleAnimationClass = (element) => element.classList.toggle('show_and_hide')

const animation = (element, time=2) => {
  toggleAnimationClass(element)
  setTimeout(() => toggleAnimationClass(element), time * 1000);
}

const showNotification = (notification) => {
  if (notification) {
    animation(notification, 2)
  }
}

export const showFailureNotification = () => {
  const notification = document.querySelector('#failure-notification')
  showNotification(notification)
}
export const showSuccessNotification = () => {
  const notification = document.querySelector('#success-notification')
  showNotification(notification)
}


