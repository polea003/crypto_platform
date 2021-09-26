<template>
  <div class="home">
    <div class="flex justify-center">
    <img alt="Vue logo" src="../assets/logo.png" @click="sendMessage" class="cursor-pointer">
    </div>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <router-link to="/Blog">About</router-link>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  data: function() {
    return {
      connection: null,
      coins: null,
      coinData: undefined
    }
  },
  created: function() {

    this.fetchData()

    console.log("Starting connection to WebSocket Server")
    this.connection = new WebSocket("wss://portal.coinroutes.com/api/streaming/real_price/?token=6c634e1eacecc4801b000249287fbf923d5c8824")

    // this.connection = new WebSocket("wss://ws-postman.eu-gb.mybluemix.net/ws/echo")
    this.connection.onmessage = (event) => {
      console.log(JSON.parse(event.data));
      let response = JSON.parse(event.data)
      this.coinData = response
    }

    this.connection.onopen = function(event) {
      console.log(event)
      console.log("Successfully connected to the echo websocket server...")
    }

    // fetch('https://portal.coinroutes.com/api/currency_pairs/', {
    //   method: "GET",
    //   headers: {"Authorization": "Token 6c634e1eacecc4801b000249287fbf923d5c8824"}
    // })
    // .then(response => response.json()) 
    // .then(json => console.log(json)) 
    // .catch(err => console.log(err));

    // this.axios.get('https://api.coingecko.com/api/v3/coins/list').then(res => {
    //         console.log(res);
    //       }).catch(err => {
    //         console.log(err.response); https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Cdogecoin&vs_currencies=usd
    //       });
    
    // this.axios.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').then(res => {
    //     console.log(res);
    //   }).catch(err => {
    //     console.log(err.response);
    //   });
    
    this.axios.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Cdogecoin&vs_currencies=usd').then(res => {
        console.log(res.data)
        this.coins = res.data
      }).catch(err => {
        console.log(err.response);
      });
  },
  methods: {
    fetchData: function() {
      this.axios.get('https://api.coingecko.com/api/v3/coins/bitcoin?localization=false&community_data=false&developer_data=false&sparkline=false').then(res => {
          console.log(res.data)
          this.coinData = res.data
        }).catch(err => {
          console.log(err.response);
        });
        setTimeout(function () { this.fetchData() }.bind(this), 3000)
    },
    sendMessage: function() {
      // this.connection.send('hello');
      this.connection.send('{"currency_pair":"BTC-USD", "quantity":"5.00"}');
    }
  }
}
</script>