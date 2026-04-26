import { ref, computed } from 'vue'
import api from '@/api'

export function useAuthForm(url, successMessage) {
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
      status.value = 'ok: ' + (response.data.message || successMessage)
    } catch (error) {
      status.value = 'error: ' + (error.response?.data?.error || 'Сервер недоступен')
    }
  }

  const isFormValid = computed(() => {
    return username.value.trim() != '' && password.value.trim() != ''
  })

  return { username, password, status, handleSubmit, isFormValid }
}
