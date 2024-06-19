import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/'

class AuthService {
  login(user) {
    console.log(JSON.stringify(user))
    return axios
      .post(API_URL + 'login', JSON.stringify(user), {
        headers: { 'Content-Type': 'application/json' }
      })
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
    return axios.post(API_URL + 'registrate', {
      email: user.email,
      password: user.password
    })
  }
}

export default new AuthService()
