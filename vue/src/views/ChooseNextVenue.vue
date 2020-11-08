<template>
  <div class="home">

    <section class="hero is-primary">
          <div class="hero-body">
            <div class="container">
              <h1 class="title">
        <h1>Where to <b>next?</b></h1>
              </h1>
              <h2 class="subtitle">
                A little exploration goes a long way!
              </h2>
            </div>
          </div>
        </section>

      <Map ref="map"/>
      <VenueList ref="vlist"/>
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
                        radius: 5000,
                        categories: this.$root.$data.vuey.category_preference
                    }
                }
            );
            for (var i = 0; i < data.length; i++) {
                var point = [data[i].point.lat, data[i].point.lon]

                

                this.$L.marker(point).addTo(this.$refs.map.mymap);

                this.$refs.vlist.addVenue(data[i]);
            }  
        }
    },
    created(){
        this.getLocations();
    }

}
</script>
