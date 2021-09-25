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
      connection: null
    }
  },
  created: function() {
    console.log("Starting connection to WebSocket Server")
    this.connection = new WebSocket("wss://portal.coinroutes.com/api/streaming/real_price/?token=6c634e1eacecc4801b000249287fbf923d5c8824")

    // this.connection = new WebSocket("wss://ws-postman.eu-gb.mybluemix.net/ws/echo")
    this.connection.onmessage = function(event) {
      console.log(event);
    }

    this.connection.onopen = function(event) {
      console.log(event)
      console.log("Successfully connected to the echo websocket server...")
    }

    fetch('https://portal.coinroutes.com/api/currency_pairs/', {
      method: "GET",
      headers: {"Authorization": "Token 6c634e1eacecc4801b000249287fbf923d5c8824"}
    })
    .then(response => response.json()) 
    .then(json => console.log(json)) 
    .catch(err => console.log(err));
    
  },
  methods: {
    sendMessage: function() {
      // this.connection.send('hello');
      this.connection.send('{"currency_pair":"BTC-USD", "quantity":"5.00"}');
    }
  }
}
</script>