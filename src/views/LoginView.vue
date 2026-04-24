<script setup>
import { ref } from 'vue'
import api from '@/api'
import { isDark } from '@/themeState' // хз насколько норм идея так делать
import { RouterLink } from 'vue-router'

const username = ref('')
const password = ref('')
const status = ref('')

const handleLogin = async () => {
  try {
    const response = await api.post('/login', {
      username: username.value,
      password: password.value,
    })
    status.value = 'ok' + (response.data.message || 'Вход выполнен')
  } catch (error) {
    status.value = 'error' + (error.response?.data?.error || 'Сервер недоступен')
  }
}
</script>

<template>
  <div class="text-center login-page">
    <div
      class="login-form border shadow-sm"
      :class="[isDark ? 'is-dark border-secondary' : 'border-light']"
    >
      <h2 class="mb-4">Авторизация</h2>
      <form @submit.prevent="handleLogin" class="d-flex flex-column align-items-center">
        <input class="form-control mb-3" type="text" v-model="username" placeholder="Логин" />
        <input class="form-control mb-4" type="password" v-model="password" placeholder="Пароль" />
        <button
          class="btn"
          :class="isDark ? 'btn-light' : 'btn-dark'"
          style="width: 50%"
          type="submit"
        >
          Войти
        </button>
      </form>
      <p class="mt-4">
        <RouterLink to="/register">Еще нет аккаунта?</RouterLink>
      </p>
      <p v-if="status">{{ status }}</p>
      <div style="margin-top: 50px; color: gray">
        <p>Попробуй ввести в логин: <span style="color: red">' OR 1=1--</span></p>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss"></style>
