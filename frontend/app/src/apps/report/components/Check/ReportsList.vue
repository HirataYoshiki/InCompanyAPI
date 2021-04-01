<template>
  <div>
    <b-img :src="faceimg" fluid alt="Responsive image"></b-img>
    <b-form class="mt-4">
      <b-form-group>
        <b-card-group deck id="cardgroup">
          <div v-for="report in List" :key="report.localreportid">
            <ReportCard :report="report"/>
          </div>
        </b-card-group>
      </b-form-group>
    </b-form>
  </div>
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
  data () {
    return {
      faceimg: require('@/assets/reportcheckheader.png')
    }
  },
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
