<template>
  <div id="app">
    <Headercolumn :value="username" :status="LoginStatus"/>
    <b-container fluid>
      <b-row>
        <b-col class="col-2 d-md-block bg-secondary sidebar-sticky min-vh-100">
          <Sidebar :apps="apps"/>
        </b-col>
        <b-col>
          <section id="cover" class="min-vh-100">
            <router-view :MyCharacter="character" :loginstatus="LoginStatus"/>
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
        contents: {
          id: 0,
          username: 'test',
          department: '',
          position: '',
          skills: [
          ]
        },
        NewUser: false
      },
      reports: {
        contents: {}
      },
      apps: [
        {
          name: 'Profile',
          url: '/profile',
          description: 'Set your profiles',
          icon: 'person-circle'
        },
        {
          name: 'Report',
          url: '/report',
          description: 'Build up Report. With Simple MarkDown Editor.',
          icon: 'file-earmark-text'
        }
      ]
    }
  },
  methods: {
    init () {
      this.username = 'Please Sign in'
      this.LoginStatus = false
      this.character.NewUser = false
      this.character.contents = {
        id: 0,
        username: 'test',
        department: 'test_department',
        position: 'test_position',
        skills: [
          'test_skill1',
          'test_skill2'
        ]
      }
      this.$router.push('/')
    },
    create_header_with_accesstoken: function () {
      try {
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
      } catch (e) {
        this.$router.push('/signin')
      }
    },
    async set_character () {
      let URL = 'http://localhost:8080/characters/me'
      try {
        const headers = this.create_header_with_accesstoken() 
        const response = await this.$axios.get(URL, headers)
        this.character.contents = JSON.parse(JSON.stringify(response.data))
      } catch (e) {
        this.character.NewUser = true
      }
    },
    get_status: function () {
      return this.LoginStatus
    }
  },
  provide () {
    return {
      create_headers: this.create_header_with_accesstoken,
      loginstatus: this.get_status,
      apps: this.apps
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
