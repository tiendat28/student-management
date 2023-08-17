<template>
    <div>
        <div class="px-8 py-10 overflow-auto">
            <v-data-table :headers="headers" :items="member" sort-by="calories" class="elevation-4">
                <template v-slot:top>
                    <v-toolbar flat>
                        <v-toolbar-title>Member</v-toolbar-title>
                        <v-divider class="mx-4" inset vertical></v-divider>
                        <v-spacer></v-spacer>
                        <v-dialog v-model="dialog" max-width="500px">
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn color="#0f766e" dark class="mb-2" v-bind="attrs" v-on="on">New member</v-btn>
                            </template>
                            <v-card>
                                <v-card-title>
                                    <span class="text-h5">{{ formTitle }}</span>
                                </v-card-title>

                                <v-card-text>
                                    <v-container>
                                        <v-row>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field label="Username" :rules="nameRules" v-model="editdata.username" required></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field label="Password" :rules="nameRules" v-model="editdata.password" required></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field label="First Name" :rules="nameRules" v-model="editdata.first_name" required></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field label="Last Name" :rules="nameRules" v-model="editdata.last_name" required></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field label="Phone" :rules="nameRules" v-model="editdata.phone" required></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field label="Address" :rules="nameRules" v-model="editdata.address" required></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field label="Email" :rules="emailRules" v-model="editdata.email" required></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field label="Sex" :rules="nameRules" v-model="editdata.sex" required></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="12">
                                                <v-select label="Role" :items="items" v-model="editdata.role" required></v-select>
                                            </v-col>
                                        </v-row>
                                    </v-container>
                                </v-card-text>

                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn color="red darken-1" text @click="close()"> Cancel</v-btn>
                                    <v-btn color="green darken-1" text @click="save()"> Save</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
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
                    </v-toolbar>
                </template>
                <template v-slot:item.actions="{ item }">
                    <v-icon height="40px" color="green" class="mr-2" @click="editItem(item.id)"> mdi-pencil </v-icon>
                    <v-icon height="40px" color="red" @click="deleteItem(item.id)"> mdi-delete</v-icon>
                </template>
            </v-data-table>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import API_URL_USER from '@/links/user.js'
import API_URL_STUDENT from '@/links/student.js'
import API_URL_TEACHER from '@/links/teacher.js'

const Member ={
    data(){
        return{
            dialog: false,
            dialogDelete: false,
            editedId: -1,
            nameRules: [ v => !!v || 'This field is required',],
            emailRules: [ v => !!v || 'This field is required', v => /.+@.+/.test(v) || 'Invalid email',],
            items: ['Manager', 'Teacher', 'Student'],
            headers: [
                { text: 'No', value: 'id' },
                { text: 'Username', value: 'username' },
                { text: 'First Name', value: 'first_name' },
                { text: 'Last Name', value: 'last_name' },
                { text: 'Address', value: 'address' },
                { text: 'Phone', value: 'phone' },
                { text: 'Email', value: 'email' },
                { text: 'Sex', value: 'sex' },
                { text: 'Role', value: 'role' },
                { text: 'Actions', value: 'actions', sortable: false },
            ],
            member: [],
            teacher: [],
            student: [],
            default:{id:null, username:null, password:null, first_name: null, last_name: null, phone: null, address: null, email: null, sex: null, role:null, active: 'true'},
            editdata:{id:'', username:'', password:'', first_name: '', last_name: '', phone: '', address: '', email: '', sex: '', role:'', active: 'true'},
        }
    },
    methods:{
        async getMember() {
            try{
                const {data} =await axios.get(`${API_URL_USER}`)
                this.member = data.filter(item => item.active !==false)  
            }catch(error){
                console.log(error)
            }
        },
        async getTeacher() {
            try{
                const {data} =await axios.get(`${API_URL_TEACHER}`)
                this.teacher = data.filter(item => item.active !==false )  
            }catch(error){
                console.log(error)
            }
        },
        async getStudent() {
            try{
                const {data} =await axios.get(`${API_URL_STUDENT}`)
                this.student = data.filter(item => item.active !==false )  
            }catch(error){
                console.log(error)
            }
        },
        save(){
            if (this.editedId > -1){
                const role = this.editdata.role
                const username = this.editdata.username
                if (role == 'Teacher'){
                    const teacher = this.teacher.filter(item => item.username == username)[0]
                    axios.put(`${API_URL_TEACHER}${teacher.id}`, this.editdata)
                        .then(response => {
                            this.editedId = -1
                            this.editdata = this.default
                            this.getMember()
                            this.dialog = false
                            console.log(response)
                        })
                        .catch(error => {
                        })
                } else if (role == 'Student'){
                    const student = this.student.filter(item => item.username == username)[0]
                    axios.put(`${API_URL_STUDENT}${student.id}`, this.editdata)
                        .then(response => {
                            this.editedId = -1
                            this.editdata = this.default
                            this.getMember()
                            this.dialog = false
                            console.log(response)
                        })
                        .catch(error => {
                        })
                }
            } else {
                const existingUser = this.member.find(
                    item => item.username === this.editdata.username || item.email === this.editdata.email
                )
                if (existingUser) {
                    alert('Account or email already in use!')
                    return
                }
                else if (!existingUser)
                    if (this.editdata.role === 'Student') {
                        axios.post(`${API_URL_STUDENT}`, this.editdata)
                        .then(response => {
                            this.editedId = -1
                            this.editdata = this.default
                            this.getMember()
                            this.dialog = false
                        })
                        .catch(error => {
                        })
                    } else if (this.editdata.role === 'Teacher') {
                        axios.post(`${API_URL_TEACHER}`, this.editdata)
                        .then(response => {
                            this.editedId = -1
                            this.editdata = this.default
                            this.getMember()
                            this.dialog = false
                            console.log(response)
                        })
                        .catch(error => {
                        })
                    }
            }
        },
        close(){
            this.editedId = -1
            this.editdata = this.default
            this.dialog = false
        },
        editItem(item){
            this.editedId = item
            const data = this.member.filter(a => a.id == item)
            this.editdata = data[0]
            this.dialog = true
        },
        deleteItem(item) {
            this.editedId = item
            this.dialogDelete = true
        },
        deleteItemConfirm(){
            axios.delete(`${API_URL_USER}${this.editedId}`)
            .then(response => {
                this.dialogDelete = false
                this.getMember()
                console.log(response)
            })
            .catch(error => {
            })
            const member = this.member.filter(item => item.id == this.editedId)
            const role = member[0].role
            const username = member[0].username
            if (role == 'Teacher'){
                    const teacher = this.teacher.filter(item => item.username == username)[0]
                    axios.delete(`${API_URL_TEACHER}${teacher.id}`)
                        .then(response => {
                            this.editedId = -1
                            this.getMember()
                            this.dialog = false
                            console.log(response)
                        })
                        .catch(error => {
                        })
                } else if (role == 'Student'){
                    const student = this.student.filter(item => item.username == username)[0]
                    axios.delete(`${API_URL_STUDENT}${student.id}`)
                        .then(response => {
                            this.editedId = -1
                            this.getMember()
                            this.dialog = false
                            console.log(response)
                        })
                        .catch(error => {
                        })
                }
        }
    },
    computed: {
      formTitle () {
        return this.editedId === -1 ? 'New member' : 'Edit member'
      }
    },
    mounted(){
        this.getMember()
        this.getTeacher()
        this.getStudent()
    }
}
export default Member
</script>