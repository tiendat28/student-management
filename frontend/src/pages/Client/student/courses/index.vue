<template>
    <div class="bg-gray-200 w-full">
        <div class="flex py-[30px] px-8">
            <span class="font-bold text-2xl">Lớp học</span>
        </div>
        <h1 class="px-9">Lớp của bạn</h1>
        <div class="grid gap-10 px-8 justify-stretch">
            <div class="flex items-start flex-wrap">
                <div @click="move(item.subject_id)" v-for="item in classdata" :key="item.subject_id" class="m-4 rounded-md w-[340px]">
                    <v-btn height="280px" class="w-[340px]" style="background: white;">
                        <span class="flex flex-col justify-center items-center">
                            <div :style="{background: 'green' }" class="w-[100px] h-[100px] text-white text-2xl flex justify-center items-center">  
                                TĐ  
                            </div>
                            <h1 class="pt-3 text-xl">{{ item.name }}</h1>
                        </span>
                    </v-btn>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import API_URL_SUBJECT from '@/links/course.js'
import router from '@/router/index.ts'
import Header from '@/components/layout/client/header.vue'
import jwtDecode from 'jwt-decode'
const Courses = {
    data(){
        return{
            dialog: false,
            classdata: [],
            data: [],
            colors: [{color: 'red'},{color: 'blue'},{color: 'green'},]
        }
    },
    methods: {
        async fetchStudentAndCourses() {
            await this.getStudent()
            await this.getCourses()
        },
        async getStudent(){
            const token = localStorage.getItem('token')
            try{
                const decodedToken = jwtDecode(token)
                this.data = decodedToken
            }catch(error){
                console.log(error)
            }
        },
        async getCourses() {
            try{
                const student_id = this.data.id
                const {data} =await axios.get(`${API_URL_SUBJECT}${'subject_of_user'}${'/'}${student_id}`)
                this.classdata = data[0].subject
            }catch(error){
                console.log(error)
            }
        },
        move(item){
            const name = this.classdata.filter(a => a.subject_id == item)[0].name
            localStorage.setItem('name', name)
            router.push({ name: 'S_course_id_homepage', params: { id: item} })
        },
    },
    components: {
        Header
    },
    mounted(){
        this.getStudent()
        this.getCourses()
    },
    created() {
        this.fetchStudentAndCourses()
    }
}
export default Courses
</script>
<style scoped>

</style>