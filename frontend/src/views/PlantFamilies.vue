<template>
  <div class="locations">
    <v-data-table
      :headers="headers"
      :items="plant_families"
      :items-per-page="10"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PlantFamilies",
  data() {
    return {
      api_data: null,
      headers: [
        { text: "Family Name", align: "start", value: "family_name" },
       
       
      ],
      plant_families: [],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/plant_families/all")
      .then((response) => (this.plant_families = response.data));
  },
  components: {},
};
</script>