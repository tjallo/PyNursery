<template>
  <div class="locations">
    <v-data-table
      :headers="headers"
      :items="locations"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: "Locations",
  data() {
    return {
      api_data: null,
      headers: [
        { text: "Name", align: "start", value: "name" },
        { text: "Climate", value: "climate.climate_name" },
        { text: "Area (m²)", value: "area" },
        { text: "Climate Type", value: "climate.climate_type" },
      ],
      locations: [],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/locations/all")
      .then((response) => (this.locations = response.data));
  },
  components: {},
};
</script>