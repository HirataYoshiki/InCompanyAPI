<template>
  <div id="mde">
    <vue-simplemde v-model="text" ref="markdownEditor"/>
    <b-button @click="show">show</b-button>
  </div>
</template>

<script>
import VueSimplemde from 'vue-simplemde'
export default {
  name: 'mdetest',
  components: {
    VueSimplemde
  },
  props: {
    initialtext: String,
    localreportid: Number
  },
  inject: [
    'create_headers'
  ],
  data () {
    return {
      text: ''
    }
  },
  beforeMount () {
    this.text = this.initialtext
  },
  methods: {
    show () {
      alert(this.text)
    },
    async post_content () {
      try {
        const url1 = 'http://localhost:8080/reportapp/contents'
        const headers = this.create_headers
        const ContentResponse = await this.$axios.post(url1, {'content': this.text}, headers) 
        const url2 = 'http://localhost:8080/reportapp/' + String(this.localreportid)
        const data = { 
          contentsid: ContentResponse.localreportid
        }
        await this.$axios.put(url2, data, headers)
      } catch (e) {
        alert(e)
      }
    }
  },
  watch: {
    initialtext: function () {
      this.initialtext = this.initialtext
    }
  }
}
</script>
<style scoped>
#mde {
  text-align: left;
}
</style>