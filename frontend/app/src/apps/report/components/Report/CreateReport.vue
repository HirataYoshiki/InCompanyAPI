<template>
  <div v-if="this.$route.path==='/report/report'">
    <b-img :src="img" fluid alt="Responsive image"></b-img>
    <ReportEditor
      :pagetitle="pagetitle"
      :reporttitle="reporttitle"
      :description="description"
      :reporttitlegetter="reporttitlegetter"
      :reporttitlesetter="reporttitlesetter"
      :descriptiongetter="descriptiongetter"
      :descriptionsetter="descriptionsetter"
      :ordercontentsgetter="ordercontentsgetter"
      :ordercontentssetter="ordercontentssetter"
      :selectedcontentgetter="selectedcontentgetter"
      :selectedcontentsetter="selectedcontentsetter"
      :savefunc="save"
      :viewerpathname="'createreportviewer'"
    />
  </div>
  <div v-else>
    <router-view/>
  </div>
</template>

<script>
import ReportEditor from '@/apps/report/components/objects/ReportEditor'
export default {
  name: 'createreport',
  components: {
    ReportEditor
  },
  inject: [
    'create_headers'
  ],
  data () {
    return {
      img: require('@/assets/report/buildreportheader.png'),
      pagetitle: 'Create Report',
      reporttitle: '',
      description: '',
      ordercontents: [],
      selectedcontent: {
        content: '',
        contentid: 0,
        localcontentid: 0,
        username: ''
      }
    }
  },
  methods: {
    reporttitlegetter: function () {
      return this.reporttitle
    }, 
    reporttitlesetter: function (value) {
      this.reporttitle = value
    }, 
    descriptiongetter: function () {
      return this.description
    }, 
    descriptionsetter: function (value) {
      this.description = value
    }, 
    ordercontentsgetter: function () {
      return this.ordercontents
    },
    ordercontentssetter: function (contents) {
      this.ordercontents = contents
    }, 
    selectedcontentgetter: function () {
      return this.selectedcontent
    },
    selectedcontentsetter: function (content) {
      this.selectedcontent = content
    },
    async _post (endpoint, data) {
      const headers = this.create_headers()
      const response = await this.$axios.post(endpoint, data, headers)
      return response.data
    },
    async save () {
      var data1 = { localcontentids: this.ordercontents.map(n => n.localcontentid) }
      var url1 = 'http://localhost:8080/reportapp/groups'
      const resgroup = await this._post(url1, data1)

      var body = {
        title: this.reporttitle,
        localgroupid: resgroup.localgroupid
      }
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