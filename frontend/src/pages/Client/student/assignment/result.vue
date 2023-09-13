<template>
    <div class="w-full h-screen">
        <div class="relative top-0 left-0 table-reponsive overflow-x-hidden w-full h-full">
            <div class="w-[60%] absolute top-0 left-[340px]">
                <div class="px-8 py-6">
                    <div class="h-[270px]">
                        <div class="bg-teal-500 h-[70px] rounded-t-lg flex items-center px-6 text-xl text-white">
                            <div>KẾT QUẢ --- MÔN TIẾNG ANH</div>
                        </div>
                        <div class="h-[200px] rounded-b-lg border-gray-300 border-2 items-center px-8 pt-8 text-xl">
                            <div v-for="item in table" :key="item.title" class="flex">
                                <div class="flex justify-start w-[180px]">
                                    <span class="text-xl font-semibold">{{ item.title }}</span>
                                </div>
                                <div>
                                    <span class="px-2">{{ item.text }}</span>
                                </div>
                            </div>
                            <div class="flex">
                                <div class="flex justify-start w-[180px]">
                                    <span class="text-xl font-semibold">Điểm</span>
                                </div>
                                <div v-for="item in answer" :key="item.id">
                                    <span class="px-2"> {{ item.user.score_total }} / {{ item.questions.length }}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-for="(item, index) in questions" :key="item.id"  class="px-8 pt-6 ">
                    <div class="h-[230px] border-gray-300 border-2 rounded-lg">
                        <div class="flex justify-between px-8 pt-8">
                            <div>
                                <span class="text-xl pr-2">{{ index + 1 }}. {{ item.text }}</span>
                                <v-icon v-if="item.is_correct == true" :size="30" color="green">mdi-check</v-icon>
                                <v-icon v-if="item.is_correct == false" :size="30" color="red">mdi-close</v-icon>
                            </div>
                            <span v-if="item.is_correct == true" class="text-green-700 text-lg font-semibold">{{item.score}}/{{item.score}}</span>
                            <span v-if="item.is_correct == false" class="text-red-500 text-lg font-semibold">0/{{item.score}}</span>
                        </div>
                        <div class="px-8">
                            <v-radio-group v-model="item.select_answer">
                                <v-radio v-model="item.option1" :label="item.option1" :value="item.option1"></v-radio>
                                <v-radio v-model="item.option2" :label="item.option2" :value="item.option2"></v-radio>
                                <v-radio v-model="item.option3" :label="item.option3" :value="item.option3"></v-radio>
                                <v-radio v-model="item.option4" :label="item.option4" :value="item.option4"></v-radio>
                            </v-radio-group>
                        </div>
                    </div>
                    <div class="p-3 text-lg">
                        <span>Đáp án đúng: <b>{{ item.correct_answer }}</b></span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import API_URL_ANSWER from '@/links/answer.js'
import jwtDecode from 'jwt-decode'
const Result = {
    data(){
        return{
            table: [
                {title: 'Bắt đầu lúc', text:'1h'},
                {title: 'Trạng thái', text:'Đã nộp'},
                {title: 'Nộp bài lúc', text:'2h'},
                {title: 'Thời gian thực hiện', text:'1h'},
            ],
            answer: [],
            questions: [],
            data: []
        }
    },
    methods: {
        async getUser(){
            const token = localStorage.getItem('token')
            try{
                const decodedToken = jwtDecode(token)
                this.data = decodedToken
            }catch(error){
                console.log(error)
            }
        },
        async getAnswer(){
            try{
                const user_id = this.data.id
                const {data} =await axios.get(`${API_URL_ANSWER}${'of_'}${user_id}`)
                this.answer = data.filter(item => item.active !==false)
                this.questions = this.answer[0].questions
            }catch(error){
                console.log(error)
            }
        },
    },
    mounted(){
        this.getUser()
        this.getAnswer()
    }
}
export default Result
</script>

<style scoped>
.table-reponsive {
    max-height: calc(100vh - 100px);
}
</style>