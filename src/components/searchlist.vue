<script setup lang="ts">
import com_brief_list_search from '../components/com_brief_list_search.vue'
import desc_block from '../components/desc_block.vue'
import account_panel from '../components/account_panel.vue'
import footer_ from '../components/footer.vue'
import { ref, computed } from 'vue'
import { onMounted } from 'vue'
import axios from 'axios'
import trainer_brief_list_search from '../components/trainer_brief_list_search.vue'
import abon_profile_brief_list_search from '../components/abon_profile_brief_list_search.vue'
import { useRouter } from 'vue-router'

const query = ref([])
const router = useRouter()

const complexescheck = ref([])
const trainerscheck = ref([])
const abonschek = ref([])
const price_min = ref(0)
const price_max = ref(0)
const duration_min = ref(0)
const duration_max = ref(0)
const unit = ref('')

onMounted(async () => {
  query.value = router.currentRoute.value.query.search
})
</script>
<template>
  <div class="flex">
    <div class="w-1/5 bg-slate-700 items-center">
      <p class="text-2xl text-slate-200 font-bold m-5 text-center">Абонементы</p>
      <div class="flex gap-5 my-5 mx-5 items-center">
        <p class="text-white text-sm">Цена от</p>
        <input v-model="price_min" type="number" class="w-12 p-1 rounded-xl bg-slate-200" />
      </div>
      <div class="flex gap-5 my-5 mx-5 items-center">
        <p class="text-white text-sm">Цена до</p>
        <input v-model="price_max" type="number" class="w-12 p-1 rounded-xl bg-slate-200" />
      </div>
      <div class="flex gap-5 my-5 mx-5 items-center">
        <p class="text-white text-sm">Длительность от</p>
        <input v-model="duration_min" type="number" class="w-12 p-1 rounded-xl bg-slate-200" />
      </div>
      <div class="flex gap-5 my-5 mx-5 items-center">
        <p class="text-white text-sm">Длительность до</p>
        <input v-model="duration_max" type="number" class="w-12 p-1 rounded-xl bg-slate-200" />
      </div>
      <div class="text-center flex gap-5 justify-center items-center mx-5">
        <p class="text-white text-sm">Измерение:</p>
        <select v-model="unit" class="w-1/2 bg-slate-200 rounded-xl text-black p-3 font-bold m-5">
          <option value="любое">Любое</option>
          <option value="трен">Тренировка</option>
          <option value="нед">Неделя</option>
          <option value="мес">Месяц</option>
        </select>
      </div>
    </div>
    <div class="w-4/5">
      <com_brief_list_search :searchquery="query" />
      <trainer_brief_list_search :searchquery="query" />
      <abon_profile_brief_list_search
        :searchquery="query"
        :price_min="price_min"
        :price_max="price_max"
        :duration_min="duration_min"
        :duration_max="duration_max"
        :unit="unit"
      />
    </div>
  </div>
</template>
