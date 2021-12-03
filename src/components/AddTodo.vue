<template>
  <modal v-if="showModal" @close="showModal = false">
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
import Modal from "../ui/Modal.vue";
export default {
  components: { Modal },
};
</script>
