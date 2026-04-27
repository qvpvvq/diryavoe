<script setup>
import { RouterLink } from 'vue-router'
import { onMounted } from 'vue'
import api from './api'
import { isDark, toggleTheme } from '@/themeState'
import darkThemeIcon from './assets/moon.svg'
import lightThemeIcon from './assets/sun.svg'
import { useSessionStore } from './stores/userSession'

const store = useSessionStore()

onMounted(async () => {
  try {
    const response = await api.get('/me')
    store.login(response.data.username, response.data.role)
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4 navcolor">
    <div class="container">
      <RouterLink class="navbar-brand" to="/">FakeSocial</RouterLink>
      <div class="navbar-nav ms-auto">
        <button @click="toggleTheme" class="nav-link d-flex align-items-center navbarButton">
          <img class="themeIcon" v-if="isDark" :src="darkThemeIcon" alt="Dark" />
          <img class="themeIcon" v-else :src="lightThemeIcon" alt="Light" />
        </button>
        <RouterLink class="nav-link navbarButton" to="/search">Поиск</RouterLink>
        <template v-if="store.isLoggedIn">
          <span class="nav-link">Привет, {{ store.username }}</span>
          <button class="nav-link navbarButton" @click="store.logout">Выйти</button>
        </template>
        <template v-else>
          <RouterLink class="nav-link navbarButton" to="/login">Логин</RouterLink>
          <RouterLink class="nav-link navbarButton" to="/register">Регистрация</RouterLink>
        </template>
      </div>
    </div>
  </nav>

  <router-view />
</template>

<style scoped>
.navcolor {
  background-color: #222222 !important;
}
.themeIcon {
  aspect-ratio: 1;
  width: 20px;
  filter: invert(1);
  opacity: 0.6;

  padding: 0;
}

.navbarButton {
  background: none;
  border: none;
  padding: auto;
  border-radius: 7px;
}
.navbarButton:hover {
  background-color: gray;
}
</style>
