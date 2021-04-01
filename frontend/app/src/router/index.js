import Vue from 'vue'
import Router from 'vue-router'
import { AppsRoute } from '@/apps/appsroute'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueSimplemde from 'vue-simplemde'
import 'simplemde/dist/simplemde.min.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.prototype.$axios = axios

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueAxios, axios)
Vue.use(Router)
Vue.use(VueSimplemde)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: AppsRoute
})