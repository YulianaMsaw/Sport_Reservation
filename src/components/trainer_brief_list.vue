<script setup>
import trainer_brief from './trainer_brief.vue'
import axios from 'axios'
import { ref } from 'vue'
import { onMounted } from 'vue'

const ObjectsOnPage = 8
const trainers = ref([])
const CurrentPage = ref(0)
const CountPages = ref([])
const PagingList = ref([])

onMounted(async () => {
  try {
    const { data } = await axios.get('http://127.0.0.1:8000/trainers')
    trainers.value = data
    CountPages.value = trainers.value.length
  } catch (error) {
    console.error(error)
  }
  GetList()
})

const GetList = () => {
  PagingList.value.length = 0
  var j = 0
  for (
    var i = CurrentPage.value * ObjectsOnPage;
    i < CurrentPage.value * ObjectsOnPage + ObjectsOnPage && i < CountPages.value;
    i++
  ) {
    PagingList.value[j] = trainers.value[i]
    j++
  }
}
const NextPage = () => {
  if ((CurrentPage.value + 1) * ObjectsOnPage < CountPages.value) {
    CurrentPage.value++
    GetList()
  }
}
const PrevPage = () => {
  if (CurrentPage.value > 0) {
    CurrentPage.value--
    GetList()
  }
}
</script>

<template>
  <div class="w-4/5 m-auto">
    <h2 class="my-20 text-center text-2xl text-black font-bold">Тренеры</h2>
    <div class="flex flex-wrap gap-5 justify-center justify-content: stretch">
      <trainer_brief
        v-for="item in PagingList"
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
    <div class="flex bg-white w-24 rounded-2xl p-3 my-20 shadow-xl mx-auto">
      <button @click="PrevPage" class="text-slate-600 w-1/2">&#8592;</button>
      <span class="text-slate-300">&#448;</span>
      <button @click="NextPage" class="text-black w-1/2">&#8594;</button>
    </div>
  </div>
</template>
