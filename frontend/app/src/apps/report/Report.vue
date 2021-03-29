<template>
  <div v-if="$route.path==='/report'">
    <ReportHome/>
  </div>
  <div v-else>
    <router-view/>
  </div>
</template>

<script>
import ReportHome from '@/apps/report/components/Home/ReportHome'
export default {
  name: 'report',
  inject: [
    'create_headers'
  ],
  components: {
    ReportHome
  },
  data () {
    return {
      content: {
        text: '',
        endpoint: 'http://localhost:8080/reportapp/contents'
      },
      report: {
        report: {
          title: '',
          subtitle: '',
          order: []
        },
        endpoint: 'http://localhost:8080/reportapp/reports'
      },
      reports: [],
      contents: []
    }
  },
  methods: {
    get_content: function () {
      return this.content.text
    },
    set_content: function (text) {
      this.content.text = text
    },
    get_report: function () {
      return this.report.report
    },
    set_report: function (report) {
      this.report.report = report 
    },
    get_reports: function () {
      return this.reports
    },
    get_contents: function () {
      return this.contents
    },
    push_reports: function (report) {
      this.reports.push(report)
    },
    push_contents: function (content) {
      this.contents.push(content)
    },
    async request_reports () {
      try {
        const headers = this.create_headers()
        const response = await this.$axios.get(this.report.endpoint, headers)
        this.reports = response.data
      } catch (e) {
        alert(e)
        alert('Reports Request error')
      }
    },
    async request_contents () {
      try {
        const headers = this.create_headers()
        const response = await this.$axios.get(this.content.endpoint, headers)
        this.contents = response.data
      } catch (e) {
        alert('Contents Request error')
      }
    }
  },
  beforeMount () {
    this.request_reports()
    this.request_contents()
  },
  provide () {
    return {
      get_content: this.get_content,
      set_content: this.set_content,
      get_report: this.get_report,
      set_report: this.set_report,
      get_reports: this.get_reports,
      get_contents: this.get_contents
    }
  }
}
</script>