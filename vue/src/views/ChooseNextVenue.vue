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
                '/api/otm', {
                    params: {
                        lat: this.user_lat,
                        lon: this.user_lon,
                        radius: 50000,
                        categories: this.$root.$data.vuey.category_preference
                    }
                }
            );
            for (var i = 0; i < data.length; i++) {
                var point = [data[i].point.lat, data[i].point.lon]
                console.log(point)
                var marker = this.$L.marker(point);
                marker.addTo(this.$refs.map.mymap);

                var venue = data[i];
                venue.marker = marker;
                this.$refs.vlist.addVenue(venue);
            }  
        }
    },
    created(){
        this.getLocations();
    }

}
</script>
