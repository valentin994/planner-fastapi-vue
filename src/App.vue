<template>
  <h1>Ghost Planner</h1>
  <TodoList :todos="todos" />
  <button @click="showModal = true">Add Todo</button>
  <AddTodo :showModal="showModal" @onClose="showModal = false" />
</template>

<script>
import TodoList from "./components/TodoList.vue";
import AddTodo from "./components/AddTodo.vue";
import axios from "axios";
//TODO implement vue store for the todo list
export default {
  name: "App",
  components: { TodoList, AddTodo },
  data() {
    return {
      todos: [],
      showModal: false,
      title: "",
      text: "",
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
