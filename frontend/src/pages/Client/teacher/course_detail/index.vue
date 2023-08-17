<template>
    <div class="flex w-full">
      <div class="bg-slate-200 w-[30%] h-full">
          <div class="h-[90px] flex justify-between items-center px-6">
            <router-link class="flex hover" :to="{ name: 'T_courses', params: { name: 'T_courses'}}">
              <v-icon>mdi-chevron-left</v-icon>
              <div class="text-xl font-light">Tất cả các lớp</div>
            </router-link>
          </div>
          <div class="px-6">
            <div class="w-[100px] h-[100px] text-white text-2xl flex justify-center items-center bg-green-600">TĐ</div>
            <div v-for="item in data" :key="item.id" class="px-6 py-6 text-2xl font-bold uppercase">
              {{ item.name }}
              </div>
          </div>
          <div class="px-1">
            <router-link class="flex flex-col" v-for="(item, index) in items" :key="index" :to="{ name: item.name, params: { name: item.name }}">
                <span class="text-lg px-5 py-2 hover:bg-white rounded-md">{{ item.text }}</span>
            </router-link>
          </div>
      </div>
      <div class="bg-gray-100 w-full h-full">
          <router-view></router-view>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import API_URL_SUBJECT from '@/links/course.js'
  const Homepage = {
    data(){
          return{
            data: [],
            items: [
                  {icon: 'mdi-home',text: 'Trang chủ', name: 'T_course_id_homepage'},
                  {icon: 'mdi-comment-account',text: 'Điểm danh', name: 'T_attendance'},
                  {icon: 'mdi-book-account-outline',text: 'Điểm số'},
                  {icon: 'mdi-sword-cross',text: 'Giao Bài Tập'},
                  {icon: 'mdi-book-edit-outline',text: 'Kết quả làm bài'},
                  {icon: 'mdi-flip-horizontal',text: 'Tự học'},
              ],
              a: null
          }
      },
      methods: {
        async getCourses() {
              const name = localStorage.getItem('name')
              try{
                  const {data} =await axios.get(`${API_URL_SUBJECT}`)
                  this.data = data.filter(item => item.name == name)
              }catch(error){
                  console.log(error)
              }
          },
          setActiveItem(index) {
              this.a = index
              localStorage.setItem('activeItem', index)
          }
      },
      mounted(){
        this.getCourses()
      }
  }
  export default Homepage
  </script>
  
  <style scoped>
  .v-application p {
      margin-bottom: 0px;
  }
  .v-application a {
      color:black
  }
  .hover :hover{
      color: #0f766e;
  }
  </style>