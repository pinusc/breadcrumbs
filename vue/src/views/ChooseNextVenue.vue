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
distance({"lat":1,"lon":1},{"lat":1,"lon":1});

export default {
    name: 'ChooseNextVenue',
    components: {
        Map,
        VenueList
    },
    computed: {
        user_lat: function(){
            return this.$root.$data.vuey.userCurrentLocation.lat;
        },
        user_lon: function(){
            return this.$root.$data.vuey.userCurrentLocation.lon;
        }
    },
    methods: {
        async getLocations () {
            const { data } = await this.$http.get(
                '/api/otm', {
                    params: {
                        lat: this.user_lat,
                        lon: this.user_lon,
                        radius: this.$root.$data.vuey.walkDistance/2,
                        categories: this.$root.$data.vuey.category_preference
                    }
                }
            );
            if(! ("SPECIAL_TARGET" in this.$root.$data.vuey.venue_detail)){
            
                var targetObject = {
                    "xid": "SPECIAL_TARGET",
                    "name": "Your Designated Target Marker",
                    point: this.$root.$data.vuey.finalDestinationLocation,
                    wikipedia_extracts: {
                        "html": "This label represents the target destination you designated at the start of the application. You can use this as place to visit in order to get directions and/or finish your breadcrumb experience. Thanks for using breadcrumb and exploring the city with us!"
                    }
                
                }
                this.$root.$data.vuey.venue_detail["SPECIAL_TARGET"] = targetObject;
                data.unshift(targetObject);
            }

            for (var i = 0; i < data.length; i++) {
                var point = [data[i].point.lat, data[i].point.lon]

                // u:user p:point t:target
                var d_u2p = distance({"lat":data[i].point.lat, "lon":data[i].point.lon}, this.$root.$data.vuey.userCurrentLocation);
                var d_p2t = distance({"lat":data[i].point.lat, "lon":data[i].point.lon}, this.$root.$data.vuey.finalDestinationLocation);
                //var d_u2t = distance(this.$root.$data.vuey.userCurrentLocation, this.$root.$data.vuey.finalDestinationLocation);

                if (d_u2p + d_p2t < this.$root.$data.vuey.walkDistance * 0.95){
                    var marker = this.$L.marker(point);
                    marker.addTo(this.$refs.map.mymap);

                    var venue = data[i];
                    venue.marker = marker;
                    this.$refs.vlist.addVenue(venue);
                }
                
                
            }  
        }
    },
    created(){
        this.getLocations();
    }

}
</script>
