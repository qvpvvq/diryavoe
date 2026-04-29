<script setup>
import { ref } from 'vue'
import api from '@/api'
import { isDark } from '@/themeState'
import searchUserRow from '@/components/searchUserRow.vue'
const users = ref([])
const query = ref('')
const tempInput = ref('')

const handleSearch = async () => {
  query.value = tempInput.value
  try {
    const response = await api.get('/search', {
      params: { query: query.value },
    })
    users.value = response.data.users
    console.log('ok: ' + (response.data.message || 'session confirmed'))
  } catch (error) {
    console.log('error: ' + (error.response?.data?.error || 'server unavalaible'))
  }
}
</script>

<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card shadow-sm searchWin" :class="{ is_dark: isDark }">
          <div class="card-body">
            <h3 class="card-title mb-4 text-center">Поиск пользователей</h3>
            <form @submit.prevent="handleSearch" class="input-group mb-4">
              <input type="text" class="form-control form-control-lg" placeholder="Введите ник..."
                v-model="tempInput" />
            </form>
            <template v-if="query">
              <hr />
              <p>Результаты для: {{ query }}</p>
              <div v-if="users.length" class="list-group">
                <searchUserRow v-for="user in users" :key="user.id" :username="user.username"></searchUserRow>
              </div>
              <div v-else class="alert alert-warning py-2">
                Никого не нашли. Попробуй поискать кого-то другого.
              </div>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.searchWin.is_dark {
  background-color: #222222;
  color: white;

  .form-control {
    background-color: transparent !important;
    color: white !important;
    border: 1px solid #6c757d;

    &::placeholder {
      color: #adb5bd;
    }

    &:focus {
      background-color: rgba(255, 255, 255, 0.05) !important;
      border-color: #f8f9fa;
      box-shadow: none;
    }
  }
}
</style>
