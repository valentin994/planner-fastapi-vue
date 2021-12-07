<template>
  <div>
    <ul v-for="todo in todos" :key="todo.id">
      <li>Title: {{ todo.title }}</li>
      <li>Text: {{ todo.text }}</li>
      <button @click="deleteTodo()">Delete</button>
    </ul>
  </div>
</template>
<script>
export default {
  //TODO props with static typing
  props: ["todos"],
  methods: {
    async deleteTodo() {
      console.log(1);
    },
  },
};
</script>
<style scoped>
ul {
  list-style-type: none;
}
</style>
