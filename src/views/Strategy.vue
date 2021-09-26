<template>
  <div class="md:mx-4 mb-20">
    <div class="m-2 text-xl font-bold mb-4">Investment Strategy</div>

      <div class="flex flex-col ml-2">
        <div class="font-bold">Scheduled Orders</div>
        <div class="flex items-center border-t border-gray-300">
          <div class="flex flex-col w-13/16 py-2">
            <div class="font-bold">Dollar Cost Averaging</div>
            <div>Buy assets at regularly scheduled intervals, mitigating the risk of volatility.</div>
          </div>
          <div class="text-2xl font-bold flex-grow text-right mr-4">></div>
        </div>
        <div class="flex items-center border-t border-gray-300">
          <div class="flex flex-col w-13/16 py-2">
            <div class="font-bold">Incremental Reduction</div>
            <div>Sell assets at regularly scheduled intervals, mitigating the opportunity cost of liquidating an asset all at once.</div>
          </div>
          <div class="text-2xl font-bold flex-grow text-right mr-4">></div>
        </div>

        <div class="font-bold mt-6">Conditional Orders</div>
        <div class="flex items-center border-t border-gray-300">
          <div class="flex flex-col w-13/16 py-2">
            <div class="font-bold">Buy Limit Order</div>
            <div>Buy assets if price falls to a set amount</div>
          </div>
          <div class="text-2xl font-bold flex-grow text-right mr-4">></div>
        </div>
        <div class="flex items-center border-t border-gray-300">
          <div class="flex flex-col w-13/16 py-2">
            <div class="font-bold">Buy Stop Order</div>
            <div>Buy assets if price rises to a set amount</div>
          </div>
          <div class="text-2xl font-bold flex-grow text-right mr-4">></div>
        </div>
        <div class="flex items-center border-t border-gray-300">
          <div class="flex flex-col w-13/16 py-2">
            <div class="font-bold">Sell Limit Order</div>
            <div>Sell assets if price rises to a set amount</div>
          </div>
          <div class="text-2xl font-bold flex-grow text-right mr-4">></div>
        </div>
        <div class="flex items-center border-t border-gray-300">
          <div class="flex flex-col w-13/16 py-2">
            <div class="font-bold">Sell Stop Order</div>
            <div>Sell assets if price falls to a set amount</div>
          </div>
          <div class="text-2xl font-bold flex-grow text-right mr-4">></div>
        </div>
      


      <div class="font-bold mt-6">Crypto Literacy</div>
        <div class="flex items-center border-t border-gray-300">
          <div class="flex flex-col w-13/16 py-2">
            <div class="font-bold">Bitcoin White Paper</div>
            <div>The 2008 academic paper that revolutionalized financial freedom</div>
          </div>
          <div class="text-2xl font-bold flex-grow text-right mr-4">></div>
        </div>
        <div class="flex items-center border-t border-gray-300">
          <div class="flex flex-col w-13/16 py-2">
            <div class="font-bold">How Blockchain Works</div>
            <div>The algorithm that powers cryptocurrency</div>
          </div>
          <div class="text-2xl font-bold flex-grow text-right mr-4">></div>
        </div>

      </div>


  </div>
</template>

<script>

export default {
  name: "App",
  data() {
    return {
      chartData: {
        Books: 24,
        Magazine: 30,
        Newspapers: 10
      }
    };
  }
};
</script>