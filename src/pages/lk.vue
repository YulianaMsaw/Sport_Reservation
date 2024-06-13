<script>
export default {
  name: 'LK',

  computed: {
    currentUser() {
      return this.$store.state.auth.user
    }
  },

  logout() {
    this.$store.dispatch('userLogout').then(() => {
      this.$router.push('/')
    })
  },

  async mounted() {
    if (!this.currentUser) {
      this.$router.push('/signin')
    }
  }
}
</script>
<script setup>
import profile_desc from '../components/profile_desc.vue'
import axios from 'axios'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { onMounted } from 'vue'
import abon_profile_brief_list from '../components/abon_profile_brief_list.vue'
import abon_control from '../components/abon_control.vue'

const store = useStore()
const router = useRouter()
const userdata = ref([])
const userabons = ref([])
const user = store.state.auth.user

const logout = () => {
  store.dispatch('auth/logout')
  router.push({ name: 'Home' })
}

onMounted(async () => {
  if (!user) {
    router.push('/signin')
  } else {
    console.log(JSON.stringify(user))
    user.accessToken = user.accessToken.toString()
    user.email = user.email.toString()
    user.password = user.password.toString()
    console.log(JSON.stringify(user))
    try {
      const { data } = await axios.post('http://127.0.0.1:8000/getUserData', JSON.stringify(user), {
        headers: { 'Content-Type': 'application/json' }
      })
      userdata.value = data
    } catch (error) {
      console.error(error)
    }
  }
  try {
    const { data } = await axios.post('http://127.0.0.1:8000/getUserAbons', JSON.stringify(user), {
      headers: { 'Content-Type': 'application/json' }
    })
    userabons.value = data
    console.log(userabons.value[0])
  } catch (error) {
    console.error(error)
  }
})
</script>
<template>
  <div class="w-4/5 m-auto">
    <div class="flex gap-5 items-center my-5">
      <RouterLink to="/"> <img src="/back.png" alt="back" class="w-5 h-5" /></RouterLink>
      <p class="text-xl text-black text-bold font-bold">Личный кабинет</p>
    </div>
    <profile_desc
      :name="userdata.name"
      :surname="userdata.surname"
      :phone="userdata.phone"
      :burthday="userdata.burthday"
      :vk="userdata.vk"
      :insta="userdata.insta"
      :telegram="userdata.telegram"
      :email="userdata.email"
      :pic="userdata.pic"
      :aboncount="userabons.length"
    />
    <div class="flex justify-between my-20">
      <div class="w-8/12">
        <h2 class="text-2xl text-slate-300 font-bold">Мои абонементы</h2>
        <abon_profile_brief_list :items="userabons" :reserv="false" />
      </div>
      <abon_control />
    </div>
  </div>
</template>
