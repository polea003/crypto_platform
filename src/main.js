import Vue from 'vue'
import App from './App.vue'
import './index.css'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuex from 'vuex'

Vue.use(Vuex)
Vue.config.productionTip = false
Vue.use(VueAxios, axios)


const store = new Vuex.Store({
  state: {
    user: {
      portfolio: {
        coins: [
          {
            id: 'bitcoin',
            quantity: 0.012
          },
          {
            id: 'ethereum',
            quantity: 0.102
          },
          {
            id: 'dogecoin',
            quantity: 330.27
          },            
        ]
      },
      coinData: undefined
    }
  },
  mutations: {
    updateCoinData (state, coinData) {
      state.coinData = coinData
    }
  }
})

new Vue({
  router,
  store: store,
  render: h => h(App)
}).$mount('#app')
