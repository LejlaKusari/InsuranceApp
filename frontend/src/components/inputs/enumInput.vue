<template>
    <div class="row form-group">
        <label class="col-sm-2 col-form-label">{{ field.name }} {{ field.isRequired ? '*' : null }}</label>
        <select class="form-control col-md-10" v-model="data.value">
          <option disabled value="">Please select one</option>
          <option v-for="option in field.options" :key="option.name">{{ option.name }}</option>
        </select>
    </div>
</template>

<script>
export default {
  name: "enumInput",
  props: {
    field: { required: true },
    data: { required: true }
  }
};
</script>