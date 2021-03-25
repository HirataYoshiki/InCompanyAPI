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
  props: {
    initialtext: String
  },
  data () {
    return {
      text: this.initialtext
    }
  },
  methods: {
    show () {
      alert(this.text)
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