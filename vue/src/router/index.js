import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Start from '../views/Start.vue'
import Final from '../views/Final.vue'
import Venue from '../views/Venue.vue'
import Destination from '../views/Destination.vue'
import ChooseNextVenue from '../views/ChooseNextVenue.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    },
    {
        path: '/Start',
        component: Start
    },
    {
        path: '/Destination',
        component: Destination
    },
    {
        path: '/ChooseNextVenue',
        component: ChooseNextVenue
    },
    {
        path: '/Venue',
        component: Venue
    },
    {
        path: '/Final',
        component: Final
    },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
