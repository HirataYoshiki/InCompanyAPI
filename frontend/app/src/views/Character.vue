<template>
  <div>
    <div v-for="(value, name) in MyCharacter" :key="name">
      <ui>
        <li>
          <p>
            {{name}} : {{value}}
          </p>
        </li>
      </ui>
    </div>
  </div>
</template>

<script>
export default {
  name: 'character',
  props: {
    MyCharacter: Object
  },
  watch: {
    MyCharacter: function () {
      this.MyCharacter = this.MyCharacter
    }
  }
}
</script>