import { createStore, createLogger } from "vuex";
import api from "../api";
//import axios from "axios";
export default createStore({
  state() {
    return {
      count: 0,
      todos: [],
    };
  },
  mutations: {
    setTodos(state, allTodos) {
      state.todos = allTodos;
    },
  },
  actions: {
    async getAllTodos({ commit }) {
      const todos = await api.getTodos();
      commit("setTodos", todos);
    },
  },
  plugins: [createLogger()],
});
