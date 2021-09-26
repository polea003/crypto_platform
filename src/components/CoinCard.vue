<template>
        <div @click="$router.push({name:'Coin', params:{coin: coin, symbol: coinData.symbol}})" class="rounded border-2 w-40 h-24 text-black m-1 cursor-pointer" :class="{'bg-green-400 border-green-500': this.coinData.market_data.market_cap_change_percentage_24h >= 0 || this.coinData === undefined,
            'bg-red-400 border-red-500': this.coinData.market_data.market_cap_change_percentage_24h < 0}">
          <div class="flex flex-col p-2">
            <div class="flex items-center justify-between">
              <div class="text-xl font-bold capitalize truncate">{{coin}}</div>
              <div class="text-sm uppercase">{{this.coinData.symbol}}</div>
            </div>
            <div class="flex justify-between">
              <div>${{this.coinData.market_data.current_price.usd}}</div>
              <div>{{this.coinData.market_data.market_cap_change_percentage_24h.toFixed(2)}}%</div>
            </div>
                <div class="uppercase rounded-full bg-white px-4 mt-1 font-bold text-center bg-opacity-50 cursor-pointer">Buy</div>
          </div>
        </div>
</template>

<script>

export default {
    data () {
        return {
            coinData: undefined
        }
    },
    created () {
        this.fetchData()
    },
    props: {
        coin: {
            type: String,
            required: true
        }
    },
    methods: {
        fetchData: function() {
        this.axios.get(`https://api.coingecko.com/api/v3/coins/${this.coin}?localization=false&community_data=false&developer_data=false&sparkline=false`).then(res => {
            // console.log(res.data)
            this.coinData = res.data
            }).catch(err => {
            console.log(err.response);
            });
            setTimeout(function () { this.fetchData() }.bind(this), 3000)
        }
    }

}
</script>
