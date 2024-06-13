<script setup>
import abon_view from './abon_view.vue'
import { ref } from 'vue'
import { onMounted } from 'vue'
import axios from 'axios'
import { useStore } from 'vuex'

const store = useStore()
const user = store.state.auth.user

const ReservAbon = () => {
  try {
    console.log(idabon)
    const { data } = axios.post(
      'http://127.0.0.1:8000/reservabon',
      JSON.stringify({
        accessToken: user.accessToken,
        phone: user.phone,
        password: user.password,
        id: idabon
      }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
  } catch (error) {
    console.error(error)
  }
}

const trainerdata = ref([])
const complexdata = ref([])
onMounted(async () => {
  user.accessToken = user.accessToken.toString()
  user.email = user.email.toString()
  user.password = user.password.toString()

  try {
    console.log(props.id.toString())
    const { data } = await axios.post(
      'http://127.0.0.1:8000/getTrainerFullNameById',
      JSON.stringify({ id: props.trainer }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    trainerdata.value = data
    console.log('4365464654654645654')
    console.log(props.reserv)
  } catch (error) {
    console.error(error)
  }

  try {
    console.log(props.id.toString())
    const { data } = await axios.post(
      'http://127.0.0.1:8000/getComplexFullNameById',
      JSON.stringify({ id: props.complex }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    complexdata.value = data
    console.log('4365464654654645654')
    console.log(props.reserv)
  } catch (error) {
    console.error(error)
  }
})

let ShowModal = ref(false)

const props = defineProps({
  imageURL: String,
  trainer: String,
  name: String,
  type: String,
  id: Number,
  price: Number,
  duration: Number,
  unit: String,
  status: String,
  reserv: Boolean,
  complex: String
})
const idabon = props.id
const reserv = props.reserv
</script>

<template>
  <abon_view
    :id="id"
    :status="status"
    v-if="ShowModal"
    @closeabonview="ShowModal = !ShowModal"
    :reserv="reserv"
  />
  <div>
    <div
      @click="(ShowModal = !ShowModal), console.log(ShowModal)"
      class="h-88 bg-white shadow-lg w-56 relative border-slate-100 rounded-2xl p-3 cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition"
    >
      <img :src="imageURL" alt="abon_pic" class="rounded-2xl object-fill aspect-square" />
      <div class="my-2 flex gap-5 items-center">
        <p class="text-left text-bold font-sans">
          {{ trainerdata.name }} {{ trainerdata.surname }}
        </p>
      </div>
      <div class="flex flex-col justify-end">
        <p class="mt-1 text-left font-bold font-sans justify-self-end">{{ name }}</p>
        <div v-if="!props.reserv">
          <div
            v-if="status == 'active'"
            class="w-1/2 bg-lime-500 rounded-xl text-sm text-white p-1 font-bold my-1 hover:-translate-y-2 hover:shadow-3xl transition"
          >
            <p class="text-sm text-white font-bold m-1 text-center">Активен</p>
          </div>
          <div
            v-if="status == 'freezed'"
            class="w-2/3 bg-cyan-500 rounded-xl text-sm text-white p-1 font-bold my-1 hover:-translate-y-2 hover:shadow-3xl transition"
          >
            <p class="text-sm text-white font-bold m-1 text-center">Заморожен</p>
          </div>
          <div
            v-if="status == 'wait'"
            class="w-2/3 bg-amber-600 rounded-xl text-sm text-white p-1 font-bold my-1 hover:-translate-y-2 hover:shadow-3xl transition"
          >
            <p class="text-sm text-white font-bold m-1 text-center">В ожидании</p>
          </div>
          <div
            v-if="status == 'ended'"
            class="w-1/2 bg-rose-800 rounded-xl text-sm text-white p-1 font-bold my-1 hover:-translate-y-2 hover:shadow-3xl transition"
          >
            <p class="text-sm text-white font-bold m-1 text-center">Истек</p>
          </div>
        </div>
        <div v-if="props.reserv">
          <div class="flex justify-center gap-3 m-1">
            <div
              class="text-center bg-slate-100 rounded-xl p-2 cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition"
            >
              <p class="text-xs">{{ duration }} {{ unit }}</p>
            </div>
            <div
              class="bg-slate-100 rounded-xl p-2 cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition"
            >
              <p class="text-xs">{{ price }} руб.</p>
            </div>
          </div>
          <button
            @click="ReservAbon"
            class="w-full bg-black rounded-xl text-white p-1 font-bold my-1 cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition"
          >
            Записаться
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
