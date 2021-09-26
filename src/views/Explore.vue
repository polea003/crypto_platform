<template>
  <div class="md:mx-4 mb-20">
    <div class="m-2 text-xl font-bold mb-4">Explore Investments</div>

    <div class="ml-2 font-bold md:text-center">Watch List</div>

    <div class="flex flex-col items-center">

      <div class="flex flex-grow flex-wrap px-4">

        <CoinCard :coin="'bitcoin'"  />
        <CoinCard :coin="'ethereum'"  />
        <CoinCard :coin="'dogecoin'"  />
        <CoinCard :coin="'litecoin'"  />

      </div>
    </div>

    <div class="flex items-end md:justify-center">
      <div class="ml-2 mt-4 pb-1 font-bold">Trending Coins</div>
      <div class="text-sm font-bold p-1 ml-4 cursor-pointer">View All</div>
    </div>
    
    <div class="flex flex-col items-center">

      <div class="flex flex-grow flex-wrap px-4">

        <CoinCard v-for="coin in trendingCoins.coins" :coin="coin.item.id" :key="coin.item.id"/>

      </div>
    </div>

    <div class="flex items-end md:justify-center">
      <div class="ml-2 mt-4 pb-1 font-bold">Largest Market Cap</div>
      <div class="text-sm font-bold p-1 ml-4 cursor-pointer">View All</div>
    </div>
    
    <div class="flex flex-col items-center">

      <div class="flex flex-grow flex-wrap px-4">

        <CoinCard :coin="'bitcoin'"  />
        <CoinCard :coin="'ethereum'"  />
        <CoinCard :coin="'cardano'"  />
        <CoinCard :coin="'tether'"  />

      </div>
    </div>



  </div>
</template>

<script>
import CoinCard from "@/components/CoinCard.vue";

export default {
    data () {
        return {
          trendingCoins: undefined
        }
    },
    created () {
        this.fetchTrendingCoins()
    },
    components: {
      CoinCard
    },    
    props: {

    },
    methods: {
        fetchTrendingCoins: async function() {
        this.axios.get('https://api.coingecko.com/api/v3/search/trending').then(res => {
            // console.log(res.data)
            this.trendingCoins = res.data
            }).catch(err => {
            console.log(err.response);
            });
        }
    }

}
</script>