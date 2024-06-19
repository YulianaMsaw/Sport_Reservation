<script setup>
import trainer_brief from './trainer_brief.vue'
import axios from 'axios'
import { ref, computed } from 'vue'
import { onMounted } from 'vue'

const props = defineProps({
  searchquery: String
})

const trainers = ref([])

onMounted(async () => {
  try {
    const { data } = await axios.get('http://127.0.0.1:8000/trainers')
    trainers.value = data
  } catch (error) {
    console.error(error)
  }
})

const query = ref('')
const queryTrainers = computed(() => {
  let p = trainers.value
  p = p.filter((item) => {
    return (
      item.name.indexOf(props.searchquery) !== -1 || item.surname.indexOf(props.searchquery) !== -1
    )
  })

  return p
})
</script>

<template>
  <div v-if="queryTrainers.length > 0" class="w-4/5 m-auto">
    <h2 class="my-20 text-center text-2xl text-black font-bold">Тренеры</h2>
    <div class="flex flex-wrap gap-5 justify-center justify-content: stretch my-10">
      <trainer_brief
        v-for="item in queryTrainers"
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
  </div>
</template>
