<template>
  <div class="locations">
    <v-data-table
      show-select
      item-key="family_name"
      v-model="selected"
      :headers="headers"
      :items="plant_families"
      :items-per-page="10"
      class="elevation-1"
    ></v-data-table>

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
        <v-list-item>
          <v-list-item-content v-for="item in selected" :key="item">
            <v-list-item-title class="blueText">{{
              item.family_name
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
          label="Family Name"
          :rules="rulesName"
          hide-details="auto"
        ></v-text-field>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="closeAdd">Cancel</v-btn>
          <v-btn color="green" text @click="addConfirm" :disabled="!form.name"
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
  name: "PlantFamilies",
  data() {
    return {
      api_data: null,
      form: { name: "" },
      dialogDelete: false,
      dialogAdd: false,
      selected: [],
      rulesName: [
        (value) => !!value || "Required.",
        (value) => (value && value.length >= 3) || "Min 3 characters",
      ],
      headers: [{ text: "Family Name", align: "start", value: "family_name" }],
      plant_families: [],
    };
  },
  methods: {
    closeDelete() {
      this.dialogDelete = false;
    },
    deleteItemConfirm() {
      this.closeDelete();
      this.deleteItemsPost(this.selected);
    },
    addConfirm() {
      this.addItemPost(this.form.name);
    },
    deleteItemsPost(selected_items) {
      let query = {
        family_names: [],
      };

      selected_items.forEach((element) => {
        query.family_names.push(element);
      });

      axios
        .post("http://localhost:8000/plant_families/delete", query)
        .then((response) => {
          console.log(response);
          location.reload();
        });
    },
    addItemPost(family_name) {
      axios
        .post("http://localhost:8000/plant_families/add", {
          family_name: family_name,
        })
        .then((response) => {
          console.log(response);
          location.reload();
        });
    },
    deleteAll() {},
    addItem() {
      this.dialogAdd = true;
    },
    deleteItem() {
      this.dialogDelete = true;
    },
    closeAdd() {
      this.dialogAdd = false;
    },
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/plant_families/all")
      .then((response) => (this.plant_families = response.data));
  },
  components: {},
};
</script>


<style scoped>
.blueText {
  color: #bbdefb;
}
</style>