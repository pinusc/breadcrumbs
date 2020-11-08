<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
   integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
   crossorigin=""/>

<template>
  <div id="mapview">
  <div id="mapid"></div>
  </div>

</template>

<script>
//import Vue from 'vue'

export default {
  name: 'Map',
  data: function() {
    return{
      venues:[{"name":"a"}],
      destination: {lat: null, lng: null, marker: null}
    }
  },
  props: {
    msg: String,
    isChoosingLocation: Boolean
  },
  computed: {
    user_lat: function(){
      return this.$root.$data.vuey.userCurrentLocation.lat;
    },
    user_lon: function(){
      return this.$root.$data.vuey.userCurrentLocation.lon;
    }
  },
  mounted: function() {
    this.$nextTick(function () {
    // Code that will run only after the
    // entire view has been rendered
        var mymap = this.$L.map('mapid').setView([this.user_lat, this.user_lon], 13);
        this.$L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox/streets-v11',
            tileSize: 512,
            zoomOffset: -1,
            accessToken: 'pk.eyJ1IjoicGludXNjIiwiYSI6ImNraDgyNjRrejA1ZGEycnFpZXU5dTJqMjkifQ.RyyPpqxIelqUtOiWdn4efg'
        }).addTo(mymap);
        this.mymap = mymap;
        var darkIcon = this.$L.icon({iconUrl: '/static/img/marker-icon-darkgreen.png'});
        var userMarker = this.$L.marker([this.user_lat, this.user_lon]).addTo(mymap);
        userMarker.setIcon(darkIcon);
        if (this.isChoosingLocation) {
            setUpLocationChooser(this, mymap);
        }
    })

  }
}

function setUpLocationChooser(that, mymap) {
    console.log("setting up");
    var userMarker = that.$L.marker({lat:that.user_lat, lng:that.user_lon, color: "#FF0000"});
    userMarker.addTo(that.mymap);
    that.destination = {
        lat: that.user_lat,
        lon: that.user_lng,
        marker: userMarker
    }
    that.$root.$data.vuey.finalDestinationLocation = that.destination;

    mymap.on('click', function(e) {
        if (that.destination.marker) {
            that.destination.marker.removeFrom(that.mymap);
        }

        var marker = that.$L.marker(e.latlng);
        marker.addTo(that.mymap);
        that.destination = {
            lat: e.latlng.lat,
            lon: e.latlng.lng,
            marker
        }
        that.$root.$data.vuey.finalDestinationLocation = that.destination;
    });
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
#mapid { height: 500px; }
</style>
