<template>
  <div class="home">
      <section class="hero is-primary is-bold">
          <div class="hero-body">
              <h1 class=title>Breadcrumbs</h1>
          </div>
      </section>
      <div class="box has-background-info is-size-5" @click="updateCategoryPreference">
          <h1 class="subtitle has-text-light">What kind of places would you like to see?</h1>
          <ul id=categories-list>
              <li v-for="i in categories.length" :key=i>
                  <div class="box" >
                      <label class="checkbox">
                          <span class="checkbox__input">
                              <input type="checkbox" name="checked" checked v-model="categoriesChecked[i-1]">
                              <span class="checkbox__control">
                                  <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' aria-hidden="true" focusable="false">
                                      <path fill='none' stroke='currentColor' stroke-width='3' d='M1.73 12.91l6.37 6.37L22.79 4.59' /></svg>
                              </span>
                          </span>
                          <span v-bind:class="{ 'has-text-weight-bold': categoriesChecked[i-1] }" class="radio__label">{{ categoryNames[i-1] }}</span>
                      </label>
                  </div>
              </li>
          </ul>
      </div>
      <div id="walk-distance-box" class="box has-background-warning">
          
          <h1 class="subtitle">How long would you like to walk? (meters)</h1>
        <div class="columns">

           <div class="column is-two-thirds">  
                <input class="input" type="number" v-model="maxWalkDistance" value=1000>
           </div>
           <div class="column is-one-third">
                <p>meters</p>
           </div>

        </div>
          
      </div>
      <div id=next-page class="box has-background-link has-text-light has-text-centered">
          <router-link class="has-text-light" :to="{name:'ChooseNextVenue'}">Show me what's around!</router-link>
      </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
    name: 'Start',
    data: function() {
        return {
            categories: ["architecture", "cultural", "historic", "natural","industrial_facilities", "religion", "other"],
            categoriesChecked: [false, false, true, true, false, false, false],
            categoryNames: ["Architecture", "Cultural", "Historic", "Natural", "Industrial facilities", "Religion", "Other"],
            maxWalkDistance: null
        }
    },
    computed:{

        categoriesJoin: function(){
            var toJoin = [];
            for(var i=0; i< this.categories.length; i++){
                if(this.categoriesChecked[i]){
                    toJoin.push(this.categories[i])
                }

            }
            return toJoin.join(",");
        }
    },
    methods:{
        updateCategoryPreference(){
            this.$root.$data.vuey.category_preference = this.categoriesJoin;
        }
    }

}
</script>

<style scoped lang=scss>
.card {
    margin: 1em;
}

#app .box {
    margin: 0.5em;
}

#categories-list .box {
    margin: 0.5em;
}

#walk-distance-box label {
    span {
        margin-left: 0.5em;
    }
}

.checkbox {
    display: grid;
    grid-template-columns: min-content auto;
    grid-gap: 0.5em;
    color: var(--color);
}

.checkbox__input {
  input {
    opacity: 0;
    width: 1em;
    height: 1em;
  }
}

.checkbox__control {
  display: inline-grid;
  width: 1em;
  height: 1em;
  border-radius: 0.25em;
  border: 0.1em solid currentColor;
}

.checkbox__input {
  display: grid;
  grid-template-areas: "checkbox";
  
  > * {
    grid-area: checkbox;
  }
}

.checkbox__control svg {
  transition: transform 0.1s ease-in 25ms;
  transform: scale(0);
  transform-origin: bottom left;
}

.checkbox__input input:checked
 + .checkbox__control svg {
  transform: scale(1);
}
</style>
