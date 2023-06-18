<template>
    <div class="w-full h-screen flex justify-center items-center ">
        <div class="bg-white-400 elevation-4 w-[450px] h-[500px] rounded-xl">
            <h1 class="text-black text-center text-xl py-6 ">Đăng nhập</h1>
            <v-form v-model="valid" class="m-8" >
                <v-text-field v-model="editdata.users" :rules="nameRules" label="Tài khoản"></v-text-field>

                <v-text-field v-model="editdata.password" :rules="nameRules" :type="showPassword ? 'password': 'text'"  label="Mật khẩu"></v-text-field>
    
                <div class="flex justify-between items-center ">
                    <v-checkbox @click="Show()" label="Hiện mật khẩu"></v-checkbox>
                    <h2 class="hover:text-blue-500">Quên mật khẩu</h2>
                </div>
                
                <v-btn class="text-center" @click="submit()"> Đăng nhập </v-btn>

                <h2 class="py-4">Đăng nhập bằng tài khoản khác</h2>

                <div class="flex justify-around">
                    <v-icon class="hover:scale-150" style="color: #1906e7">mdi-facebook</v-icon>
                    <v-icon class="hover:scale-150" style="color: #1da1f2">mdi-twitter</v-icon>
                    <v-icon class="hover:scale-150" style="color: #ba3118">mdi-google</v-icon>
                    <v-icon class="hover:scale-150" style="color: #98e35b">mdi-gmail</v-icon>
                </div>
                
                <v-row class="py-6" justify="center">
                    <v-dialog v-model="dialog" persistent max-width="450px">
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn color="primary" dark v-bind="attrs" v-on="on">Đăng ký</v-btn>
                        </template>
                        <v-card class="w-[450px] h-[500px]">
                            <v-card-title class="text-center">
                                <span class="text-h5">Thông tin</span>
                            </v-card-title>
                            <v-card-text>
                                <v-container>
                                    <v-row>
                                        <v-col cols="12" sm="6" md="6">
                                            <v-text-field label="Tài khoản" :rules="nameRules" v-model="editdata.users" required></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="6">
                                            <v-text-field label="Mật khẩu" :rules="nameRules" v-model="editdata.password" required></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="6">
                                            <v-text-field label="Họ" :rules="nameRules" v-model="editdata.surname" required></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="6">
                                            <v-text-field label="Tên" :rules="nameRules" v-model="editdata.name" required></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="12">
                                            <v-text-field label="Email" :rules="emailRules" v-model="editdata.email" required></v-text-field>
                                        </v-col>
                                    </v-row>
                                </v-container>
                            </v-card-text>
                            <v-card-actions>
                            <div class="flex justify-center">
                                <v-btn color="green darken-1" text @click="post()">Đăng ký</v-btn>
                                <v-btn color="red darken-1" text @click="dialog = false">Đóng</v-btn>
                            </div>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </v-row>
            </v-form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import API_URL from '@/links/index.js'
import router from '@/router/index.ts'
import Home from '@/components/home/home.vue'
const Login = {
    data(){
        return{
            valid: false,
            showPassword:true,
            dialog: false,
            data: [],
            editdata:{id:'', users:'', password:'', surname: '', name: '', email: '', active: 'true'},
            nameRules: [
                v => !!v || 'Trường này bắt buộc',
            ],
            emailRules: [
                v => !!v || 'Trường này bắt buộc',
                v => /.+@.+/.test(v) || 'E-mail không hợp lệ',
            ],
        }
    },
    methods:{
        Show() {
            this.showPassword = !this.showPassword
        },
        async getLogin(){
            try{
                const {data} =await axios.get(`${API_URL}`)
                this.data = data.filter(item => item.active !==false )
                console.log(this.data)
            }catch(error){
                console.log(error)
            }
        },
        submit(){
            const users = this.editdata.users
            const password = this.editdata.password
            const info = this.data.some(function(item){
               return item.users === users && item.password === password 
            })
            const token = this.data.filter(item => item.users === users && item.password === password)[0].token
            if(info){
                localStorage.setItem('token', token)
                setTimeout(() => {
                    localStorage.removeItem('token');
                }, 10000)
                router.push({
                    path: '/home',
                    component: Home,
                })
            }else{
                alert('Tài khoản hoặc mật khẩu không đúng')
            }
        },
        post(){
            const existingUser = this.data.find(
                item => item.users === this.editdata.users || item.email === this.editdata.email
            );

            if (existingUser) {
                alert('Tài khoản hoặc email đã được sử dụng!')
                return
            }
            axios.post(`${API_URL}`,this.editdata)
            .then(response => {
                this.getLogin()
                this.dialog = false
          })
        }
    },
    mounted(){
      this.getLogin()
    }
}
export default Login
</script>

<style></style>