<template>
  <div v-if="status">
    <h1>Company app</h1>
    <h2>You can create and check reports</h2>
    <b-container fluid>
      <b-row class="justify-content-md-center">
        <div v-for="app in apps" :key="app.name">
          <b-col>
            <Homenavcard :url="app.url" :name="app.name" :description="app.description" :icon="app.icon"/>
          </b-col>
        </div>
      </b-row>
    </b-container>
  </div>
  <div v-else>
    <h1>Welcome to my App</h1>
    <h2>Please Login</h2>
  </div>
</template>

<script>
import Homenavcard from '@/apps/home/components/HomeNav'
export default {
  name: 'home',
  components: {
    Homenavcard
  },
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