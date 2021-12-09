import { createApp } from "vue";
import { createStore } from "vuex";
import App from "./App.vue";
import { createLogger } from "vuex";
//TODO implement filter option
//TODO move store to separate file
const store = createStore({
  state() {
    return {
      count: 0,
    };
  },
  plugins: [createLogger()],
});

const app = createApp(App);

app.use(store);
app.mount("#app");
