<template>
  <b-container fluid>
    <b-form-row id="topside" class="h-50">
      <b-col col lg="4" id="top-leftside">
        <b-row id="pictureframe" align-v="stretch" class="justify-content-md-center">
          <b-col xl="5">
            <b-avatar sqare size="6rem"></b-avatar>
          </b-col>
        </b-row>
        <b-row id="idframe" align-v="end">
          <b-col>
            No. {{character.id}}
          </b-col>
        </b-row>
      </b-col>
      <b-col id="top-rightside">
        <div class="text-align-left">
          <h3><u>Name: {{character.username}}</u></h3>
          <h4><u>Department: {{character.department}}</u></h4>
          <h4><u>Position: {{character.position}}</u></h4>
        </div>
      </b-col>
    </b-form-row>
    <b-form-row id="bottomside" class="text-center">
      <div>
        <b-form-tags input-id="tags-basic" tag-variant="primary" v-model="character.skills" placeholder="Add your skill" v-bind:disabled="NotEditMode"></b-form-tags>
      </div>
      <div>
        <b-button variant="success" @click="switch_edit_mode">Edit Profile</b-button>
      </div>
    </b-form-row>
  </b-container>
</template>

<script>
export default {
  name: 'character',
  props: {
    MyCharacter: Object
  },
  data () {
    return {
      character: {
        id: this.MyCharacter.id,
        username: this.MyCharacter.username,
        department: this.MyCharacter.department,
        position: this.MyCharacter.position,
        skills: this.MyCharacter.skills
      },
      NotEditMode: true
    }
  },
  methods: {
    switch_edit_mode () {
      if (this.NotEditMode) {
        this.NotEditMode = false
      } else {
        this.NotEditMode = true
      }
    }
  },
  watch: {
    MyCharacter: function () {
      this.MyCharacter = this.MyCharacter
    }
  }
}
</script>