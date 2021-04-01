<template>
  <b-container fluid class="mt-4">
    <div v-if="!MyCharacter.NewUser">
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
          <div v-show="!NotEditMode">
            <b-form-group>
              <b-button size="small" pill variant="warning" @click="update_profile">Update !<b-icon icon="check-circle"></b-icon></b-button>
            </b-form-group>
            <b-form-group>
              <b-button size="small" pill variant="danger" @click="rollback_edit">Decline <b-icon icon="x-circle"></b-icon></b-button>
            </b-form-group>
          </div>
          <b-row id="editbutton" v-if="NotEditMode">
            <b-col>
              <b-button size="small" pill variant="outline-success" @click="switch_edit_mode">Edit Profile<b-icon icon="pencil-square"></b-icon></b-button>
            </b-col>
          </b-row>
        </b-col>
        <b-col id="top-rightside">
          <div>
            <b-form-group label="Name: " label-for="text_name" label-cols-sm="3" label-align-sm="right">
              <b-form-input id="text_name" v-model="character.username" disabled></b-form-input>
            </b-form-group>
            <b-form-group label="Department: " label-for="text_department" label-cols-sm="3" label-align-sm="right">
              <b-form-input id="text_department" v-model="character.department" v-bind:disabled="NotEditMode"></b-form-input>
            </b-form-group>
            <b-form-group label="Position: " label-for="text_position" label-cols-sm="3" label-align-sm="right">
              <b-form-input id="text_position" v-model="character.position" v-bind:disabled="NotEditMode"></b-form-input>
            </b-form-group>
            <b-form-group label="Skills: " label-for="tag_skills" label-cols-sm="3" label-align-sm="right">
              <b-form-tags input-id="tags-basic" id="tag_skills" tag-variant="primary" v-model="character.skills" placeholder="Add your skill" v-bind:disabled="NotEditMode" remove-on-delete></b-form-tags>
            </b-form-group>
          </div>
        </b-col>
      </b-form-row>
    </div>
    <div v-else>
      <b-card bg-variant="light">
        <b-form-group
          label-cols-lg="3"
          label="Add Profile"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <b-form-group
            label="Department:"
            label-for="nested-department"
            label-cols-sm="3"
            label-align-sm="right"
          >
            <b-form-input id="nested-department" v-model="character.department"></b-form-input>
          </b-form-group>
          <b-form-group
            label="Position:"
            label-for="nested-position"
            label-cols-sm="3"
            label-align-sm="right"
          >
            <b-form-input id="nested-position" v-model="character.position"></b-form-input>
          </b-form-group>
          <b-form-group
            label="Skills:"
            label-for="nested-skills"
            label-cols-sm="3"
            label-align-sm="right"
          >
            <b-form-tags id="nested-skills" input-id="tags-basic" tag-variant="primary" v-model="character.skills" placeholder="Add your skill" remove-on-delete></b-form-tags>
          </b-form-group>
          <b-form-group>
            <b-button  size="small" pill variant="primary" @click="post_new_profile"><b-icon icon="person-plus-fill"></b-icon>Create Profile</b-button>
          </b-form-group>
        </b-form-group>
      </b-card>
    </div>
  </b-container>
</template>

<script>
export default {
  name: 'character',
  props: {
    MyCharacter: Object
  },
  inject: [
    'create_headers'
  ],
  data () {
    return {
      character: {
        id: this.MyCharacter.contents.id,
        username: this.MyCharacter.contents.username,
        department: this.MyCharacter.contents.department,
        position: this.MyCharacter.contents.position,
        skills: this.MyCharacter.contents.skills
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
    },
    async update_profile () {
      let requestbody = {
        department: this.character.department,
        position: this.character.position,
        skills: this.character.skills
      }
      let URL = 'http://localhost:8080/characters/me'
      try {
        let headers = this.create_headers()
        const response = await this.$axios.put(URL, requestbody, headers)
        this.$parent.character.contents = JSON.parse(JSON.stringify(response.data))
        this.NotEditMode = true
      } catch (e) {
        alert(e)
      }
    },    
    async post_new_profile () {
      let URL = 'http://localhost:8080/characters'
      try {
        let headers = this.create_headers()
        const response = await this.$axios.post(URL, this.character, headers)
        this.$parent.character.contents = JSON.parse(JSON.stringify(response.data))
        this.$parent.character.NewUser = false
        this.NotEditMode = true
        alert('Register Complete')
      } catch (e) {
        alert(e)
      }
    },
    async rollback_edit () {
      await this.$parent.set_character()
      this.NotEditMode = true
    }
  },
  watch: {
    MyCharacter: function () {
      this.MyCharacter = this.MyCharacter
    }
  }
}
</script>