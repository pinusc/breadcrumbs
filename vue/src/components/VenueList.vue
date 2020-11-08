<template>
    <div>
        <VenueListItem v-for="venue in venues" v-bind:key="venue.name" v-bind:venue="venue" />
        <p>hey</p>
    </div>
</template>

<script>
import VenueListItem from './VenueListItem.vue'

export default {
  name: 'VenueList',
  components:{
      VenueListItem
    },
    data: function() {
        return{
        venues:[{"name":"a"}]
        }
    },
    methods:{
      addVenue(newVenue){
          this.venues.push(newVenue);
      }
  }
}
</script>

<style scoped>

</style>