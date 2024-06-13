<script setup lang="ts">
import com_brief_list from '../components/com_brief_list.vue'
import desc_block from '../components/desc_block.vue'
import account_panel from '../components/account_panel.vue'
import footer_ from '../components/footer.vue'
import { ref } from 'vue'
import { onMounted } from 'vue'
import axios from 'axios'
import trainer_brief_list from '../components/trainer_brief_list.vue'

const complexes = ref([])
const trainers = ref([])

const complexescheck = ref([])
const trainerscheck = ref([])
const abonschek = ref([])
const userscheck = ref([])
onMounted(async () => {
  try {
    const { data } = await axios.get('http://127.0.0.1:8000/complexes')
    complexes.value = data
    console.log(complexes.value)
  } catch (error) {
    console.error(error)
  }

  try {
    const { data } = await axios.get('http://127.0.0.1:8000/trainers')
    trainers.value = data
    console.log(trainers.value)
  } catch (error) {
    console.error(error)
  }
})
</script>
<template>
  <div class="flex">
    <div class="w-1/5 bg-slate-700">
      <input class="m-5" type="checkbox" id="checkbox" v-model="checked" />
      <label class="text-white text-sm mx-5" for="checkbox">Комплексы</label><br />
      <input class="m-5" type="checkbox" id="checkbox" v-model="checked" />
      <label class="text-white text-sm mx-5" for="checkbox">Тренеры</label><br />
      <input class="m-5" type="checkbox" id="checkbox" v-model="checked" />
      <label class="text-white text-sm mx-5" for="checkbox">Абонементы</label><br />
      <input class="m-5" type="checkbox" id="checkbox" v-model="checked" />
      <label class="text-white text-sm mx-5" for="checkbox">Пользователи</label><br />
    </div>
    <div class="w-3/4">
      <com_brief_list :items="complexes" />
      <trainer_brief_list :items="trainers" />
      <account_panel />
    </div>
  </div>
</template>
