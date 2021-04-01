<template>
  <div>
    <b-img :src="faceimg" fluid alt="Responsive image"></b-img>
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
      faceimg: require('@/assets/reporthome.png'),
      links: [
        {
          img: require('@/assets/content.png'),
          title: 'Create content',
          description: 'Create a part of report. You can gather contents to build up a report.',
          link: 'content'
        },
        {
          img: require('@/assets/build.png'),
          title: 'Build up Report',
          description: 'Choose contents, Set title, Create a new report.',
          link: 'report'
        },
        {
          img: require('@/assets/contents.png'),
          title: 'Your contents',
          description: 'Under developping',
          link: 'contents'
        },
        {
          img: require('@/assets/reports.png'),
          title: 'Your Reports',
          description: 'Check, Edit, Delete your reports.',
          link: 'check'
        }
      ]
    }
  }
}
</script>