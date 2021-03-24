<template>
  <div id="mde">
    <vue-simplemde v-model="text" value="MarkDown形式で記入してください。" ref="markdownEditor"/>
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
  data () {
    return {
      text: ''
    }
  },
  methods: {
    show () {
      alert(this.text)
    }
  }
}
</script>
<style scoped>
#mde {
  text-align: left;
}
</style>