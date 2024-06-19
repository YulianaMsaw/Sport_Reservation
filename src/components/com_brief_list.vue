<script setup>
import com_brief from './com_brief.vue'
import axios from 'axios'
import { ref } from 'vue'
import { onMounted } from 'vue'

const ObjectsOnPage = 4
const complexes = ref([])
const CurrentPage = ref(0)
const CountPages = ref([])
const PagingList = ref([])

onMounted(async () => {
  try {
    const { data } = await axios.get('http://127.0.0.1:8000/complexes')
    complexes.value = data
    CountPages.value = complexes.value.length
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
    PagingList.value[j] = complexes.value[i]
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
  <div class="bg-slate-100">
    <div class="w-4/5 m-auto border-b border-t items-center">
      <h2 class="my-20 text-center text-2xl text-slate-300 font-bold">Спортивные комплексы</h2>
      <div class="flex flex-wrap gap-5 justify-center">
        <com_brief
          v-for="item in PagingList"
          :key="item.id"
          :imageURL="item.pic"
          :title="item.title"
          :type="item.type"
          :id="item.id.toString()"
        />
      </div>
      <div class="flex bg-white w-24 rounded-2xl p-3 my-20 shadow-xl mx-auto">
        <button @click="PrevPage" class="text-slate-600 w-1/2">&#8592;</button>
        <span class="text-slate-300">&#448;</span>
        <button @click="NextPage" class="text-black w-1/2">&#8594;</button>
      </div>
    </div>
  </div>
</template>
