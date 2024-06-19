<script setup>
import review_view from './review_view.vue'
import review_create from '../components/review_create.vue'

const props = defineProps({
  items: Array,
  type: String,
  id: String
})
</script>

<template>
  <div class="w-4/5 m-auto p-10">
    <h2 class="text-center text-2xl text-black font-bold">Отзывы</h2>
    <div class="my-10">
      <review_view
        v-for="item in items"
        :key="item.id"
        :imageURL="item.pic"
        :name="item.name"
        :surname="item.surname"
        :date="item.date"
        :text="item.text"
        :id="item.id.toString()"
      />
    </div>
    <review_create @createReview="items.push($event)" :type="props.type" :id="props.id" />
  </div>
</template>
