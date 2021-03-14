<template>
  <div id="app">
    <Headercolumn/>
    <router-view/>
  </div>
</template>

<script>
import Headercolumn from './components/Headercolumn'
export default {
  name: 'App',
  components: {
    Headercolumn
  },
  data () {
    return {
      username: 'Please Sign in.'
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
