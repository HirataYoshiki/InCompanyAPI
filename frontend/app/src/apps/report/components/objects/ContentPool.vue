<template>
  <b-list-group horizontal>
    <draggable v-model="List" :group="group" draggable=".button">
      <b-list-group-item id="item" class="button flex-column align-items-start" v-for="content in List" :key="content.contentid">
        <b-icon icon="box" role="img" alt="icon" font-scale="2"></b-icon>
        <p>{{content.content.substr(0, 21)}}</p>
      </b-list-group-item>
    </draggable>
  </b-list-group>
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
  #item {
    display: inline-block;
    margin: 10px;
    padding: 10px;
    border: 1px solid #7f7f7f;
    border-radius: 10px;
    background-color: #ffffff;
  }

  #item:hover {
    cursor: grab;
  }
  #item:active {
    cursor: grabbing;
  }
</style>