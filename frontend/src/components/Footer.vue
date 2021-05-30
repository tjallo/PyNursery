<template>
  <v-footer dark padless app>
    <v-card class="flex" flat tile>
      <v-card-title class="teal">
        <strong class="subheading"
          >Get connected with us on social networks!</strong
        >

        <v-spacer></v-spacer>

        <v-btn v-for="icon in icons" :key="icon" class="mx-4" :href="icon[1]" dark icon> 
          <v-icon size="24px">
            {{ icon[0] }}
          </v-icon>
        </v-btn>
      </v-card-title>

      <v-card-text class="py-2 white--text text-center">
        {{ new Date().getFullYear() }} — <strong>Tjalle Wolterink</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  name: "Footer",
  data: () => ({
    icons: [["mdi-linkedin", "https://www.linkedin.com/in/tjallewolterink/"]],
  }),
};
</script>