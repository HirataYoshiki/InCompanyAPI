<template>
  <div v-if="this.$route.path==='/report/contents'">
    <div>
      <b-img :src="img" fluid alt="Responsive image"></b-img>
    </div>
    <b-card-group deck class="mt-2">
      <div v-for="(content, i) in contents" :key="content.contentid">
        <Contentcard
          :content="content"
          :title="'Content '+(i+1)"
          :icon="'box'"
          :description="content.content"
          :subtitle="''"
          :overlayOKfunc="overlaydeleteok"
          :contentgetter="contentgetter"
          :contentsetter="contentsetter"
          :savefunc="savefunc"
          :selectedcontentsetter="selectedcontentsetter"
        />
      </div>
    </b-card-group>
  </div>
  <div v-else>
    <router-view/>
  </div>
</template>

<script>
import Contentcard from '@/apps/report/components/Contents/Card/Contentcard'
export default {
  name: 'contents',
  components: {
    Contentcard
  },
  inject: [
    'get_contents',
    'create_headers',
    'delete_from_contents',
    'request_contents'
  ],
  data () {
    return {
      img: require('@/assets/report/contentsheader.png'),
      selectedcontent: {
        content: '',
        contentid: 0,
        localcontentid: 0,
        username: ''
      }
    }
  },
  computed: {
    contents () {
      return this.get_contents()
    }
  },
  methods: {
    contentgetter () {
      return this.selectedcontent.content
    },
    contentsetter (value) {
      this.selectedcontent.content = value
    },
    selectedcontentgetter () {
      return this.selectedcontent
    },
    selectedcontentsetter (selectedcontent) {
      this.selectedcontent = selectedcontent
    },
    async overlaydeleteok (content) {
      try {
        const headers = this.create_headers()
        const url = 'http://localhost:8080/reportapp/contents/' + String(content.localcontentid)
        await this.$axios.delete(url, headers)
        this.delete_from_contents(content)
      } catch (e) {
        alert('the content is used in some report. cant delete this.')
      }
    },
    async savefunc () {
      try {
        const headers = this.create_headers()
        const url = 'http://localhost:8080/reportapp/contents/' + String(this.selectedcontent.localcontentid)
        const data = {content: this.selectedcontent.content}
        await this.$axios.put(url, data, headers)
        await this.request_contents()
      } catch (e) {
        alert('Error')
      }
    }
  } 
}
</script>