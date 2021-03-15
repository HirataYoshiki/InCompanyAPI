<template>
  <header>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand to="/">
        Company App
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-text size="sm" class="mr-sm-2">
            {{text}}
          </b-nav-text>
          <b-nav-form>
            <div v-if="status">
              <b-button size="sm" class="my-2 my-sm-0" variant="outline-secondary" @click="go_signout">Sign out</b-button>
            </div>
            <div v-else>
              <b-button size="sm" class="my-2 my-sm-0" variant="primary" @click="go_signin">Sign in</b-button>
            </div>
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </header>
</template>

<script>
export default {
  name: 'headercolumn',
  props: {
    value: String,
    status: Boolean
  },
  data () {
    return {
      text: 'Hello! ' + this.value + '  '
    }
  },
  methods: {
    go_signin () {
      this.$router.push('/signin')
    },
    go_signout () {
      document.cookie = 'accesstoken=; max-age=0'
      this.$parent.init()
    }
  },
  watch: {
    value: function () {
      this.text = 'Hello! ' + this.value + '  '
    },
    status: function () {
      this.status = this.status
    }
  }
}
</script>
