//TODO Add add todo button //TODO Add add todo Component
<template>
  <h1>Ghost Planner</h1>
  <TodoList :todos="todos" />
  <button @click="addTodo">Add Todo</button>
</template>

<script>
import TodoList from "./components/TodoList.vue";
import axios from "axios";
export default {
  name: "App",
  components: { TodoList },
  data() {
    return {
      todos: [],
      showModal: false,
    };
  },
  methods: {
    async getTodos() {
      try {
        await axios
          .get("http://127.0.0.1:8000/todos/")
          .then((response) => (this.todos = response.data));
      } catch (error) {
        console.log(error);
      }
    },
    async addTodo() {
      try {
        console.log("I have added a todo");
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
