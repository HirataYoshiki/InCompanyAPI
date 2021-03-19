<template>
  <b-card bg-variant="light">
    <b-form-group label="Title " label-size="lg" label-for="title_input" label-align-xl="left" label-cols-xl="3">
      <b-form-input id="title_input" size="lg" v-bind:disable="edit">{{report.title}}</b-form-input>
    </b-form-group>
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
        reportid: 0,
        localreportid: 0,
        username: 'Unknown',
        title: 'Unknown',
        contentsid: null,
        timestamp: null,
        teamid: null,
        headerid: null
      }
    }
  },
  watch: {
    Report () {
      this.Report = this.Report
      this.report = this.Report.report
    }
  }
}
</script>
