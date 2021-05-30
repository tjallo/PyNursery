<template>
  <div class="plants">
    <v-data-table
      :headers="headers"
      :items="trays"
      :items-per-page="10"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Trays",
  data() {
    return {
      api_data: null,
      headers: [
        { text: "Tray Type", align: "start", value: "tray_type" },
        { text: "Footprint (m²)", value: "footprint" },
        { text: "Capacity", value: "capacity" },
      ],
      trays: [],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/tray_types/all")
      .then((response) => (this.trays = response.data));
  },
  components: {},
};
</script>