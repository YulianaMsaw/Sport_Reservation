<script setup>
import com_desc from '../components/com_desc.vue'
import abon_profile_brief_list from '../components/abon_profile_brief_list.vue'
import { onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useRoute } from 'vue-router'
import { ref } from 'vue'

const complexdata = ref([])
const complexabons = ref([])
const route = useRoute()
const router = useRouter()

onMounted(async () => {
  try {
    console.log(route.params.id.toString())
    const { data } = await axios.post(
      'http://127.0.0.1:8000/getComplexData',
      JSON.stringify({ id: route.params.id.toString() }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    complexdata.value = data
    console.log(complexdata.value)
  } catch (error) {
    console.error(error)
  }
  try {
    const { data } = await axios.post(
      'http://127.0.0.1:8000/getComplexAbons',
      JSON.stringify({ id: route.params.id.toString() }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    complexabons.value = data
    console.log(complexabons.value)
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div class="w-4/5 m-auto">
    <div class="flex gap-5 items-center my-5">
      <RouterLink to="/"><img src="/back.png" alt="back" class="w-5 h-5" /></RouterLink>
      <p class="text-xl text-black text-bold font-bold">Спортивный комплекс</p>
    </div>
    <com_desc
      :imageURL="complexdata.pic"
      :name="complexdata.title"
      :type="complexdata.type"
      :desc="complexdata.desc"
      :shortdesc="complexdata.shortdesc"
    />
    <div class="w-full my-20">
      <img src="/coms/map.png" alt="" />
    </div>
    <div class="my-20 w-full">
      <abon_profile_brief_list :items="complexabons" :reserv="true" />
    </div>
  </div>
</template>
