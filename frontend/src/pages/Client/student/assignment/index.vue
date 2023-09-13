<template>
  <div class="w-full h-screen">
    <nav class="p-8 text-xl flex justify-between items-center h-[80px] border-b-2 border-gray-150">
        <div class="flex items-center">
            <div>
                <span @click="Upcoming()" v-bind:class="{ 'border-b-4 border-teal-600 font-medium': upcoming }" class="py-2 hover:border-gray-300 hover:border-b-4 hover:cursor-pointer">Sắp tới</span>
            </div>
            <div class="px-8">
                <span @click="Expire()" v-bind:class="{ 'border-b-4 border-teal-600 font-medium': expire }" class="py-2 hover:border-gray-300 hover:border-b-4 hover:cursor-pointer">Quá hạn</span>
            </div>
            <div>
                <span @click="Done()" v-bind:class="{ 'border-b-4 border-teal-600 font-medium': done }" class="py-2 hover:border-gray-300 hover:border-b-4 hover:cursor-pointer">Đã hoàn thành</span>
            </div>
        </div>
        <div>
            <v-icon>mdi-view-headline</v-icon>
        </div>
    </nav>
    <div v-show="upcoming" class="relative top-0 left-0 table-reponsive overflow-x-hidden w-full h-full">
        <div class="w-[60%] absolute top-0 left-[340px]">
            <div class="px-8 pt-4">
                <div class="h-[160px]">
                    <div class="bg-teal-500 h-[70px] rounded-t-lg flex justify-between items-center px-6 text-xl text-white">
                        <div>PHẦN TRẮC NGHIỆM --- MÔN TIẾNG ANH</div>
                        <div v-show="score">90/100 Điểm</div>
                    </div>
                    <div class="h-[90px] rounded-b-lg border-gray-300 border-2 flex items-center px-6 text-xl">Chọn câu trả lời đúng nhất</div>
                </div>
            </div>
            <div v-for="(item, index) in questions" :key="item.id"  class="px-8 pt-6 ">
                <div class="h-[230px] border-gray-300 border-2 rounded-lg">
                    <div class="flex justify-between px-8 pt-8">
                        <span class="text-xl">{{ index + 1 }}. {{ item.q_text }}</span>
                        <span>{{item.score}} điểm</span>
                    </div>
                    <div class="px-8">
                        <v-radio-group v-model="item.option">
                            <v-radio v-model="item.option1" :label="item.option1" :value="item.option1"></v-radio>
                            <v-radio v-model="item.option2" :label="item.option2" :value="item.option2"></v-radio>
                            <v-radio v-model="item.option3" :label="item.option3" :value="item.option3"></v-radio>
                            <v-radio v-model="item.option4" :label="item.option4" :value="item.option4"></v-radio>
                        </v-radio-group>
                    </div>
                </div>
            </div>
            <div class="py-6 px-8">
                <v-btn @click="submit()" style="color: white;" color="#0d9488">Submit</v-btn>
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
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from 'jwt-decode'
import API_URL_QUESTIONS from '@/links/questions.js'
import API_URL_ANSWER from '@/links/answer.js'
import router from '@/router/index.ts'
const Assignment = {
    data() {
        return {
            upcoming: true,
            expire: false,
            done: false,
            score: false,
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
        submit(){
            const user_id = this.data.id
            const answer = this.questions.map(item => {
                return {
                    q_id: item.id,
                    user_id: user_id,
                    select_answer: item.option, 
                    is_correct: null 
                }
            })
            let select_answer = true
            for (let i = 0; i < answer.length; i++) {
                if (answer[i].select_answer === undefined) {
                    select_answer = false
                    break
                }
            }
            if(!select_answer){
                alert('Đáp án không được để trống')
            } else {
                console.log(answer)
                axios.post(`${API_URL_ANSWER}`, answer)
                .then(response => {
                    router.push('/S_home/assignment_done')
                    console.log(response)
                })
                .catch(error => {
                    console.error(error)
                })
            }
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
        }
    },
    mounted(){
        this.getQuestions()
        this.getAccount()
    }
}
export default Assignment
</script>

<style scoped>
.table-reponsive {
    max-height: calc(100vh - 160px);
}
</style>