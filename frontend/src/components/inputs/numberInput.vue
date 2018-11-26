<template>
    <div class="row form-group">
        <label class="col-sm-2 col-form-label">{{ field.label }} {{ field.isRequired ? '*' : null }}</label>
        <input class="form-control col-md-10" type="number" :placeholder="field.placeholder" v-model="data.value">
    </div>
</template>

<script>
export default {
  name: "numberInput",
  props: {
    field: { required: true },
    data: { required: true }
  }
};
</script>