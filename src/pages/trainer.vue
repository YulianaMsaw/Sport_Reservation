<script setup>
import profile_desc from '../components/profile_desc.vue'
import abon_profile_brief_list from '../components/abon_profile_brief_list.vue'
import abon_control from '../components/abon_control.vue'

import trainer_cover from '../components/trainer_cover.vue'
import trainer_desc from '../components/trainer_desc.vue'
import trainer_coms from '../components/trainer_coms.vue'
import { onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useRoute } from 'vue-router'
import { ref } from 'vue'

const trainerdata = ref([])
const trainerabons = ref([])

const route = useRoute()
const router = useRouter()

const checkBool = (x) => {
  if (x == 'true') {
    return true
  } else {
    return false
  }
}

onMounted(async () => {
  try {
    const { data } = await axios.post(
      'http://127.0.0.1:8000/getTrainerData',
      JSON.stringify({ id: route.params.id.toString() }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    trainerdata.value = data
    console.log(trainerdata.value)
  } catch (error) {
    console.error(error)
  }

  try {
    const { data } = await axios.post(
      'http://127.0.0.1:8000/getTrainerAbons',
      JSON.stringify({ id: route.params.id.toString() }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    trainerabons.value = data
    console.log(trainerabons.value)
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div class="w-4/5 m-auto">
    <div class="flex gap-5 items-center my-10">
      <RouterLink to="/"><img src="/back.png" alt="back" class="w-5 h-5" /></RouterLink>
      <p class="text-xl text-black text-bold font-bold">Тренер</p>
    </div>
    <trainer_cover
      :cover="trainerdata.pic"
      :avatar="trainerdata.avatar"
      :checked="checkBool(trainerdata.checked)"
    />
    <div class="flex gap-10 justify-between">
      <trainer_desc
        :name="trainerdata.name"
        :surname="trainerdata.surname"
        :desc="trainerdata.desc"
      />
      <div class="w-1/2">
        <div class="w-1/2 border-b-2 border-black m-auto items-center p-3">
          <p class="text-xl font-bold text-center">Тренировки</p>
        </div>
        <abon_profile_brief_list :items="trainerabons" :reserv="true" />
      </div>
    </div>
  </div>
</template>
