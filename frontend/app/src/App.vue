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
            <router-view :MyCharacter="character"/>
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
      character: {
        id: 0,
        username: 'test',
        department: 'test_department',
        position: 'test_position',
        skills: [
          'test_skill1',
          'test_skill2'
        ]
      },
      reports: []
    }
  },
  methods: {
    init () {
      this.username = 'Please Sign in'
      this.LoginStatus = false
      this.$router.push('/')
    },
    create_header_with_accesstoken () {
      let cookies = document.cookie.split(';')
      var MyAccesstoken = ''
      for (var cookie of cookies) {
        let array = cookie.split('=')
        if (array[0]==='accesstoken') {
          MyAccesstoken = array[1]
        }
      }
      let headers = {
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer ' + MyAccesstoken
        }
      }
      return headers
    },
    async set_character () {
      const URL = 'http://localhost:8080/characters/me'
      try {
        const headers = this.create_header_with_accesstoken() 
        const response = await this.$axios.get(URL, headers)
        alert(JSON.stringify(response.data))
        this.character = JSON.parse(JSON.stringify(response.data))
      } catch (e) {
        alert(e)
      }
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
