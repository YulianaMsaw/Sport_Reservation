<script setup>
import abon_folder from './abon_folder.vue'

defineProps({
  all: Number,
  active: Number,
  freezed: Number,
  ended: Number
})
const emit = defineEmits(['all', 'active', 'freezed', 'ended'])
</script>
<template>
  <div class="w-1/3 bg-white shadow-lg border-slate-100 rounded-2xl p-5">
    <p class="my-5 text-xl text-black text-bold font-bold">Управление абонементами</p>
    <abon_folder
      @click="emit('all')"
      imageURL="/users/abon_folders/kostikovayuliana/1.png"
      title="Все абонементы"
      :count="all"
    />
    <abon_folder
      @click="emit('active')"
      imageURL="/users/abon_folders/kostikovayuliana/2.png"
      title="Действующие абонементы"
      :count="active"
    />
    <abon_folder
      @click="emit('freezed')"
      imageURL="/users/abon_folders/kostikovayuliana/1.png"
      title="Замороженные абонементы"
      :count="freezed"
    />
    <abon_folder
      @click="emit('ended')"
      imageURL="/users/abon_folders/kostikovayuliana/2.png"
      title="Архив"
      :count="ended"
    />
    <p class="my-5 text-xl text-black text-bold font-bold">Добавить папку</p>
    <p class="my-5 text-sm text-slate-400 text-bold">
      Придумайте название папки и выберите в выпадающем списке какие абонементы в нее поместить
    </p>
    <input
      class="w-full my-5 text-sm text-bold border-solid border-2 border-black rounded-xl text-slate-400 p-3 text-center"
      name="search"
      placeholder="Наименование Группы"
    />
    <button class="w-full bg-black rounded-xl text-white p-3 font-bold">Создать</button>
  </div>
</template>
