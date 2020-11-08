<template>
  <div class="home">
      <router-link to="/Venue">Go to this venue</router-link>
      <Map/>
  </div>
</template>

<script>
// @ is an alias to /src

import Map from '@/components/Map.vue'
export default {
  name: 'ChooseNextVenue',
  components: {
    Map
  }
}
</script>
