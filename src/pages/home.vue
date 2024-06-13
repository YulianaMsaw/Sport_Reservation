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
  <desc_block />
  <com_brief_list :items="complexes" />
  <trainer_brief_list :items="trainers" />
  <account_panel />
</template>
