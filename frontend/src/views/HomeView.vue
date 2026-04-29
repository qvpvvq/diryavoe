<script setup>
import { useSessionStore } from '@/stores/userSession'
import { RouterLink } from 'vue-router'
import { ref, onMounted } from 'vue'
import api from '@/api'
import postCard from '@/components/postCard.vue'

const store = useSessionStore()
const posts = ref([])
const postFormInput = ref('')

const handlePostSubmit = async () => {
  try {
    const response = await api.post('/posts', {
      content: postFormInput.value,
    })
    console.log('ok: ' + (response.data.message || 'session confirmed'))
    getPosts()
  } catch (error) {
    console.log('error: ' + (error.response?.data?.error || 'server unavalaible'))
  }
}
const getPosts = async () => {
  try {
    const response = await api.get('/posts')
    posts.value = response.data.posts
    console.log(response.data.status, response.data.message)
    console.log('================')
    console.log(posts.value)
  } catch (error) {
    console.error(error)
  }
}

onMounted(async () => {
  getPosts()
})
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4">
        <div class="card shadow-sm mb-4">
          <div class="card-body">
            <div v-if="store.isLoggedIn">
              <h5 class="card-title">Поделиться мыслью</h5>
              <form @submit.prevent="handlePostSubmit">
                <textarea
                  class="form-control mb-3"
                  rows="3"
                  placeholder="Напиши что-нибудь..."
                  v-model="postFormInput"
                ></textarea>
                <button type="submit" class="btn btn-primary w-100">Опубликовать</button>
              </form>
            </div>
            <template v-else>
              <div class="text-center py-3">
                <p class="text-muted">Хотите написать пост?</p>
                <RouterLink to="/login" class="btn btn-outline-primary btn-sm"
                  >Войти в аккаунт</RouterLink
                >
              </div>
            </template>
          </div>
        </div>
      </div>
      <div class="col-md-8">
        <template v-if="posts.length">
          <postCard v-for="post in posts" :key="post.id" :post="post"></postCard>
        </template>
        <div v-else class="alert alert-light text-center border">Здесь пока тишина...</div>
      </div>
    </div>
  </div>
</template>
