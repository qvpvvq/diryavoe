import { defineStore } from 'pinia'

export const useSessionStore = defineStore('session', {
  state: () => ({ username: '', role: '', isLoggedIn: '' }),
})
