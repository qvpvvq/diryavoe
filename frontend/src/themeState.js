import { ref, watch } from 'vue'
const savedTheme = localStorage.getItem('theme')
export const isDark = ref(savedTheme ? JSON.parse(savedTheme) : true)

export const toggleTheme = () => {
  isDark.value = !isDark.value
  localStorage.setItem('theme', isDark.value)
}
watch(
  isDark,
  () => {
    if (isDark.value) {
      document.body.classList.add('dark-theme')
    } else {
      document.body.classList.remove('dark-theme')
    }
  },
  { immediate: true },
)
