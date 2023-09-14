<template>
    <div class="bg-white shadow-lg">
        <div class="flex justify-end items-center border-b-2 w-full h-[75px]">
            <div class="pr-[5px]">
                <v-icon class="pr-[10px]" color="#0f766e">mdi-bell</v-icon>
                <v-icon class="pr-[10px]" color="#0f766e">mdi-account-circle-outline</v-icon>
                <span class="font-medium">{{data.first_name}} {{ data.last_name }}</span>
                <v-menu bottom left>
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn icon v-bind="attrs" v-on="on">
                            <v-icon>mdi-dots-vertical</v-icon>
                        </v-btn>
                    </template>

                    <template>
                        <v-card class="mx-auto" max-width="300" height="100%">
                            <v-list>
                                <v-list-item-group color="#134e4a">
                                    <v-list-item  @click="pick1(item.text)" v-for="(item, i) in logout" :key="i">
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
                </v-menu>
            </div>
        </div>
    </div>
</template>

<script>
import jwtDecode from 'jwt-decode'
const Header = {
    data(){
        return{
            data: [],
            logout: [
                // {icon: 'mdi-cog',text: 'Cài đặt & quyền riêng tư'},
                // {icon: 'mdi-help-circle-outline',text: 'Trợ giúp & hỗ trợ'},
                // {icon: 'mdi-weather-night',text: 'Màn hình & trợ năng'},
                {icon: 'mdi-logout',text: 'Đăng xuất'},
            ],
        }
    },
    methods:{
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
        pick1(item){
            const selectedItem = this.logout.find(a => a.text === item);
            if (selectedItem && selectedItem.text === 'Đăng xuất') {
                localStorage.removeItem('token')
                this.$router.push('/login')
            }
        }
    },
    mounted(){
      this.getAccount()
    }
}
export default Header
</script>