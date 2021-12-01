//TODO Add add todo Component
<template>
  <h1>Ghost Planner</h1>
  <TodoList :todos="todos" />
  <button @click="showModal = true">Add Todo</button>
  <modal v-if="showModal" @close="showModal = false">
    //TODO Transfer this to a component
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
import TodoList from "./components/TodoList.vue";
import Modal from "./ui/Modal.vue";
import axios from "axios";
export default {
  name: "App",
  components: { TodoList, Modal },
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
    async addTodo() {
      //TODO Pass this function to the modal button
      try {
        await axios
          .post("http://127.0.0.1:8000/todo/", {
            title: this.title,
            text: this.text,
          })
          .then((response) => console.log(response));
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
