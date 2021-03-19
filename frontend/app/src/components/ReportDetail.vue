<template>
  <b-card bg-variant="light">
    <b-form-group>
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
  }
}
</script>
