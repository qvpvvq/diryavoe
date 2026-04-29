<script setup>
defineProps({
  user: Object,
})
</script>

<template>
  <tr>
    <td>{{ user.id }}</td>
    <td>
      <strong>{{ user.username }}</strong>
    </td>
    <td>
      <code>{{ user.password }}</code>
    </td>
    <td>
      <span class="badge bg-secondary">{{ user.role }}</span>
    </td>
  </tr>
</template>
