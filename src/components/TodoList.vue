//TODO Add remove todo button
<template>
  <div>
    <ul v-for="todo in todos" :key="todo.text">
      <li>Title: {{ todo.title }}</li>
      <li>Text: {{ todo.text }}</li>
    </ul>
  </div>
</template>
<script>
export default {
  props: ["todos"],
};
</script>
<style scoped>
ul {
  list-style-type: none;
}
</style>
