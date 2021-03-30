<template>
  <div>
    <div v-if="$route.path==='/report/check'">
      <ReportsList/>
    </div>
    <div v-else>
      <router-view/>
    </div>
  </div>
</template>

<script>
import ReportsList from '@/apps/report/components/Check/ReportsList'
export default {
  name: 'checkreport',
  components: {
    ReportsList
  },
  inject: [
    'get_reports'
  ],
  data () {
    return {
      reports: [],
      orderedcontents: [],
      SelectedReport: {
        reportid: 0,
        timestamp: '2021-01-01T00:00:00',
        headerid: 0,
        title: '',
        localreportid: 0,
        contentgroupid: 0,
        teamid: 0,
        username: ''
      },
      SelectedContent: {
        content: '',
        username: '',
        localcontentid: 0,
        contentid: 0
      },
      group: 'check'
    }
  },
  methods: {
    set_orderedcontents: function (orderedcontents) {
      this.orderedcontents = orderedcontents
    },
    get_orderedcontents: function () {
      return this.orderedcontents
    },
    get_selected_report: function () {
      return this.SelectedReport
    },
    set_selected_report: function (report) {
      this.SelectedReport = report
    },
    get_selected_content: function () {
      return this.SelectedContent
    },
    set_selected_content: function (content) {
      this.SelectedContent = content
    }
  },
  beforeMount () {
    this.reports = this.get_reports()
  },
  provide () {
    return {
      get_orderedcontents: this.get_orderedcontents,
      set_orderedcontents: this.set_orderedcontents,
      get_selected_report: this.get_selected_report,
      set_selected_report: this.set_selected_report,
      get_selected_content: this.get_selected_content,
      set_selected_content: this.set_selected_content,
      group: this.group
    }
  }
}
</script>