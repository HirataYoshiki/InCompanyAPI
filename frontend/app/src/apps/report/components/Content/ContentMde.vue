<template>
  <div>
    <b-img :src="img" fluid alt="Responsive image"></b-img>
    <b-navbar>
      <b-navbar-nav class="ml-auto">
        <b-button variant="success" @click="save">Save</b-button>
      </b-navbar-nav>
    </b-navbar>
    <div id="mde">
      <vue-simplemde v-model="text" :configs="mdeconf"/>
    </div>
  </div>
</template>

<script>
import VueSimplemde from 'vue-simplemde'
export default {
  name: 'contentmde',
  components: {
    VueSimplemde
  },
  inject: [
    'create_headers',
    'request_contents'
  ],
  data () {
    return {
      text: '',
      img: require('@/assets/report/contentheader.png'),
      mdeconf: {
        placeholder: 'Input Content here',
        spellChecker: false
      }
    }
  },
  methods: {
    async save () {
      const headers = this.create_headers()
      const url = 'http://localhost:8080/reportapp/contents'
      const data = {
        content: this.text
      }
      await this.$axios.post(url, data, headers)
      alert('Saved')
      this.text = ''
      await this.request_contents()
    }
  }
}
</script>
<style scoped>
#mde {
  text-align: left;
}
</style>