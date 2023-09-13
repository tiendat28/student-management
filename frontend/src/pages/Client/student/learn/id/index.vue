<template>
    <div class="bg-gray-200 w-full h-screen">
        <div class="px-8 pt-8 pb-4">
            <span class="font-bold text-3xl"><b class="text-teal-400 hover:cursor-pointer" @click="back()">Todo List / </b> Task</span>
        </div>
        <div class="px-[500px] pb-3">
            <div class="p-8 bg-white rounded-lg">
                <form class="relative overflow-x-hidden table-reponsive ">
                    <div class="mb-4">
                        <label class="text-lg">Lớp học</label>
                        <v-select solo hide-details='' v-model="addtodo.subject_id" :items="subject" label="Python" required></v-select>
                    </div>
                    <div class="mb-4">
                        <label class="text-lg">Nhiệm vụ</label>
                        <input type="text" v-model="addtodo.name" placeholder="Viết API">
                    </div>
                    <div class="mb-4">
                        <label class="text-lg">Thời gian</label>
                        <input type="text" v-model="addtodo.time" placeholder="6h sáng">
                    </div>
                    <div class="mb-4">
                        <label class="text-lg">Mức độ</label>
                        <input type="text" v-model="addtodo.level" placeholder="Dễ">
                    </div>
                    <div class="w-full flex justify-end">
                        <v-btn color="#0f766e" dark @click="Save()"> Lưu lại</v-btn>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import router from '@/router/index.ts'
import jwtDecode from 'jwt-decode'
import API_URL_TODOLIST from '@/links/todolist.js'
import API_URL_SUBJECT from '@/links/course.js'
const Assignment = {
    data() {
        return {
            data: [],
            classdata: [],
            subject: [],
            addtodo: {subject_id:'', student_id:'', name:'', time:'', level:''}
        }
    },
    methods: {
        async getAccount(){
            const token = localStorage.getItem('token')
            try{
                const decodedToken = jwtDecode(token)
                this.data = decodedToken
            }catch(error){
                console.log(error)
            }
            if (!token) {
                this.$router.push('/login');
            } else {

            }
        },
        async getCourses() {
            try{
                const student_id = this.data.id
                const {data} =await axios.get(`${API_URL_SUBJECT}${'subject_of_user'}${'/'}${student_id}`)
                this.classdata = data
                this.subject = data[0].subject.map(item => item.name)
            }catch(error){
                console.log(error)
            }
        },
        Save(){
            console.log(this.classdata)
            console.log(this.data)
            const subject = this.classdata.find(item => item.student.user_id === this.data.id).subject
            const subject_id = subject.filter(item => item.name === this.addtodo.subject_id)[0].subject_id
            this.addtodo.subject_id = subject_id
            if(true){
                axios.post(`${API_URL_TODOLIST}`, 
                    {
                        subject_id: this.addtodo.subject_id,
                        student_id: this.classdata[0].student.student_id,
                        name: this.addtodo.name,
                        time: this.addtodo.time,
                        level: this.addtodo.level,
                        status: false
                    }
                )
                .then(response => {
                    this.$router.push({ name: 'S_learn' })
                    alert('Thêm thành công')
                    console.log(response)
                })
            }
        },
        back(){
            router.push({ name: 'S_learn' })
        }
    },
    mounted(){
        this.getAccount()
        this.getCourses()
    }
}
export default Assignment
</script>

<style scoped>
.table-reponsive {
    max-height: calc(100vh - 220px);
}
input {
  width: 100%;
  padding: 10px; 
  border: 1px solid #cbd5e1; 
  border-radius: 5px; 
  font-size: 16px;
}
input:focus {
    border: 2px solid green !important;
}
</style>