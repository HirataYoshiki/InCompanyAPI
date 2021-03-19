<template>
  <div v-if="select">
    <ReportDetail :Report="SelectedReport.report"/>
  </div>
  <div v-else>
    <ReportsList :List="reports"/>
  </div>  
</template>

<script>
import ReportsList from '@/components/ReportsList'
import ReportDetail from '@/components/ReportDetail'
export default {
  name: 'report',
  components: {
    ReportsList,
    ReportDetail
  },
  props: {
    loginstatus: Boolean
  },
  data () {
    return {
      reports: [],
      SelectedReport: {
        report: {
          reportid: 0,
          localreportid: 0,
          username: '',
          title: '',
          contentsid: null,
          timestamp: null,
          teamid: null,
          headerid: null
        },
        header: {
          localheaderid: 0,
          type: ''
        },
        content: {
          localcontentid: 0,
          content: '',
          groupid: null
        }
      },
      urls: {
        BASE: 'http://localhost:8080/reportapp/reports'
      },
      select: false
    }
  },
  methods: {
    async get_reports () {
      try {
        let headers = this.$parent.create_header_with_accesstoken()
        const response = await this.$axios.get(this.urls.BASE, headers)
        this.reports = response.data
      } catch (e) {
        alert(e)
      }
    }
  },
  created () {
    this.get_reports()
  },
  watch: {
    loginstatus: function () {
      this.loginstatus = this.loginstatus
      if (!this.loginstatus) {
        this.reports = [{id: 0}]
        this.SelectedReport = {
          report: {
            reportid: 0,
            localreportid: 0,
            username: '',
            title: '',
            contentsid: null,
            timestamp: null,
            teamid: null,
            headerid: null
          },
          header: {
            localheaderid: 0,
            type: ''
          },
          content: {
            localcontentid: 0,
            content: '',
            groupid: null
          }
        }
      } else {
        this.get_reports()
      }
    }
  }
}
</script>
