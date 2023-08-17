<template>
    <div>
        <div class="flex text-2xl font-semibold mb-10 justify-between items-center">
            <div>
                <h1 class="font-bold text-3xl">Class List</h1>
            </div>
            <div>
                <v-dialog v-model="dialog" persistent max-width="500px">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn color="#0f766e" dark v-bind="attrs" v-on="on"> + Add Class</v-btn>
                </template>
                    <v-card>
                        <v-card-title>
                            <span class="text-h5">Class Information</span>
                        </v-card-title>
                        <v-card-text>
                            <v-container>
                                <v-row>
                                    <v-col cols="12" sm="12">
                                        <v-text-field v-model="addData.name" label="Name" required></v-text-field>
                                    </v-col>
                                    <v-col cols="12" sm="12">
                                        <v-text-field v-model="addData.class_room" label="Class room" required></v-text-field>
                                    </v-col>
                                    <v-col cols="12" sm="12">
                                        <v-select v-model="addData.timetable" :items="['Session 1', 'Session 2', 'Session 3', 'Session 4']" label="Timetable" required></v-select>
                                    </v-col>
                                    <v-col cols="12" sm="12">
                                        <v-select v-model="addData.teacher_id" :items="teacher" label="Teacher" required></v-select>
                                    </v-col>
                                    <v-col cols="12">
                                        <v-select v-model="addData.student_ids" :items="student" small-chips multiple label="Students"></v-select>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="red darken-1" text @click="dialog = false">Cancel</v-btn>
                            <v-btn color="green darken-1" text @click="addClass()">Save</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </div>
        </div>
        <div class="relative overflow-auto rounded-lg shadow-sm table-reponsive">
            <table class="w-full text-sm text-left text-gray-500 whitespace-nowrap">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50">
                    <tr>
                        <th scope="col" class="px-6 py-3">No</th>
                        <th scope="col" class="px-6 py-3">Class Name</th>
                        <th scope="col" class="px-6 py-3">Class Room</th>
                        <th scope="col" class="px-6 py-3">Timetable</th>
                        <th scope="col" class="px-6 py-3">Teacher</th>
                        <th scope="col" class="px-6 py-3 flex justify-end">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(item, index) in classdata" :key="item.id" class="bg-white border-b ">
                        <td scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap ">{{ index + 1 }}</td>
                        <td class="px-6 py-4">{{ item.name }}</td>
                        <td class="px-6 py-4">{{ item.class_room }}</td>
                        <td class="px-6 py-4">{{ item.timetable }}</td>
                        <td class="px-6 py-4">{{ item.teacher.fullname }}</td>
                        <td class="pr-8 py-4 flex justify-end">
                            <v-icon height="40px" color="red" @click="handleDelete(item.id)"> mdi-delete</v-icon>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <v-dialog v-model="dialogDelete" max-width="350px">
            <v-card>
                <v-card-title class="text-sm">Are you sure you want to delete?</v-card-title>
                <v-card-actions>
                    <v-spacer></v-spacer>
                        <v-btn color="red darken-1" text @click="dialogDelete = false">Cancel</v-btn>
                        <v-btn color="green darken-1" text @click="deleteItemConfirm()">OK</v-btn>
                    <v-spacer></v-spacer>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
import axios from 'axios'
import API_URL_SUBJECT from '@/links/course.js'
import API_URL_TEACHER from '@/links/teacher.js'
import API_URL_STUDENT from '@/links/student.js'
const Courses = {
    data(){
        return{
            dialog: false,
            dialogDelete: false,
            classdata: [],
            addData: {name: '',class_room: '', timetable: '',teacher_id: '', student_ids: ''},
            teacherdata: [],
            teacher: [],
            studentdata: [],
            student: [],
            id: []
        }
    },
    methods: {
        async getTeacher(){
            try{
                const {data} =await axios.get(`${API_URL_TEACHER}`)
                this.teacherdata = data.filter(item => item.active == true ).map(item => {
                    return {
                        fullname : item.first_name + ' ' + item.last_name,
                        teacher_id: item.id
                    }
                })
                this.teacher = this.teacherdata.map(item => item.fullname)

            }catch(error){
                console.log(error)
            }
        },
        async getStudent(){
            try{
                const {data} =await axios.get(`${API_URL_STUDENT}`)
              
                this.studentdata = data.filter(item => item.active == true ).map(item => {
                    return {
                        fullname : item.first_name + ' ' + item.last_name,
                        student_id: item.id
                    }
                })
                this.student = this.studentdata.map(item => item.fullname)
                
            }catch(error){
                console.log(error)
            }
        },
        async getCourses() {
            try{
                const {data} =await axios.get(`${API_URL_SUBJECT}`)
                this.classdata = data.filter(item => item.active !== false)
            }catch(error){
                console.log(error)
            }
        },
        addClass(){
            const selectedTeacher = this.teacherdata.find(item => item.fullname === this.addData.teacher_id)
            const selectedStudents = this.studentdata.filter(item => this.addData.student_ids.includes(item.fullname))
            const studentIds = selectedStudents.map(item => item.student_id)

            if (true) {
                this.addData.teacher_id = selectedTeacher.teacher_id
                this.addData.student_ids = studentIds
                axios.post(`${API_URL_SUBJECT}`,this.addData)
                .then(response => {
                    this.getCourses()
                    this.dialog = false
                    console.log(response)
                })
            }
        },
        handleDelete(item){
            this.id = item
            this.dialogDelete = true
        },
        deleteItemConfirm(){
            axios.delete(`${API_URL_SUBJECT}${this.id}`)
            .then(response => {
                this.dialogDelete = false
                this.getCourses()
                console.log(response)
            })
            .catch(error => {
            })
        }
    },
    mounted(){
      this.getCourses()
      this.getTeacher()
      this.getStudent()
    }
}
export default Courses
</script>