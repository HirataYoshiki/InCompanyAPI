<template>
  <div v-if="select">
    <ReportDetail :Report="SelectedReport.report" v-on:back="changeselectmode"/>
  </div>
  <div v-else>
    <ReportsList :List="reports"/>
  </div>  
</template>

<script>
import ReportsList from '@/components/Report/ReportsList'
import ReportDetail from '@/components/Report/ReportDetail'
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
  inject: [
    'create_headers'
  ],
  methods: {
    get_reports: async function () {
      try {
        let headers = this.create_headers()
        const response = await this.$axios.get(this.urls.BASE, headers)
        this.reports = response.data
      } catch (e) {
        alert(e)
      }
    },
    changeselectmode: function () {
      this.select = !this.select
    },
    set_selected_report: function (selectedreport) {
      this.SelectedReport.report = selectedreport
      this.select = true
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
  },
  provide () {
    return {
      show_detail: this.set_selected_report,
      changeselectmode: this.changeselectmode,
      reset_reports: this.get_reports
    }
  }
}
</script>
