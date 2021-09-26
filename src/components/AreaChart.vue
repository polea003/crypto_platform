<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  data() {
    return {
      gradient: null,
      gradient2: null
    };
  },
  mounted() {
    this.gradient = this.$refs.canvas
      .getContext("2d")
      .createLinearGradient(0, 0, 0, 450);
    this.gradient2 = this.$refs.canvas
      .getContext("2d")
      .createLinearGradient(0, 0, 0, 450);

    this.gradient.addColorStop(0, "rgba(66, 185, 131, 0.5)");
    this.gradient.addColorStop(0.5, "rgba(66, 185, 131, 0.25)");
    this.gradient.addColorStop(1, "rgba(66, 185, 131, 0)");

    // this.gradient2.addColorStop(0, "rgba(66, 185, 131, 0.9)");
    // this.gradient2.addColorStop(0.5, "rgba(66, 185, 131, 0.25)");
    // this.gradient2.addColorStop(1, "rgba(66, 185, 131, 0)");

    this.renderChart(
      {
        labels: [
          "1/21",
          "2/21",
          "3/21",
          "4/21",
          "5/21",
          "6/21",
          "7/21"
        ],
        datasets: [
          {
            label: "Portfolio Value",
            borderColor: "#42b983",
            pointBackgroundColor: "white",
            borderWidth: 1,
            pointBorderColor: "white",
            backgroundColor: this.gradient,
            data: [40, 39, 10, 40, 39, 80, 60]
          }
          // {
          //   label: "Data Two",
          //   borderColor: "#42b983",
          //   pointBackgroundColor: "white",
          //   pointBorderColor: "white",
          //   borderWidth: 1,
          //   backgroundColor: this.gradient2,
          //   data: [60, 55, 32, 10, 2, 12, 53]
          // }
        ]
      },
      { responsive: true, maintainAspectRatio: false }
    );
  }
};
</script>
