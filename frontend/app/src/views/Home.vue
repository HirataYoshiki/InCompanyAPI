<template>
  <div v-if="status">
    <h1><strong>Build Up Report</strong></h1>
    <h2>You can create and check reports</h2>
    <b-card-group deck>
      <div v-for="item in links" :key="item.number">
        <Homenavcard :img="item.img" :title="item.title" :description="item.description" :link="item.link"/>
      </div>
    </b-card-group>
  </div>
  <div v-else>
    <h1><strong>Build Up Report</strong></h1>
    <h2>Please Login</h2>
  </div>
</template>

<script>
import Homenavcard from '@/components/Home/HomeNav'
export default {
  name: 'home',
  components: {
    Homenavcard
  },
  inject: [
    'loginstatus'
  ],
  data () {
    return {
      links: [
        {
          number: 0,
          img: 'file-text',
          title: 'Create content',
          description: 'Create a part of report. You can gather content parts to build up a report.',
          link: '/test'
        },
        {
          number: 1,
          img: 'layers',
          title: 'Build up Report',
          description: 'Choose contents, Set title, Create a new report.',
          link: '/report'
        },
        {
          number: 2,
          img: 'folder',
          title: 'Your Reports',
          description: 'Check, Edit, Delete your reports.',
          link: '/report'
        }
      ]
    }
  },
  computed: {
    status () {
      return this.loginstatus()
    }
  }
}
</script>