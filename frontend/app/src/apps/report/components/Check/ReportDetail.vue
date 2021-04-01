<template>
  <section class="min-vh-100">
    <b-navbar>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto mr-auto">
          <b-nav-text><h3>Report</h3></b-nav-text>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <b-button :variant="save_button_color" @click="save">Save</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <b-row>
      <b-col cols="9">
        <b-form id="mde">
          <b-form-group label="Title:" label-for="input-title">
            <b-form-input id="input-title" v-model="reporttitle" placeholder="Input title" v-on:update="updated('title')"></b-form-input>
          </b-form-group>
          <b-form-group label="Description:" label-for="input-description">
            <b-form-input id="input-description" v-model="description" placeholder="Input some descripstions." v-on:update="updated('description')"></b-form-input>
          </b-form-group>
          <b-form-group label="Content:" label-for="input-content">
            <div id="input-content">
              <vue-simplemde v-model="selectedcontentvalue"/>
            </div>
          </b-form-group>
          <b-form-group label="Contents:" label-for="contents">
            <div id="contents">
              <ContentPool :getter="get_contents" :setter="return_true" :group="group"/>
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
            <draggable v-model="ReportContents" :group="group" draggable=".button" v-on:update="updated('order')" v-on:add="updated('order')">
              <b-list-group-item
              v-for="(content, i) in ReportContents"
              class="button"
              @click.capture="change_content(content)"
              :key="content.contentid"
              :variant="color(content)"
              >
                <strong>{{i+1}}.</strong>
                <b-icon icon="file-text"></b-icon>
                {{content.content.substr( 0, 21)}}
              </b-list-group-item>
              <b-list-group-item slot="footer" variant="light" id="contentorderfooter">Drag and Drop Content</b-list-group-item>
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
    'set_selected_description',
    'group'
  ],
  data () {
    return {
      edit: {
        content: false,
        order: false,
        title: false,
        description: false
      }
    }
  },
  methods: {
    return_true (value) {
      return true
    },
    updated (key) {
      this.edit[key] = true
    },
    change_content (content) {
      if (this.edit.content) {
        alert('not saved. Save?')
      }
      this.set_selected_content(content)
      this.edit.content = false
    },
    color (content) {
      if (content === this.get_selected_content()) {
        return 'success'
      }
      return ''
    },
    save () {
      if (!this.edit_something) {
        return true
      } else {
        for (var key in this.edit) {
          this.edit[key] = false
        }
        alert('Saved')
        return true
      }
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
        this.updated('content')
      }
    },
    ReportContents: {
      get () {
        return this.get_orderedcontents()
      },
      set (value) {
        this.set_orderedcontents(value)
      }
    },
    description: {
      get () {
        return this.get_selected_description()
      },
      set (value) {
        this.get_selected_description(value)
      }
    },
    edit_something () {
      for (var item in this.edit) {
        if (this.edit[item]) {
          return true
        }
      }
      return false
    },
    save_button_color () {
      if (this.edit_something) {
        return 'success'
      }
      return 'light'
    }
  },
  beforeMount () {
    const orderedcontents = this.get_orderedcontents()
    this.set_selected_content(orderedcontents[0])
  },
  mounted () {
    this.edit.content = false
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
