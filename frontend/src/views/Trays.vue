<template>
  <div class="plants">
    <v-data-table
      show-select
      item-key="tray_type"
      v-model="selected"
      :headers="headers"
      :items="trays"
      :items-per-page="10"
      class="elevation-1"
    ></v-data-table>

    <v-col class="text-right">
      <v-btn
        @click="deleteButton()"
        color="red"
        rounded
        :disabled="!(selected.length > 0)"
        >Delete Selection</v-btn
      >
      <v-btn @click="addButton()" color="green" class="mx-2" rounded
        >Add Item</v-btn
      >
    </v-col>

    <v-dialog v-model="dialogDelete" max-width="500px">
      <v-card>
        <v-card-title class="headline"
          >Are you sure you want to delete these items?</v-card-title
        >
        <v-list-item>
          <v-list-item-content v-for="item in selected" :key="item">
            <v-list-item-title class="blueText">{{
              item.tray_type
            }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green" text @click="closeDelete">Cancel</v-btn>
          <v-btn color="red" text @click="confirmDelete">OK</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogAdd" max-width="500px">
      <v-card>
        <v-text-field
          v-model="form.tray_type"
          class="mx-10"
          label="Tray Type"
          :rules="rulesName"
          hide-details="auto"
        ></v-text-field
        ><v-text-field
          v-model="form.capacity"
          class="mx-10"
          label="Capacity"
          :rules="rulesCap"
          hide-details="auto"
        ></v-text-field>
        <v-text-field
          v-model="form.footprint"
          class="mx-10"
          label="Footprint"
          :rules="rulesCap"
          hide-details="auto"
        ></v-text-field>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="closeAdd">Cancel</v-btn>
          <v-btn
            color="green"
            text
            @click="confirmAdd"
            :disabled="!(form.tray_type && form.capacity && form.footprint)"
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
  name: "Trays",
  data() {
    return {
      api_data: null,
      form: { tray_type: "", capacity: 0, footprint: 0.0 },
      dialogDelete: false,
      dialogAdd: false,
      selected: [],
      rulesName: [
        (value) => !!value || "Required.",
        (value) => (value && value.length >= 3) || "Min 3 characters",
      ],
      rulesCap: [
        (value) => !!value || "Required.",
        (value) =>
          Number.isInteger(Number.parseInt(value)) || "Must be an integer",
      ],
      headers: [
        { text: "Tray Type", align: "start", value: "tray_type" },
        { text: "Footprint (m²)", value: "footprint" },
        { text: "Capacity", value: "capacity" },
      ],
      trays: [],
    };
  },
  methods: {
    addButton() {
      this.dialogAdd = true;
    },
    deleteButton() {
      this.dialogDelete = true;
    },
    closeAdd() {
      this.dialogAdd = false;
    },
    closeDelete() {
      this.dialogDelete = false;
    },
    confirmAdd() {
      this.closeAdd();
      let query = {
        tray_type: this.form.tray_type,
        capacity: this.form.capacity,
        footprint: this.form.footprint,
      };

      axios
        .post("http://localhost:8000/tray_types/add", query)
        .then((response) => {
          console.log(response);
          location.reload();
        });
    },
    confirmDelete() {},
  },
  mounted() {
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