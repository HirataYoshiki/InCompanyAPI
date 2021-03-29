<template>
    <draggable v-model="List" :clone="clone">
      <div class="item" style="width: 15rem; height: 20rem;" v-for="content in List" :key="content.contentid">
        <b-icon icon="file-text" role="img" alt="icon" font-scale="4"></b-icon>
      </div>
    </draggable>
</template>

<script>
import draggable from 'vuedraggable'
export default {
  name: 'contentpool',
  props: {
    getter: Function,
    setter: Function
  },
  components: {
    draggable
  },
  methods: {
    clone (content) {
      return content
    }
  },
  computed: {
    List: {
      get () {
        return this.getter()
      },
      set (value) {
        this.setter(value)
      }
    }
  }
}
</script>
<style scoped>
 .item {
    display: inline-block;
  }
</style>