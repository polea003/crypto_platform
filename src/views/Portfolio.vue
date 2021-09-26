<template>
  <div class="md:mx-4 mb-20">
    <div class="m-2">
    <div class="text-xl font-bold">Portfolio Performance</div>
    <div class="text-2xl font-bold">$789.45</div>
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
      <PieChart class="w-64"/>
    

      <div class="flex flex-col items-center ml-6">
        <div class="flex font-bold">
          <div class="w-20">%</div>
          <div class="w-28">Asset</div>
          <div class="w-20">Quantity</div>
          <div class="w-20">Value</div>
        </div>
        <div class="flex flex-col">
          <div class="flex items-center">
            <div class="w-20">45</div>
            <div class="w-28">Bitcoin</div>
            <div class="w-20">0.0034</div>
            <div class="w-20 text-green-500">$425.45</div>
          </div>
          <div class="flex items-center">
            <div class="w-20">35</div>
            <div class="w-28">Ethereum</div>
            <div class="w-20">0.54</div>
            <div class="w-20 text-green-500">$275.35</div>
          </div>
          <div class="flex items-center">
            <div class="w-20">20</div>
            <div class="w-28">Dogecoin</div>
            <div class="w-20">134.21</div>
            <div class="w-20 text-green-500">$134.57</div>
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
  data() {
    return {
      
    }
  }
};
</script>