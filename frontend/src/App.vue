<script setup>
import { onMounted } from 'vue'
import api from './api'
import { useSessionStore } from './stores/userSession'
import TheHeader from './components/theHeader.vue'

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
  <TheHeader></TheHeader>
  <router-view />
</template>

<style scoped></style>
