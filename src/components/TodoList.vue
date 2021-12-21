<template>
  <div>
    <ul v-for="todo in todos" :key="todo.id">
      <li>Title: {{ todo.title }}</li>
      <li>Text: {{ todo.text }}</li>
      <li>{{ todo.is_done }}</li>
      <input type="checkbox" id="isDone" name="isDone" v-model="todo.is_done" />
      <label for="isDone">Done</label>
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
