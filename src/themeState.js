import { ref } from 'vue'

export const isDark = ref(false)
export const toggleTheme = () => {
  isDark.value = !isDark.value

  if (isDark.value) {
    document.body.classList.add('dark-theme')
  } else {
    document.body.classList.remove('dark-theme')
  }
}
