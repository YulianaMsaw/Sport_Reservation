<script setup>
import profile_desc from '../components/profile_desc.vue'
import axios from 'axios'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { ref, computed } from 'vue'
import { onMounted } from 'vue'
import abon_profile_brief_list from '../components/abon_profile_brief_list.vue'
import abon_control from '../components/abon_control.vue'

const store = useStore()
const router = useRouter()
const userdata = ref([])
const controldata = ref([])
const userabons = ref([])
const requestabons = ref([])
const user = store.state.auth.user

const getRequests = async () => {
  try {
    const { data } = await axios.post(
      'http://127.0.0.1:8000/getRequestsAbons',
      JSON.stringify(user),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    requestabons.value = data
  } catch (error) {
    console.error(error)
  }
}
const logout = () => {
  store.dispatch('auth/logout')
  router.push({ name: 'Home' })
}

const getControl = async () => {
  try {
    const { data } = await axios.post(
      'http://127.0.0.1:8000/getControlData',
      JSON.stringify(user),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    )
    controldata.value = data
  } catch (error) {
    console.error(error)
  }
}
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
    } catch (error) {
      console.error(error)
    }
    getControl()
    if (userdata.value.acctype === 'company') {
    }
  }
  try {
    const { data } = await axios.post('http://127.0.0.1:8000/getUserAbons', JSON.stringify(user), {
      headers: { 'Content-Type': 'application/json' }
    })
    userabons.value = data
  } catch (error) {
    console.error(error)
  }
})

const controlStatus = ref('all')
const queryAbons = computed(() => {
  let p = userabons.value
  if (controlStatus.value === 'all') {
    return p
  } else {
    p = p.filter((item) => {
      return item.status.indexOf(controlStatus.value) !== -1
    })

    return p
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
        <abon_profile_brief_list @changeControl="getControl" :items="queryAbons" :reserv="false" />
        <div v-if="userdata.acctype === 'company'">
          <h2 class="text-2xl text-slate-300 font-bold">Мои абонементы</h2>
          <abon_profile_brief_list
            @changeControl="getControl"
            :items="requestabons"
            :reserv="false"
          />
        </div>
      </div>
      <abon_control
        @all="queryAbons.value = 'all'"
        @active="queryAbons.value = 'active'"
        @freezed="queryAbons.value = 'freezed'"
        @ended="queryAbons.value = 'ended'"
        :all="controldata.allcount"
        :active="controldata.activecount"
        :freezed="controldata.freezedcount"
        :ended="controldata.endedcount"
      />
    </div>
  </div>
</template>
