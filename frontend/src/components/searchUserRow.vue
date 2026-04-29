<script setup>
import { isDark } from '@/themeState'
defineProps({
    username: String
})
</script>

<template>

    <div class="list-group-item d-flex align-items-center" :class="{ is_dark: isDark }">
        <img :src="`https://api.dicebear.com/9.x/identicon/svg?seed=${username}`" class="me-3"
            style="width: 40px; height: 40px" alt="avatar" />
        <span>{{ username }}</span>
    </div>

</template>


<style lang="scss" scoped>
.is_dark {
    background-color: transparent !important;
    color: white !important;
    border: 1px solid #6c757d;

}
</style>