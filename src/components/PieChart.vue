<script>
import { Pie } from "vue-chartjs";

export default {
  extends: Pie,
  mounted() {
    // this.gradient = this.$refs.canvas
    //   .getContext("2d")
    //   .createLinearGradient(0, 0, 0, 450);
    // this.gradient2 = this.$refs.canvas
    //   .getContext("2d")
    //   .createLinearGradient(0, 0, 0, 450);

    // this.gradient.addColorStop(0, "rgba(223, 152, 22, 0.5)");
    // this.gradient.addColorStop(0.5, "rgba(223, 152, 22, 0.25)");
    // this.gradient.addColorStop(1, "rgba(223, 152, 22, 0)");

    // this.gradient2.addColorStop(0, "rgba(66, 185, 131, 0.9)");
    // this.gradient2.addColorStop(0.5, "rgba(66, 185, 131, 0.25)");
    // this.gradient2.addColorStop(1, "rgba(66, 185, 131, 0)");
    this.renderChart(
      {
        labels: ["BTC", "ETH", "DOGE"],
        datasets: [
          {
            backgroundColor: ["#df9816", "#42b983", "#00D8FF"],
            data: [40, 20, 10]
          }
        ]
      },
      { responsive: true, maintainAspectRatio: false }
    );
  }
};
</script>