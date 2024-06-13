<script setup>
const props = defineProps({
  imageURL: String,
  title: String,
  type: String,
  id: String
})

const linkOpen = `/complex/${props.id}`
</script>

<template>
  <div>
    <div
      class="relative bg-white shadow-lg w-56 relative border-slate-100 rounded-2xl p-3 cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition"
    >
      <img :src="imageURL" alt="sec_pic" class="rounded-2xl object-fill aspect-square" />
      <p class="mt-2 text-left underline font-bold font-sans">{{ title }}</p>
      <div class="flex justify-between mt-5">
        <div>
          <p class="font-bold text-slate-300 text-sm">{{ type }}</p>
        </div>
        <div>
          <RouterLink :to="linkOpen">
            <button
              class="w-24 h-10 bg-zinc-950 rounded-lg text-white py-1.5 text-sm text-center font-semibold"
            >
              Подробнее
            </button>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>
