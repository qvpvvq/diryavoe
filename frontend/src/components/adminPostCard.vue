<script setup>
const emit = defineEmits(['deletePostCard'])
defineProps({
  post: Object,
})
</script>

<template>
  <tr>
    <td>@{{ post.username }}</td>
    <td>{{ post.content.length > 100 ? post.content.slice(0, 100) + '...' : post.content }}</td>
    <td>
      <button class="btn btn-danger btn-sm" @click="emit('deletePostCard', post.id)">
        Удалить
      </button>
    </td>
  </tr>
</template>
