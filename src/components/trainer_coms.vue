<script setup>
import abon_profile_brief from './abon_profile_brief.vue'

defineProps({
  items: Array
})
</script>

<template>
  <div class="w-1/2">
    <div class="w-1/2 border-b-2 border-black m-auto items-center p-3">
      <p class="text-xl font-bold text-center">Тренировки</p>
    </div>
    <div class="grid grid-cols-2 gap-10 my-10">
      <abon_profile_brief
        v-for="item in items"
        :key="item.id"
        :imageURL="item.pic"
        :name="item.name"
        :type="item.type"
        :price="item.price"
        :duration="item.duration"
        :unit="item.unit"
      />
    </div>
  </div>
</template>
