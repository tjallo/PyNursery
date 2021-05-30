<template>
  <!-- App.vue -->

  <v-app>
    <Navigation />
    <Appbar />

    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>

    <Footer />
  </v-app>
</template>

<script>
import Footer from "@/components/Footer.vue";
import Navigation from "@/components/Navigation.vue";
import Appbar from "@/components/Appbar.vue";
export default {
  name: "App",
  components: {
    Footer,
    Appbar,
    Navigation,
  },
  data: () => ({
    //
  }),
};
</script>
