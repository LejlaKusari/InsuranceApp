<template>
    <div class="container">
      <h1>{{ schema.name }}</h1>
      <p v-if="entrySubmitted" style="color: green">Entry successfully saved.</p>
      <form>
        <template v-for="field in schema">
          <component :is="field.type" :field="field" :data.sync="data[field.name]" :key="field.name"></component>
        </template>
      </form>
      <p v-if="entryErrors.length > 0" style="color: red">{{ entryErrors }}</p>
      <button class="btn btn-outline-primary btn-lg" @click="submitEntry">Submit</button>
    </div>
</template>

<script>
import textInput from "./inputs/textInput.vue";
import numberInput from "./inputs/numberInput.vue";
import dateInput from "./inputs/dateInput.vue";
import enumInput from "./inputs/enumInput.vue";

export default {
  components: {
    textInput: textInput,
    numberInput: numberInput,
    dateInput: dateInput,
    enumInput: enumInput,
  },
  methods: {
    submitEntry() {
      this.$store.dispatch("submitEntry", {
        risk_type: this.$route.params.id,
        entry_data: this.entryData
      })
    }
  },
  computed: {
    entryData() {
      return this.$store.getters.formData;
    },
    entryErrors() {
      return this.$store.getters.entryErrors;
    },
    entrySubmitted() {
      return this.$store.getters.entrySubmitted;
    }
  },
  props: {
    schema: { required: true },
    data: { required: true }
  },
  watch: {
    data: {
      handler(val){
        this.$store.dispatch("getFormData", val)
      },
      deep: true
    }
  }
} 
</script>