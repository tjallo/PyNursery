<template>
  <div class="plants">
    <v-data-table
      :headers="headers"
      :items="plants"
      :items-per-page="10"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Plants",
  data() {
    return {
      api_data: null,
      headers: [
        { text: "Family Name", align: "start", value: "family_name" },
        { text: "Name", value: "name" },
      ],
      plants: [],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/plants/all")
      .then((response) => (this.plants = response.data));
  },
  components: {},
};
</script>