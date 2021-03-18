<template>
  <div>
    <b-card-group deck>
      <div v-for="report in List" :key="report.reportid">
        <b-card
          border-variant="primary"
          v-bind:header="headertime(report.timestamp)"
          header-border-variant="primary"
          align="center"
          v-bind:title="report.title"
          @click="go_to_report(report.localreportid)">
          <b-card-text>Some descriptions.</b-card-text>
        </b-card>
      </div>
    </b-card-group>
  </div>
</template>

<script>
export default {
  name: 'reportslist',
  props: {
    List: Array
  },
  data () {
    return {
      sortlist: {
      }
    }
  },
  methods: {
    go_to_report (num) {
      alert('localreportid: ' + num)
    },
    headertime: function (thetime) {
      return 'Created at ' + thetime
    }
  },
  watch: {
    List: function () {
      this.List = this.List
    }
  }
}
</script>
