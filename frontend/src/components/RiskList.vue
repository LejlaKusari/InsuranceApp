<template>
  <div class="container">
    <ul class="list-group"> 
      <li class="list-group-item list-group-item-action list-group-item-light" v-for="risk in risks" :key="risk">
        <router-link :to="`new-risk-entry/${risk.pk}`" style="float: left">{{ risk.name }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  methods: {
    getRisks() {
      this.$store.dispatch("getRisks");
    }
  },
  computed: {
    risks() {
      return this.$store.getters.risks;
    }
  },
  beforeMount() {
    this.$store.dispatch('getRisks');
  },

}
</script>
