<script setup>
import { useStore } from 'vuex'
import { onMounted } from 'vue'
import { ref } from 'vue'
import axios from 'axios'

const emit = defineEmits(['createReview'])

const props = defineProps({
  type: String,
  id: String
})

const store = useStore()
const user = store.state.auth.user
const reviewResponse = ref([])
const userdata = ref([])
const reviewtext = ref([])
const datecreation = ref(new Date().toISOString().slice(0, 10))
let reviewcreating = ref(false)

const createReview = async () => {
  if (reviewtext.value.length > 0) {
    try {
      const { data } = await axios.post(
        'http://127.0.0.1:8000/createReview',
        JSON.stringify({
          user: userdata.value.id,
          date: datecreation.value,
          text: reviewtext.value,
          type: props.type,
          id_objet: props.id
        }),
        {
          headers: { 'Content-Type': 'application/json' }
        }
      )
      reviewcreating.value = !reviewcreating.value
      reviewResponse.value = data

      reviewcreating.value = false
      emit('createReview', {
        name: userdata.value.name,
        surname: userdata.value.surname,
        pic: userdata.value.pic,
        date: datecreation.value,
        text: reviewtext.value,
        type: props.type,
        id_objet: props.id,
        id: reviewResponse.value.id
      })
    } catch (error) {
      console.error(error)
    }
  }
}

onMounted(async () => {
  user.accessToken = user.accessToken.toString()
  user.email = user.email.toString()
  user.password = user.password.toString()
  try {
    const { data } = await axios.post('http://127.0.0.1:8000/getUserData', JSON.stringify(user), {
      headers: { 'Content-Type': 'application/json' }
    })
    userdata.value = data
  } catch (error) {
    console.error(error)
  }
})
</script>
<template>
  <div @click="reviewcreating = !reviewcreating" v-if="!reviewcreating" class="text-center">
    <button class="w-1/3 bg-black rounded-xl text-white p-3 font-bold m-10">Оставить отзыв</button>
  </div>

  <div v-if="reviewcreating" class="w-4/5 m-auto bg-white rounded-2xl p-5 shadow-lg my-10">
    <div class="flex gap-5 items-center border-b h-20 text-center">
      <img
        :src="userdata.pic"
        alt="user_logo"
        class="w-12 h-12 rounded-full object-cover aspect-square"
      />
      <div>
        <p class="font-bold">{{ userdata.name }} {{ userdata.surname }}</p>
        <p class="m-auto">{{ datecreation }}</p>
      </div>
    </div>
    <div class="my-5">
      <textarea
        placeholder="Введите текст отзыва"
        v-model="reviewtext"
        type="text"
        class="w-full p-3 h-80 outline rounded-xl"
      ></textarea>
    </div>
    <div class="text-center">
      <button @click="createReview" class="bg-black rounded-xl text-white p-3 font-bold m-5">
        Отправить
      </button>
    </div>
  </div>
</template>
