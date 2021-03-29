<template>
  <div>
    <div v-if="$route.path==='/report/check'">
      <ReportsList :List="reports"/>
    </div>
    <div v-else>
      <router-view/>
    </div>
  </div>
</template>

<script>
import ReportsList from '@/apps/report/components/Check/ReportsList'
export default {
  name: 'checkreport',
  components: {
    ReportsList
  },
  inject: [
    'get_reports'
  ],
  data () {
    return {
      reports: []
    }
  },
  beforeMount () {
    this.reports = this.get_reports()
  }
}
</script>
