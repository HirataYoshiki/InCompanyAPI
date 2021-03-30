<template>
  <section class="min-vh-100">
    <b-row>
      <b-col cols="9">
        <b-form id="mde">
          <b-form-group label="Title:" label-for="input-title">
            <b-form-input id="input-title" v-model="reporttitle"></b-form-input>
          </b-form-group>
          <b-form-group label="Content:" label-for="input-content">
            <div id="input-content">
              <VueSimplemde :value="selectedcontentvalue"/>
            </div>
          </b-form-group>
          <b-form-group label="Contents:" label-for="contents">
            <div id="contents">
              <ContentPool :getter="get_contents" :setter="no_return"/>
            </div>
          </b-form-group>
        </b-form>
      </b-col>
      <b-col align-self="stretch">
        hi
      </b-col>
    </b-row>
  </section>
</template>

<script>
import VueSimplemde from 'vue-simplemde'
import ContentPool from '@/apps/report/components/objects/ContentPool'
export default {
  name: 'reportdetail',
  components: {
    VueSimplemde,
    ContentPool
  },
  inject: [
    'get_contents',
    'create_headers',
    'set_orderedcontents',
    'get_orderedcontents',
    'get_selected_report',
    'set_selected_report',
    'get_selected_content',
    'set_selected_content'
  ],
  data () {
    return {
      list: []
    }
  },
  methods: {
    no_return (value) {
      return true
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
      }
    },
    selectedcontentvalue: {
      get () {
        return this.get_selected_content().content
      },
      set (value) {
        let content = this.get_selected_content()
        content.content = value
      }
    }
  }
}

</script>
<style scoped>
#mde {
  text-align: left;
}
</style>
