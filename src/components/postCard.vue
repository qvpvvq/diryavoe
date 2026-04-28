<script setup>
defineProps({
  post: Object,
})
</script>

<template>
  <div class="card mb-3 border-0 shadow-sm">
    <div class="card-body">
      <h6 class="card-subtitle mb-2 text-primary">@{{ post.username }}</h6>
      <p class="card-text">{{ post.content }}</p>
    </div>
  </div>
</template>
