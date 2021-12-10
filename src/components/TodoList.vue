<template>
  <div>
    <ul v-for="todo in todos" :key="todo.id">
      <li>Title: {{ todo.title }}</li>
      <li>Text: {{ todo.text }}</li>
      <button @click="deleteTodo(todo.id)">Delete</button>
    </ul>
  </div>
</template>
<script>
import axios from "axios";
import { mapState } from "vuex";
export default {
  computed: mapState({
    todos: (state) => state.todos,
  }),
  methods: {
    async deleteTodo(id) {
      try {
        axios
          .delete(`http://127.0.0.1:8000/todo/${id}`)
          .then((response) => console.log(response));
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.$store.dispatch("getAllTodos");
  },
};
</script>
<style scoped>
ul {
  list-style-type: none;
}
</style>
