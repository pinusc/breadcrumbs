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
          <div class="box has-background-info">
              <h1 class="subtitle has-text-light">Where would you like to end your trip at?</h1>
              <button class="button is-link" @click="setTargetLocation('userLocation')">Where I am right now</button>
              OR
              <p> Function to be added: choose destination </p>
              
          </div>
      </section>
    
  </div>
</template>

<script>
// @ is an alias to /src
import LocationManager from '@/components/LocationManager.vue'
import router from '@/router'

export default {
    name: 'Destination',
    components: {
      LocationManager
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
