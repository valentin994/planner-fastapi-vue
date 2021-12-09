import { createStore, createLogger } from "vuex";
import api from "../api";

export default createStore({
  state() {
    return {
      count: 0,
      todos: [],
    };
  },
  mutations: {
    setTodos(state, todos) {
      console.log(todos);
      state.todos = todos;
    },
  },
  actions: {
    async getAllTodos({ commit }) {
      let todos = await api.getTodos();
      commit("setTodos", todos);
    },
  },
  plugins: [createLogger()],
});
