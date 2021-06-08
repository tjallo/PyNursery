<template>
  <v-container>
    <h1>Company Portfolio:</h1>
    <v-row v-for="n in stats" :key="n" no-gutters>
      <v-card color="accent" outlined class="text pa-2 ma-3">
        {{ n.name }}: {{ n.count }}
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      stats: [],
    };
  },
  components: {},
  mounted() {
    let names = [
      "plant_batches",
      "locations",
      "plant_families",
      "plants",
      "tray_types",
    ];

    for (const name of names) {
      axios.get(`http://localhost:8000/statistics/${name}`).then((response) => {
        console.log(response);
        this.stats.push(response.data);
      });
    }
  },
};
</script>

<style >
.text {
  color: blue;
}
</style>
