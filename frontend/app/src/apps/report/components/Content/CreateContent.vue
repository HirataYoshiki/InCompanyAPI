<template>
  <ContentEditor
    :contentgetter="contentgetter"
    :contentsetter="contentsetter"
    :savefunc="save"
  />
</template>

<script>
import ContentEditor from '@/apps/report/components/objects/ContentEditor'
export default {
  name: 'contentmde',
  components: {
    ContentEditor
  },
  inject: [
    'create_headers',
    'request_contents'
  ],
  data () {
    return {
      content: ''
    }
  },
  methods: {
    async save () {
      const headers = this.create_headers()
      const url = 'http://localhost:8080/reportapp/contents'
      const data = {
        content: this.content
      }
      await this.$axios.post(url, data, headers)
      alert('Saved')
      this.content = ''
      await this.request_contents()
    },
    contentgetter () {
      return this.content
    },
    contentsetter (value) {
      this.content = value
    }
  }
}
</script>
<style scoped>
#mde {
  text-align: left;
}
</style>