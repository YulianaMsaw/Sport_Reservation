<template>
  <div class="w-4/5 flex justify-between m-auto">
    <div class="w-1/3 pt-10 pb-20">
      <p class="text-4xl font-bold text-black text-left my-8">Выбирай Спортивную Секцию Для Себя</p>
      <p class="text-sm font-semibold text-slate-400 text-left my-8">
        Гибкий поиск спортивных коплексов, секций и мастер-класов в Таганроге. Удобное управление
        абониментами в личном кабинете
      </p>
      <div class="w-full flex gap-10 my-20 justify-center text-sm">
        <button class="w-2/5 bg-black rounded-xl text-white p-3 font-bold">
          <RouterLink to="/lk"> Личный кабинет </RouterLink>
        </button>
        <button
          class="w-2/5 border-solid border-2 border-black rounded-xl text-black p-3 font-bold"
        >
          Поиск
        </button>
      </div>
    </div>
    <div class="w-1/2 relative pt-10">
      <img src="/desc/desc1.png" alt="desc_pic" class="absolute w-72 h-56 left-0" />
      <img src="/desc/desc2.png" alt="desc_pic" class="absolute w-56 h-56 right-0 top-1/3" />
      <div
        class="absolute flex bg-white w-24 rounded-2xl p-3 my-20 shadow-xl mx-auto mb-auto left-24 top-1/2"
      >
        <button class="text-slate-600 w-1/2">&#8592;</button>
        <span class="text-slate-300">&#448;</span>
        <button class="text-black w-1/2">&#8594;</button>
      </div>
    </div>
  </div>
</template>
