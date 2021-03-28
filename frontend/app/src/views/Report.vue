<template>
  <div v-if="PageNumber === 0">
    <h1><strong>Build Up Report</strong></h1>
    <h2>You can create and check reports</h2>
      <b-container fluid>
        <b-row class="justify-content-md-center">
        <div v-for="item in links" :key="item.pagenumber">
          <b-col>
            <ReportNavCard :img="item.img" :title="item.title" :description="item.description" :pagenumber="item.pagenumber"/>
          </b-col>
        </div>
      </b-row>
    </b-container>
  </div>
  <div v-else-if="PageNumber === 1">
    <Mde/>
  </div>
  <div v-else-if="PageNumber === 2">
    <Mde/>
  </div>
  <div v-else-if="PageNumber === 3">
    <ReportCheck/>
  </div>
</template>

<script>
import Mde from '@/views/Mde'
import ReportNavCard from '@/components/Report/ReportNavCard'
import ReportCheck from '@/components/Report/ReportCheck'
export default {
  name: 'home',
  components: {
    Mde,
    ReportNavCard,
    ReportCheck
  },
  inject: [
    'loginstatus'
  ],
  data () {
    return {
      PageNumber: 0,
      links: [
        {
          pagenumber: 1,
          img: 'file-text',
          title: 'Create content',
          description: 'Create a part of report. You can gather content parts to build up a report.'
        },
        {
          pagenumber: 2,
          img: 'layers',
          title: 'Build up Report',
          description: 'Choose contents, Set title, Create a new report.'
        },
        {
          pagenumber: 3,
          img: 'folder',
          title: 'Your Reports',
          description: 'Check, Edit, Delete your reports.'
        }
      ]
    }
  },
  methods: {
    set_page_number: function (pagenumber) {
      this.PageNumber = pagenumber
    }
  },
  computed: {
    status () {
      return this.loginstatus()
    }
  },
  provide () {
    return {
      set_page_number: this.set_page_number
    }
  }
}
</script>