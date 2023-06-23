<template>
    <div>
        <div class="flex w-full h-[calc(100vh-60px)]">
            <div class=" w-[300px] h-full">
                <template>
                    <v-card class="mx-auto" max-width="300" height="100%">
                        <v-list class="p-0">
                            <v-list-item-group mandatory color="#134e4a">
                                <v-list-item  @click="pick(item.text)" v-for="(item, i) in items" :key="i">
                                    <v-list-item-icon>
                                        <v-icon>{{ item.icon }}</v-icon>
                                    </v-list-item-icon>

                                    <v-list-item-content>
                                        <v-list-item-title>{{ item.text }}</v-list-item-title>
                                    </v-list-item-content>
                                </v-list-item>
                            </v-list-item-group>
                        </v-list>
                    </v-card>
                </template>
            </div>
            <div class="w-full h-full">
                <component :is="selectedComponent"></component>
            </div>
        </div>
    </div>
</template>

<script>
import HomePage from '@/components/main/homepage.vue'
import Attendance from '@/components/main/attendance.vue'
import Scores from '@/components/main/scores.vue'
import Notifications from '@/components/main/notifications.vue'
import Homework from '@/components/main/homework.vue'
import FileAssign from '@/components/main/fileassign.vue'
import Results from '@/components/main/results.vue'
import SeltLearn from '@/components/main/seltlearn.vue'
const Navigation = {
    data(){
        return{
            items: [
                {icon: 'mdi-home',text: 'Trang chủ'},
                {icon: 'mdi-comment-account',text: 'Điểm danh'},
                {icon: 'mdi-book-account-outline',text: 'Điểm số'},
                {icon: 'mdi-bell-ring',text: 'Thông báo'},
                {icon: 'mdi-sword-cross',text: 'Giao Bài Tập'},
                {icon: 'mdi-file-alert-outline',text: 'Giao Bài Tập File'},
                {icon: 'mdi-book-edit-outline',text: 'Kết quả làm bài'},
                {icon: 'mdi-flip-horizontal',text: 'Tự học'},
            ],
            selectedComponent: HomePage,
        }
    },
    methods:{
        pick(item){
            const mapping = {
                'Trang chủ': HomePage,
                'Điểm danh': Attendance,
                'Điểm số': Scores,
                'Thông báo': Notifications,
                'Giao Bài Tập': Homework,
                'Giao Bài Tập File': FileAssign,
                'Kết quả làm bài': Results,
                'Tự học': SeltLearn
            };

            const selectedItem = this.items.find(a => a.text === item);
            if (selectedItem) {
                this.selectedComponent = mapping[selectedItem.text] || null;
            } else {
                this.selectedComponent = null;
            }
        }
    },
    components:{
        HomePage,
        Attendance,
        Scores,
        Notifications,
        Homework,
        FileAssign,
        Results,
        SeltLearn
    },
    mounted(){
    
    }
} 
export default Navigation
</script>