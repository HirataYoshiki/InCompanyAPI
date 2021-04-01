<template>
    <b-card-group deck>
      <draggable v-model="List" :group="group">
        <b-card class="item m-1" style="width: 10rem; height: 15rem;" v-for="content in List" :key="content.contentid">
          <b-card-body>
            <b-icon icon="box" role="img" alt="icon" font-scale="2"></b-icon>
            <b-card-text>{{content.content.substr(0, 21)}}</b-card-text>
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