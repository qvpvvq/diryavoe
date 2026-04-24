<script setup>
import { isDark } from '@/themeState'
import api from '@/api'
import { RouterLink } from 'vue-router'
import { ref, computed } from 'vue'

const username = ref('')
const password = ref('')
const status = ref('')

const isFormValid = computed(() => {
  return username.value.trim() != '' && password.value.trim() != ''
})

const handleRegister = async () => {
  if (!isFormValid.value) {
    return (status.value = 'error: Заполните все поля')
  }

  try {
    const response = await api.post('/register', {
      username: username.value,
      password: password.value,
    })
    status.value = 'ok: ' + (response.data.message || 'Аккаунт создан')
  } catch (error) {
    status.value = 'error: ' + (error.response?.data?.error || 'Сервер недоступен')
  }
}
</script>

<template>
  <div class="text-center login-page">
    <div
      class="login-form border shadow-sm"
      :class="[isDark ? 'is-dark border-secondary' : 'border-light']"
    >
      <h2 class="mb-4">Регистрация</h2>
      <form @submit.prevent="handleRegister" class="d-flex flex-column align-items-center">
        <input class="form-control mb-3" type="text" v-model="username" placeholder="Логин" />
        <input class="form-control mb-4" type="password" v-model="password" placeholder="Пароль" />
        <button
          :disabled="!isFormValid"
          class="btn"
          :class="isDark ? 'btn-light' : 'btn-dark'"
          style="width: 50%"
          type="submit"
        >
          Зарегистрироваться
        </button>
      </form>
      <p class="mt-4">
        <RouterLink to="/login">Уже есть аккаунт?</RouterLink>
      </p>
      <p v-if="status">{{ status }}</p>
      <div style="margin-top: 50px; color: gray">
        <p>Попробуй ввести в логин: <span style="color: red">' OR 1=1--</span></p>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss"></style>
