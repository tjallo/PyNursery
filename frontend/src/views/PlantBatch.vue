<template>
  <div class="locations">
    <v-data-table
      v-model="selected"
      :headers="headers"
      :items="batches"
      item-key="planting_time"
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
            <v-list-item-title class="blueText"
              >{{ item.plant.family_name }} {{ item.plant.name }} -
              {{ item.n_tray }} x {{ item.tray_type.tray_type }} -
              {{ item.location.name }} -
              {{ item.planting_time }}</v-list-item-title
            >
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
          v-model="form.family_name"
          class="mx-10"
          label="Family Name"
          :rules="rulesName"
          hide-details="auto"
        ></v-text-field>
        <v-text-field
          v-model="form.name"
          class="mx-10"
          label="Name"
          :rules="rulesName"
          hide-details="auto"
        ></v-text-field>
        <v-text-field
          v-model="form.n_trays"
          class="mx-10"
          label="Number of Trays"
          :rules="rulesArea"
          hide-details="auto"
        ></v-text-field>
        <v-select
          :items="trays.map((t) => t.tray_type)"
          v-model="form.tray_type"
          class="mx-10"
          label="Tray Type"
          hide-details="auto"
        ></v-select>
        <v-select
          :items="locations.map((t) => t.name)"
          v-model="form.location"
          class="mx-10"
          label="Locations"
          hide-details="auto"
        ></v-select>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="closeAdd">Cancel</v-btn>
          <v-btn
            color="green"
            text
            @click="addConfirm"
            :disabled="
              !(
                form.family_name &&
                form.name &&
                form.n_trays &&
                form.tray_type &&
                form.location
              )
            "
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
      batches: [],
      locations: [],
      trays: [],
      headers: [
        { text: "Plant Family", align: "start", value: "plant.family_name" },
        { text: "Plant", value: "plant.name" },
        { text: "Location", value: "location.name" },
        { text: "Tray", value: "tray_type.tray_type" },
        { text: "Number of Trays", value: "n_tray" },
        { text: "Number of plants/tray", value: "tray_type.capacity" },
        { text: "Planting Time", value: "planting_time" },
      ],
      dialogDelete: false,
      dialogAdd: false,
      selected: [],
      sure: false,
      form: {
        family_name: "",
        name: "",
        n_trays: 0,
        tray_type: "",
        location: "",
      },
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
      this.closeDelete();
      this.deleteBatch();
    },
    addConfirm() {
      this.closeAdd();
      this.addBatch(this.form);
    },
    addBatch(form) {
      let loc, pl, tr;

      this.locations.forEach((l) => {
        if (l.name == form.location) {
          loc = l;
        }
      });

      this.trays.forEach((t) => {
        if (t.tray_type == form.tray_type) {
          tr = t;
        }
      });

      pl = {
        family_name: form.family_name,
        metadata: {},
        name: form.name,
      };

      let query = {
        plant: pl,
        location: loc,
        tray_type: tr,
        n_trays: form.n_trays,
        planting_time: new Date(Date.now()).toISOString(),
      };

      axios
        .post("http://localhost:8000/plant_batch/add", query)
        .then((response) => {
          console.log(response);
          location.reload();
        });
    },
    deleteBatch() {
      const query = {
        plant_batches: [],
      };
      console.log(query);
      for (const i of this.selected) {
        console.log(i);

        let body = {
          plant: i.plant,
          location: i.location,
          tray_type: i.tray_type,
          n_trays: i.n_tray,
          planting_time: i.planting_time,
        };

        query.plant_batches.push(body);
      }

      axios
        .post("http://127.0.0.1:8000/plant_batch/delete", query)
        .then((response) => {
          console.log(response);
          location.reload();
        });
    },
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/plant_batch/all")
      .then((response) => (this.batches = response.data));

    axios
      .get("http://127.0.0.1:8000/locations/all")
      .then((response) => (this.locations = response.data));

    axios
      .get("http://127.0.0.1:8000/tray_types/all")
      .then((response) => (this.trays = response.data));
  },
  components: {},
};
</script>

<style scoped>
.blueText {
  color: #bbdefb;
}
</style>