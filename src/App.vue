<script setup>
import { RouterLink } from 'vue-router'
import { isDark, toggleTheme } from '@/themeState'
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4 navcolor">
    <div class="container">
      <RouterLink class="navbar-brand" to="/">FakeSocial</RouterLink>
      <div class="navbar-nav ms-auto">
        <button @click="toggleTheme" class="btn nav-link btn-sm d-flex align-items-center">
          {{ isDark ? '🌙 Темная' : '☀️ Светлая' }}
        </button>
        <RouterLink class="nav-link" to="/search">Поиск</RouterLink>
        <RouterLink class="nav-link" to="/login">Логин</RouterLink>
        <RouterLink class="nav-link" to="/register">Регистрация</RouterLink>
      </div>
    </div>
  </nav>

  <router-view />
</template>

<style scoped>
.navcolor {
  background-color: #222222 !important;
}
</style>
