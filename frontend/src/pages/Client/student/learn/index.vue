<template>
    <div class="w-full h-screen">
        <div class="bg-slate-200 w-full h-full">
            <div class="p-8">
                <div class="flex text-2xl font-semibold mb-8 px-10 justify-between items-center">
                    <div>
                        <h1 class="font-bold text-3xl">Todo List</h1>
                    </div>
                    <div>
                        <v-btn color="#0f766e" dark @click="CreateOrUpdate(0)"> + Nhiệm vụ</v-btn>
                    </div>
                </div>
                <div class="flex justify-center">
                    <div class="pr-8">
                        <div class="relative overflow-x-hidden shadow-sm table-reponsive">
                            <div class="w-[400px] flex flex-col">
                                <div v-for="item in todolist" :key="item.id" class="pb-6">
                                    <div class="bg-white w-[400px] p-8">
                                        <div class="pb-3">
                                            <span class="text-lg font-medium">{{ item.subject.name }}</span>
                                        </div>
                                        <div class="py-2 flex" v-for="item in item.task" :key="item.id">
                                            <input class="w-[20px] h-[20px]" type="checkbox" v-model="item.status">
                                            <span v-if="item.status === true" class="px-2 text-base checked">{{ item.name }}</span>
                                            <span v-if="item.status === false" class="px-2 text-base">{{ item.name }}</span>
                                        </div>
                                    </div>
                                </div> 
                            </div>
                        </div>
                        <!-- <div class="py-2">
                            <v-btn class="w-full" color="#0f766e" dark @click="Save()">Lưu lại</v-btn> 
                        </div> -->
                    </div>
                    <div class="relative overflow-x-hidden shadow-sm table-reponsive">
                        <div class="bg-white w-[1400px]">
                            <table class="w-full text-sm text-left text-gray-500 whitespace-nowrap">
                                <thead class="text-base sticky top-0 z-50 text-teal-700 bg-gray-300">
                                    <tr>
                                        <th scope="col" class="px-6 py-3">STT</th>
                                        <th scope="col" class="px-6 py-3">Thời gian</th>
                                        <th scope="col" class="px-6 py-3">Nhiệm vụ</th>
                                        <th scope="col" class="px-6 py-3">Lớp học</th>
                                        <th scope="col" class="px-6 py-3">Mức độ</th>
                                        <th scope="col" class="px-6 py-3">Trạng thái</th>
                                        <th scope="col" class="px-6 py-3 flex justify-end">Hành động</th>
                                    </tr>
                                </thead>
                                <tbody v-for="i in todolist" :key="i.id">
                                    <tr v-for="(item, index) in i.task" :key="item.id" class="bg-white border-b-2 text-base ">
                                        <td scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap ">{{ index + 1 }}</td>
                                        <td class="px-6 py-4">{{ item.time }}</td>
                                        <td class="px-6 py-4">{{ item.name }}</td>
                                        <td class="px-6 py-4">{{ i.subject.name }}</td>
                                        <td class="px-6 py-4">{{ item.level }}</td>
                                        <td v-if="item.status == true" class="px-6 py-4 text-green-400">Done</td>
                                        <td v-if="item.status == false" class="px-6 py-4 text-red-400">No Done</td>
                                        <td class="pr-8 py-4 flex justify-end">
                                            <v-icon height="40px" color="red" @click="handleDelete(item.id)"> mdi-delete</v-icon>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import router from '@/router/index.ts'
import jwtDecode from 'jwt-decode'
import API_URL_TODOLIST from '@/links/todolist.js'
const Todolist = {
    data() {
        return {
            data: [],
            todolist: [],
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
        async getTodoList(){
            try{
                const id = this.data.id
                const {data} = await axios.get(`${API_URL_TODOLIST}${id}`)
                this.todolist = data  
            }catch(error){
                console.log(error)
            }
        },
        // Save(){
        //     axios.post(`${API_URL_todolist}`, this.addtodolist)
        //     .then(response => {
        //         this.upcoming = true
        //         this.getQuestions()
        //         this.addQuestions = this.default
        //         console.log(response)
        //     })
        //     .catch(error => {
        //     })
        // },
        CreateOrUpdate(id){
            router.push({
                name: 'S_selt_learn_edit',
                params:{
                    id: id
                }
            })
        }
    },
    mounted(){
        this.getAccount()
        this.getTodoList()
    },

}
export default Todolist
</script>

<style scoped>
.table-reponsive {
    max-height: calc(100vh - 180px);
}
.checked {
  text-decoration: line-through; 
  color: #999; 
}
</style>