<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { onMounted } from 'vue'
import { useStore } from 'vuex'

const store = useStore()
const user = store.state.auth.user
const props = defineProps({
  id: String,
  status: String,
  reserv: Boolean
})
const idabon = props.id
const abondata = ref([])
const trainerdata = ref([])
const complexdata = ref([])
const owndata = ref([])
const show = ref([])
const linkOpenComplex = ref([])
const linkOpenTrainer = ref([])
const abonstatus = ref([])
abonstatus.value = props.status
const emit = defineEmits(['closeabonview'])
const closeModal = () => {
  emit('closeabonview')
}

const ReservAbon = () => {
  try {
    const { data } = axios.post(
      'http://127.0.0.1:8000/reservabon',
      JSON.stringify({
        accessToken: user.accessToken.toString(),
        phone: user.phone.toString(),
        password: user.password.toString(),
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

const FreezeAbon = async () => {
  try {
    const { data } = axios.post(
      'http://127.0.0.1:8000/freezeabon',
      JSON.stringify({
        accessToken: user.accessToken.toString(),
        phone: user.phone.toString(),
        password: user.password.toString(),
        id: idabon
      }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    abonstatus.value = 'freezed'
  } catch (error) {
    console.error(error)
  }
}

const UnFreezeAbon = () => {
  try {
    console.log(idabon)
    const { data } = axios.post(
      'http://127.0.0.1:8000/unfreezeabon',
      JSON.stringify({
        accessToken: user.accessToken.toString(),
        phone: user.phone.toString(),
        password: user.password.toString(),
        id: idabon
      }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    abonstatus.value = 'active'
  } catch (error) {
    console.error(error)
  }
}

const ExtendAbon = () => {
  try {
    console.log(idabon)
    const { data } = axios.post(
      'http://127.0.0.1:8000/extendabon',
      JSON.stringify({
        accessToken: user.accessToken.toString(),
        phone: user.phone.toString(),
        password: user.password.toString(),
        id: idabon
      }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    abonstatus.value = 'active'
  } catch (error) {
    console.error(error)
  }
}
onMounted(async () => {
  try {
    const { data } = await axios.post(
      'http://127.0.0.1:8000/getAbonData',
      JSON.stringify({ id: props.id }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    abondata.value = data
  } catch (error) {
    console.error(error)
  }
  try {
    const { data } = await axios.post(
      'http://127.0.0.1:8000/getTrainerData',
      JSON.stringify({ id: abondata.value.trainer }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    trainerdata.value = data
    linkOpenTrainer.value = `/trainer/${trainerdata.value.id}`
  } catch (error) {
    console.error(error)
  }
  try {
    const { data } = await axios.post(
      'http://127.0.0.1:8000/getComplexData',
      JSON.stringify({ id: abondata.value.complex }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    complexdata.value = data
    linkOpenComplex.value = `/complex/${complexdata.value.id}`
  } catch (error) {
    console.error(error)
  }
})
</script>
<template>
  <div
    class="w-full z-10 fixed inset-0 bg-black bg-opacity-80 grid place-items-center overflow-auto"
    @click.self="closeModal"
  >
    <div class="w-3/4 m-auto flex items-center justify-center relative rounded-2xl bg-white p-5">
      <div
        class="w-5 h-5 cursor-pointer absolute top-5 right-5 bg-black rounded-full opacity-90 text-center items-center flex justify-center flex"
        @click="closeModal"
      >
        <span class="text-white">X</span>
      </div>
      <div class="flex gap-10 justify-between">
        <div class="w-2/5">
          <img
            :src="abondata.pic"
            alt="abon_view"
            class="w-full rounded-2xl object-cover aspect-square relative cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition"
          />
          <p class="text-2xl text-black font-bold m-5 underline text-center">{{ abondata.name }}</p>
          <div class="flex justify-center gap-5 m-5">
            <div
              class="bg-slate-100 rounded-2xl p-3 cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition"
            >
              <p>{{ abondata.duration }} {{ abondata.unit }}</p>
            </div>
            <div
              class="bg-slate-100 rounded-2xl p-3 cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition"
            >
              <p>{{ abondata.price }} руб.</p>
            </div>
          </div>
          <div v-if="!props.reserv">
            <div v-if="abonstatus == 'active'" class="my-5">
              <div
                class="w-full bg-lime-500 rounded-xl text-white p-3 font-bold my-5 hover:-translate-y-2 hover:shadow-3xl transition"
              >
                <p class="text-xl text-white font-bold m-3 text-center">Активен</p>
              </div>
              <button
                @click="FreezeAbon"
                class="w-full bg-black text-white rounded-xl font-bold my-5 p-3 hover:-translate-y-2 hover:shadow-3xl transition"
              >
                Заморозить
              </button>
              <button
                class="w-full bg-black text-white rounded-xl font-bold my-5 p-3 hover:-translate-y-2 hover:shadow-3xl transition"
              >
                Отменить
              </button>
            </div>
            <div v-if="abonstatus == 'freezed'">
              <div
                class="w-full bg-cyan-500 rounded-xl text-white p-3 font-bold my-5 hover:-translate-y-2 hover:shadow-3xl transition"
              >
                <p class="text-xl text-white font-bold m-3 text-center">Заморожен</p>
              </div>
              <button
                @click="UnFreezeAbon"
                class="w-full bg-black text-white rounded-xl font-bold my-5 p-3 hover:-translate-y-2 hover:shadow-3xl transition"
              >
                Разморозить
              </button>
              <button
                class="w-full bg-black text-white rounded-xl font-bold my-5 p-3 hover:-translate-y-2 hover:shadow-3xl transition"
              >
                Отменить
              </button>
            </div>
            <div v-if="abonstatus == 'wait'">
              <div
                class="w-full bg-amber-600 rounded-xl text-white p-3 font-bold my-5 hover:-translate-y-2 hover:shadow-3xl transition"
              >
                <p class="text-xl text-white font-bold m-3 text-center">В ожидании</p>
              </div>
              <button
                class="w-full bg-black text-white rounded-xl font-bold my-5 p-3 hover:-translate-y-2 hover:shadow-3xl transition"
              >
                Отменить
              </button>
            </div>
            <div v-if="abonstatus == 'ended'">
              <div
                class="w-full bg-rose-800 rounded-xl text-white p-3 font-bold my-5 hover:-translate-y-2 hover:shadow-3xl transition"
              >
                <p class="text-xl text-white font-bold m-3 text-center">Истек</p>
              </div>
              <button
                @click="ExtendAbon"
                class="w-full bg-black text-white rounded-xl font-bold my-5 p-3 hover:-translate-y-2 hover:shadow-3xl transition"
              >
                Продлить
              </button>
              <button
                class="w-full bg-black text-white rounded-xl font-bold my-5 p-3 hover:-translate-y-2 hover:shadow-3xl transition"
              >
                Удалить
              </button>
            </div>
          </div>
          <button
            @click="ReservAbon"
            v-if="props.reserv"
            class="w-full bg-black rounded-xl text-white p-3 font-bold my-5 cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition"
          >
            Записаться
          </button>
        </div>
        <div class="w-2/5">
          <div>
            <p class="text-2xl text-black font-bold m-3 underline text-center">Описание</p>
            <p>
              {{ abondata.desc }}
            </p>
          </div>
          <div>
            <p class="text-2xl text-black font-bold m-3 underline text-center">
              Спортиный Комплекс
            </p>
            <RouterLink :to="linkOpenComplex"
              ><div
                class="flex gap-5 justify-center items-center my-5 bg-white shadow-lg border-slate-100 rounded-2xl cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition p-5"
              >
                <img
                  :src="complexdata.pic"
                  alt="complex"
                  class="w-12 h-12 object-cover rounded-full"
                />
                <p class="font-bold text-sm">{{ complexdata.title }}</p>
              </div></RouterLink
            >
            <div class="text-center">
              <p class="text-sm text-slate-400">{{ complexdata.adress }}</p>
            </div>
          </div>
        </div>
        <div class="w-2/5">
          <p class="text-2xl text-black font-bold m-3 underline text-center">Тренер</p>
          <RouterLink :to="linkOpenTrainer"
            ><div
              class="p-5 flex gap-5 justify-between items-center my-5 bg-white shadow-lg border-slate-100 rounded-2xl cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition"
            >
              <img
                :src="trainerdata.avatar"
                alt="trainer"
                class="w-12 h-12 object-cover rounded-full"
              />
              <p>{{ trainerdata.name }} {{ trainerdata.surname }}</p>
              <img
                v-show="trainerdata.checked"
                src="/checked.png"
                alt="checked"
                class="w-5 h-5 object-cover"
              />
            </div>
          </RouterLink>
          <div>
            <p class="text-2xl text-black font-bold m-3 underline text-center">Расписание</p>
            <div>
              <p>Понедельник</p>
              <p>12:00 - 14:00</p>
            </div>
            <div>
              <p>Среда</p>
              <p>12:00 - 14:00</p>
            </div>
            <div>
              <p>Пятница</p>
              <p>12:00 - 14:00</p>
            </div>
          </div>
          <p
            v-if="trainerdata.individual"
            class="text-2xl text-black font-bold m-3 underline text-center"
          >
            Индивидуальные тренировки
          </p>
          <p
            v-else="trainerdata.individual"
            class="text-2xl text-black font-bold m-3 underline text-center"
          >
            Групповые тренировки
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
