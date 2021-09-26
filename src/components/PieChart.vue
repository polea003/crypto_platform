<script>
import { Pie } from "vue-chartjs";

export default {
  extends: Pie,
  mounted () {

    this.renderChart(
      {
        labels: this.labels,
        datasets: [
          {
            backgroundColor: ["#df9816", "#42b983", "#00D8FF"],
            data: this.data
          }
        ]
      },
      { responsive: true, maintainAspectRatio: false }
    );
  },
  props: {
      labels: {
          type: Array,
          required: true
      },
      data: {
          type: Array,
          required: true
      }
  },
  computed: {
    portfolioValuation () {
      let value = 0
      this.coinData.forEach(element =>
        value = value + (element.quantity * element.market_data.current_price.usd)
      )
      return value.toFixed(2)
    }
  }
}
</script>