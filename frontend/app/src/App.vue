<template>
  <div id="app">
    <Headercolumn/>
    <b-container fluid>
      <b-row>
        <b-col cols="2">
          <Sidebar/>
        </b-col>
        <b-col>
          <router-view/>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Headercolumn from '@/components/Headercolumn'
import Sidebar from '@/components/Sidebar'
export default {
  name: 'App',
  components: {
    Headercolumn,
    Sidebar
  },
  data () {
    return {
      username: 'Please Sign in',
      login: false
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
