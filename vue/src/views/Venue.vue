<template>
  <div class="home">
      <p>xid:  {{this.xid}}</p>
      <h1>You're going to <b>{{this.info.name}}</b></h1>
      <div id="wiki-blurb" v-if="hasWikipediaExtracts">
          <h1>{{this.info.wikipedia_extracts.title.substr(3)}}</h1>
          <div v-html="this.info.wikipedia_extracts.html"></div>
      </div>
      <div v-else>
          <p>Unfortunately, we couldn't find more info on this venue. Try using a search engine?</p>
      </div>
      <button @click="finalizeVenue">I'm here</button>

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
      info: function(){
          return this.$root.$data.vuey.venue_detail[this.xid];
      }
  },
  methods:{
    finalizeVenue: function(){
      if (this.info.point.lat == this.$root.$data.vuey.finalDestinationLocation.lat &
        this.info.point.lon == this.$root.$data.vuey.finalDestinationLocation.lon ){
          router.push("Final");
      }else{
        router.push("ChooseNextVenue");
      }
    }
  },
  created() {
      this.xid = this.$route.params.xid;
  }
}
</script>
