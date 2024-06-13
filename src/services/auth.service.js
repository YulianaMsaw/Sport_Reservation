import axios from 'axios'

const API_URL = 'http://localhost:3000/'

class AuthService {
  login(user) {
    console.log(JSON.stringify({ login: user.email, password: user.password }))
    return axios
      .post(
        API_URL + 'auth/login',
        JSON.stringify({ login: user.email, password: user.password }),
        {
          headers: { 'Content-Type': 'application/json' }
        }
      )
      .then((response) => {
        if (response.data.accessToken) {
          localStorage.setItem('user', JSON.stringify(response.data))
        }

        return response.data
      })
  }

  logout() {
    localStorage.removeItem('user')
  }

  register(user) {
    return axios.post(API_URL + 'signup', {
      email: user.email,
      password: user.password
    })
  }
}

export default new AuthService()
