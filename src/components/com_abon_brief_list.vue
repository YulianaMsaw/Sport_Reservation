<script setup>
import abon_profile_brief from './abon_profile_brief.vue'
import { ref } from 'vue'

const props = defineProps({
  items: Array
})
const ObjectsOnPage = 4
const CurrentPage = ref(0)
const CountPages = props.items.length

const NextPage = () => {
  if (CurrentPage.value < CountPages - 1) {
    CurrentPage.value++
  }
}
const PrevPage = () => {
  if (CurrentPage.value > 0) {
    CurrentPage.value--
  }
}
</script>

<template>
  <div class="w-full">
    <h2 class="text-2xl text-slate-300 font-bold">Список абонементов</h2>
    <div class="my-10 flex flex-wrap gap-10">
      <abon_profile_brief
        v-for="item in items"
        :key="item.id"
        :imageURL="item.pic"
        :trainer="item.trainer"
        :name="item.name"
        :type="item.type"
        :status="item.status"
        :id="item.id"
      />
    </div>
    <div class="flex bg-white w-24 rounded-2xl p-3 my-20 shadow-xl mx-auto">
      <button @click="PrevPage" class="text-slate-600 w-1/2">&#8592;</button>
      <span class="text-slate-300">&#448;</span>
      <button @click="NextPage" class="text-black w-1/2">&#8594;</button>
    </div>
  </div>
</template>
