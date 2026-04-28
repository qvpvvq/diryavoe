<script setup>
import adminPostCard from '@/components/adminPostCard.vue'
import adminUserCard from '@/components/adminUserCard.vue'
import { useRouter } from 'vue-router'
import api from '@/api'
import { ref, onMounted } from 'vue'

const router = useRouter()
const posts = ref([])
const users = ref([])
onMounted(() => {
  getAdminData()
})

const getAdminData = async () => {
  try {
    const response = await api.get('/admin')
    users.value = response.data.users
    posts.value = response.data.posts
  } catch (error) {
    console.error(error, error.response?.data?.error || '')
    if (error.response?.status === 403) {
      router.replace('/')
    }
  }
}

const handleDelete = async (id) => {
  try {
    const response = await api.delete('/admin/posts', {
      data: {
        id: id,
      },
    })
    console.log(response.data.status + response.data.message)
    posts.value = posts.value.filter((post) => post.id !== id)
  } catch (error) {
    console.log(error.response?.data?.error || 'Сервер недоступен')
  }
}
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <h2 class="mb-4 text-center">Панель администратора</h2>
        <div class="card shadow-sm mb-5">
          <div class="card-header bg-dark text-white">Список пользователей</div>
          <div class="card-body">
            <table class="table table-sm">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Логин</th>
                  <th>Пароль</th>
                  <th>Роль</th>
                </tr>
              </thead>
              <tbody>
                <adminUserCard v-for="user in users" :key="user.id" :user="user"></adminUserCard>
              </tbody>
            </table>
          </div>
        </div>
        <div class="card shadow-sm">
          <div class="card-header bg-primary text-white">Управление лентой</div>
          <div class="card-body">
            <table class="table table-hover">
              <thead>
                <tr>
                  <th>Автор</th>
                  <th>Контент</th>
                  <th>Действие</th>
                </tr>
              </thead>
              <tbody>
                <adminPostCard
                  @deletePostCard="handleDelete"
                  v-for="post in posts"
                  :key="post.id"
                  :post="post"
                >
                </adminPostCard>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
