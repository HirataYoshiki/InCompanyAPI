<template>
  <section class="min-vh-100">
    <b-navbar>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto mr-auto">
          <b-nav-text><h3>{{pagetitle}}</h3></b-nav-text>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <b-button :variant="save_button_color" @click="save">Save</b-button>
          <b-button variant="info" :to="{name: viewerpathname, params: {contents: allcontentstext}}" append>Preview</b-button>
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
          <b-form-group label="Selected Content:" label-for="input-content">
            <div id="input-content">
              <vue-simplemde v-model="mdevalue" :configs="conf"/>
            </div>
          </b-form-group>
          <b-form-group label="Contents:" label-for="contents">
            <div id="contents">
              <ContentPool :getter="get_contents" :setter="return_true" group="group"/>
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
          <b-list-group>
            <draggable v-model="contents" group="group" draggable=".button" v-on:update="updated('order')" v-on:add="updated('order')">
              <b-list-group-item
                id="contentorder"
                v-for="(content, i) in contents"
                class="button"
                @click.capture="change_content(content)"
                :key="content.contentid"
                :variant="color(content)"
              >
                <strong>{{i+1}}.</strong>
                <b-icon icon="box"></b-icon>
                {{content.content.substr(0, 21)}}
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
  name: 'reporteditor',
  components: {
    VueSimplemde,
    ContentPool,
    draggable
  },
  props: {
    pagetitle: String,
    reporttitlegetter: Function,
    reporttitlesetter: Function,
    descriptiongetter: Function,
    descriptionsetter: Function,
    ordercontentsgetter: Function,
    ordercontentssetter: Function,
    selectedcontentgetter: Function,
    selectedcontentsetter: Function,
    savefunc: Function,
    viewerpathname: String
  },
  inject: [
    'get_contents'
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
      this.savefunc(this.edit)
      for (var key in this.edit) {
        this.edit[key] = false
      }
    },
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
      this.selectedcontentsetter(content)
      this.edit.content = false
    },
    color (content) {
      if (content === this.selectedcontent) {
        return 'success'
      }
      return ''
    },
    go_to_viewer () {
      const textarray = this.contents.map(n => n.content)
      this.$router.push({path: this.$route.path + '/viewer', params: {contents: textarray.join('\n\n')}})
    }
  },
  computed: {
    reporttitle: {
      get () {
        return this.reporttitlegetter()
      },
      set (value) {
        this.reporttitlesetter(value)
        this.updated('title')
      }
    },
    description: {
      get () {
        return this.descriptiongetter()
      },
      set (value) {
        this.descriptionsetter(value)
        this.updated('description')
      }
    },
    contents: {
      get () {
        return this.ordercontentsgetter()
      },
      set (contents) {
        this.ordercontentssetter(contents)
        this.updated('order')
      }
    },
    selectedcontent: {
      get () {
        return this.selectedcontentgetter()
      },
      set (content) {
        this.selectedcontentsetter(content)
        this.updated('content')
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
    },
    mdevalue: {
      get () {
        return this.selectedcontent.content
      },
      set (content) {
        this.updated('content')
        this.selectedcontent.content = content
      }
    },
    allcontentstext () {
      return this.contents.map(n => n.content).join('\n\n')
    }
  },
  mounted () {
    if (!this.contents.length === 0) {
      this.selectedcontentsetter(this.contents[0])
    }
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