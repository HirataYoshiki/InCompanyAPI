<template>
  <b-nav vertical pills class="vw-auto">
    <b-nav-text class="text-dark font-weight-bold pt-0 font-size-large">
      Apps
    </b-nav-text>
    <div v-for="item in apps" :key="item.name">
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
  props: {
    apps: Array
  }
}
</script>