<template>
  <b-card>
    <b-form-group label="Your Reports" label-size="lg" label-class="font-weight-bold pt-0">
      <b-card-group deck>
        <div v-for="report in List" :key="report.reportid">
          <b-card
            border-variant="primary"
            v-bind:header="headertime(report.timestamp)"
            header-bg-variant="primary"
            header-text-variant="white"
            header-border-variant="primary"
            align="center"
            class="mb-2"
            v-bind:title="report.title">
            <b-card-text>Some descriptions.</b-card-text>
            <b-button @click="go_to_report(report.localreportid)" variant="primary">Edit</b-button>
          </b-card>
        </div>
      </b-card-group>
    </b-form-group>
  </b-card>
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
    go_to_report (localreportid) {
      for (var report of this.List) {
        if (report.localreportid===localreportid) {
          this.$parent.SelectedReport.report = report
        }
      }
      this.$parent.select = true
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
