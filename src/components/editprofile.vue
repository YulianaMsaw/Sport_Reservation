<script></script>

<template>
  <div class="w-1/2 m-auto">
    <form action="" method="POST" enctype="multipart/form-data">
      <input
        id="fio"
        class="w-4/5 h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center"
        name="fio"
        placeholder="ФИО"
      />
      <input
        id="date"
        class="w-4/5 h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center"
        name="date"
        placeholder="Дата рождения"
      />
      <input
        id="phone"
        class="w-4/5 h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center"
        name="phone"
        placeholder="Телефон"
      />
      <input
        id="logo"
        class="w-4/5 h-12 text-sm bg-gray-100 rounded-xl text-slate-200 p-3 text-center"
        name="logo"
        type="file"
        accept=".jpg, .jpeg, .png"
      />

      <button
        @click="update"
        class="w-1/5 bg-black text-white rounded-xl font-bold my-5 p-3 hover:-translate-y-2 hover:shadow-3xl transition"
      >
        Обновить
      </button>
    </form>
  </div>
</template>
