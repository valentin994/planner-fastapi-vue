<template>
  <h1>Ghost Planner</h1>
  <TodoList />
  <button @click="showModal = true">Add Todo</button>
  <AddTodo :showModal="showModal" @onClose="showModal = false" />
</template>

<script>
import TodoList from "./components/TodoList.vue";
import AddTodo from "./components/AddTodo.vue";
//TODO docstrings all around
export default {
  name: "App",
  components: { TodoList, AddTodo },
  data() {
    return {
      showModal: false,
      title: "",
      text: "",
    };
  },
  created() {},
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
