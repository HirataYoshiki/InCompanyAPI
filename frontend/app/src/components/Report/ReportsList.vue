<template>
  <b-card>
    <b-form-group label="Your Reports" label-size="lg" label-class="font-weight-bold pt-0">
      <b-icon icon="file-earmark-plus" class="ml-auto" variant="success"></b-icon>
      <b-card-group deck>
        <div v-for="report in List" :key="report.localreportid">
          <ReportCard :report="report" v-on:selectreport="setreport"/>
        </div>
      </b-card-group>
    </b-form-group>
  </b-card>
</template>

<script>
import ReportCard from '@/components/Report/Cards/ReportCard'
export default {
  name: 'reportslist',
  components: {
    ReportCard
  },
  props: {
    List: Array
  },
  data () {
    return {
      selecter: {},
      text: 'this is reportslist'
    }
  },
  methods: {
    setreport (report) {
      this.selecter = report 
    } 
  },
  watch: {
    List: function () {
      this.List = this.List
    },
    selecter: function () {
      this.selecter = this.selecter
      this.$parent.SelectedReport.report = this.selecter
      this.$parent.select = true
    }
  }
}
</script>
