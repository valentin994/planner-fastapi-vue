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
import { mapState, mapActions } from "vuex";
//TODO Add checkmark if something is done or not
export default {
  computed: mapState({
    todos: (state) => state.todos,
  }),
  methods: {
    ...mapActions(["deleteTodo"]),
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
