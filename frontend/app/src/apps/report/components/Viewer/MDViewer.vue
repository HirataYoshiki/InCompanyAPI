<template>
  <vue-simplemde id="mde" :value="contents" :configs="configs"/>
</template>
<script>
import VueSimplemde from 'vue-simplemde'
export default {
  name: 'mdeviewer',
  components: {
    VueSimplemde
  },
  props: {
    contents: String
  },
  data () {
    return {
      configs: {
        showIcons: ['preview'],
        spellCheck: false
      }
    }
  }
}
</script>
<style scoped>
#mde {
  text-align: left;
}
</style>