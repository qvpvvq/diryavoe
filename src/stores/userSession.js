import { defineStore } from 'pinia'

export const useSessionStore = defineStore('session', {
  username: '',
  role: '',
  isLoggedIn: '',
})
