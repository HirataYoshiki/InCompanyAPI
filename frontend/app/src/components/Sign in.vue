<template>
  <form>
    <div class="form-group">
      <label for="username">UserName</label>
      <input type="username" v-model="username" class="form-control" id="username" aria-describedby="usernameHelp" placeholder="Enter Your Name">
      <small id="usernameHelp" class="form-text text-muted">The input should be alphabets.</small>
    </div>
    <div class="form-group">
      <label for="Password">Password</label>
      <input type="password" v-model="password" class="form-control" id="Password" placeholder="Enter Password">
    </div>
      <div class="form-group">
      <label for="mailaddress">e-mail address</label>
      <input type="mailaddress" v-model="mailaddress" class="form-control" id="mailaddress" placeholder="Enter Your E-Mail">
      <small id="mailaddressHelp" class="form-text text-muted">Enter e-mail address if you want.</small>
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
    <div>
      <p>{{texte}}</p>
    </div>
  </form>
</template>
<script>
export default {
  name: 'Signin',
  data () {
    return {
      username: '',
      password: '',
      mailaddress: '',
      texte: ''
    } 
  },
  async get_token () {
    let form = new FormData()
    const url='https://localhost:8080/token'
    form.append('username', this.username, 'password', this.password)
    if (this.mailaddress !== '') {
      form.append('mailaddress', this.mailaddress)
    }
    const response = await this.axios.post(url, form) 
    this.texte = response.data.access_token
  }
}
</script>

<style scoped>
form {
  width: 50%;
  align-self: center;
}
</style>