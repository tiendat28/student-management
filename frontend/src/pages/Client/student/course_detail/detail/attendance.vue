<template>
    <div>
        <div class="h-[90px] flex justify-between items-center px-8 border-b-2 border-[#cbd5e1]">
            <div class="flex">
                <v-icon color="#0f766e" class="pr-3" :size="50">mdi-book-account</v-icon>
                <span class="font-bold text-2xl flex justify-center items-center">Điểm danh</span>
            </div>
        </div>
        <div class="p-8 w-full bg-gray-100">
            <div class="p-6 rounded-lg shadow-sm h-[150px] w-full bg-white flex justify-between items-center">
                <div>
                    <v-icon class="pr-6" color="blue" :size="80">mdi-bullhorn-outline</v-icon>
                    <span class="text-xl">Thông báo tháng 8</span>
                </div>
                <div class="h-[120px] w-[160px] p-3 rounded-lg border-2 border-teal-600 shadow-sm">
                    <div>Tổng số học sinh</div>
                    <div class="flex justify-between items-center px-1 pt-6">
                        <span class="text-2xl"><b>{{ this.length }}</b></span>
                        <v-icon :size="30">mdi-check-all</v-icon>
                    </div>
                </div>
                <div class="h-[120px] w-[160px] p-3 rounded-lg border-2 border-teal-600 shadow-sm">
                    <div>Nghỉ không phép</div>
                    <div class="flex justify-between items-center px-1 pt-6">
                        <span class="text-2xl"><b>1</b></span>
                        <v-icon color="red" :size="30">mdi-alert-outline</v-icon>
                    </div>
                </div>
                <div class="h-[120px] w-[160px] p-3 rounded-lg border-2 border-teal-600 shadow-sm">
                    <div>Nghỉ có phép</div>
                    <div class="flex justify-between items-center px-1 pt-6">
                        <span class="text-2xl"><b>1</b></span>
                        <v-icon color="yellow" :size="30">mdi-alert-decagram-outline</v-icon>
                    </div>
                </div>
                <div class="h-[120px] w-[160px] p-3 rounded-lg border-2 border-teal-600 shadow-sm">
                    <div>Điểm chuyên cần</div>
                    <div class="flex justify-between items-center px-1 pt-6">
                        <span class="text-2xl"><b>1</b></span>
                        <v-icon color="green" :size="30">mdi-check-outline</v-icon>
                    </div>
                </div>
            </div>
            <div class="relative overflow-auto rounded-lg shadow-sm table-reponsive pt-6">
                <table class="w-full text-sm text-left text-gray-500 whitespace-nowrap">
                    <thead class="text-sm text-gray-700 uppercase">
                        <tr class="bg-white border-b ">
                            <th scope="col" class="px-6 py-3">STT</th>
                            <th scope="col" class="px-6 py-3">Date</th>
                            <th v-for="item in classData.student" :key="item.id" scope="col" class="px-6 py-3">{{ item.fullname }}</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(item, index) in attendanceData" :key="item.date" class="bg-white border-b text-base">
                            <td scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap ">{{ index + 1 }}</td>
                            <td class="px-6 py-4">{{ item.date.split("-").reverse().join('-') }}</td>
                            <td class="px-6 py-4" v-for="item in item.student" :key="item.student">
                                {{ item.status }}
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import API_URL_SUBJECT from '@/links/course.js'
import API_URL_ATTENDANCE from '@/links/attendance.js'
const Attendance ={
  data(){
      return{
          datetime: new Date().toISOString().substr(0, 10),
          classData: '',
          length: '',
          attendanceData : [],
          status: ['Đi học', 'Nghỉ có phép', 'Nghỉ không phép']
      }
  },
  methods:{
      async awaiting() {
          await this.getCourses()
          await this.getAttendance()
      },
      async getCourses() {
        const name = localStorage.getItem('name')
        try{
            const {data} = await axios.get(`${API_URL_SUBJECT}`)
            this.classData = data.filter(item => item.name == name)[0]
            this.length = this.classData.student.length
        }catch(error){
            console.log(error)
        }
      },
      async getAttendance(){
        try{
            const {data} = await axios.get(`${API_URL_ATTENDANCE}`)
            const id = this.classData.id
            this.attendanceData = data.filter(item => item.subject_id == id)[0].date
        }catch(error){
            console.log(error)
        }
      }
  },
  mounted(){
      this.getCourses()
      this.getAttendance()
  },
  computed: {
      DateTime() {       
          const [year, month, day] = this.datetime.split("-")
          return `${day}-${month}-${year}`
      }
  },
  created() {
      this.awaiting()
  }
}
export default Attendance
</script>