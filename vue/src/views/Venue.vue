<template>
  <div class="home">

      <section class="hero is-primary">
          <div class="hero-body">
            <div class="container">
              <h1 class="title">
        <h1>You're going to <b>{{this.info.name}}</b></h1>
              </h1>
              <h2 class="subtitle">
                Don't forget to enjoy your journey!
              </h2>
            </div>
          </div>
        </section>



      
      <div class="box is-clearfix">
        <div id="preview" v-if="hasPreview">
          <img :src="this.info.preview.source">
        </div>
        <div id="wiki-blurb" v-if="hasWikipediaExtracts">

            <div v-html="this.info.wikipedia_extracts.html"></div>
        </div>
        <div v-else>
            <p>Unfortunately, we couldn't find more info on this venue. Try using a search engine?</p>
        </div>
        <a :href="directionsUrl" target="_blank"><button class="button is-pulled-left is-light">Get Directions</button></a>
        <button class="button is-pulled-right is-primary" @click="finalizeVenue">I'm here</button>
      </div>

  </div>
</template>

<script>
// @ is an alias to /src
import router from '@/router'

export default {
  name: 'Venue',
  data: function(){
    return {
      xid:-1
    }
  },
  computed:{
      hasAdress: function(){
          return 'address' in this.$root.$data.vuey.venue_detail[this.xid]
      },
      hasWikipediaLink: function(){
          return 'wikipedia' in this.$root.$data.vuey.venue_detail[this.xid]
      },
      hasWikipediaExtracts: function(){
          return 'wikipedia_extracts' in this.$root.$data.vuey.venue_detail[this.xid]
      },
      hasPreview: function(){
        return 'preview' in this.$root.$data.vuey.venue_detail[this.xid]
      },
      info: function(){
          return this.$root.$data.vuey.venue_detail[this.xid];
      },
      directionsUrl: function(){
        var currLocation = this.$root.$data.vuey.userCurrentLocation;
        var destLocation = this.info.point
        return "https://www.google.com/maps/dir/" +
          currLocation.lat.toString() + "," + currLocation.lon.toString() + "/" + 
          destLocation.lat.toString() + "," + destLocation.lon.toString();
      }
  },
  methods:{
    finalizeVenue: function(){
      if (this.info.point.lat == this.$root.$data.vuey.finalDestinationLocation.lat &
        this.info.point.lon == this.$root.$data.vuey.finalDestinationLocation.lon ){
          router.push("Final");
      }else{
        this.$root.$data.vuey.userCurrentLocation = {
          "lat": this.info.point.lat,
          "lon": this.info.point.lon
        };
        router.push("ChooseNextVenue");
      }
    }
  },
  created() {
      this.xid = this.$route.params.xid;
  }
}
</script>
