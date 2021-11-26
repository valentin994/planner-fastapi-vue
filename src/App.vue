<template>
  <h1>Ghost Planner</h1>
  <TodoList :todos="todos" />
</template>

<script>
import TodoList from "./components/TodoList.vue";

export default {
  name: "App",
  components: { TodoList },
  data() {
    return {
      todos: [],
    };
  },
  methods: {
    async getTodos() {
      try {
        let response = await fetch("http://127.0.0.1:8000/todos/");
        this.todos = await response.json();
        console.log(this.todos);
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getTodos();
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
