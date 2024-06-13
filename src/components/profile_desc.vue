<script setup>
defineProps({
  name: String,
  surname: String,
  phone: String,
  password: String,
  burthday: String,
  vk: String,
  insta: String,
  telegram: String,
  pic: String,
  email: String,
  aboncount: Number
})
</script>
<template>
  <div class="relative bg-white shadow-lg border-slate-100 rounded-2xl p-5 m-auto">
    <div class="flex justify-between gap-10">
      <img :src="pic" alt="pic" class="w-1/2 rounded-2xl object-cover aspect-square relative" />
      <div class="w-2/5 ml-auto flex flex-col justify-between">
        <div class="fixed-top">
          <p class="text-2xl text-black text-bold font-bold">{{ surname }} {{ name }}</p>
          <p class="mt-3 text-sm">Телефон: +{{ phone }}</p>
          <p class="mt-3 text-sm">Почта: {{ email }}</p>
          <p class="mt-3 text-sm">Дата рождения: {{ burthday }}</p>
        </div>
        <div class="fixed-bottom">
          <p class="text-sm text-slate-400 items-center mb-3">Кол-во абониментов</p>
          <div class="flex gap-3 mb-10 items-center">
            <img src="/count.png" alt="count" class="w-5 h-8" />
            <p class="text-3xl text-black text-bold font-bold">{{ aboncount }}</p>
          </div>
          <button
            class="w-full bg-black rounded-xl text-white p-3 justify-self-end text-bold font-bold"
          >
            Изменить профиль
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
