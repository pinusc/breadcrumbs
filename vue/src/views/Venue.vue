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

function distance(loc1, loc2) {
    var lat1 = loc1.lat;
    var lat2 = loc2.lat;
    var lon1 = loc1.lon;
    var lon2 = loc2.lon;

	if ((lat1 == lat2) && (lon1 == lon2)) {
		return 0;
	}
	else {
		var radlat1 = Math.PI * lat1/180;
		var radlat2 = Math.PI * lat2/180;
		var theta = lon1-lon2;
		var radtheta = Math.PI * theta/180;
		var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
		if (dist > 1) {
			dist = 1;
		}
		dist = Math.acos(dist);
		dist = dist * 180/Math.PI;
		dist = dist * 60 * 1.1515;
		dist = dist * 1.609344 * 1000 // to km, and then meters
		return dist;
	}
}

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
        // u:user p:point
        var d_u2p = distance({"lat":this.info.point.lat , "lon":this.info.point.lon}, this.$root.$data.vuey.userCurrentLocation);

        this.$root.$data.vuey.walkDistance = this.$root.$data.vuey.walkDistance - d_u2p

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
