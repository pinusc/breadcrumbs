<template>
  <div id="app">
    <h1>Breadcrumbs</h1>
    <LocationManager />
    <Map msg="Welcome to Your Vue.js App"/>
    <div class="notification">
  <button class="delete"></button>
  Lorem ipsum dolor sit amet, consectetur
  adipiscing elit lorem ipsum dolor. <strong>Pellentesque risus mi</strong>, tempus quis placerat ut, porta nec nulla. Vestibulum rhoncus ac ex sit amet fringilla. Nullam gravida purus diam, et dictum <a>felis venenatis</a> efficitur. Sit amet,
  consectetur adipiscing elit
</div>
  </div>
</template>

<script>
import Map from './components/Map.vue'
import LocationManager from './components/LocationManager.vue'

export default {
  name: 'App',
  components: {
    Map,
    LocationManager
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
