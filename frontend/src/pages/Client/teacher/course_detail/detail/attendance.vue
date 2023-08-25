<template>
    <div>
        <div class="h-[90px] flex justify-start items-center px-8 border-b-2 border-[#cbd5e1]">
            <div class="flex">
                <v-icon color="#0f766e" class="pr-3" :size="50">mdi-book-account</v-icon>
                <span class="font-bold text-2xl flex justify-start items-center">Điểm danh</span>
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
                    <div>Nghỉ KP nhiều </div>
                    <div class="flex justify-between items-center px-1 pt-6">
                        <span class="text-2xl"><b>Sơn</b></span>
                        <v-icon color="red" :size="30">mdi-alert-outline</v-icon>
                    </div>
                </div>
                <div class="h-[120px] w-[160px] p-3 rounded-lg border-2 border-teal-600 shadow-sm">
                    <div>Nghỉ CP nhiều</div>
                    <div class="flex justify-between items-center px-1 pt-6">
                        <span class="text-2xl"><b>Hoàng</b></span>
                        <v-icon color="yellow" :size="30">mdi-alert-decagram-outline</v-icon>
                    </div>
                </div>
                <div class="h-[120px] w-[160px] p-3 rounded-lg border-2 border-teal-600 shadow-sm">
                    <div>Chuyên cần</div>
                    <div class="flex justify-between items-center px-1 pt-6">
                        <span class="text-2xl"><b>Đạt</b></span>
                        <v-icon color="green" :size="30">mdi-check-outline</v-icon>
                    </div>
                </div>
            </div>
            <div class="pt-6">
                <v-dialog v-model="dialog" persistent max-width="450px">
                    <template v-slot:activator="{ on, attrs }">
                        <div class="flex justify-start pb-6">
                            <v-btn color="#0f766e" dark v-bind="attrs" v-on="on">Điểm danh</v-btn>
                        </div>
                    </template>
                    <v-card class="w-[450px] h-[450px]">
                        <v-card-title class="flex justify-between bg-teal-700">
                            <div class="flex">
                                <span class="text-h5 text-white">Điểm danh </span>
                                <h4 class="pl-3 text-white font-light">{{ DateTime }}</h4>
                            </div>
                            <v-btn color="white darken-1" text @click="dialog = false">X</v-btn>
                        </v-card-title>
                        <v-card-text>
                            <v-container>
                                <v-row >
                                    <v-col v-for="item in classData.student" :key="item.id" cols="12" sm="6" md="6">
                                        <v-select :label="item.fullname" :items="status" v-model="item.status"></v-select>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-card-text>
                        <v-card-actions>
                        <div class="flex justify-center">
                            <v-btn color="green darken-1" width="100%" text @click="post()">Lưu</v-btn>
                        </div>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </div>
            <div class="relative overflow-auto rounded-lg shadow-sm table-reponsive">
                <table class="w-full text-sm text-left text-gray-500 whitespace-nowrap">
                    <thead class="text-sm text-gray-700 uppercase bg-gray-50">
                        <tr class="bg-white border-b ">
                            <th scope="col" class="px-6 py-3">STT</th>
                            <th scope="col" class="px-6 py-3">Date</th>
                            <th v-for="item in classData.student" :key="item.id" scope="col" class="px-6 py-3">{{ item.fullname }}</th>
                            <th scope="col" class="px-6 py-3 flex justify-end">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(item, index) in attendanceData" :key="item.date" class="bg-white border-b text-base">
                            <td scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap ">{{ index + 1 }}</td>
                            <td class="px-6 py-4">{{ item.date.split("-").reverse().join('-') }}</td>
                            <td class="px-6 py-4" v-for="item in item.student" :key="item.student">
                                {{ item.status }}
                            </td>
                            <td class="px-6 py-4 flex justify-end">
                                <v-icon style="color: green"  :size="25" @click="Count()">mdi-pencil</v-icon>
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
            dialog: false,
            datetime: new Date().toISOString().substr(0, 10),
            classData: '',
            length: '',
            attendanceData : [],
            status: ['Đi học', 'Nghỉ có phép', 'Nghỉ không phép'],
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
        },
        post() {
            const subject_id = this.classData.id
            const teacher_id = this.classData.teacher.teacher_id
            const attendanceData = this.classData.student.map(item => {
                return {
                    subject_id: subject_id,
                    teacher_id: teacher_id,
                    student_id: item.student_id, 
                    date: this.datetime + 'T04:30:43.107Z',
                    status: item.status, 
                }
            })

            axios.post(API_URL_ATTENDANCE, attendanceData)
                .then(response => {
                    this.getAttendance()
                    this.dialog = false
                    console.log(response)
                })
                .catch(error => {
                    console.error(error)
                })
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