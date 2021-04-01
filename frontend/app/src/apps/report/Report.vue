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
          description: '',
          order: []
        },
        endpoint: 'http://localhost:8080/reportapp/reports'
      },
      description: {
        description: '',
        endpoint: 'http://localhost:8080/reportapp/headers'
      },
      reports: [],
      groups: [],
      contents: [],
      descriptions: []
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
    get_description: function () {
      return this.description.description
    },
    set_description: function (description) {
      this.description.description = description
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
    get_descriptions: function () {
      return this.descriptions
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
    async _request_get (endpoint) {
      try {
        const headers = this.create_headers()
        const response = await this.$axios.get(endpoint, headers)
        return response.data
      } catch (e) {
        alert('Request error')
      }
    },
    request_contents: async function () {
      this.contents = await this._request_get(this.content.endpoint)
    },
    async request_groups () {
      this.groups = await this._request_get(this.group.endpoint)
    },
    async request_reports () {
      this.reports = await this._request_get(this.report.endpoint)
    },
    async request_descriptions () {
      this.descriptions = await this._request_get(this.description.endpoint)
    }
  },
  async mounted () {
    await this.request_reports()
    await this.request_contents()
    await this.request_groups()
    await this.request_descriptions()
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
      get_descriptions: this.get_descriptions,
      get_contents: this.get_contents,
      push_contents: this.push_contents,
      delete_from_reports: this.delete_from_reports,
      delete_from_contents: this.delete_from_contents,
      request_contents: this.request_contents
    }
  }
}
</script>