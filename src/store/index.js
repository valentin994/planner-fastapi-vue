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
    setTodos(state, allTodos) {
      state.todos = allTodos;
    },
    removeTodo(state, id) {
      state.todos = [...state.todos.filter((todo) => todo.id !== id)];
    },
  },
  actions: {
    async getAllTodos({ commit }) {
      const todos = await api.getTodos();
      commit("setTodos", todos);
    },
    async deleteTodo({ commit }, id) {
      commit("removeTodo", id);
    },
  },
  plugins: [createLogger()],
});
