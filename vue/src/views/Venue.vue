<template>
  <div class="home">
      <router-link to="/Final">I'm here {{xid}}</router-link>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Venue',
  data: function(){
    return {
      xid:-1
    }
  },
  created() {
      this.xid = this.$route.params.xid;
  }
}
</script>
