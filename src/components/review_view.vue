<script setup>
const props = defineProps({
  imageURL: String,
  name: String,
  surname: String,
  text: String,
  date: String,
  id: String
})
</script>

<template>
  <div class="w-4/5 m-auto bg-white rounded-2xl p-5 shadow-lg my-10">
    <div class="flex gap-5 items-center border-b h-20 text-center">
      <img
        :src="imageURL"
        alt="user_logo"
        class="w-12 h-12 rounded-full object-cover aspect-square"
      />
      <div>
        <p class="font-bold">{{ name }} {{ surname }}</p>
        <p class="m-auto">{{ date }}</p>
      </div>
    </div>
    <div class="my-5">
      <p>{{ text }}</p>
    </div>
  </div>
</template>
