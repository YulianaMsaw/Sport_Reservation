<script setup>
defineProps({
  imageURL: String,
  name: String,
  desc: String,
  map: String,
  shortdesc: String,
  type: String
})
</script>
<template>
  <div class="relative bg-white shadow-lg border-slate-100 rounded-2xl p-5 m-auto">
    <div class="flex justify-between gap-10">
      <img
        :src="imageURL"
        alt="avatar"
        class="w-1/2 rounded-2xl object-cover aspect-square relative"
      />
      <div class="w-2/5 ml-auto flex flex-col justify-between">
        <div class="fixed-top">
          <p class="text-3xl text-black text-bold font-bold">{{ name }}</p>
          <p class="mt-3 text-slate-400 text-sm">{{ type }}</p>
        </div>
        <div class="my-5">
          <p class="text-xl text-black text-bold font-bold">Описание клуба</p>
          <p class="text-lg text-slate-400 items-center my-5">
            {{ desc }}
          </p>
        </div>
        <div class="my-5">
          <button
            class="w-full bg-black rounded-xl text-white p-3 justify-self-end text-bold font-bold"
          >
            Выбрать абонемент
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
