<template>
  <div class="home">
      <section class="hero is-primary">
          <div class="hero-body">
            <div class="container">
              <h1 class="title">
        <h1>Where would you like to end your trip?</h1>
              </h1>
              <h2 class="subtitle">
                Every explorer deserves a break...
              </h2>
            </div>
          </div>
        </section>

      <section v-if="this.$root.$data.vuey.userLocation">
          <div class="box has-background-info has-text-centered">
              <button class="button is-warning mb-4" @click="setTargetLocation('userLocation')">Where I am right now</button>
              <hr />
              <Map v-bind:is-choosing-location=true />
                  <router-link to="Start" class="button is-warning mt-4">The map marker</router-link>
          </div>
      </section>
  </div>
</template>

<script>
// @ is an alias to /src

import Map from '@/components/Map.vue'
import router from '@/router'

export default {
    name: 'Destination',
    components: {
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

#or {
  color: white;
}

#categories-list .box {
    margin: 0.5em;
}
</style>
