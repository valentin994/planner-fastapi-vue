import { createStore, createLogger } from "vuex";

export default createStore({
  state() {
    return {
      count: 0,
      todos: [],
    };
  },
  actions: {},
  plugins: [createLogger()],
});
