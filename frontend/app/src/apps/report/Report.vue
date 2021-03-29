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
      group: {
        group: [],
        endpoint: 'http://localhost:8080/reportapp/groups'
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
      groups: [],
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
    get_groups: function () {
      return this.groups
    },
    get_contents: function () {
      return this.contents
    },
    push_reports: function (report) {
      this.reports.push(report)
    },
    delete_from_reports: function (report) {
      const newArray = this.reports.filter(n => n !== report)
      this.reports = newArray
    },
    push_contents: function (content) {
      this.contents.push(content)
    },
    delete_from_contents: function (content) {
      const newArray = this.contents.filter(n => n !== content)
      this.contents = newArray
    },
    async request_contents () {
      try {
        const headers = this.create_headers()
        const response = await this.$axios.get(this.content.endpoint, headers)
        this.contents = response.data
      } catch (e) {
        alert('Contents Request error')
      }
    },
    async request_groups () {
      try {
        const headers = this.create_headers()
        const response = await this.$axios.get(this.group.endpoint, headers)
        this.groups = response.data
      } catch (e) {
        alert(e)
        alert('Groups Request error')
      }
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
    }
  },
  beforeMount () {
    this.request_reports()
    this.request_contents()
    this.request_groups()
  },
  provide () {
    return {
      get_content: this.get_content,
      set_content: this.set_content,
      get_report: this.get_report,
      set_report: this.set_report,
      get_reports: this.get_reports,
      push_reports: this.push_reports,
      get_groups: this.get_groups,
      get_contents: this.get_contents,
      push_contents: this.push_contents,
      delete_from_reports: this.delete_from_reports,
      delete_from_contents: this.delete_from_contents
    }
  }
}
</script>