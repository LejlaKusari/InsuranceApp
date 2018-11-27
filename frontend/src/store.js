import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";


Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    riskName: "",
    fields: [],
    fieldName: "",
    fieldType: "",
    fieldIsRequired: true,
    fieldOptions: [],
    fieldOption: "",
    fieldErrors: [],
    formErrors: "",
    entryErrors: "",
    formSubmitted: false,
    entrySubmitted: false,
    formSchema: {},
    formData: {},
    risks: [],
    previous: "",
    next: "",
  },
  mutations: {
    GET_RISK_NAME(state, value) {
      state.riskName = value;
    },
    GET_FIELD_NAME(state, value) {
      state.fieldName = value;
    },
    GET_FIELD_TYPE(state, value) {
      state.fieldType = value;
    },
    GET_FIELD_IS_REQUIRED(state, value) {
      state.fieldIsRequired = value;
    },
    GET_FIELD_OPTION(state, value) {
      state.fieldOption = value;
    },
    ADD_NEW_FIELD(state) {
      let field = {
        name: state.fieldName,
        field_type: state.fieldType,
        is_required: state.fieldIsRequired,
      }
      if (state.fieldOptions.length > 0) field.options = state.fieldOptions

      state.fieldErrors = [];
      state.fields.push(field);
    },
    ADD_FIELD_ERROR(state, errorMessage) {
      state.fieldErrors.push(errorMessage);
    },
    REMOVE_FIELD_DATA(state) {
      state.fieldName = "";
      state.fieldType = "";
      state.fieldIsRequired = true;
      state.fieldOptions = [];
    },
    ADD_NEW_OPTION(state) {
      if (state.fieldOption.length > 0) {
        state.fieldOptions.push({ name: state.fieldOption })
      }
    },
    REMOVE_OPTION(state) {
      state.fieldOption = "";
    },
    ADD_FORM_ERROR(state, value) {
      state.formErrors = value;
    },
    SUBMIT_FORM(state, value) {
      state.formSubmitted = value;
    },
    GET_FORM_SCHEMA(state, obj) {
      state.formSchema = obj
    },
    GET_FORM_DATA(state, obj) {
      state.formData = obj
    },
    GET_RISKS(state, value) {
      state.risks = value;
    },
    ADD_ENTRY_ERROR(state, errorMessage) {
      state.entryErrors = errorMessage;
    },
    SUBMIT_ENTRY(state, value) {
      state.entrySubmitted = value;
    }
  },
  actions: {
    getRiskName({ commit }, value) {
      commit("GET_RISK_NAME", value);
    },
    getFieldName({ commit }, value) {
      commit("GET_FIELD_NAME", value);
    },
    getFieldType({ commit }, value) {
      commit("GET_FIELD_TYPE", value);
    },
    getFieldIsRequired({ commit }, value) {
      commit("GET_FIELD_IS_REQUIRED", value);
    },
    getFieldOption({ commit }, value) {
      commit("GET_FIELD_OPTION", value);
    },
    addNewField({ commit, state, dispatch }) {
      if (
        state.fieldName.length > 0 && state.fieldType.length > 0 &&
        !state.fields.map(field => field.name).includes(state.fieldName)
      ) {
        commit("ADD_NEW_FIELD");
        dispatch("removeFieldData");
      } else if (state.fields.map(field => field.name).includes(state.fieldName)) {
        dispatch("addFieldError", "A field with this name already exists.")
      } else {
        dispatch("addFieldError", "The field is incomplete, please check if all necessary data is filled.")
      }
    },
    removeFieldData({ commit }) {
      commit("REMOVE_FIELD_DATA");
    },
    addFieldError({commit, state}, errorMessage) {
      if (!state.fieldErrors.includes(errorMessage)) commit("ADD_FIELD_ERROR", errorMessage);
    },
    addNewOption({ commit }) {
      commit("ADD_NEW_OPTION");
    },
    removeOption({ commit }) {
      commit("REMOVE_OPTION");
    },
    submitForm({ commit, state }, obj) {
      if (!state.riskName) {
        commit("ADD_FORM_ERROR", "Please fill out the model name.");
        return
      } else {
        commit("ADD_FORM_ERROR", "");
      }
      axios
        .post("https://4jsq8d101c.execute-api.us-east-2.amazonaws.com/prod/risks/create/", obj)
        .then(function(response) {
          // eslint-disable-next-line
          console.log(response);
          commit("SUBMIT_FORM", true);
        })
        .catch(function(error) {
          // eslint-disable-next-line
          console.log(error);
          commit("SUBMIT_FORM", false);
        });
    },
    getFormSchema({commit}, id) {
      axios
        .get(`https://4jsq8d101c.execute-api.us-east-2.amazonaws.com/prod/risks/${id}/`)
        .then(function(response) {
          commit("GET_FORM_SCHEMA", 
            response.data.fields.map(field =>
              (
                {
                  type: `${field.field_type}Input`,
                  name: field.name,
                  label: field.name,
                  placeholder: `Enter ${field.name}`,
                  options: field.options,
                  isRequired: field.is_required
                }
              )
            )
          )
          commit("GET_FORM_DATA",
            response.data.fields.reduce(
              (obj, key) => ({ ...obj, [key.name]: { value: '' }}), {}
            )
          )
        })
        .catch(function(error) {
          // eslint-disable-next-line
          console.log(error)
        })
    },
    getFormData({commit}, obj) {
      commit("GET_FORM_DATA", obj)
    },
    getRisks({commit}) {
      axios
        .get('https://4jsq8d101c.execute-api.us-east-2.amazonaws.com/prod/risks/list/')
        .then(function(response) {
          commit("GET_RISKS", response.data.results)
        })
        .catch(function(error) {
          // eslint-disable-next-line
          console.log(error)
        })
    },
    submitEntry({commit, state}, obj) {
      axios
        .post("https://4jsq8d101c.execute-api.us-east-2.amazonaws.com/prod/risks/entry/", obj)
        .then(function(response) {
          // eslint-disable-next-line
          console.log(response);
          commit("SUBMIT_ENTRY", true);
          commit("ADD_ENTRY_ERROR", "");
        })
        .catch(function(error) {
          state.entryErrors = [];
          let errorMessage = error.response.data.errors.missing_fields.join(', ') + ' are required but not filled.'
          commit("ADD_ENTRY_ERROR", errorMessage)
          commit("SUBMIT_ENTRY", false);
        });
    }
  },
  getters: {
    riskName: state => state.riskName,
    fieldName: state => state.fieldName,
    fieldType: state => state.fieldType,
    fieldIsRequired: state => state.fieldIsRequired,
    fieldOptions: state => state.fieldOptions,
    fields: state => state.fields,
    fieldErrors: state => state.fieldErrors,
    formSchema: state => state.formSchema,
    formData: state => state.formData,
    risks: state => state.risks,
    entryErrors: state => state.entryErrors,
    entrySubmitted: state => state.entrySubmitted,
    formSubmitted: state => state.formSubmitted,
    formErrors: state => state.formErrors,
  }
});

