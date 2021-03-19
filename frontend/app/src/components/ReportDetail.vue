<template>
  <b-card bg-variant="light">
    <b-container fluid>
      <b-row align-v="center" class="bg-secondary">
        <b-col class="text-white">
          <h2>{{report.title}}</h2>
        </b-col>
      </b-row>
      <b-row>
        <b-col class="ml-auto text-secondary" md="4">
          <h5>Name: {{report.username}}</h5>
        </b-col>
      </b-row>
    </b-container>
  </b-card>
</template>

<script>
export default {
  name: 'reportdetail',
  props: {
    Report: Object
  },
  data () {
    return {
      edit: false,
      report: {
        localreportid: this.Report.localreportid,
        username: this.Report.username,
        title: this.Report.title,
        timestamp: this.Report.timestamp
      }
    }
  },
  watch: {
    Report () {
      this.Report = this.Report
    }
  }
}
</script>
