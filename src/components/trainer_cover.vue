<script setup>
defineProps({
  cover: String,
  avatar: String,
  checked: Boolean
})
</script>

<template>
  <div class="relative m-auto">
    <img :src="cover" alt="cover" class="w-full rounded-3xl" />
    <div class="absolute bottom-0 left-20">
      <div class="relative">
        <img
          :src="avatar"
          alt="avatar"
          class="w-32 h-32 relative rounded-full top-0 border-4 border-slate-200"
        />
        <div class="absolute bottom-0 right-5">
          <img v-show="checked" src="/checked.png" alt="checked" class="w-5 h-5" />
        </div>
      </div>
    </div>
  </div>
</template>
