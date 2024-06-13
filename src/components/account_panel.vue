<template>
  <div class="w-4/5 m-auto rounded-2xl bg-zinc-950 flex p-8 my-40">
    <div class="mb-5">
      <p class="text-2xl text-white font-bold mb-2">Личный Кабинет</p>
      <p class="text-sm text-slate-300">Для упраления абониментами необходимо авторизоваться</p>
      <div class="mt-10 flex gap-10">
        <button class="w-36 bg-white text-black rounded-xl p3 font-bold">
          <RouterLink to="/signin">Вход</RouterLink>
        </button>
        <button class="w-36 border-solid border-2 border-white rounded-xl text-white p-3 font-bold">
          <RouterLink to="/registration">Регистрация</RouterLink>
        </button>
      </div>
    </div>
    <img src="/logo.png" alt="logo" class="m-auto aspect-square w-32" />
  </div>
</template>
