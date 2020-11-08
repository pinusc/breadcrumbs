import Vue from 'vue'
import router from './router'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

Vue.config.productionTip = false

var store = {
    state: {
        message: 'Hello!',
        userLocation: null,
        userCurrentLocation: null,
        finalDestinationLocation: null,
        venue_detail: {},
        category_preference: "interesting_places",
        walkDistance: 1000
    }
}

new Vue({
    router,
    render: h => h(App),
    data: {
        vuey: store.state,
    }
}).$mount('#app')

import L from 'leaflet'
Object.defineProperty(Vue.prototype, '$L', { value: L });
