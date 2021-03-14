<template>
  <b-list-group>
    <div v-for="item in items" :key="item.name">
     <b-list-group-item v-bind:to="item.url">{{item.name}}</b-list-group-item>
    </div>
  </b-list-group>
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