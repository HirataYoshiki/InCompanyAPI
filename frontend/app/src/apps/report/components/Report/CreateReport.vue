<template>
  <div>
    <b-img :src="img" fluid alt="Responsive image"></b-img>
    <b-navbar>
      <b-navbar-nav class="ml-auto">
        <b-button variant="success" @click="save">Save</b-button>
      </b-navbar-nav>
    </b-navbar>
    <b-form-input label="Title:" v-model="title" placeholder="Enter title"></b-form-input>
    <b-form-input label="Description:" v-model="description" placeholder="Enter description"></b-form-input>
    <b-container fluid>
      <b-row>
        <b-col>
          <ContentPool :getter="get_contents" :setter="return_true" :group="group"/>
        </b-col>
        <b-col>
          <b-icon icon="layers" font-scale="4"></b-icon>
          <b-form-group
            label="Build up report!"
            label-for="content_order"
          >
            <b-list-group id="content_order">
              <draggable v-model="order" :group="group" draggable=".button">
                <b-list-group-item
                  id="contentorder"
                  class="button"
                  v-for="(content, i) in order" :key="i"
                >
                  <strong>{{i+1}}.</strong>
                  <b-icon icon="box"></b-icon>
                  {{content.content.substr( 0, 21)}}
                </b-list-group-item>
              </draggable>
              <b-list-group-item slot="footer" variant="light" id="contentorderfooter">Drag and Drop Content</b-list-group-item>
            </b-list-group>
          </b-form-group>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import ContentPool from '@/apps/report/components/objects/ContentPool'
import draggable from 'vuedraggable'
export default {
  name: 'createreport',
  components: {
    ContentPool,
    draggable
  },
  inject: [
    'get_contents',
    'create_headers'
  ],
  data () {
    return {
      img: require('@/assets/buildreportheader.png'),
      group: 'createreport',
      title: '',
      description: '',
      order: []
    }
  },
  methods: {
    return_true () {
      return true
    },
    async _post (endpoint, data) {
      const headers = this.create_headers()
      const response = await this.$axios.post(endpoint, data, headers)
      return response.data
    },
    async save () {
      var data1 = { localcontentids: this.order.map(n => n.localcontentid) }
      var url1 = 'http://localhost:8080/reportapp/groups'
      const resgroup = await this._post(url1, data1)

      var body = {
        title: this.title,
        localgroupid: resgroup.localgroupid
      }
      alert(resgroup.localgroupid)
      if (this.description) {
        var url2 = 'http://localhost:8080/reportapp/headers'
        var data2 = { type: this.description }
        const resheader = await this._post(url2, data2)
        body.headerid = resheader.localheaderid
      }
      var url3 = 'http://localhost:8080/reportapp/reports'
      await this._post(url3, body)
      alert('saved')
    }
  }
}
</script>
<style scoped>
#contentorder {
  text-align: left;
}
</style>