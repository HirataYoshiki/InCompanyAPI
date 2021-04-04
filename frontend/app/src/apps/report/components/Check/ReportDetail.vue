<template>
  <ReportEditor
    :pagetitle="'Edit Report'"
    :reporttitlegetter="reporttitlegetter"
    :reporttitlesetter="reporttitlesetter"
    :descriptiongetter="descriptiongetter"
    :descriptionsetter="descriptionsetter"
    :ordercontentsgetter="ordercontentsgetter"
    :ordercontentssetter="ordercontentssetter"
    :selectedcontentgetter="selectedcontentgetter"
    :selectedcontentsetter="selectedcontentsetter"
    :savefunc="save"
  />
</template>

<script>
import ReportEditor from '@/apps/report/components/objects/ReportEditor'
export default {
  name: 'reportdetail',
  components: {
    ReportEditor
  },
  props: {
    new: Boolean
  },
  inject: [
    'get_contents',
    'create_headers',
    'set_orderedcontents',
    'get_orderedcontents',
    'get_selected_report',
    'set_selected_report',
    'get_selected_content',
    'set_selected_content',
    'get_selected_description',
    'set_selected_description'
  ],
  data () {
    return {
      edit: {
        content: false,
        order: false,
        title: false,
        description: false
      },
      conf: {
        placeholder: 'Input content here',
        spellChecker: false
      }
    }
  },
  methods: {
    save () {
      alert('detail')
    },
    reporttitlegetter () {
      return this.get_selected_report().title
    },
    reporttitlesetter (value) {
      let report = this.get_selected_report()
      report.title = value
      this.set_selected_report(report)
    },
    descriptiongetter () {
      return this.get_selected_description()
    },
    descriptionsetter (value) {
      this.get_selected_description(value)
    },
    ordercontentsgetter () {
      return this.get_orderedcontents()
    },
    ordercontentssetter (value) {
      this.set_orderedcontents(value)
    },
    selectedcontentgetter () {
      return this.get_selected_content()
    },
    selectedcontentsetter (content) {
      this.set_selected_content(content)
    }
  }
}

</script>
<style scoped>
#mde {
  text-align: left;
}
#contentorder {
  text-align: left;
}
</style>
