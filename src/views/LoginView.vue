<script setup>
import { ref } from "vue";
import api from "@/api";
import { isDark } from "@/themeState"
import { RouterLink } from "vue-router";

const username = ref("");
const password = ref("");
const status = ref("")

const handleLogin = async () => {
  try {
    const response = await api.post('/login', {
      username: username.value,
      password: password.value,
    });
    status.value = "ok" + (response.data.message || "Вход выполнен")
  }
  catch (error) {
    status.value = "error" + (error.response?.data?.error || "Сервер недоступен")
  }
}
</script>

<template>
  <div class="text-center login-page">
    <div class="login-form border shadow-sm" :class="[isDark ? 'is-dark border-secondary' : 'border-light']">
      <h2 class="mb-4">Авторизация</h2>
      <form @submit.prevent="handleLogin">
        <input class="form-control" type="text" v-model="username" placeholder="Логин"><br><br>
        <input class="form-control" type="password" v-model="password" placeholder="Пароль"><br><br>
        <button class="btn" :class="isDark ? 'btn-light' : 'btn-dark'" style="width: 50%;" type="submit">Войти</button>
      </form>
      <p class="mt-4">
        <RouterLink to="/register">Еще нет аккаунта?</RouterLink>
      </p>
      <p v-if="status">{{ status }}</p>
      <div style="margin-top: 50px; color: gray;">
        <p>Подсказка: попробуй ввести в логин: <span style="color: red;">' OR 1=1--</span></p>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.login-page {
  display: flex;
  justify-content: center;
  padding-top: 2%;
}

.login-form {
  width: 400px;
  padding: 5px 10px 0px 10px;
  border-radius: 20px;
  background-color: white;

  &.is-dark {
    background-color: #222222;
  }
}
</style>
