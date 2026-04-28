<script setup>
import { useAuthForm } from '@/composables/useAuthForm'
import { isDark } from '@/themeState' // хз насколько норм идея так делать
import { RouterLink } from 'vue-router'

const { username, password, handleSubmit, isFormValid } = useAuthForm(
  '/login',
  'Вход выполнен',
  '/',
)
</script>

<template>
  <div class="text-center login-page">
    <div
      class="login-form border shadow-sm"
      :class="[isDark ? 'is-dark border-secondary' : 'border-light']"
    >
      <h2 class="mb-4">Авторизация</h2>
      <form @submit.prevent="handleSubmit" class="d-flex flex-column align-items-center">
        <input class="form-control mb-3" type="text" v-model="username" placeholder="Логин" />
        <input class="form-control mb-4" type="password" v-model="password" placeholder="Пароль" />
        <button
          :disabled="!isFormValid"
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
      <div style="margin-top: 50px; color: gray">
        <p>Попробуй ввести в логин: <span style="color: red">' OR 1=1--</span></p>
      </div>
    </div>
  </div>
</template>
