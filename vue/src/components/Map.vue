<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
   integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
   crossorigin=""/>

<template>
  <div id="mapview">
  <button v-on:click="initmap"> init </button>
  <h1 v-on:click="ajaxm">map</h1>
    <p>{{ msg }}</p>
    <div id="mapid"></div>
  </div>
</template>

<script>
export default {
  name: 'Map',
  props: {
    msg: String,
  },
  methods:{
    initmap () { 
        // var mymap = L.map('mapid').setView([51.505, -0.09], 13)
        var mymap = this.$L.map('mapid').setView([51.500944, 0.124618], 13);
        this.$L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox/streets-v11',
            tileSize: 512,
            zoomOffset: -1,
            accessToken: 'pk.eyJ1IjoicGludXNjIiwiYSI6ImNraDgyNjRrejA1ZGEycnFpZXU5dTJqMjkifQ.RyyPpqxIelqUtOiWdn4efg'
        }).addTo(mymap);
        this.mymap = mymap;
    },
    async ajaxm () {
      const { data } = await this.$http.get(
              'http://localhost:5000/api/otm?lat=51.500944&lon=0.124618', 
      );
      for (var i = 0; i < data.length; i++) {
        var point = [data[i].point.lat, data[i].point.lon]
        console.log(point)
        this.$L.marker(point).addTo(this.mymap);
      }
      console.log(data);
      // example response: { id: 1, name: "something" }
    }
  }
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
