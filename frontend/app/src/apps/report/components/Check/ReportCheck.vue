<template>
  <div>
    <div v-if="$route.path==='/report/check'">
      <ReportsList/>
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
      reports: [],
      orderedcontents: []
    }
  },
  methods: {
    set_orderedcontents: function (orderedcontents) {
      this.orderedcontents = orderedcontents
    },
    get_orderedcontents: function () {
      return this.orderedcontents
    }
  },
  beforeMount () {
    this.reports = this.get_reports()
  },
  provide () {
    return {
      set_orderedcontents: this.set_orderedcontents,
      get_orderedcontents: this.get_orderedcontents
    }
  }
}
</script>