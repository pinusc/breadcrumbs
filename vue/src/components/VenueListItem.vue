<template>
    <div class="box is-clickable has-shadow">
        <p class="subtitle has-text-weight-semibold" v-on:click="toggleExpand" v-bind:class="{active: expanded}">{{venue.name}}</p>
        <div v-if="expanded">
            <div v-if="dataLoaded">
                <div id="preview" v-if="hasPreview">
                    <img :src="this.info.preview.source">
                </div>
                <div id="wiki-blurb" v-if="hasWikipediaExtracts">
                    <div v-html="this.info.wikipedia_extracts.html"></div>
                </div>
                <div v-else>
                    <p>Unfortunately, we couldn't find more info on this venue. Try using a search engine?</p>
                </div>
                <router-link :to="{name: 'Venue', params: {xid: this.venue.xid}}" ><button class="button is-light">I wanna go to this location!</button></router-link>
            </div>
            <div v-else>
                <progress class="progress is-small is-primary" max="100"></progress>
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
          dataLoaded: false,
          redIcon: this.$L.icon({iconUrl: '/static/img/marker-icon-red.png'}),
          blueIcon: this.$L.icon({iconUrl: '/static/img/marker-icon.png'})
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
      hasPreview: function(){
        return 'preview' in this.$root.$data.vuey.venue_detail[this.venue.xid]
      },
      info: function(){
          return this.$root.$data.vuey.venue_detail[this.venue.xid];
      }

  },
  methods:{
      async toggleExpand(){
          this.expanded = !this.expanded
          if(this.expanded){
              this.venue.marker.setIcon(this.redIcon);
              if (this.venue.xid in this.$root.$data.vuey.venue_detail){
                  this.dataLoaded = true;
              }

              if(! this.dataLoaded){
                  console.log("heys");
                  // make ajax request and load data
                  const { data } = await this.$http.get(
                      '/api/otm/detail', {
                          params: {
                              xid: this.venue.xid
                          }
                      }
                  );
                  console.log(data);
                  this.dataLoaded = true;
                  this.$root.$data.vuey.venue_detail[this.venue.xid] = data;
              }
          } else {
              this.venue.marker.setIcon(this.blueIcon);
          }
      },
      selectVenue(){
          router.push("Venue")
      }
    
  }
}
</script>

<style scoped>
.active{
    font-weight: bold;
}
</style>
