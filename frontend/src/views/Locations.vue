<template>
  <div class="locations">
    <v-data-table
      v-model="selected"
      :headers="headers"
      :items="locations"
      item-key="name"
      show-select
      class="elevation-1"
    >
    </v-data-table>

    <v-col class="text-right">
      <v-btn @click="deleteItem()" color="red" rounded>Delete Selection</v-btn>
      <v-btn @click="addItem()" color="green" class="mx-2" rounded
        >Add Item</v-btn
      >
    </v-col>

    <v-dialog v-model="dialogDelete" max-width="500px">
      <v-card>
        <v-card-title class="headline"
          >Are you sure you want to delete these items?</v-card-title
        >
        <v-card-text v-for="item in selected" :key="item">{{
          item.name
        }}</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green" text @click="closeDelete">Cancel</v-btn>
          <v-btn color="red" text @click="deleteItemConfirm">OK</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogAdd" max-width="500px">
      <v-card>
        <v-text-field
          class="mx-10"
          label="Name"
          :rules="rulesName"
          hide-details="auto"
        ></v-text-field>
        <v-text-field
          class="mx-10"
          label="Area"
          :rules="rulesArea"
          hide-details="auto"
        ></v-text-field>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="closeAdd">Cancel</v-btn>
          <v-btn color="green" text @click="addConfirm">Add</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
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
        { text: "Area (m²)", value: "area" },
        { text: "Climate", value: "climate.climate_name" },
        { text: "Climate Type", value: "climate.climate_type" },
      ],
      locations: [],
      dialogDelete: false,
      dialogAdd: true,
      selected: [],
      sure: false,
      rulesName: [
        (value) => !!value || "Required.",
        (value) => (value && value.length >= 3) || "Min 3 characters",
      ],
      rulesArea: [
        (value) => !!value || "Required.",
        (value) => (value && Number.isInteger(value)) || "Must be an integer",
      ],
    };
  },
  methods: {
    addItem() {},
    deleteItem() {
      if (this.selected.length > 0) {
        this.dialogDelete = true;
      }
    },
    closeDelete() {
      this.dialogDelete = false;
    },
    deleteItemConfirm() {
      this.closeDelete();
      console.log("Deleting : " + this.selected);
    },
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/locations/all")
      .then((response) => (this.locations = response.data));
  },
  components: {},
};
</script>