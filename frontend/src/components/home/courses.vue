<template>
    <div id="courses" class="container p-12 mx-auto">
        <div class="flex flex-col justify-center items-center uppercase text-[#06b6d4] text-5xl font-medium p-10">Chọn khóa học</div>
        <div class="flex justify-between items-center">
            <div class="w-[40%]">
                <h1 class="text-xl text-[#cbd5e1] font-normal pb-3">Choose what to learn</h1>
                <p class="text-[#cbd5e1]">Start learning the best programming languages.</p>
            </div>
            <div class="pl-3">
                <div class="flex flex-wrap justify-between md:flex md:justify-between">
                    <div @click="move(item.id)" v-for="item in classdata" :key="item.id" class="m-2 rounded-md border-teal-700 w-[200px] md:w-[200px]">
                        <v-btn height="60px" color="#1e293b" class="w-[200px] flex justify-start md:w-[200px]">
                            <div class="w-[40px] h-[40px] py-[5px] bg-[#475569] rounded-full">
                                <v-icon color="#06b6d4">mdi-account-group</v-icon>
                            </div>
                            <h1 class="pl-[15px] text-[#cbd5e1]">{{ item.name }}</h1>
                        </v-btn>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import API_URL_SUBJECT from '@/links/course.js'
const Course = {
    data(){
        return {
            classdata: [],
        }
    },
    methods: {
        async getCourses() {
            try{
                const {data} =await axios.get(`${API_URL_SUBJECT}`)
                this.classdata = data.filter(item => item.active !== false )
            }catch(error){
                console.log(error)
            }
        }
    },
    mounted(){
      this.getCourses()
    }
}
export default Course
</script>

<style>

</style>