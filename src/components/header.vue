<script setup>
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
const store = useStore()
const router = useRouter()
const logout = () => {
  store.dispatch('auth/logout')
  router.push({ name: 'Home' })
}
</script>
<template>
  <div class="bg-white w-4/5 m-auto">
    <header class="flex py-10 items-center gap-20">
      <div>
        <RouterLink to="/"> <img src="/logo.png" alt="logo" class="w-15 h-15" /></RouterLink>
      </div>

      <div class="w-full flex gap-10 uppercase text-bold items-center relative">
        <img src="/search.png" alt="search" class="absolute wh-5 left-3 top-3" />
        <input
          class="w-4/5 h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center"
          name="search"
          placeholder="Поиск комплексов"
        />

        <button
          v-if="$route.path != '/lk'"
          class="w-1/5 bg-black h-12 text-sm rounded-xl text-center text-white px-3 font-bold revealUp"
        >
          <RouterLink to="/lk">Личный кабинет</RouterLink>
        </button>

        <button
          v-else
          class="w-1/5 bg-black h-12 text-sm rounded-xl text-center text-white px-3 font-bold ml-auto"
          @click="logout"
        >
          Выход
        </button>
      </div>
    </header>
  </div>
</template>
