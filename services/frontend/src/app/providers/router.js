import { createWebHistory, createRouter } from 'vue-router'
import { routes } from './routes.js'

export const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.hasOwnProperty('active') && to.meta.active) {
    const meta = to.meta
    delete meta.active

    for (let key of Object.keys(meta)) {
      to.meta[key] = to.meta[key](to)
    }
  }
  document.title = to.meta.title;
  next();
});

