<template>
  <div>
    <b-list-group>
      <b-list-group-item><h4 class="text-align-start">Name: {{Name}}</h4></b-list-group-item>
      <b-list-group-item><h6 class="text-align-start"><u>-Department: {{Department}}</u></h6></b-list-group-item>
      <b-list-group-item><h6 class="text-align-start"><u>-Position: {{Position}}</u></h6></b-list-group-item>
      <b-list-group-item>
        <b-form-tags input-id="tags-basic" tag-variant="primary" v-model="Skills" placeholder="Add your skill" remove-on-delete></b-form-tags>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
export default {
  name: 'CharacterRightside',
  props: {
    Name: String,
    Department: String,
    Position: String,
    Skills: Object
  },
  watch: {
    Name: function () {
      this.Name = this.Name
    },
    Department: function () {
      this.Department = this.Department
    },
    Position: function () {
      this.Position = this.Position
    },
    Skills: function () {
      this.Skills = this.Skills
    }
  }
}
</script>
