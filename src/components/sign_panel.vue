<script>
export default {
  name: 'SingIn',
  data() {
    return {
      email: '',
      password: ''
    }
  },

  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn
    }
  },
  created() {
    if (this.loggedIn) {
      this.$router.push('/lk')
    }
  },
  methods: {
    handleLogin(user) {
      this.loading = true

      this.$store.dispatch('auth/login', user).then(
        () => {
          this.$router.push('/lk')
        },
        (error) => {
          this.loading = false
          this.message =
            (error.response && error.response.data && error.response.data.message) ||
            error.message ||
            error.toString()
        }
      )
    }
  }
}
</script>

<template>
  <div class="w-full grid place-items-center">
    <div class="w-2/5 m-auto rounded-2xl p-5">
      <div class="w-1/2 m-auto items-center p-3">
        <h1 class="text-xl font-bold text-center">Личный Кабинет</h1>
      </div>
      <div class="w-1/2 m-auto items center p-3">
        <input
          v-model="email"
          id="user.email"
          class="shadow-xl w-full h-12 my-5 text-sm text-bold border-none rounded-md text-slate-400 p-3 text-left"
          placeholder="Адрес почты"
        />
        <input
          v-model="password"
          id="user.password"
          class="shadow-xl w-full h-12 my-5 text-sm text-bold border-none rounded-md text-slate-400 p-3 text-left"
          name="password"
          placeholder="Пароль"
        />

        <button
          v-on:click="
            handleLogin({
              email: this.email,
              password: this.password
            })
          "
          class="my-5 btn-primary w-full bg-black rounded-xl text-white p-3 font-bold"
        >
          Войти
        </button>
        <RouterLink to="/registration"
          ><p class="my-5 text-xs text-slate-400 text-bold font-bold text-center">
            Зарегистрироваться
          </p>
        </RouterLink>
      </div>
    </div>
  </div>
</template>
