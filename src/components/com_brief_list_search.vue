<script setup>
import com_brief from './com_brief.vue'
import axios from 'axios'
import { ref, computed } from 'vue'
import { onMounted } from 'vue'

const props = defineProps({
  searchquery: String
})

const complexes = ref([])
onMounted(async () => {
  try {
    const { data } = await axios.get('http://127.0.0.1:8000/complexes')
    complexes.value = data
  } catch (error) {
    console.error(error)
  }
})

const query = ref('')
const queryComplexes = computed(() => {
  let p = complexes.value
  p = p.filter((item) => {
    return item.title.indexOf(props.searchquery) !== -1
  })

  return p
})
</script>

<template>
  <div v-if="queryComplexes.length > 0" class="bg-slate-100">
    <div class="w-4/5 m-auto border-b border-t items-center">
      <h2 class="my-20 text-center text-2xl text-slate-300 font-bold">Спортивные комплексы</h2>
      <div class="flex flex-wrap gap-5 justify-center my-20">
        <com_brief
          v-for="item in queryComplexes"
          :key="item.id"
          :imageURL="item.pic"
          :title="item.title"
          :type="item.type"
          :id="item.id.toString()"
        />
      </div>
    </div>
  </div>
</template>
