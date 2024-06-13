<script setup>
import abon_profile_brief from './abon_profile_brief.vue'

const props = defineProps({
  items: Array,
  reserv: Boolean
})
</script>

<template>
  <div class="my-10 flex flex-wrap gap-5 justify-center">
    <abon_profile_brief
      v-for="item in props.items"
      :key="item.id"
      :imageURL="item.pic"
      :trainer="item.trainer"
      :name="item.name"
      :type="item.type"
      :status="item.status"
      :id="item.id"
      :duration="item.duration"
      :unit="item.unit"
      :price="item.price"
      :reserv="props.reserv"
    />
  </div>
  <div class="flex bg-white w-24 rounded-2xl p-3 my-20 shadow-xl mx-auto">
    <button class="text-slate-600 w-1/2">&#8592;</button>
    <span class="text-slate-300">&#448;</span>
    <button class="text-black w-1/2">&#8594;</button>
  </div>
</template>
