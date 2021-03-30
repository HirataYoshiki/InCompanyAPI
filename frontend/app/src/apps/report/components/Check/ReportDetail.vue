<template>
  <section class="min-vh-100">
    <h1>Report</h1>
    <b-row>
      <b-col cols="9">
        <b-form id="mde">
          <b-form-group label="Title:" label-for="input-title">
            <b-form-input id="input-title" v-model="reporttitle"></b-form-input>
          </b-form-group>
          <b-form-group label="Content:" label-for="input-content">
            <div id="input-content">
              <VueSimplemde v-model="selectedcontentvalue"/>
            </div>
          </b-form-group>
          <b-form-group label="Contents:" label-for="contents">
            <div id="contents">
              <ContentPool :getter="get_contents" :setter="return_none" :group="group"/>
            </div>
          </b-form-group>
        </b-form>
      </b-col>
      <b-col align-self="stretch">
        <b-icon icon="layers" font-scale="4"></b-icon>
        <b-form-group
        label="Build Up Report!"
        label-for="contentorder"
        >
          <b-list-group id="contentorder">
            <draggable v-model="ReportContents" :group="group">
              <b-list-group-item
              v-for="(content, i) in ReportContents"
              class="button"
              @click="set_selected_content(content)"
              :key="content.contentid"
              :variant="color(content)"
              >
                <strong>{{i+1}}.</strong>
                <b-icon icon="file-text"></b-icon>
                {{content.content.substr( 0, 21)}}
              </b-list-group-item>
            </draggable>
          </b-list-group>
        </b-form-group>
      </b-col>
    </b-row>
  </section>
</template>

<script>
import VueSimplemde from 'vue-simplemde'
import draggable from 'vuedraggable'
import ContentPool from '@/apps/report/components/objects/ContentPool'
export default {
  name: 'reportdetail',
  components: {
    VueSimplemde,
    ContentPool,
    draggable
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
    'group'
  ],
  data () {
    return {
      list: [],
      edit: false
    }
  },
  methods: {
    return_none (value) {
      return true
    },
    color (content) {
      if (content === this.get_selected_content()) {
        return 'success'
      }
      return ''
    }
  },
  computed: {
    selectedreport () {
      return this.get_selected_report()
    },
    reporttitle: {
      get () {
        return this.get_selected_report().title
      },
      set (value) {
        let report = this.get_selected_report()
        report.title = value
        this.set_selected_report(report)
      }
    },
    selectedcontentvalue: {
      get () {
        return this.get_selected_content().content
      },
      set (value) {
        let content = this.get_selected_content()
        content.content = value
        this.set_selected_content(content)
      }
    },
    ReportContents: {
      get () {
        return this.get_orderedcontents()
      },
      set (value) {
        this.set_orderedcontents(value)
      }
    }
  },
  beforeMount () {
    const orderedcontents = this.get_orderedcontents()
    this.set_selected_content(orderedcontents[0])
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
