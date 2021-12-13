import axios from "axios";

export default {
  async getTodos() {
    try {
      const data = axios
        .get("http://127.0.0.1:8000/todos/")
        .then((response) => {
          return response.data;
        });
      return data;
    } catch (error) {
      console.log(error);
    }
  },
  async deleteTodo(id) {
    try {
      axios.delete(`http://127.0.0.1:8000/todo/${id}`);
    } catch (error) {
      console.log(error);
    }
  },
};
