<template>
  <div id="cover-caption">
    <div class="container">
      <div class="row text-green">
        <div class="col-xl-5 col-lg-6 col-md-8 col-sm-10 mx-auto text-center form p-4">
          <h1 class="display-4 py-2 text-truncate">
            <div v-if="signup">Sign UP!</div>
            <div v-else>Sign in</div>
          </h1>
            <div class="px-2">
              <form action="" class="justify-content-center">
                <div class="form-group row">
                  <label for="username" class="col-sm-4 col-form-label">UserName</label>
                  <div class="col-sm-8">
                    <input class="form-control" v-bind:class="{'is-invalid':authentify_error}" id="username" placeholder="Enter your name." v-model="username" required>
                  </div>
                </div>
                <div class="form-group row">
                  <label for="password" class="col-sm-4 col-form-label">Password</label>
                  <div class="col-sm-8">
                    <input type="password" class="form-control" v-bind:class="{'is-invalid':authentify_error}" id="password" placeholder="Enter password." v-model="password" required>
                    <div class="invalid-feedback">
                      Username or Password is invalid. Try again!
                    </div>
                  </div>
                </div>
                <div v-if="signup">
                  <div class="form-group row">
                    <label for="mailaddress" class="col-sm-4 col-form-label">E-mail</label>
                    <div class="col-sm-8">
                      <input type="mailaddress" class="form-control" id="mailaddress" placeholder="Enter your e-mail address." v-model="mailaddress">
                      <div class="invalid-feedback">
                        Username or Password is invalid. Try again!
                      </div>
                    </div>
                  </div>
                </div>
                <div v-if="signup">
                  <b-button variant="primary" @click="create_user">
                    Let's Join us!</b-button>
                </div>
                <div v-else>
                  <b-button variant="primary" @click="request_token">
                    Sign in</b-button>
                </div>
              </form>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Signin',
  props: {
    signup: Boolean
  },
  data () {
    return {
      username: '',
      password: '',
      mailaddress: '',
      authentify_error: false
    } 
  },
  methods: {
    async request_token () {
      let form = new FormData()
      const url='http://localhost:8080/token'
      form.append('username', this.username)
      form.append('password', this.password)
      if (this.mailaddress !== '') {
        form.append('mailaddress', this.mailaddress)
      }
      try {
        const response = await this.$axios.post(url, form)
        document.cookie = 'accesstoken=; max-age=0'
        document.cookie = 'accesstoken=' + response.data.access_token + '; max-age=3600'
        this.authentify_error = false
        this.go_home()
      } catch (error) {
        this.authentify_error = true
      }
    },
    go_home () {
      if (!this.authentify_error) {
        this.$parent.username = this.username
        this.$parent.LoginStatus = true
        try {
          this.$parent.set_character()
          this.$router.push('/')
        } catch (e) {
          this.$router.push('/')
        }
      }
    },
    async create_user () {
      const url='http://localhost:8080/users'
      let data = {
        username: this.username,
        password: this.password,
        mailaddress: this.mailaddress
      }
      try {
        await this.$axios.post(url, data)
        await this.request_token()
      } catch (error) {
        this.authentify_error = true
      }
    }
  },
  watch: {
    signup () {
      this.signup = this.signup
    }
  }
}
</script>