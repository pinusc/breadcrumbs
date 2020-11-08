<template>
  <div class="home">
      <router-link to="/Start">Start</router-link>
    <Map />
  </div>
</template>

<script>
// @ is an alias to /src
import Map from '@/components/Map.vue'

export default {
  name: 'Home',
  components: {
    Map
  }
}
</script>
