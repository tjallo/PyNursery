<template>
  <v-navigation-drawer flat app expand-on-hover clipped class="secondary"> 
    <v-divider></v-divider>

    <v-list nav dense v-for="item in items" :key="item">
      <v-list-item link :href="item[2]">
        <v-list-item-icon>
          <v-icon>{{ item[1] }}</v-icon>
        </v-list-item-icon>
        <v-list-item-title>{{ item[0] }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>


<script>
export default {
  name: "Navigation",
  data: () => ({
    items: [
      ["Home", "mdi-home", "/"],
      ["Plant Batches", "mdi-person", "/plant_batch"],
      ["Locations", "mdi-barn", "/locations"],
      ["Plant Families", "mdi-nature-people", "/plant_families"],
      ["Plants", "mdi-sprout-outline", "/plants"],
      ["Trays", "mdi-tray-full", "/trays"],
    ],
  }),
};
</script>