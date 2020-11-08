<template>
    <div>
        <p v-on:click="toggleExpand">I'm a venue! {{venue.name}}</p>
        <div v-if="expanded">
            <div id="wiki-blurb" v-if="hasWikipediaExtracts">
                <h1>{{this.info.wikipedia_extracts.title.substr(3)}}</h1>
                <div v-html="this.info.wikipedia_extracts.html"></div>
            </div>
            <div v-else>
                <p>Unfortunately, we couldn't find more info on this venue. Try using a search engine?</p>
            </div>
            <button v-on:click="selectVenue">I wanna go to this location!</button>
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
          dataLoaded: false,
          info: {}
      }
  },
  
  computed: {
      hasAdress: function(){
          return ('address' in this.info)
      },
      hasWikipediaLink: function(){
          return ('wikipedia' in this.info)
      },
      hasWikipediaExtracts: function(){
          return ('wikipedia_extracts' in this.info)
      }
  },
  methods:{
      async toggleExpand(){
          this.expanded = !this.expanded
          if(this.expanded){
            if(!this.dataLoaded){
                // make ajax request and load data

                const { data } = await this.$http.get(
                        'http://localhost:5000/api/otm/detail', {
                            params: {
                                xid: this.venue.xid
                            }
                        }
                );
                this.info = data;
                this.dataLoaded = true;

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
