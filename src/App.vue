<script setup>
import header_ from './components/header.vue'
import footer_ from './components/footer.vue'
</script>

<template>
  <header_ v-if="$route.path != '/signin' && $route.path != '/registration'" />
  <router-view />
  <footer_ v-if="$route.path != '/signin' && $route.path != '/registration'" />
</template>
