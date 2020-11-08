<template>
  <div class="home">

    
      <section class="hero is-primary is-bold">
          <div class="hero-body">
              <h1 class=title>Breadcrumbs</h1>
          </div>
      </section>


    <section>
      <div class="box has-background-info">
          <h1 class="subtitle has-text-light">We need your current location to suggest venues.</h1>

          <LocationManager />
          
      </div>
    </section>



      <section>
          <div class="box has-background-info">
              <h1 class="subtitle has-text-light">Where would you like to end your trip at?</h1>

              <button class="button is-link">Where I am right now</button>
              OR
              <p> Function to be added: choose destination </p>
              
          </div>
      </section>
    
      

      <router-link to="/">Choose a destination</router-link>
  </div>
</template>

<script>
// @ is an alias to /src
import LocationManager from '@/components/LocationManager.vue'

export default {
    name: 'Destination',
    components: {
      LocationManager
    }
}
</script>

<style scoped lang=scss>
.card {
    margin: 1em;
}

#categories-list .box {
    margin: 0.5em;
}
</style>
