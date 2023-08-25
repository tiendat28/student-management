<template>
    <div>
        <div class="flex w-full h-[calc(100vh-60px)]">
            <div class="bg-slate-100 w-[90px] h-full">
                <div class="flex flex-col justify-between items-center py-0 hover">
                    <router-link class="flex flex-col py-3" v-for="(item, index) in items" :key="index" :to="{ name: item.name, params: { name: item.name }}">
                        <v-icon :size="30">{{ item.icon }}</v-icon>
                        <span class="text-sm">{{ item.text }}</span>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
const Navigation = {
    data(){
        return{
            items: [
                {icon: 'mdi-home-outline',text: 'Trang chủ', name: 'T_homepage'},
                {icon: 'mdi-chat-processing-outline',text: 'Trò chuyện', name: 'T_chat'},
                {icon: 'mdi-account-group',text: 'Lớp học', name: 'T_courses'},
                {icon: 'mdi-bell-ring-outline',text: 'Thông báo'},
                {icon: 'mdi-sword-cross',text: 'Bài Tập', name: 'T_assignment'},
                {icon: 'mdi-file-alert-outline',text: 'File', name: 'T_file'},
                {icon: 'mdi-book-edit-outline',text: 'Kết quả'},
                {icon: 'mdi-flip-horizontal',text: 'Tự học'},
            ]
        }
    },
    methods: {

    }
} 
export default Navigation
</script>
<style scoped>
.v-application a {
    color:#475569
}
.hover :hover{
    color: #34d399;
    font-weight: 600 ;
}
.v-list-item {
    padding: 0;
}
</style>
