import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";
//TODO implement filter option

const app = createApp(App);

app.use(store);
app.mount("#app");
