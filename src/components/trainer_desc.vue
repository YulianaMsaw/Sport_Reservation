<script setup>
defineProps({
  name: String,
  surname: String,
  desc: String
})
</script>

<template>
  <div class="w-1/3 my-10">
    <div class="border-b border-slate-300">
      <h1 class="text-3xl font-bold text-black">{{ name }} {{ surname }}</h1>
      <p class="text-slate-400 text-sm mt-3 mb-5 font-bold">Тренер</p>
    </div>

    <div class="border-b border-slate-300">
      <p class="text-slate-400 text-sm my-5">
        {{ desc }}
      </p>
      <p class="text-slate-400 text-xl font-bold mb-5">Расписание</p>
    </div>
    <ul class="flex gap-5 items-center my-5">
      <li><img src="/instagram_b.png" alt="instagram" /></li>
      <li><img src="/linkin_b.png" alt="linkin" /></li>
      <li><img src="/facebook_b.png" alt="facebook" /></li>
      <li><img src="/twitter_b.png" alt="twitter" /></li>
    </ul>
  </div>
</template>
