<template>
    <div class="row form-group" style="position: relative">
        <label class="col-sm-2 col-form-label">{{ field.name }} {{ field.isRequired ? '*' : null }}</label>
        <date-picker class="form-control col-md-10" type="text" :placeholder="field.placeholder" v-model="data.value"></date-picker>
    </div>
</template>

<script>
import datePicker from 'vue-bootstrap-datetimepicker';
import 'pc-bootstrap4-datetimepicker/build/css/bootstrap-datetimepicker.css';

export default {
  name: "dateInput",
  components: {
    datePicker
  },
  props: {
    field: { required: true },
    data: { required: true }
  },
  data () {
    return {
      date: new Date(),
      options: {
        format: 'L',
        useCurrent: false,
      }       
    }
  },
};
</script>