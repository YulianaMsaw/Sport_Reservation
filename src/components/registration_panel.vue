<script>
import { Form, Field, ErrorMessage } from 'vee-validate'
import * as yup from 'yup'
import axios from 'axios'

export default {
  name: 'Register',
  components: {
    Form,
    Field,
    ErrorMessage
  },

  data() {
    const ConfCode = ''
    const schema = yup.object().shape({
      email: yup.string().required('Необходимо заполнить почту!').email('Неверный формат почты!'),
      password: yup
        .string()
        .required('Необходимо заполнить пароль!')
        .min(6, 'Пароль должен содержать не менее 6 символов!')
        .max(40, 'Пароль должен содержать не более 40 символов!'),
      passwordConfirmation: yup
        .string()
        .required()
        .oneOf([yup.ref('password')], 'Пароли не совпадают!'),
      ConfirmationCode: yup
        .string()
        .required('Необходимо ввести код подтверждения!')
        .oneOf([ConfCode], 'Неверный код подтверждения!')
    })

    return {
      successful: false,
      loading: false,
      message: '',
      schema,
      ConfCode
    }
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn
    }
  },
  mounted() {
    if (this.loggedIn) {
      this.$router.push('/lk')
    }
  },
  methods: {
    async sendCode() {
      if (this.email !== '' && this.email) {
        try {
          const data = await axios
            .post('http://127.0.0.1:8000/sendcode', JSON.stringify({ email: this.email }), {
              headers: { 'Content-Type': 'application/json' }
            })
            .then((response) => {
              this.$data.schema.fields.ConfirmationCode = yup
                .string()
                .required('Необходимо ввести код подтверждения!')
                .oneOf([response.data.code], 'Неверный код подтверждения!')
            })
        } catch (error) {
          console.error(error)
        }
      } else {
        const input = document.getElementById('user.email')
        input.focus()
      }
    },
    handleRegister(user) {
      this.message = ''
      this.successful = false
      this.loading = true

      this.$store.dispatch('auth/register', user).then(
        (data) => {
          this.successful = true
          this.loading = false
        },
        (error) => {
          this.message =
            (error.response && error.response.data && error.response.data.message) ||
            error.message ||
            error.toString()
          this.successful = false
          this.loading = false
        }
      )
      this.$store.dispatch('auth/login', user).then(
        (data) => {
          this.$router.push('/lk')
        },
        (error) => {
          this.message =
            (error.response && error.response.data && error.response.data.message) ||
            error.message ||
            error.toString()
          this.successful = false
          this.loading = false
        }
      )
    }
  }
}
</script>

<template>
  <div class="w-full grid place-items-center">
    <div class="w-1/3 m-auto rounded-2xl p-5">
      <div class="w-1/2 m-auto items-center p-3">
        <h1 class="text-xl font-bold text-center">Регистрация</h1>
      </div>
      <Form @submit="handleRegister" :validation-schema="schema">
        <div v-if="!successful">
          <div class="w-full m-auto items center p-3">
            <div class="form-group">
              <Field
                name="email"
                v-model="email"
                id="user.email"
                class="shadow-xl w-full h-12 my-5 text-sm text-bold border-none rounded-md text-slate-400 p-3 text-left"
                placeholder="Адрес почты"
              />
            </div>
            <ErrorMessage as="div" name="email" v-slot="{ message }">
              <p>{{ message }}</p>
            </ErrorMessage>
            <div class="form-group">
              <Field
                name="password"
                v-model="password"
                id="user.password"
                class="shadow-xl w-full h-12 my-5 text-sm text-bold border-none rounded-md text-slate-400 p-3 text-left"
                placeholder="Пароль"
              />
            </div>
            <ErrorMessage name="password" as="p" />
            <div class="form-group">
              <Field
                name="passwordConfirmation"
                v-model="passwordConfirmation"
                class="shadow-xl w-full h-12 my-5 text-sm text-bold border-none rounded-md text-slate-400 p-3 text-left"
                placeholder="Подтверждение пароля"
              />
            </div>
            <ErrorMessage as="div" name="passwordConfirmation" v-slot="{ message }">
              <p>{{ message }}</p>
            </ErrorMessage>
            <div class="form-group flex gap-3 items-center">
              <Field
                name="ConfirmationCode"
                v-model="ConfirmationCode"
                class="shadow-xl w-full h-12 my-5 text-sm text-bold border-none rounded-md text-slate-400 p-3 text-left"
                placeholder="Код подтверждения"
              />
              <button
                type="button"
                class="w-1/4 bg-black rounded-xl text-white p-1 font-bold h-12"
                @click="sendCode"
              >
                <p class="text-white text-xs">Отправить</p>
              </button>
            </div>
            <ErrorMessage as="div" name="ConfirmationCode" v-slot="{ message }">
              <p>{{ message }}</p>
            </ErrorMessage>

            <div class="form-group">
              <button
                type="submit"
                v-on:click="
                  handleRegister({
                    email: this.email,
                    password: this.password,
                    acc_type: this.acc_type
                  })
                "
                class="my-5 btn-primary w-full bg-black rounded-xl text-white p-3 font-bold"
                :disabled="loading"
              >
                <span v-show="loading" class="spinner-border spinner-border-sm"></span>
                Зарегистрироваться
              </button>
            </div>
            <RouterLink to="/signin">
              <p class="my-5 text-xs text-slate-400 text-bold font-bold text-center">Войти</p>
            </RouterLink>
          </div>
        </div>
      </Form>
    </div>
  </div>
</template>
