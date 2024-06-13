<script setup>
defineProps({
  imageURL: String,
  title: String,
  count: String
})
</script>
<template>
  <div
    class="items-center w-full bg-white shadow-lg border-slate-100 rounded-2xl p-5 flex my-5 gap-5 cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition"
  >
    <img :src="imageURL" alt="sec_pic" class="rounded-2xl object-cover rounded-full size-12" />
    <p class="">{{ title }}</p>
    <div class="ml-auto">
      <div class="flex gap-3 my-3 items-center">
        <img src="/count.png" alt="count" class="w-3 h-5" />
        <p class="text-xl text-bold text-black font-bold">{{ count }}</p>
      </div>
    </div>
  </div>
</template>
