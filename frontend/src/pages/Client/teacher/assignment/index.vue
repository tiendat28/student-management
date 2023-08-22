<template>
    <div class="w-full h-screen">
        <nav class="p-8 text-xl flex justify-between items-center h-[80px] border-b-2 border-gray-150">
            <div class="flex items-center">
                <div>
                    <span @click="Upcoming()" v-bind:class="{ 'border-b-4 border-teal-600 font-medium': upcoming }" class="py-2 hover:border-gray-300 hover:border-b-4 hover:cursor-pointer">Bài tập</span>
                </div>
                <div class="px-8">
                    <span @click="Expire()" v-bind:class="{ 'border-b-4 border-teal-600 font-medium': expire }" class="py-2 hover:border-gray-300 hover:border-b-4 hover:cursor-pointer">DS Nộp bài</span>
                </div>
                <div>
                    <span @click="Done()" v-bind:class="{ 'border-b-4 border-teal-600 font-medium': done }" class="py-2 hover:border-gray-300 hover:border-b-4 hover:cursor-pointer">BĐ Đáp án</span>
                </div>
            </div>
            <div>
                <v-icon>mdi-view-headline</v-icon>
            </div>
        </nav>
        <div v-show="upcoming" class="bg-gray-200 w-full h-full">
            <div class="p-8">
                <div class="flex text-2xl font-semibold mb-10 justify-between items-center">
                    <div>
                        <h1 class="font-bold text-3xl">Ngân hàng đề</h1>
                    </div>
                    <div>
                        <v-btn color="#0f766e" dark @click="Add()"> + Câu hỏi</v-btn>
                    </div>
                </div>
                <div class="relative overflow-x-hidden rounded-lg shadow-sm table-reponsive">
                    <table class="w-full text-sm text-left text-gray-500 whitespace-nowrap">
                        <thead class="text-xs text-gray-700 bg-gray-50">
                            <tr>
                                <th scope="col" class="px-6 py-3">STT</th>
                                <th scope="col" class="px-6 py-3">Câu hỏi</th>
                                <th scope="col" class="px-6 py-3">Lựa chọn 1</th>
                                <th scope="col" class="px-6 py-3">Lựa chọn 2</th>
                                <th scope="col" class="px-6 py-3">Lựa chọn 3</th>
                                <th scope="col" class="px-6 py-3">Lựa chọn 4</th>
                                <th scope="col" class="px-6 py-3">Đáp án</th>
                                <th scope="col" class="px-6 py-3">Date from</th>
                                <th scope="col" class="px-6 py-3">Date to</th>
                                <th scope="col" class="px-6 py-3">Điểm</th>
                                <th scope="col" class="px-6 py-3 flex justify-end">Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(item, index) in questions" :key="item.id" class="bg-white border-b ">
                                <td scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap ">{{ index + 1 }}</td>
                                <td class="px-6 py-4">{{ item.q_text }}</td>
                                <td class="px-6 py-4">{{ item.option1 }}</td>
                                <td class="px-6 py-4">{{ item.option2 }}</td>
                                <td class="px-6 py-4">{{ item.option3 }}</td>
                                <td class="px-6 py-4">{{ item.option4 }}</td>
                                <td class="px-6 py-4">{{ item.correct_answer }}</td>
                                <td class="px-6 py-4">{{ item.date_from }}</td>
                                <td class="px-6 py-4">{{ item.date_to }}</td>
                                <td class="px-6 py-4">{{ item.score }}</td>
                                <td class="pr-8 py-4 flex justify-end">
                                    <v-icon height="40px" color="red" @click="handleDelete(item.id)"> mdi-delete</v-icon>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div v-show="expire" class="relative top-0 left-0 table-reponsive overflow-x-hidden w-full h-full">
            <div class="p-8" v-for="item in items" :key="item.title">
                <span class="text-xl"><b>{{ item.date }}</b> {{ item.day }}</span>
                <div class="pt-6">
                    <div class="flex justify-between border-2 border-teal-300 rounded-lg p-6">
                        <div class="flex">
                            <div class="flex items-center">
                                <v-img class="w-[50px] h-[50px]" :src = 'item.image'></v-img>
                            </div>
                            <div class="">
                                <div class="px-4 flex flex-col">
                                    <span class="text-xl">{{ item.title }}</span>
                                    <span class="py-2 text-red-500">Đã hết hạn: {{ item.sent }} </span>
                                    <span>Lớp: {{ item.class }} </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-show="done" class="relative top-0 left-0 table-reponsive overflow-x-hidden w-full h-full">
            <div class="p-8" v-for="item in items" :key="item.title">
                <span class="text-xl"><b>{{ item.date }}</b> {{ item.day }}</span>
                <div class="pt-6">
                    <div class="flex justify-between border-2 border-teal-300 rounded-lg p-6">
                        <div class="flex">
                            <div class="flex items-center">
                                <v-img class="w-[50px] h-[50px]" :src = 'item.image'></v-img>
                            </div>
                            <div class="">
                                <div class="px-4 flex flex-col">
                                    <span class="text-xl">{{ item.title }}</span>
                                    <span class="py-2">Đã gửi vào lúc: {{ item.sent }} </span>
                                    <span>Lớp: {{ item.class }} </span>
                                </div>
                            </div>
                        </div>
                        <div>
                            <div class="bg-green-200 rounded-md py-1 px-2">
                                <v-icon>mdi-check</v-icon>
                                <span class="px-2">Đã nộp bài</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-show="question" class="bg-gray-200 w-full h-full">
            <div class="px-8 pt-8 pb-4">
                <span class="font-bold text-3xl"><b class="text-teal-400 hover:cursor-pointer" @click="Upcoming()">Ngân hàng đề / </b> Câu hỏi</span>
            </div>
            <div class="px-[500px]">
                <div class="p-8 bg-white rounded-lg">
                    <form class="relative overflow-x-hidden table-reponsive1 ">
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
    </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from 'jwt-decode'
import API_URL_QUESTIONS from '@/links/questions.js'
import API_URL_ANSWER from '@/links/answer.js'
const Assignment = {
    data() {
        return {
            upcoming: true,
            expire: false,
            done: false,
            question: false, 
            data: [],
            items: [
                {'date': '4 Tháng 8', 'day': 'Thứ sáu', 'image':'https://ungdung.mobi/wp-content/uploads/2022/07/autocad.png', 'title': 'THI CUỐI KỲ - Kíp 4, 15h00 Thứ 6 ngày 04/08/23', 'sent': '12h00', 'class': 'Autocad'},
                {'date': '4 Tháng 3', 'day': 'Thứ bảy', 'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNt0jKRnbtC2cp008h8mSwEC7vc-9oVJIX6E2_7UCRmOeWHRvJmg3-1JDm7xsuTuXcLjw&usqp=CAU', 'title': 'TIỂU LUẬN CUỐI KỲ', 'sent': '15h00', 'class': 'Javascript'},
                {'date': '19 Tháng 7', 'day': '2022', 'image':'https://wallpaperaccess.com/full/1892752.jpg', 'title': 'Đồ án chuyên ngành', 'sent': '10h00', 'class': 'IT-20180655'},
                {'date': '28 Tháng 2', 'day': '2022', 'image':'https://absarcs.info/how-to/implementing-rot13-caesar-cipher-python3//d09e3a9ec3f6ca8e160f21aa00f3402e.png', 'title': 'Bài tập lớn', 'sent': '12h00', 'class': 'Python'},
                {'date': '22 Tháng 10', 'day': '2022', 'image':'https://hoclamweb123.com/wp-content/uploads/2020/07/lap-trinh-php.jpg', 'title': 'Bài tập nhóm', 'sent': '17h00', 'class': 'PHP'},
                {'date': '9 Tháng 9', 'day': '2022', 'image':'https://crisp.chat/static/blog/content/images/2022/05/How-to-Migrate-a-large-project-from-Vue-2-to-Vue-3.jpg', 'title': 'Bài kiểm tra', 'sent': '12h00', 'class': 'VueJS'},
            ],
            questions: [],
            addQuestions: {q_text: '', option1: '', option2: '', option3: '', option4: '', correct_answer: '', date_from: '', date_to: '', score: '', active: 'true'},
            default: {q_text: null, option1: null, option2: null, option3: null, option4: null, correct_answer: null, date_from: null, date_to: null, score: null, active: 'true'},
            answer: []
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
        async getQuestions(){
            try{
                const {data} =await axios.get(`${API_URL_QUESTIONS}`)
                this.questions = data.filter(item => item.active !==false)  
            }catch(error){
                console.log(error)
            }
        },
        async getAnswer(){
            try{
                const {data} =await axios.get(`${API_URL_ANSWER}`)
                this.answer = data.filter(item => item.active !==false)  
            }catch(error){
                console.log(error)
            }
        },
        Save(){
            axios.post(`${API_URL_QUESTIONS}`, this.addQuestions)
            .then(response => {
                this.upcoming = true
                this.getQuestions()
                this.addQuestions = this.default
                console.log(response)
            })
            .catch(error => {
            })
        },
        handleDelete(item){
            axios.delete(`${API_URL_QUESTIONS}${item}`)
            .then(response => {
                this.dialogDelete = false
                this.getQuestions()
                console.log(response)
            })
            .catch(error => {
            })
        },
        Upcoming(){
            this.upcoming = true
            this.expire = false
            this.done = false
        },
        Expire(){
            this.upcoming = false
            this.expire = true
            this.done = false
        },
        Done(){
            this.upcoming = false
            this.expire = false
            this.done = true
        },
        Add(){
            this.upcoming = false
            this.expire = false
            this.done = false
            this.question = true
        },
    },
    mounted(){
        this.getQuestions()
        this.getAnswer()
        this.getAccount()
    }
}
export default Assignment
</script>

<style scoped>
.table-reponsive {
    max-height: calc(100vh - 150px);
}
.table-reponsive1 {
    max-height: calc(100vh - 320px);
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