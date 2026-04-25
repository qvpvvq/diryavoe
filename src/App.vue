<script setup>
import { RouterLink } from 'vue-router'
import { isDark, toggleTheme } from '@/themeState'
import darkThemeIcon from './assets/moon.svg'
import lightThemeIcon from './assets/sun.svg'
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
        <RouterLink class="nav-link navbarButton" to="/login">Логин</RouterLink>
        <RouterLink class="nav-link navbarButton" to="/register">Регистрация</RouterLink>
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
  padding: 4px 8px;
  border-radius: 7px;
}
.navbarButton:hover {
  background-color: gray;
}
</style>
