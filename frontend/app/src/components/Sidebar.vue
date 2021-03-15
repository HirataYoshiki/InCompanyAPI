<template>
  <b-nav vertical pills>
    <div v-for="item in items" :key="item.name">
      <b-nav-item v-bind:to="item.url">{{item.name}}</b-nav-item>
    </div>
  </b-nav>
</template>

<script>
export default {
  name: 'Sidebar',
  data () {
    return {
      items: [
        {
          name: 'Character',
          url: '/character'
        },
        {
          name: 'Report',
          url: '/report'
        }
      ]
    }
  }
}
</script>