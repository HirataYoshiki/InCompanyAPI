<template>
  <b-form-group>
    <label for="cardgroup"><h1><b-icon icon="folder"></b-icon> Reports</h1></label>
    <b-card-group deck id="cardgroup">
      <div v-for="report in List" :key="report.localreportid">
        <ReportCard :report="report"/>
      </div>
    </b-card-group>
  </b-form-group>
</template>

<script>
import ReportCard from '@/apps/report/components/Check/Cards/ReportCard'
export default {
  name: 'reportslist',
  components: {
    ReportCard
  },
  inject: [
    'get_reports'
  ],
  methods: {
    setreport (report) {
      this.selecter = report
    } 
  },
  computed: {
    List () {
      return this.get_reports()
    }
  },
  watch: {
    selecter: function () {
      this.selecter = this.selecter
      this.$parent.SelectedReport.report = this.selecter
      this.$parent.select = true
    }
  }
}
</script>
