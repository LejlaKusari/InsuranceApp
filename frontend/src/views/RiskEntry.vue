<template>
    <div class="risk-entry">
        <RiskEntryForm v-bind:schema="formSchema" v-bind:data="formData" @change="getFormData" />
    </div>
</template>

<script>
import RiskEntryForm from "@/components/RiskEntryForm.vue";

export default {
  name: "RiskEntry",
  components: {
    RiskEntryForm
  },
  methods: {
    getFormSchema() {
      this.$store.dispatch('getFormSchema')
    },
    getFormData() {
      this.$store.dispatch('getFormData')
    }
  },
  computed: {
    formSchema() {
      return this.$store.getters.formSchema
    },
    formData() {
      return this.$store.getters.formData
    }
  },
  beforeMount() {
    this.$store.dispatch('getFormSchema', this.$route.params.id)
  },
};
</script>