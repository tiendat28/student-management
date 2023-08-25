<template>
    <div class="bg-gray-200 w-full h-full">
        <div class="px-8 pt-8 pb-4">
            <span class="font-bold text-3xl"><b class="text-teal-400 hover:cursor-pointer" @click="back()">Ngân hàng đề / </b> Câu hỏi</span>
        </div>
        <div class="px-[500px] pb-3">
            <div class="p-8 bg-white rounded-lg">
                <form class="relative overflow-x-hidden table-reponsive ">
                    <div class="mb-4">
                        <label class="text-lg">Câu hỏi</label>
                        <input v-model="addQuestions.q_text" type="text" placeholder="Nhập câu hỏi">
                    </div>
                    <div class="mb-4">
                        <label class="text-lg">Lựa chọn 1</label>
                        <input v-model="addQuestions.option1" type="text" placeholder="Nhập lựa chọn 1">
                    </div>
                    <div class="mb-4">
                        <label class="text-lg">Lựa chọn 2</label>
                        <input v-model="addQuestions.option2" type="text" placeholder="Nhập lựa chọn 2">
                    </div>
                    <div class="mb-4">
                        <label class="text-lg">Lựa chọn 3</label>
                        <input v-model="addQuestions.option3" type="text" placeholder="Nhập lựa chọn 3">
                    </div>
                    <div class="mb-4">
                        <label class="text-lg">Lựa chọn 4</label>
                        <input v-model="addQuestions.option4" type="text" placeholder="Nhập lựa chọn 4">
                    </div>
                    <div class="mb-4">
                        <label class="text-lg">Đáp án</label>
                        <input v-model="addQuestions.correct_answer" type="text" placeholder="Nhập đáp án">
                    </div>
                    <div class="mb-4">
                        <label class="text-lg">Thời gian bắt đầu</label>
                        <input v-model="addQuestions.date_from" type="date">
                    </div>
                    <div class="mb-4">
                        <label class="text-lg">Thời gian kết thúc</label>
                        <input v-model="addQuestions.date_to" type="date">
                    </div>
                    <div class="mb-4">
                        <label class="text-lg">Điểm</label>
                        <input v-model="addQuestions.score" type="text" placeholder="Nhập số điểm">
                    </div>
                    <div class="mb-4">
                        <label  class="text-lg">Mô tả</label>
                        
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
import API_URL_QUESTIONS from '@/links/questions.js'
const Assignment = {
    data() {
        return {
            data: [],
            addQuestions: {q_text: '', option1: '', option2: '', option3: '', option4: '', correct_answer: '', date_from: '', date_to: '', score: '', active: 'true'},
            default: {q_text: null, option1: null, option2: null, option3: null, option4: null, correct_answer: null, date_from: null, date_to: null, score: null, active: 'true'},
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
        Save(){
            const isCreate = String(this.$route.params.id) === '0'
            const body = this.addQuestions
            Object.keys(body).forEach(key => {
                body[key] = body[key] === '' ? null : body[key]
            })
            if (isCreate) {
                axios.post(`${API_URL_QUESTIONS}`, body)
                .then(response => {
                    this.addQuestions = this.default
                    this.$router.push({ name: 'T_assignment' })
                    alert('Thêm thành công')
                    console.log(response)
                })
                .catch(error => {
                })
            }else {
                axios.put(`${API_URL_QUESTIONS}${this.$route.params.id}`, body)
                .then(response => {
                    this.addQuestions = this.default
                    this.$router.push({ name: 'T_assignment' })
                    alert('Cập nhật thành công')
                    console.log(response)
                })
                .catch(error => {
                })
            }
        },
        back(){
            router.push({ name: 'T_assignment' })
        }
    },
    mounted(){
        this.getAccount()
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