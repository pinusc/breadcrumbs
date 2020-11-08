<template>
  <div class="home">
    
      <section class="hero is-primary">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            breadcrumbs
          </h1>
          <h2 class="subtitle">
            Explore cities, the better way...
          </h2>
          
      <div v-if="!this.$root.$data.vuey.userLocation">
          <h1 class="subtitle has-text-light">We need your current location to suggest venues.</h1>
          <LocationManager />
      </div>
      <router-link v-else to="/Destination">
      <button  class="button is-primary is-light">Start</button>
      </router-link>  
          </div>
        </div>
      </section>

        <figure class="image">
        <img src="../assets/city.jpeg">
      </figure>
      
  </div>
</template>

<script>
// @ is an alias to /src
import LocationManager from '@/components/LocationManager.vue'

export default {
  name: 'Home',
  components: {
      LocationManager
    }
}
</script>
