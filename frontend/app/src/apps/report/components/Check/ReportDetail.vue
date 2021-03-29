<template>
  <section class="min-vh-100">
    <div id="mde">
      <VueSimplemde/>
    </div>
    <ContentPool :getter="get_contents" :setter="no_return"/>
    <b-row>
      <b-col align-self="stretch">
        hi
      </b-col>
    </b-row>
  </section>
</template>

<script>
import VueSimplemde from 'vue-simplemde'
import ContentPool from '@/apps/report/components/objects/ContentPool'
export default {
  name: 'reportdetail',
  components: {
    VueSimplemde,
    ContentPool
  },
  inject: [
    'get_contents',
    'create_headers',
    'set_orderedcontents',
    'get_orderedcontents'
  ],
  data () {
    return {
      list: []
    }
  },
  methods: {
    no_return (value) {
      return true
    }
  }
}

</script>
<style scoped>
#mde {
  text-align: left;
}
</style>
