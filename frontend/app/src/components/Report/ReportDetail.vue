<template>
  <b-card bg-variant="light">
    <b-container fluid>
      <b-row>
        <b-col class="ml-auto text-secondary" md="4">
          <b-button :variant="[ edit ? 'warning': 'primary' ]" pill @click="change_editmode">
            {{ButtonLabel}}
          </b-button>
          <b-button @click="back" variant="dark">Back</b-button>
        </b-col>
      </b-row>
      <b-row align-v="center" class="bg-secondary">
        <b-col class="text-white">
          <h2>{{report.title}}</h2>
        </b-col>
      </b-row>
      <b-row>
        <b-col class="ml-auto text-secondary" md="4">
          <h5>Name: {{report.username}}</h5>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <div id="mde">
            <vue-simplemde v-model="Mdevalue" ref="markdownEditor"></vue-simplemde>
          </div>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <b-button variant="danger" @click="_create_content">
            content
          </b-button>
          <b-button variant="warning" @click="_create_group">
            group
          </b-button>
          <b-button variant="success" @click="create_report">
            report
          </b-button>

        </b-col>
      </b-row>
    </b-container>
  </b-card>
</template>

<script>
import VueSimplemde from 'vue-simplemde'
export default {
  name: 'reportdetail',
  components: {
    VueSimplemde
  },
  props: {
    Report: Object
  },
  inject: [
    'create_headers',
    'changeselectmode'
  ],
  data () {
    return {
      edit: false,
      ButtonLabel: 'Edit', 
      report: {
        localreportid: this.Report.localreportid,
        username: this.Report.username,
        title: this.Report.title,
        timestamp: this.Report.timestamp
      },
      contents: [],
      Mdevalue: '',
      endpoints: {
        reports: 'http://localhost:8080/reportapp/reports',
        groups: 'http://localhost:8080/reportapp/groups',
        contents: 'http://localhost:8080/reportapp/contents'
      }
    }
  },
  methods: {
    async set_value () {
      try {
        const url = this.endpoints.reports + '/' + String(this.Report.localreportid)
        const headers = this.create_headers
        const response = await this.$axios.get(url, headers)
        const groupid = response.data.localgroupid
        const url2 = this.endpoints.groups + '/' + String(groupid)
        const response2 = await this.$axios.get(url2, headers)
        const contentid = response2.data.contents[0]
        const url3 = this.endpoints.contents + '/' + String(contentid)
        const response3 = await this.$axios.get(url3, headers)
        this.Mdevalue = response3.data.content
      } catch (e) {
        this.Mdevalue = '## Hi.\n### try it again'
      }
    },
    change_editmode () {
      if (this.edit) {
        this.edit = false
        this.ButtonLabel = 'Edit'
      } else {
        this.edit = true
        this.ButtonLabel = 'Update'
      }
    },
    back () {
      this.changeselectmode()
    },
    async _create_content () {
      try {
        const headers = this.create_headers
        const data = {content: this.Mdevalue}
        const response = await this.$axios.post(this.endpoints.contents, data, headers)
        return response.data
      } catch (e) {
        alert('Error: create contents', e)
      }
    },
    async _create_group () {
      try {
        const content = await this._create_content()
        const headers = this.create_headers
        const data = {localcontentids: [content.localcontentid]}
        const response = await this.$axios.post(this.endpoints.groups, data, headers)
        return response.data
      } catch (e) {
        alert('Error: create group', e)
      }
    },
    async create_report () {
      try {
        const group = await this._create_group()
        const headers = this.create_headers
        const data = {
          title: 'new',
          contentgroupid: group.localgroupid 
        }
        await this.$axios.post(this.endpoints.reports, data, headers)
      } catch (e) {
        alert(e)
      }
    }
  },
  created () {
    this.set_value()
  },
  watch: {
    Report () {
      this.Report = this.Report
    }
  }
}
</script>
<style scoped>
#mde {
  text-align: left;
}
</style>
