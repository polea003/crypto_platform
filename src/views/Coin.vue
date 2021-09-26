<template>
  <div class="md:mx-4 mb-20">

    <div class="m-2">
        <div class="text-2xl font-bold">{{coin}}</div>
    </div>

    <AreaChart/>

    <div class="flex font-bold text-xl">
        <div class="flex flex-col px-4 text-center w-1/2">
            <div>Ask</div>
            <div>${{priceData.ask_price.toFixed(4)}}</div>
        </div>
        <div class="hidden rounded-full px-12 bg-green-400 bg-opacity-75 cursor-pointer sm:flex items-center text-black">TRADE</div>
        <div class="flex flex-col px-4 text-center w-1/2">
            <div>Bid</div>
            <div>${{priceData.bid_price.toFixed(4)}}</div>
        </div>
    </div>
    <div class="text-xl font-bold rounded-full bg-green-400 bg-opacity-75 cursor-pointer flex items-center text-black px-8 py-2 justify-center my-4 mx-4 sm:hidden">TRADE</div>

    <div class="flex flex-col items-center md:flex-row md:justify-between xl:justify-evenly">

    <div class="p-2 flex flex-col mt-8">
        <div class="text-center font-bold md:hidden text-xl">Asks</div>
        <div class="flex font-bold">
            <div class="w-24">Exchange</div>
            <div class="w-32">QTY</div>
            <div class="pr-12">$</div>
        </div>
        <div v-for="ask in cbboData.asks" :key="ask" class="flex">
            <div class="w-24">{{ask.exchange}}</div>
            <div class="w-32">{{ask.qty}}</div>
            <div>{{ask.price}}</div>
        </div>
    </div>

    <div class="p-2 flex flex-col mt-8">
        <div class="text-center font-bold md:hidden text-xl">Bids</div>
        <div class="flex font-bold">
            <div class="w-24">Exchange</div>
            <div class="w-32">QTY</div>
            <div class="pr-12">$</div>
        </div>
        <div v-for="bid in cbboData.bids" :key="bid" class="flex">
            <div class="w-24">{{bid.exchange}}</div>
            <div class="w-32">{{bid.qty}}</div>
            <div>{{bid.price}}</div>
        </div>
    </div>

    </div>

  </div>
</template>

<script>
import AreaChart from "@/components/AreaChart.vue";

export default {
  name: "App",
  components: {
    AreaChart
  },
  computed: {
      uppercaseSymbol () {
          return this.symbol.toUpperCase()
      }


  },
  props: {
      coin: {
          type: String,
          required: true
      },
      symbol: {
          type: String,
          required: true
      }
  },
  data() {
    return {
        priceData: undefined,
        cbboData: undefined,
        connection: undefined,
        connection2: undefined
    }
  },
  created () {

    this.connection = new WebSocket("wss://portal.coinroutes.com/api/streaming/real_price/?token=6c634e1eacecc4801b000249287fbf923d5c8824")
    this.connection2 = new WebSocket("wss://portal.coinroutes.com/api/streaming/cbbo/?token=6c634e1eacecc4801b000249287fbf923d5c8824")

    // this.connection = new WebSocket("wss://ws-postman.eu-gb.mybluemix.net/ws/echo")
    this.connection.onmessage = (event) => {
      console.log(JSON.parse(event.data));
      let response = JSON.parse(event.data)
      this.priceData = response
    }

    this.connection2.onmessage = (event) => {
      console.log(JSON.parse(event.data));
      let response = JSON.parse(event.data)
      this.cbboData = response
    }

    this.connection.onopen = function(event) {
      console.log(event)
    }

    this.connection2.onopen = function(event) {
      console.log(event)
    }

    setTimeout(function () { this.fetchData() }.bind(this), 3000)

  },
  methods: {
    fetchData: function() {
      this.connection.send(`{"currency_pair":"${this.uppercaseSymbol}-USD", "quantity":"5.00"}`);
      this.connection2.send(`{"currency_pair":"${this.uppercaseSymbol}-USD", "quantity":"5.00"}`);
    }

  }
};
</script>