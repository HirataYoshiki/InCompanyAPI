<template>
<div>
  <CardforEdit
    :object="report"
    :title="report.title"
    :icon="'layers'"
    :description="description"
    :subtitle="createdtime"
    :editfunc="go_to_detail"
    :overlayOK="OK"
  />
  </div>
</template>

<script>
import CardforEdit from '@/apps/report/components/objects/CardForEdit'
export default {
  name: 'reportcard',
  props: {
    report: Object
  },
  components: {
    CardforEdit
  },
  inject: [
    'create_headers',
    'get_groups',
    'get_contents',
    'get_descriptions',
    'delete_from_reports',
    'set_orderedcontents',
    'set_selected_report',
    'set_selected_description'
  ],
  data () {
    return {
      overlay: false
    }
  },
  methods: {
    go_to_detail () {
      this._orderedcontents()
      this.set_selected_report(this.report)
      this.set_selected_description(this.description)
      this.$router.push('check/detail')
    },
    show_overlay () {
      this.overlay = true
    },
    Cancel () {
      this.overlay = false
    },
    async OK () {
      let url = 'http://localhost:8080/reportapp/reports/' + String(this.report.localreportid)
      const headers = this.create_headers()
      await this.$axios.delete(url, headers)
      this.overlay = false
      this.delete_from_reports(this.report)
    },
    _orderedcontents () {
      var groups = this.get_groups().filter(n => n.localgroupid === this.report.localgroupid)
      groups.sort(function (a, b) {
        return a.order - b.order
      })
      const contents = this.get_contents()
      var orderedcontents = []
      for (var item of groups) {
        for (var content of contents) {
          if (item.contentid === content.contentid) {
            orderedcontents.push(content)
          }
        }
      }
      this.set_orderedcontents(orderedcontents)
    }
  },
  computed: {
    createdtime () {
      const date = new Date(this.report.timestamp)
      const YYYY = date.getFullYear()
      const MM = date.getMonth()+1
      const DD = date.getDate()
      return 'created at ' + YYYY + '/' + MM + '/' + DD
    },
    description () {
      try {
        let description = this.get_descriptions()
        return description.filter(n => n.localheaderid === this.report.headerid)[0].type
      } catch (e) {
        return ''
      }
    }
  },
  watch: {
    report: function () {
      this.report = this.report
    }
  }
}
</script>