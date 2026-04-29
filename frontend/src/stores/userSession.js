import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/api'

export const useSessionStore = defineStore('session', () => {
  const username = ref('')
  const role = ref('')
  const isLoggedIn = ref(false)
  function login(receivedUsername, receivedRole) {
    username.value = receivedUsername
    role.value = receivedRole
    isLoggedIn.value = true
  }
  async function logout() {
    await api.post('/logout')
    username.value = ''
    role.value = ''
    isLoggedIn.value = false
  }
  return { username, role, isLoggedIn, login, logout }
})
