import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useSessionStore = defineStore('session', () => {
  const username = ref('')
  const role = ref('')
  const isLoggedIn = ref(false)
  function login(recievedUsername, recievedRole) {
    username.value = recievedUsername
    role.value = recievedRole
    isLoggedIn.value = true
  }
  function logout() {
    username.value = ''
    role.value = ''
    isLoggedIn.value = false
  }
  return { username, role, isLoggedIn, login, logout }
})
