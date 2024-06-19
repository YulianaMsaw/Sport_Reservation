<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
const userdata = ref([])
const store = useStore()
const router = useRouter()
const user = store.state.auth.user
const previewpic = ref([])
const picfile = ref([])

onMounted(async () => {
  if (!user) {
    router.push('/signin')
  } else {
    user.accessToken = user.accessToken.toString()
    user.email = user.email.toString()
    user.password = user.password.toString()
    try {
      const { data } = await axios.post('http://127.0.0.1:8000/getUserData', JSON.stringify(user), {
        headers: { 'Content-Type': 'application/json' }
      })
      userdata.value = data
      console.log(userdata.value.burthday)
      previewpic.value = userdata.value.pic
    } catch (error) {
      console.error(error)
    }
  }
})
const onFileChange = (e) => {
  picfile.value = e.target.files[0]
  previewpic.value = URL.createObjectURL(picfile.value)
}

const handleUpdate = (userdata) => {
  const formData = new FormData()
  formData.append('id', userdata.id)
  formData.append('name', userdata.name)
  formData.append('surname', userdata.surname)
  formData.append('phone', userdata.phone)
  formData.append('burthday', userdata.burthday)
  formData.append('vk', userdata.vk)
  formData.append('insta', userdata.insta)
  formData.append('telegram', userdata.telegram)
  formData.append('email', userdata.email)
  formData.append('pic', picfile.value)

  try {
    const { data } = axios
      .post(
        'http://127.0.0.1:8000/updateProfile',

        formData,
        {
          headers: { 'Content-Type': 'multipart/form-data' }
        }
      )
      .then((response) => {
        router.push('/lk')
      })
    const success = data
  } catch (error) {
    console.error(error)
  }
}
</script>
<template>
  <div class="w-4/5 m-auto">
    <form>
      <div class="flex gap-5 my-5 justify-center">
        <div class="w-1/3">
          <input
            class="my-3 w-full h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center text-slate-950"
            v-model="userdata.name"
            placeholder="Имя"
          />
          <input
            class="my-3 w-full h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center text-slate-950"
            placeholder="Фамилия"
            v-model="userdata.surname"
          />
          <input
            class="my-3 w-full h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center text-slate-950"
            placeholder="Телефон"
            v-model="userdata.phone"
          />
          <input
            class="my-3 w-full h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center text-slate-950"
            placeholder="День рождения"
            type="date"
            v-model="userdata.burthday"
          />
          <input
            class="my-3 w-full h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center text-slate-950"
            placeholder="Адрес электронной почты"
            v-model="userdata.email"
          />
          <input
            class="my-3 w-full h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center text-slate-950"
            placeholder="Пароль"
            v-model="userdata.password"
          />
          <button
            @click="handleUpdate(userdata)"
            class="w-full bg-black rounded-xl text-white p-3 font-bold m-3"
          >
            Обновить данные
          </button>
        </div>
        <div class="w-1/3">
          <img
            :src="previewpic"
            alt="pic"
            class="my-3 w-1/2 rounded-2xl object-cover aspect-square m-auto w-48"
          />
          <input
            @change="onFileChange"
            class="my-3 w-full h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center"
            name="pic"
            type="file"
          />
          <input
            class="my-3 w-full h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center text-slate-950"
            placeholder="Вконтакте"
            v-model="userdata.vk"
          />
          <input
            class="my-3 w-full h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center text-slate-950"
            placeholder="Инстаграм"
            v-model="userdata.insta"
          />
          <input
            class="my-3 w-full h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center text-slate-950"
            placeholder="Телеграм"
            v-model="userdata.telegram"
          />
        </div>
      </div>
    </form>
  </div>
</template>
