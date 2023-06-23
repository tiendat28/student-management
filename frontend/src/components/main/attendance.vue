<template>
    <div class="p-8">
        <div class="flex">
            <v-icon class="pr-3">mdi-home</v-icon>
            <h1 class="font-bold text-lg">Điểm danh</h1>
        </div>
        <div class="flex py-4">
            <h1 class="pr-[200px]">Tên lớp: </h1>
            <h1>Sĩ số: {{ arrayLength }}</h1>
        </div>
        <div>
            <v-dialog v-model="dialog" persistent max-width="450px">
                <template v-slot:activator="{ on, attrs }">
                    <div class="flex justify-center">
                        <v-btn color="#0f766e" dark v-bind="attrs" v-on="on">Điểm danh</v-btn>
                    </div>
                </template>
                <v-card class="w-[450px] h-[500px]">
                    <v-card-title class="bg-teal-700">
                        <span class="text-h5">Điểm danh </span>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
                                <v-col v-for="item in data" :key="item.id" cols="12" sm="6" md="6">
                                    <v-select :label="item.surname + ' '+ item.name " :items="items"></v-select>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                    <div class="flex justify-center">
                        <v-btn color="green darken-1" text @click="post()">Lưu</v-btn>
                        <v-btn color="red darken-1" text @click="dialog = false">Đóng</v-btn>
                    </div>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </div>
        <div class="py-4">
            <template>
                <div class="flex justify-center">
                    <v-data-table :headers="headers" :items="students" :items-per-page="5" class="elevation-4 ">
                        <template v-slot:item.actions="{ item }">
                            <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
                            <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
                        </template>
                    </v-data-table>
                </div>
            </template>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import API_URL from '@/links/index.js'
const Attendance ={
    data(){
        return{
            dialog: false,
            data: [],
            items: ['Đúng giờ', 'Nghỉ có phép', 'Nghỉ không phép'],
            headers: [
                { text: 'Date', value: 'date'},
                { text: 'Mai Tiến Đạt', value: 'dat'},
                { text: 'Mai Tiến Đạt', value: 'dat'},
                { text: 'Mai Tiến Đạt', value: 'dat'},
                { text: 'Mai Tiến Đạt', value: 'dat'},
                { text: 'Mai Tiến Đạt', value: 'dat'},
                { text: 'Mai Tiến Đạt', value: 'dat'},
                { text: 'Actions', value: 'actions' },
            ],
            students: [
                {
                    date: '01-07-2023',
                    dat: 'Đi học'
                },
                {
                    date: '02-07-2023',
                    dat: 'Nghỉ học'
                    
                }
            ]
        }
    },
    methods:{
        Show() {
            this.showPassword = !this.showPassword
        },
        async getLogin(){
            try{
                const {data} =await axios.get(`${API_URL}`)
                this.data = data.filter(item => item.active !==false )
            }catch(error){
                console.log(error)
            }
        }
    },
    computed: {
        arrayLength() {
        return this.data.length;
        }
    },
    mounted(){
      this.getLogin()
    }
}
export default Attendance
</script>