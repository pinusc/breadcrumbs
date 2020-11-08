import Vue from 'vue'
import router from './router'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

import L from 'leaflet'
Object.defineProperty(Vue.prototype, '$L', { value: L });
