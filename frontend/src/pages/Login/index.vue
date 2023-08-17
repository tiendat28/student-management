<template>
    <div class="w-full h-screen flex flex-col justify-center items-center background">
        <div class="fixed top-0 w-full">
            <router-link to="/" class="flex justify-end px-[300px] py-5">
                <div class="flex text-xl text-white font-normal">
                    <div>
                        <span class="hover:border-cyan-400 hover:border-b-4">Home</span>
                    </div>
                    <div class="px-8">
                        <span class="hover:border-cyan-400 hover:border-b-4">About</span>
                    </div>
                    <div>
                        <span class="hover:border-cyan-400 hover:border-b-4">Course</span>
                    </div>
                    <div class="px-8">
                        <span class="hover:border-cyan-400 hover:border-b-4">Contact</span>
                    </div>
                </div>
            </router-link>
        </div>
        <div class="bg-white-100 backdrop-blur-[3px] elevation-6 w-[480px] h-[600px] rounded-lg rounded-bl-lg ">
            <h1 class="text-[#082f49] text-center text-3xl pt-[50px] font-black">Sign In</h1>
            <v-form v-model="valid" class="m-10" >
                <v-text-field class="py-4" v-model="token.username" :rules="nameRules" label="Username"></v-text-field>

                <v-text-field v-model="token.password" :rules="nameRules" :type="showPassword ? 'password': 'text'"  label="Password"></v-text-field>
    
                <div class="flex justify-between items-center py-5">
                    <v-checkbox style="font-size: 14px;" @click="Show()" label="Show password"></v-checkbox>
                    <h2 class="text-sm hover:text-blue-500">Forget password?</h2>
                </div>

                <div class="flex justify-center">
                    <v-btn style="height: 50px;" class="text-center rounded-full w-[400px]" dark color="#0c4a6e" @click="submit()"> Sign in </v-btn>
                </div>
                
                <h2 class="py-8">Sign in with another account</h2>

                <div class="flex justify-around">
                    <v-icon :size="35" class="hover:scale-150" style="color: #1906e7">mdi-facebook</v-icon>
                    <v-icon :size="35" class="hover:scale-150" style="color: #1da1f2">mdi-twitter</v-icon>
                    <v-icon :size="35" class="hover:scale-150" style="color: #ba3118">mdi-google</v-icon>
                    <v-icon :size="35" class="hover:scale-150" style="color: #98e35b">mdi-gmail</v-icon>
                </div>
            </v-form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import API_URL_USER from '@/links/user.js'
import API_URL_STUDENT from '@/links/student.js'
import API_URL_TEACHER from '@/links/teacher.js'
import router from '@/router/index.ts'
const Login = {
    data(){
        return{
            valid: false,
            showPassword:true,
            dialog: false,
            data: [],
            items: ['Manager', 'Teacher', 'Student'],
            editdata:{id:'', username:'', password:'', first_name: '', last_name: '', phone: '', address: '', email: '', sex: '', role:'', active: 'true'},
            token:{username: '', password:''},
            nameRules: [
                v => !!v || 'This field is required',
            ],
            emailRules: [
                v => !!v || 'This field is required',
                v => /.+@.+/.test(v) || 'Invalid email',
            ],
        }
    },
    methods:{
        Show() {
            this.showPassword = !this.showPassword
        },
        async getLogin(){
            try{
                const {data} =await axios.get(`${API_URL_USER}`)
                this.data = data.filter(item => item.active !==false )
            }catch(error){
                console.log(error)
            }
        },
        submit(){
            const username = this.token.username
            const password = this.token.password
            const info = this.data.some(function(item){
               return item.username === username && item.password === password 
            })
            console.log(info)
            if(info){
                axios.post(`http://127.0.0.1:8000/token/?username=${username}&password=${password}`,this.token)
                .then(response => {
                    const userRole = this.data.find(item => item.username === username).role
                    if (userRole === 'Manager') {
                        router.push('/admin/member');
                    } else if (userRole === 'Teacher') {
                        router.push('/T_home/homepage');
                    } else {
                        router.push('/S_home/homepage')
                    }
                    localStorage.setItem('token', response.data)
                })
            }else{
                alert('Incorrect account or password')
            }
        },
        post(){
            const existingUser = this.data.find(
                item => item.username === this.editdata.username || item.email === this.editdata.email
            )
            if (existingUser) {
                alert('Account or email already in use!')
                return
            }
            else if (!existingUser)
                if (this.editdata.role === 'Student') {
                    axios.post(`${API_URL_STUDENT}`, this.editdata)
                    .then(response => {
                        this.dialog = false
                    })
                    .catch(error => {
                    })
                } else if (this.editdata.role === 'Teacher') {
                    axios.post(`${API_URL_TEACHER}`, this.editdata)
                    .then(response => {
                        console.log(response)
                        this.dialog = false
                    })
                    .catch(error => {
                    })
                }
        }
    },
    mounted(){
      this.getLogin()
    }
}
export default Login
</script>

<style scoped>
.background {
    background: url('@/assets/background1.jpg');
    background-size: cover;
    background-position: center;
}
</style>