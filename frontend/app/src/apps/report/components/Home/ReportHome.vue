<template>
  <div>
    <h1><strong>Build Up Report</strong></h1>
    <h2>You can create and check reports</h2>
    <b-container fluid>
      <b-row class="justify-content-md-center">
        <div v-for="item in links" :key="item.pagenumber">
          <b-col>
            <ReportNavCard :img="item.img" :title="item.title" :description="item.description" :link="item.link"/>
          </b-col>
        </div>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import ReportNavCard from '@/apps/report/components/ReportNavCard'
export default {
  name: 'home',
  components: {
    ReportNavCard
  },
  inject: [
    'loginstatus'
  ],
  data () {
    return {
      links: [
        {
          img: 'file-text',
          title: 'Create content',
          description: 'Create a part of report. You can gather contents to build up a report.',
          link: 'content'
        },
        {
          img: 'layers',
          title: 'Build up Report',
          description: 'Choose contents, Set title, Create a new report.',
          link: 'content'
        },
        {
          img: 'folder',
          title: 'Your Reports',
          description: 'Check, Edit, Delete your reports.',
          link: 'check'
        }
      ]
    }
  }
}
</script>