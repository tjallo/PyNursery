import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/locations',
    name: 'Locations',
    component: () => import('../views/Locations.vue')
  },
  {
    path: '/plant_families',
    name: 'PlantFamilies',
    component: () => import('../views/PlantFamilies.vue')
  },
  {
    path: '/plants',
    name: 'Plants',
    component: () => import('../views/Plants.vue')
  },
  {
    path: '/trays',
    name: 'Trays',
    component: () => import('../views/Trays.vue')
  },
  {
    path: '/plant_batch',
    name: 'Plant Batch',
    component: () => import('../views/PlantBatch.vue')
  },

]

const router = new VueRouter({
  mode: 'history',
  routes: routes
})

export default router
