<script setup>
import { isDark } from '@/themeState'
defineProps({
  username: String,
})
</script>
<template>
  <div
    class="list-group-item list-group-item-action p-2 d-flex align-items-center"
    :class="{ is_dark: isDark }"
  >
    <div
      class="avatar-placeholder text-white me-3 d-flex align-items-center justify-content-center"
      style="width: 40px; height: 40px"
    >
      <img :src="`https://api.dicebear.com/9.x/identicon/svg?seed=${username}`" alt="avatar" />
    </div>
    <strong>@{{ username }}</strong>
  </div>
</template>

<style scoped>
.is_dark {
  background-color: transparent !important;
  color: white !important;
  border: 1px solid #6c757d;
}
</style>
