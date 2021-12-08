<template>
  <modal v-if="showModal" @close="$emit('onClose')" @onSubmit="addTodo">
    <template v-slot:header>
      <h1>Task</h1>
    </template>
    <template v-slot:body>
      <input v-model="title" placeholder="Title" />
      <input v-model="text" placeholder="Text" />
    </template>
  </modal>
</template>

<script>
import Modal from "../ui/Modal.vue";
import axios from "axios";
export default {
  components: { Modal },
  props: { showModal: Boolean },
  emits: ["onClose"],
  data() {
    return {
      title: "",
      text: "",
    };
  },
  methods: {
    async addTodo() {
      try {
        await axios.post("http://127.0.0.1:8000/todo/", {
          title: this.title,
          text: this.text,
        });
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
