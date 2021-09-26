<template>
  <div class="about">
    <h1>This is an about page</h1>
    <AreaChart/>
  </div>
</template>

<script>
import AreaChart from "@/components/AreaChart.vue";

export default {
  name: "App",
  components: {
    AreaChart
  },
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