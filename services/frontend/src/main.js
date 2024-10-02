import { createApp } from 'vue'
import { App, router } from '@/app'
import { Container, AsyncWrapper, PageContentWrapper } from './shared/ui'

const app = createApp(App)

app.component('container', Container)
app.component('AsyncWrapper', AsyncWrapper)
app.component('PageContentWrapper', PageContentWrapper)
app
  .use(router)
  .mount('#app')
