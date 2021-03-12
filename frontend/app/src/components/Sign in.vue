<template>
<section id="cover" class="min-vh-100">
  <div id="cover-caption">
    <div class="container">
      <div class="row text-green">
        <div class="col-xl-5 col-lg-6 col-md-8 col-sm-10 mx-auto text-center form p-4">
          <h1 class="display-4 py-2 text-truncate">Sign in</h1>
            <div class="px-2">
              <form action="" class="justify-content-center">
                <div class="form-group row">
                  <label for="username" class="col-sm-2 col-form-label">UserName</label>
                  <div class="col-sm-10">
                    <input class="form-control" id="username" placeholder="Enter your name.">
                  </div>
                </div>
                <div class="form-group row">
                  <label for="password" class="col-sm-2 col-form-label">Password</label>
                  <div class="col-sm-10">
                    <input type="password" class="form-control" id="password" placeholder="Enter password.">
                  </div>
                </div>
                <div class="form-group row">
                  <label for="mailaddress" class="col-sm-2 col-form-label">E-mail</label>
                  <div class="col-sm-10">
                    <input class="form-control" id="mailaddress" placeholder="Enter your E-mail address.">
                  </div>
                </div>
                <button type="submit" class="btn btn-primary btn-lg" @click="get_token">Sign in</button>
              </form>
            </div>
        </div>
      </div>
    </div>
  </div>
</section>
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
input {
  width: 60%;
}
</style>