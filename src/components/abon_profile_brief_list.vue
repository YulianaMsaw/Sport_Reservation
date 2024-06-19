<script setup>
import abon_profile_brief from './abon_profile_brief.vue'

const props = defineProps({
  items: Array,
  reserv: Boolean
})

const emit = defineEmits(['changeControl'])
</script>

<template>
  <div class="my-10 flex flex-wrap gap-5 justify-center">
    <abon_profile_brief
      v-for="item in props.items"
      :key="item.id"
      :imageURL="item.pic"
      :trainer="item.trainer"
      :name="item.name"
      :type="item.type"
      :status="item.status"
      :id="item.id"
      :duration="item.duration"
      :unit="item.unit"
      :price="item.price"
      :reserv="props.reserv"
    />
  </div>
</template>
