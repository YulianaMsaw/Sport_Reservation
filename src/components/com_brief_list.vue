<script setup>
import com_brief from './com_brief.vue'

defineProps({
  items: Array
})
</script>

<template>
  <div class="bg-slate-100">
    <div class="w-4/5 m-auto border-b border-t items-center">
      <h2 class="my-20 text-center text-2xl text-slate-300 font-bold">Спортивные комплексы</h2>
      <div class="flex flex-wrap gap-5 justify-center">
        <com_brief
          v-for="item in items"
          :key="item.id"
          :imageURL="item.pic"
          :title="item.title"
          :type="item.type"
          :id="item.id.toString()"
        />
      </div>
      <div class="flex bg-white w-24 rounded-2xl p-3 my-20 shadow-xl mx-auto">
        <button class="text-slate-600 w-1/2">&#8592;</button>
        <span class="text-slate-300">&#448;</span>
        <button class="text-black w-1/2">&#8594;</button>
      </div>
    </div>
  </div>
</template>
