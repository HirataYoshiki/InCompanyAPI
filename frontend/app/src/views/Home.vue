<template>
  <div v-if="status">
    <h1>Company app</h1>
    <h2>You can create and check reports</h2>
  </div>
  <div v-else>
    <h1>Welcome to my App</h1>
    <h2>Please Login</h2>
  </div>
</template>

<script>
export default {
  name: 'home',
  inject: [
    'loginstatus',
    'apps'
  ],
  computed: {
    status () {
      return this.loginstatus()
    }
  }
}
</script>