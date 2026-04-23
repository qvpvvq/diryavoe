<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <div class="container">
        <h2>Создать аккаунт</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Придумайте логин" required><br><br>
            <input type="password" name="password" placeholder="Придумайте пароль" required><br><br>
            <button type="submit">Зарегистрироваться</button>
        </form>

        <RouterLink to="/login">Уже есть аккаунт?</RouterLink>
    </div>
</template>

<style></style>
