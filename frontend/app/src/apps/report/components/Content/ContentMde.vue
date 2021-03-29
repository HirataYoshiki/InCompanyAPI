<template>
<div id="mde">
  <VueSimplemde/>
</div>
</template>

<script>
import VueSimplemde from 'vue-simplemde'
export default {
  name: 'contentmde',
  components: {
    VueSimplemde
  }
}
</script>
<style scoped>
#mde {
  text-align: left;
}
</style>