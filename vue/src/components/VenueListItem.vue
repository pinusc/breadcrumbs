<template>
    <div>
        <p v-on:click="toggleExpand">I'm a venue! {{venue.name}}</p>
        <div v-if="expanded">
            <div v-if="dataLoaded">
                <div id="wiki-blurb" v-if="hasWikipediaExtracts">
                    <h1>{{this.info.wikipedia_extracts.title.substr(3)}}</h1>
                    <div v-html="this.info.wikipedia_extracts.html"></div>
                </div>
                <div v-else>
                    <p>Unfortunately, we couldn't find more info on this venue. Try using a search engine?</p>
                </div>
                <router-link :to="{name: 'Venue', params: {xid: this.venue.xid}}" ><button>I wanna go to this location!</button></router-link>
            </div>
        </div>
    </div>
</template>

<script>
import router from '../router'

export default {
  name: 'VenueListItem',
  props: ["venue"],
  data: function(){
      return {
          expanded: false,
          dataLoaded: false
      }
  },
  
  computed: {
      hasAdress: function(){
          return 'address' in this.$root.$data.vuey.venue_detail[this.venue.xid]
      },
      hasWikipediaLink: function(){
          return 'wikipedia' in this.$root.$data.vuey.venue_detail[this.venue.xid]
      },
      hasWikipediaExtracts: function(){
          return 'wikipedia_extracts' in this.$root.$data.vuey.venue_detail[this.venue.xid]
      },
      info: function(){
          return this.$root.$data.vuey.venue_detail[this.venue.xid];
      }

  },
  methods:{
      async toggleExpand(){
          this.expanded = !this.expanded
          if(this.expanded){
            if(! this.dataLoaded){
                console.log("heys");
                // make ajax request and load data
                const { data } = await this.$http.get(
                    'http://localhost:5000/api/otm/detail', {
                        params: {
                            xid: this.venue.xid
                        }
                    }
                );
                console.log(data);
                this.dataLoaded = true;
                this.$root.$data.vuey.venue_detail[this.venue.xid] = data;

            }
          }
      },
      selectVenue(){
          router.push("Venue")
      }
    
  }
}
</script>

<style scoped>

</style>
