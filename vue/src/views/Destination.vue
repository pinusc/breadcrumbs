<template>
  <div class="home">
      <section class="hero is-primary is-bold">
          <div class="hero-body">
              <h1 class=title>Breadcrumbs</h1>
          </div>
      </section>
    <section v-if="!this.$root.$data.vuey.userLocation">
      <div class="box has-background-info">
          <h1 class="subtitle has-text-light">We need your current location to suggest venues.</h1>
          <LocationManager />
      </div>
    </section>
      <section v-if="this.$root.$data.vuey.userLocation">
          <div class="box has-background-info has-text-centered">
              <h1 class="subtitle has-text-light">Where would you like to end your trip at?</h1>
              <button class="button is-warning mb-4" @click="setTargetLocation('userLocation')">Where I am right now</button>
              <Map v-bind:is-choosing-location=true />
                  <router-link to="Start" class="button is-warning mt-4">The map marker</router-link>
          </div>
      </section>
  </div>
</template>

<script>
// @ is an alias to /src
import LocationManager from '@/components/LocationManager.vue'
import Map from '@/components/Map.vue'
import router from '@/router'

export default {
    name: 'Destination',
    components: {
      LocationManager,
      Map
    },
    data: function(){
      return {
        "test": 1
      }
    },
    methods: {
      setTargetLocation: function(location){
        if(location == "userLocation"){
          this.$root.$data.vuey.finalDestinationLocation = this.$root.$data.vuey.userLocation;
        }
        router.push("Start");
      },
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
