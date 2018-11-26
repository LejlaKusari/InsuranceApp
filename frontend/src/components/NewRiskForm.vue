<template>
    <div class="container">
        <h1>Add new risk model</h1>
        <p v-if="formSubmitted" style="color: green">New risk model successfully created</p>
        <p v-if="formErrors" style="color: red">{{ formErrors }}</p>
        <form style="margin-bottom: 30px">

            <div class="row form-group" style="margin-bottom: 30px">
              <label class="col-sm-2 col-form-label">Model Name</label>
              <input class="form-control col-md-10" :value="riskName" @input="getRiskName" placeholder="Your model name">
            </div>

            <p v-for="error in fieldErrors" :key="error" style="color: red"> {{ error }} </p>
            
            <div class="row form-group">
              <label class="col-sm-2 col-form-label">Field name</label>
              <input class="form-control col-md-10" :value="fieldName" @input="getFieldName" placeholder="Your field name">
            </div>
            <div class="row form-group">
              <label class="col-sm-2 col-form-label">Field type</label>
              <select class="form-control col-md-10" :value="fieldType" @input="getFieldType">
                  <option disabled value="">Please select one</option>
                  <option value="text">Text</option>
                  <option value="number">Number</option>
                  <option value="date">Date</option>
                  <option value="enum">Enum</option>
              </select>
            </div>
            <div class="row form-group" v-if="fieldType === 'enum'">
              <label class="col-sm-2 col-form-label">Option</label>
              <input class="form-control col-md-8" :value="fieldOption" @input="getFieldOption" placeholder="Enter an option">
              <button class="form-control col-md-2" @click="addNewOption">Add option</button>
            </div>
            <div>
              <p v-if="fieldOptions.length">Currently added options: 
                <strong>{{ fieldOptions.map(option => option.name).join(", ") }}</strong>
              </p>
            </div>
            <div class="row form-group">
              <label class="col-sm-2 col-form-label">Required?</label>
              <input class="form-control-sm checkbox" :checked="fieldIsRequired" @input="getFieldIsRequired" type="checkbox">  
            </div>

            <button class="btn btn-outline-primary" @click="addNewField">Add field</button>
            
        </form>

        <table class="table">
          <tr>
            <th>Field name</th>
            <th>Field type</th> 
            <th>Required?</th>
            <th>Options</th>
          </tr>
          <tr v-for="field in fields" :key="field.index">
            <td>{{ field.name }}</td>
            <td>{{ field.field_type }}</td>
            <td>{{ field.is_required }}</td>
            <td v-if="field.options">{{ field.options.map(option => option.name).join(", ") }}</td>
            <td v-if="!field.options"></td>
          </tr>
        </table>

        <button class="btn btn-primary" @click="submitNewRisk">Create risk model</button>
    </div>
</template>

<style>
  label {
    text-align: right;
  }
  .checkbox {
    width: 25px;
  }
</style>


<script>
export default {
  methods: {
    getRiskName(e) {
      this.$store.dispatch("getRiskName", e.target.value);
    },
    submitNewRisk() {
      this.$store.dispatch("submitForm", {
        name: this.riskName,
        fields: this.fields
      });
    },
    getFieldName(e) {
      this.$store.dispatch("getFieldName", e.target.value);
    },
    getFieldType(e) {
      this.$store.dispatch("getFieldType", e.target.value);
    },
    getFieldIsRequired(e) {
      this.$store.dispatch("getFieldIsRequired", e.target.checked);
    },
    getFieldOption(e) {
      this.$store.dispatch("getFieldOption", e.target.value);
    },
    addNewField(e) {
      this.$store.dispatch("addNewField", e.preventDefault());
      this.$store.dispatch("removeField");
    },
    addNewOption(e) {
      this.$store.dispatch("addNewOption", e.preventDefault());
      this.$store.dispatch("removeOption");
    }
  },
  computed: {
    riskName() {
      return this.$store.getters.riskName;
    },
    fields() {
      return this.$store.getters.fields;
    },
    fieldErrors() {
      return this.$store.getters.fieldErrors;
    },
    fieldName() {
      return this.$store.getters.fieldName;
    },
    fieldType() {
      return this.$store.getters.fieldType;
    },
    fieldIsRequired() {
      return this.$store.getters.fieldIsRequired;
    },
    fieldOption() {
      return this.$store.getters.fieldOption;
    },
    fieldOptions() {
      return this.$store.getters.fieldOptions;
    },
    formSubmitted() {
      return this.$store.getters.formSubmitted;
    },
    formErrors() {
      return this.$store.getters.formErrors;
    }
  }
};
</script>