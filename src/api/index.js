import axios from "axios";

export default {
  async getTodos() {
    try {
      await axios.get("http://127.0.0.1:8000/todos/").then((response) => {
        console.log(response);
        return response;
      });
    } catch (error) {
      console.log(error);
    }
  },
};
