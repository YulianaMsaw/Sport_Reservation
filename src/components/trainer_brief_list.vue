<script setup>
import trainer_brief from './trainer_brief.vue'

defineProps({
  items: Array
})
</script>

<template>
  <div class="w-4/5 m-auto">
    <h2 class="my-20 text-center text-2xl text-black font-bold">Тренеры</h2>
    <div class="flex flex-wrap gap-5 justify-center">
      <trainer_brief
        v-for="item in items"
        :key="item.id"
        :imageURL="item.avatar"
        :name="item.name"
        :surname="item.surname"
        :checked="item.checked"
        :avatar="item.avatar"
        :desc="item.desc"
        :id="item.id.toString()"
      />
    </div>
  </div>
</template>
