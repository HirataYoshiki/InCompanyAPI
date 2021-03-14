<template>
  <header>
    <nav class="navbar navbar-dark bg-primary">
      <a class="navbar-brand">Company App</a>
      <form class="form-inline">
        <button class="btn btn-secondary" @click="go_signin">Sign in</button>
      </form>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'headercolumn',
  methods: {
    go_signin () {
      this.$router.push('/signin')
    }
  }
}
</script>
