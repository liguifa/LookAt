import Vue from 'vue'
import App from './App.vue'
import Axios from "axios"
import iView from "iview"
import router from "./router"
import VueRouter from "vue-router"
import VueAsyncComputed from "vue-async-computed"
import 'iview/dist/styles/iview.css'

Vue.use(iView)
Vue.use(VueRouter)
Vue.use(VueAsyncComputed)

Vue.config.productionTip = false

Vue.mixin({
  data(){
    return {
      Axios
    }
  }
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
