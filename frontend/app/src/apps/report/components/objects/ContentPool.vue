<template>
    <b-card-group deck>
      <draggable v-model="List" :clone="clone" :group="group">
        <b-card class="item" v-for="content in List" :key="content.contentid">
          <b-card-body>
            <b-icon icon="file-text" role="img" alt="icon" font-scale="4"></b-icon>
            <b-card-text>{{content.content}}</b-card-text>
          </b-card-body>
        </b-card>
      </draggable>
    </b-card-group>
</template>

<script>
import draggable from 'vuedraggable'
export default {
  name: 'contentpool',
  props: {
    getter: Function,
    setter: Function,
    group: String
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