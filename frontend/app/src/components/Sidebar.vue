<template>
  <b-nav vertical pills>
    <b-nav-text>
      apps
    </b-nav-text>
    <div v-for="item in items" :key="item.name">
      <b-nav-item v-bind:to="item.url">
        <p class="text-white">
        {{item.name}}
        </p>
      </b-nav-item>
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