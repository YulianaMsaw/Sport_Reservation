<script setup>
defineProps({
  imageURL: String,
  trainer: String,
  title: String
})
</script>

<template>
  <div>
    <div
      class="flex flex-col justify-between h-80 bg-white shadow-lg w-48 relative border-slate-100 rounded-2xl p-3 cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition"
    >
      <img :src="imageURL" alt="abon_pic" class="rounded-2xl object-fill aspect-square" />
      <p class="text-left text-bold font-sans">{{ trainer }}</p>
      <p class="mt-2 text-left font-bold font-sans underline my-3">{{ title }}</p>
      <button class="w-full bg-black rounded-xl text-white p-3 font-bold text-sm my-3">
        Записаться
      </button>
    </div>
  </div>
</template>
