<template>
    <div class="flex w-full">
        <div class="bg-slate-200 w-[30%] h-full" style="box-shadow: 5px 5px 5px 5px rgba(0, 0, 0, 0.4)">
            <div class="h-[80px] flex justify-between items-center px-6 border-b-2 border-[#cbd5e1]">
                <div class="text-2xl font-bold">Trò chuyện</div>
                <div>
                    <v-icon>mdi-cast</v-icon>
                </div>
            </div>
            <div class="pt-3 px-1">
                <div>
                    <v-icon>mdi-triangle-small-down</v-icon>
                    <span class="font-light">Đã ghim</span>
                </div>
                <div class="flex justify-start items-center h-[60px] pl-6 hover:bg-white rounded-lg">
                    <div>
                        <v-img class="w-[45px] h-[45px] rounded-full" :src="require('@/assets/dat.jpg')"></v-img>
                    </div>
                    <span class="pl-2 text-lg">Mai Tiến Đạt (Bạn)</span>
                </div>
            </div>
            <div class="pt-3 px-1">
                <div>
                    <v-icon>mdi-triangle-small-down</v-icon>
                    <span class="font-light">Gần đây</span>
                </div>
                <div class="flex justify-start items-center h-[60px] pl-6 bg-white rounded-lg">
                    <div>
                        <v-img class="w-[45px] h-[45px] rounded-full" :src="require('@/assets/nam.jpg')"></v-img>
                    </div>
                    <span class="pl-2 text-lg">Lê Hoàng Nam</span>
                </div>
                <div class="flex justify-start items-center h-[60px] pl-6 hover:bg-white rounded-lg">
                    <div>
                        <v-img class="w-[45px] h-[45px] rounded-full" :src="require('@/assets/hoang.jpg')"></v-img>
                    </div>
                    <span class="pl-2 text-lg">Phạm Long Hoàng</span>
                </div>
                <div class="flex justify-start items-center h-[60px] pl-6 hover:bg-white rounded-lg">
                    <div>
                        <v-img class="w-[45px] h-[45px] rounded-full" :src="require('@/assets/bang.jpg')"></v-img>
                    </div>
                    <span class="pl-2 text-lg">Trần Xuân Bảng</span>
                </div>
            </div>
        </div>
        <div class="bg-gray-100 w-full h-full">
            <div class="h-[80px] flex justify-between items-center px-8 border-b-2 border-[#cbd5e1]">
                <div class="flex justify-start items-center h-[60px] hover:bg-white rounded-lg">
                    <div>
                        <v-img class="w-[45px] h-[45px] rounded-full" :src="require('@/assets/nam.jpg')"></v-img>
                    </div>
                    <span class="pl-2 text-lg">Lê Hoàng Nam</span>
                </div>
                <div>
                    <v-icon>mdi-phone</v-icon>
                    <v-icon class="px-3">mdi-video-outline</v-icon>
                    <v-icon> mdi-account-multiple-plus-outline</v-icon>
                </div>
            </div>
            <div class="relative top-0 left-[90px] overflow-auto table-reponsive bg-gray-100 w-[85%] h-[700px]">
            <div v-for="item in chat" :key="item.id">
                    <div class="flex pt-4">
                        <div class="flex justify-center items-center">
                            <v-img class="w-[45px] h-[45px] rounded-full" :src="require('@/assets/nam.jpg')"></v-img>
                        </div>
                        <div class="pl-2">
                            <span class="text-md">Lê Hoàng Nam</span>
                            <p class="bg-white rounded-md px-3 py-2">{{ item.person_1 }}</p>
                        </div>
                    </div>
                    <div class="flex pt-4 justify-end">
                        <div class="pl-[150px] pr-2">
                            <span class="flex justify-end text-md">Mai Tiến Đạt</span>
                            <p class="bg-blue-100  rounded-md px-3 py-2 flex justify-end">{{ item.person_2 }}</p>
                        </div>
                        <div class="flex justify-center items-center">
                            <v-img class="w-[45px] h-[45px] rounded-full" :src="require('@/assets/dat.jpg')"></v-img>
                        </div>
                    </div> 
                </div> 
            </div>
            <div class="pt-8">
                <div class="px-[10%]">
                    <v-text-field width="100%" label="Nhập tin nhắn mới" solo hide-details></v-text-field>
                </div>
                <div class="flex justify-between items-center px-[10%] pt-3">
                    <div>
                        <v-icon>mdi-cube-scan</v-icon>
                        <v-icon class="px-2"> mdi-attachment</v-icon>
                        <v-icon class="pr-2">mdi-emoticon-happy-outline</v-icon>
                        <v-icon>mdi-sticker-emoji</v-icon>
                    </div>
                    <v-icon>mdi-send</v-icon>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
const Chat = {
data(){
    return{
        chat:[
            {person_1:'LOL k?', person_2: 'oki' },
            {person_1:'chơi căp j?', person_2: 'Yasua Yone' },
            {person_1:'oki', person_2: 'zô' },
            {person_1:'m pv intern chưa?', person_2: 'gửi cv r' },
            {person_1:'um', person_2: 'mong pass' },
            {person_1:'ổn thôi', person_2: 'muốn vào cty đó v :(((' },
        ]
    }
}
}
export default Chat
</script>

<style scoped>
.v-application p {
    margin-bottom: 0px;
}
</style>