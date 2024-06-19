<script setup>
import abon_profile_brief from './abon_profile_brief.vue'
import axios from 'axios'
import { ref, computed } from 'vue'
import { onMounted } from 'vue'

const props = defineProps({
  items: Array,
  searchquery: String,
  price_min: Number,
  price_max: Number,
  duration_min: Number,
  duration_max: Number,
  unit: String
})
const abons = ref([])
onMounted(async () => {
  try {
    const { data } = await axios.get('http://127.0.0.1:8000/abons')
    abons.value = data
  } catch (error) {
    console.error(error)
  }
})

const query = ref('')
const queryAbons = computed(() => {
  let p = abons.value

  p = p.filter((item) => {
    return (
      item.name.indexOf(props.searchquery) !== -1 &&
      item.price >= props.price_min &&
      (item.price <= props.price_max || props.price_max === 0) &&
      item.duration >= props.duration_min &&
      (item.duration <= props.duration_max || props.duration_max === 0) &&
      (item.unit === props.unit || props.unit === 'любое' || !props.unit)
    )
  })

  return p
})
</script>

<template>
  <div v-if="queryAbons.length > 0" class="bg-slate-100">
    <div class="w-4/5 m-auto border-b border-t items-center">
      <h2 class="my-20 text-center text-2xl text-slate-300 font-bold">Абонементы</h2>
      <div class="flex flex-wrap gap-5 justify-center my-10">
        <abon_profile_brief
          v-for="item in queryAbons"
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
          :reserv="true"
        />
      </div>
    </div>
  </div>
</template>
