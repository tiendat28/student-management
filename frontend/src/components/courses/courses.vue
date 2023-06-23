<template>
    <div>
        <Header></Header>
        <div class="p-8">
            <div class="flex">
                <div class="pr-[10px]">
                    <v-btn color="#0f766e" dark>+ Thêm lớp</v-btn>
                </div>
                <div>
                    <v-btn color="#0f766e" dark>+ Button2</v-btn>
                </div>
            </div>
            <div class="flex py-[20px]">
                <v-icon class="pr-[10px]">mdi-menu</v-icon>
                <h1 class="font-bold text-lg">Danh sách lớp</h1>
            </div>
            <div class="grid gap-2">
                <div class="flex flex-wrap">
                    <div @click="move(item.id)" v-for="item in data" :key="item.id" class="m-2 rounded-md border-2 border-green-400 w-[340px]">
                        <v-btn height="50px" class="w-[340px] flex justify-start">
                            <div class="w-[40px] h-[40px] py-[5px] bg-green-300 rounded-full">
                                <v-icon color="#134e4a">{{ item.icon }}</v-icon>
                            </div>
                            <h1 class="pl-[15px]">{{ item.class }}</h1>
                        </v-btn>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Header from '@/components/header/header.vue'
const Courses = {
    data(){
        return{
            data: [
                {id: 1, icon:'mdi-account-group', class: 'Lớp 1'},
                {id: 2, icon:'mdi-account-group', class: 'Lớp 2'},
                {id: 3, icon:'mdi-account-group', class: 'Lớp 3'},
                {id: 4, icon:'mdi-account-group', class: 'Lớp 4'},
                {id: 5, icon:'mdi-account-group', class: 'Lớp 5'},
                {id: 6, icon:'mdi-account-group', class: 'Lớp 6'},
                {id: 7, icon:'mdi-account-group', class: 'Lớp 7'},
                {id: 8, icon:'mdi-account-group', class: 'Lớp 8'},
                {id: 9, icon:'mdi-account-group', class: 'Lớp 9'},
                {id: 10, icon:'mdi-account-group', class: 'Lớp 1a'},
                {id: 11, icon:'mdi-account-group', class: 'Lớp 2a'},
                {id: 12, icon:'mdi-account-group', class: 'Lớp 4a'},
                {id: 13, icon:'mdi-account-group', class: 'Lớp 1b'},
                {id: 14, icon:'mdi-account-group', class: 'Lớp 2b'},
            ],
        }
    },
    methods: {
        move(item){
            const c = this.data.filter(a => a.id == item)
            this.$router.push('/home')
        }
    },
    components: {
        Header
    }
}
export default Courses
</script>