import { ref, computed } from 'vue'
import { useSessionStore } from '@/stores/userSession'
import api from '@/api'

export function useAuthForm(url, successMessage) {
  const store = useSessionStore()
  const username = ref('')
  const password = ref('')
  const status = ref(null)

  const handleSubmit = async () => {
    if (!isFormValid.value) {
      return (status.value = 'error: Заполните все поля')
    }

    try {
      const response = await api.post(url, {
        username: username.value,
        password: password.value,
      })
      store.login(response.data.user.username, response.data.user.role)
      status.value = 'ok: ' + (response.data.message || successMessage)
    } catch (error) {
      status.value = 'error: ' + (error.response?.data?.error || 'Сервер недоступен')
    }
  }

  const isFormValid = computed(() => {
    const trimedUsername = username.value.trim()
    const trimedPassword = password.value.trim()
    return (
      trimedUsername != '' &&
      trimedPassword != '' &&
      trimedUsername.length <= 50 &&
      trimedPassword.length <= 50
    )
  })

  return { username, password, status, handleSubmit, isFormValid }
}
