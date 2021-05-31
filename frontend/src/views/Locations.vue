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
      <v-btn
        @click="deleteItem()"
        color="red"
        rounded
        :disabled="!(selected.length > 0)"
        >Delete Selection</v-btn
      >
      <v-btn @click="addItem()" color="green" class="mx-2" rounded
        >Add Item</v-btn
      >
    </v-col>

    <v-dialog v-model="dialogDelete" max-width="500px">
      <v-card>
        <v-card-title class="headline"
          >Are you sure you want to delete these items?</v-card-title
        >
        <!-- <v-card-text v-for="item in selected" :key="item">{{
          item.name
        }}</v-card-text> -->
        <v-list-item>
          <v-list-item-content v-for="item in selected" :key="item">
            <v-list-item-title class="blueText">{{
              item.name
            }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
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
          v-model="form.name"
          class="mx-10"
          label="Name"
          :rules="rulesName"
          hide-details="auto"
        ></v-text-field>
        <v-text-field
          v-model="form.area"
          class="mx-10"
          label="Area"
          :rules="rulesArea"
          hide-details="auto"
        ></v-text-field>
        <v-select
          :items="['Field - 0', 'Hoophouse - 1', 'Greenhouse - 2']"
          v-model="form.climate_type"
          class="mx-10"
          label="Climate"
          hide-details="auto"
        ></v-select>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="closeAdd">Cancel</v-btn>
          <v-btn
            color="green"
            text
            @click="addConfirm"
            :disabled="!(form.name && form.area)"
            >Add</v-btn
          >
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
      dialogAdd: false,
      selected: [],
      sure: false,
      form: { name: "", area: 0, climate_type: 0 },
      rulesName: [
        (value) => !!value || "Required.",
        (value) => (value && value.length >= 3) || "Min 3 characters",
      ],
      rulesArea: [
        (value) => !!value || "Required.",
        (value) =>
          Number.isInteger(Number.parseInt(value)) || "Must be an integer",
      ],
    };
  },
  methods: {
    addItem() {
      this.dialogAdd = true;
    },
    deleteItem() {
      if (this.selected.length > 0) {
        this.dialogDelete = true;
      }
    },
    closeDelete() {
      this.dialogDelete = false;
    },
    closeAdd() {
      this.dialogAdd = false;
    },
    deleteItemConfirm() {
      this.deleteLocations(this.selected);
      this.closeDelete();
    },
    addConfirm() {
      console.log("Confirmed");
      this.addLocation(this.form);
      this.closeAdd();
    },
    addLocation(form) {
      let parsed_climate = form.climate_type.split("-")
      parsed_climate = parsed_climate[parsed_climate.length - 1].trim()
      let data = {
        name: form.name,
        area: Number.parseFloat(form.area),
        climate_type: Number.parseInt(parsed_climate),
      };
      axios
        .post("http://localhost:8000/locations/add", data)
        .then((response) => {
          console.log(response);
          location.reload();
        });
    },
    deleteLocations(input_data) {
      let query = {
        locations: [],
        // input_data: input_data
      };

      for (let item in input_data) {
        let data = input_data[item];
        data = {
          name: data.name,
          area: data.area,
          climate_type: data.climate.climate_type,
        };
        query.locations.push(data);
      }

      axios
        .post("http://localhost:8000/locations/delete", query)
        .then((response) => {
          console.log(response);
          location.reload();
        });
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

<style scoped>
.blueText {
  color: #bbdefb;
}
</style>