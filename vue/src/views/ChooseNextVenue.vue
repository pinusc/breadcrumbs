<template>
  <div class="home">
      <router-link to="/Venue">Go to this venue</router-link>
      <VenueList ref="vlist"/>
      <button v-on:click="getLocations"> Get Locations </button>
      <Map ref="map"/>
  </div>
</template>

<script>
// @ is an alias to /src

import Map from '@/components/Map.vue'
import VenueList from '@/components/VenueList.vue'

export default {
    name: 'ChooseNextVenue',
    components: {
        Map,
        VenueList
    },
    computed: {
        user_lat: function(){
            return this.$root.$data.vuey.userLocation.lat;
        },
        user_lon: function(){
            return this.$root.$data.vuey.userLocation.lon;
        }
    },
    methods: {
        async getLocations () {
            const { data } = await this.$http.get(
                'http://localhost:5000/api/otm', {
                    params: {
                        lat: this.user_lat,
                        lon: this.user_lon,
                        radius: 5000
                    }
                }
            );
            for (var i = 0; i < data.length; i++) {
                var point = [data[i].point.lat, data[i].point.lon]
                console.log(point)
                this.$L.marker(point).addTo(this.$refs.map.mymap);

                this.$refs.vlist.addVenue(data[i]);
            }  
        }
    }

}
</script>
