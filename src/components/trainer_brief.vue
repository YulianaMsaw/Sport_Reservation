<script setup>
const props = defineProps({
  imageURL: String,
  name: String,
  surname: String,
  checked: Boolean,
  avatar: String,
  desc: String,
  id: String
})

const linkOpen = `/trainer/${props.id}`
</script>

<template>
  <div>
    <RouterLink :to="linkOpen">
      <div
        class="text-center relative bg-white shadow-lg w-56 relative border-slate-100 rounded-2xl p-3 cursor-pointer hover:-translate-y-2 hover:shadow-3xl transition"
      >
        <div class="relative text-center flex justify-center items-center">
          <img
            :src="imageURL"
            alt="trainer_pic"
            class="rounded-full object-fill aspect-square w-40"
          />
        </div>
        <div class="flex gap-5 justify-center items-center my-3">
          <p class="text-left underline font-bold font-sans text-center">
            {{ surname }} {{ name }}
          </p>

          <img v-show="checked" src="/checked.png" alt="checked" class="w-5 h-5" />
        </div>
        <div class="flex justify-between mt-5"></div>
      </div>
    </RouterLink>
  </div>
</template>
