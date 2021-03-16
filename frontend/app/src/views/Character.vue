<template>
  <b-container fluid>
    <b-form-row id="topside">
      <b-col id="top-leftside">
        <b-row id="pictureframe" class="justify-content-md-center">
          <b-col xl="5">
            <b-avatar square size="15rem"></b-avatar>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            No. {{character.id}}
          </b-col>
        </b-row>
        <b-row id="editbutton">
          <b-col>
            <b-button size="small" pill variant="outline-success" @click="switch_edit_mode">Edit Profile</b-button>
          </b-col>
        </b-row>
      </b-col>
      <b-col id="top-rightside">
        <div class="text-align-start">
          <b-list-group>
            <b-list-group-item><h4><u>Name: {{character.username}}</u></h4></b-list-group-item>
            <b-list-group-item><h6><u>-Department: {{character.department}}</u></h6></b-list-group-item>
            <b-list-group-item><h6><u>-Position: {{character.position}}</u></h6></b-list-group-item>
            <b-list-group-item>
              <b-form-tags input-id="tags-basic" tag-variant="primary" v-model="character.skills" placeholder="Add your skill" v-bind:disabled="NotEditMode"></b-form-tags>
            </b-list-group-item>
          </b-list-group>
        </div>
      </b-col>
    </b-form-row>
    <b-form-row id="bottomside" class="text-center">
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