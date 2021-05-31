<template>
  <div class="plants">
    <v-data-table
      show-select
      item-key="family_name"
      v-model="selected"
      :headers="headers"
      :items="plants"
      :items-per-page="10"
      class="elevation-1"
    ></v-data-table
    ><v-col class="text-right">
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
            <v-list-item-title class="blueText"
              >{{ item.family_name }} - {{ item.name }}</v-list-item-title
            >
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
          v-model="form.family_name"
          class="mx-10"
          label="Family Name"
          :rules="rulesName"
          hide-details="auto"
        ></v-text-field
        ><v-text-field
          v-model="form.name"
          class="mx-10"
          label="Name"
          :rules="rulesName"
          hide-details="auto"
        ></v-text-field>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="closeAdd">Cancel</v-btn>
          <v-btn
            color="green"
            text
            @click="confirmAdd"
            :disabled="!(form.name && form.family_name)"
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
  name: "Plants",
  data() {
    return {
      api_data: null,
      form: { family_name: "", name: "" },
      dialogDelete: false,
      dialogAdd: false,
      selected: [],
      rulesName: [
        (value) => !!value || "Required.",
        (value) => (value && value.length >= 3) || "Min 3 characters",
      ],
      headers: [
        { text: "Family Name", align: "start", value: "family_name" },
        { text: "Name", value: "name" },
      ],
      plants: [],
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
        name: this.form.name,
        family_name: this.form.family_name,
      };

      axios.post("http://localhost:8000/plants/add", query).then((response) => {
        console.log(response);
        location.reload();
      });
    },
    confirmDelete() {
      this.closeDelete();
      let query = {
        plants: [],
      };

      this.selected.forEach((element) => {
        query.plants.push(element);
      });

      axios
        .post("http://localhost:8000/plants/delete", query)
        .then((response) => {
          console.log(response);
          location.reload();
        });
    },
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/plants/all")
      .then((response) => (this.plants = response.data));
  },
  components: {},
};
</script>


<style scoped>
.blueText {
  color: #bbdefb;
}
</style>