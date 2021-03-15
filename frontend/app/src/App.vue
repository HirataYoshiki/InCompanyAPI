<template>
  <div id="app">
    <Headercolumn :value="username" :status="LoginStatus"/>
    <b-container fluid>
      <b-row>
        <b-col class="col-md-2 d-none d-md-block bg-secondary sidebar-sticky">
          <Sidebar/>
        </b-col>
        <b-col>
          <section id="cover" class="min-vh-100">
            <router-view/>
          </section>
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
      LoginStatus: false,
      character: [],
      reports: []
    }
  },
  methods: {
    init () {
      this.username = 'Please Sign in'
      this.LoginStatus = false
      this.$router.push('/')
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
