<template>
  <div class="md:mx-4 mb-20">
    <div class="m-2">
    <div class="text-xl font-bold">Portfolio Performance</div>
    <div class="text-2xl font-bold">${{portfolioValuation}}</div>
    </div>
    <AreaChart/>
    <div class="flex justify-between px-4 items-center">
      <div>1D</div>
      <div>1W</div>
      <div>1M</div>
      <div class="bg-green-600 text-white py-1 px-2 rounded">6M</div>
      <div>1Y</div>
    </div>
    
    <div class="text-xl mt-8 ml-2 font-bold md:text-center">Asset Breakdown</div>
    <div class="flex flex-col lg:flex-row lg:justify-center items-center">

      <div v-if="dataFetched">
        <PieChart :labels="pieLabels" :data="pieData" class="w-64"/>
      </div>

      <div class="flex flex-col items-center ml-6">
        <div class="flex font-bold">
          <div class="w-20">%</div>
          <div class="w-28">Asset</div>
          <div class="w-20">Quantity</div>
          <div class="w-20">Value</div>
        </div>
        <div class="flex flex-col">
          <div v-for="coin in coinData" :key="coin.id" class="flex items-center">
            <div class="w-20">{{(((coin.quantity * coin.market_data.current_price.usd)/portfolioValuation).toFixed(2)*100).toFixed(0)}}</div>
            <div class="w-28 capitalize truncate">{{coin.id}}</div>
            <div class="w-20">{{coin.quantity}}</div>
            <div class="w-20 text-green-500">${{(coin.quantity * coin.market_data.current_price.usd).toFixed(2)}}</div>
          </div>
        </div>
      </div>
    </div>

    <div class="text-xl mt-8 ml-2 font-bold mb-4 md:text-center">Transaction History</div>
    <div class="flex flex-col items-center">
    <div class="flex font-bold">
      <div class="w-20">Date</div>
      <div class="w-20">Asset</div>
      <div class="w-20 ml-4">Amount</div>
      <div class="w-20">Return</div>
    </div>
    <div class="flex flex-col">
      <div class="flex items-center">
        <div class="w-20">3/21/21</div>
        <div class="w-20">Bitcoin</div>
        <div class="w-20 ml-4">$140</div>
        <div class="w-20 text-green-500">+56.47%</div>
      </div>
      <div class="flex items-center">
        <div class="w-20">3/11/21</div>
        <div class="w-20">Ethereum</div>
        <div class="w-20 ml-4">$160</div>
        <div class="w-20 text-green-500">+42.34%</div>
      </div>
      <div class="flex items-center">
        <div class="w-20">3/11/21</div>
        <div class="w-20">Dogecoin</div>
        <div class="w-20 ml-4">$175</div>
        <div class="w-20 text-red-500">-22.94%</div>
      </div>
    </div>
    </div>

  </div>
</template>

<script>
import AreaChart from "@/components/AreaChart.vue";
import PieChart from "@/components/PieChart.vue";

export default {
  name: "App",
  components: {
    AreaChart,
    PieChart
  },
  computed: {
    portfolioValuation () {
      let value = 0
      this.coinData.forEach(element =>
        value = value + (element.quantity * element.market_data.current_price.usd)
      )
      return value.toFixed(2)
    },
    pieLabels () {
      return [this.coinData[0].symbol,this.coinData[1].symbol,this.coinData[2].symbol]
    },
    pieData () {
      return [
              (((this.coinData[0].quantity * this.coinData[0].market_data.current_price.usd)/this.portfolioValuation).toFixed(4)*100).toFixed(0),
              (((this.coinData[1].quantity * this.coinData[1].market_data.current_price.usd)/this.portfolioValuation).toFixed(4)*100).toFixed(0),
              (((this.coinData[2].quantity * this.coinData[2].market_data.current_price.usd)/this.portfolioValuation).toFixed(4)*100).toFixed(0)
            ]
    }
  },
  data() {
    return {
      dataFetched: false,
      user: {
        portfolio: {
          coins: [
            {
              id: 'bitcoin',
              quantity: 0.016
            },
            {
              id: 'ethereum',
              quantity: 0.156
            },
            {
              id: 'dogecoin',
              quantity: 330.27
            },            
          ]
        }
      },
      coinData: undefined
    }
  },
  created () {
      this.fetchData()
  },
  methods: {
      fetchData: async function() {
        let coinData = []
        this.user.portfolio.coins.forEach(element => 
          this.axios.get(`https://api.coingecko.com/api/v3/coins/${element.id}?localization=false&community_data=false&developer_data=false&sparkline=false`).then(res => {
          // console.log(res.data)
          let response = res.data
          response.quantity = element.quantity
          coinData.push(response)
          }).catch(err => {
          console.log(err.response);
          })
        )
        this.coinData = coinData
        this.dataFetched = true
      }
  }
};
</script>