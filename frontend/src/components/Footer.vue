<template>
  <v-footer padless>
    <v-card class="flex primary" flat>
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