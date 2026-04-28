<script setup>
import { useSessionStore } from '@/stores/userSession'
import { RouterLink } from 'vue-router'
const store = useSessionStore()
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4">
        <div class="card shadow-sm mb-4">
          <div class="card-body">
            <div v-if="store.isLoggedIn">
              <h5 class="card-title">Поделиться мыслью</h5>
              <form method="POST">
                <textarea
                  class="form-control mb-3"
                  rows="3"
                  placeholder="Напиши что-нибудь..."
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
        <h3 class="mb-4 text-secondary">Свежие новости</h3>
        <div class="alert alert-light text-center border">Здесь пока тишина...</div>
      </div>
    </div>
  </div>
</template>
