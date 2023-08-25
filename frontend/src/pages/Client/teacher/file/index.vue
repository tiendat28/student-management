<template>
    <div class="flex w-full">
        <div class="bg-slate-200 w-[28%] h-screen">
            <div class="h-[80px] flex justify-start items-center text-2xl font-semibold px-6">
                File
            </div>
            <div class="px-2">
                <div @click="Home()" v-bind:class="{ 'bg-white font-semibold border-l-4 border-teal-600': home }" class="flex justify-start items-center rounded-md text-lg font-light px-1 h-[50px] hover:bg-white">
                    <v-icon :size="30">mdi-home-outline</v-icon>
                    <span class="px-3">Trang chủ</span>
                </div>
                <div @click="File()" v-bind:class="{ 'bg-white font-semibold border-l-4 border-teal-600': file }" class="flex justify-start items-center rounded-md text-lg font-light px-3 h-[50px] hover:bg-white">
                    <v-icon :size="30">mdi-folder-file-outline</v-icon>
                    <span class="px-3">File của tôi</span>
                </div>
                <div @click="Share()" v-bind:class="{ 'bg-white font-semibold border-l-4 border-teal-600': share }" class="flex justify-start items-center rounded-md text-lg font-light px-3 h-[50px] hover:bg-white ">
                    <v-icon :size="30">mdi-share-variant</v-icon>
                    <span class="px-3">Đã chia sẻ</span>
                </div>
            </div>
            <div class="py-8 px-2">
                <div class="text-xl p-4">Truy cập nhanh</div>
                <div v-for="item in classdata" :key="item.subject_id"  class="flex justify-start items-center h-[50px] rounded-md hover:bg-white w-full px-3">
                    <div class="w-[30px] h-[30px] text-white text-xs flex justify-center items-center bg-green-600">  
                        TĐ  
                    </div>
                    <span class="px-3 text-xl">{{ item.name }} ___ (Khóa học nâng cao)</span>
                </div>
            </div>
        </div>
        <div v-show="home" class="w-full h-screen">
            <div class="bg-white h-[70px] flex justify-start items-center px-4 border-b-2">
                <div class="text-xl text-white w-[140px] h-[40px] bg-teal-600 flex justify-center items-center rounded-md">
                    <div class="px-3">
                        <v-icon class="px-2" color="white">mdi-plus</v-icon>
                        <span>Mới</span>
                        <v-icon class="px-2" color="white">mdi-chevron-down</v-icon>
                    </div>
                </div>
                <div class="px-4 flex justify-center items-center">
                    <v-file-input hide-input prepend-icon="mdi-arrow-collapse-up" show-size truncate-length="10"></v-file-input>
                    <span class="text-xl">Tải lên</span>
                </div>
            </div>
            <div class="px-8 pt-10">
                <span class="text-2xl">Gần đây</span>
                <div class="flex justify-start items-center py-6">
                    <div class="pr-3">
                        <div class="w-[100px] h-[40px] bg-gray-200 rounded-3xl flex items-center justify-center">
                            <v-icon>mdi-view-headline</v-icon>
                            <span class="pl-2">Tất cả</span>
                        </div>
                    </div>
                    <div class="pr-3">
                        <div class="w-[100px] h-[40px] bg-gray-200 rounded-3xl flex items-center justify-center">
                            <div class="w-[30px] h-[40px] flex justify-center items-center pr-2">
                                <v-img :src="require('@/assets/image/word.png')"></v-img>
                            </div>  
                            <span>Word</span>
                        </div>
                    </div>
                    <div class="pr-3">
                        <div class="w-[100px] h-[40px] bg-gray-200 rounded-3xl flex items-center justify-center">
                            <div class="w-[30px] h-[40px] flex justify-center items-center pr-2">
                                <v-img :src="require('@/assets/image/excel.png')"></v-img>
                            </div> 
                            <span>Excel</span>
                        </div>
                    </div>
                    <div class="pr-3">
                        <div class="w-[150px] h-[40px] bg-gray-200 rounded-3xl flex items-center justify-center">
                            <div class="w-[30px] h-[40px] flex justify-center items-center pr-2">
                                <v-img :src="require('@/assets/image/pp.png')"></v-img>
                            </div> 
                            <span>Powerpoint</span>
                        </div>
                    </div>
                    <div class="pr-3">
                        <div class="w-[100px] h-[40px] bg-gray-200 rounded-3xl flex items-center justify-center">
                            <div class="w-[30px] h-[40px] flex justify-center items-center pr-2">
                                <v-img :src="require('@/assets/image/pdf.png')"></v-img>
                            </div> 
                            <span>PDF</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="relative overflow-auto table-reponsive px-8 pt-4">
                <table class="w-full border-2 shadow-sm text-left text-gray-500">
                    <thead class="sticky top-[-20px] z-50 text-base text-gray-700 bg-gray-100">
                        <tr>
                            <th scope="col" class="px-6 py-3">Tên</th>
                            <th scope="col" class="px-6 py-3">Đã mở</th>
                            <th scope="col" class="px-6 py-3">Chủ sở hữu</th>
                            <th scope="col" class="px-6 py-3">Hoạt động</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in documents" :key="item.id" class="bg-white border-b ">
                            <td class="px-6 py-2">
                                <div class="flex justify-start items-center">
                                    <div class="w-[50px] h-[60px] flex justify-center items-center pr-2">
                                        <v-img :src="item.image"></v-img>
                                    </div> 
                                    <div class="flex flex-col">
                                        <span class="text-lg font-medium">{{ item.title }}</span>
                                        <span class="text-sm">{{ item.detail }}</span>
                                    </div>
                                </div>
                            </td>
                            <td class="px-6 py-4">{{ item.open }}</td>
                            <td class="px-6 py-4">{{ item.name }}</td>
                            <td class="px-6 py-4">{{ item.status }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div v-show="file" class="w-full h-screen">
            <div class="bg-white h-[70px] flex justify-start items-center px-4 border-b-2">
                <div class="text-xl text-white w-[140px] h-[40px] bg-teal-600 flex justify-center items-center rounded-md">
                    <div class="px-3">
                        <v-icon class="px-2" color="white">mdi-plus</v-icon>
                        <span>Mới</span>
                        <v-icon class="px-2" color="white">mdi-chevron-down</v-icon>
                    </div>
                </div>
                <div class="px-4 flex justify-center items-center">
                    <v-file-input hide-input prepend-icon="mdi-arrow-collapse-up" show-size truncate-length="10"></v-file-input>
                    <span class="text-xl">Tải lên</span>
                </div>
            </div>
            <div class="px-8 pt-10">
                <span class="text-2xl">OneDrive</span>
            </div>
            <div class="relative overflow-auto table-reponsive1 px-8 pt-8">
                <table class="w-full border-2 shadow-sm text-left text-gray-500">
                    <thead class="sticky top-[-35px] z-50 text-base text-gray-700 bg-gray-100">
                        <tr>
                            <th scope="col" class="px-6 py-3">Tên</th>
                            <th scope="col" class="px-6 py-3">Đã mở</th>
                            <th scope="col" class="px-6 py-3">Chủ sở hữu</th>
                            <th scope="col" class="px-6 py-3">Hoạt động</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in documents" :key="item.id" class="bg-white border-b ">
                            <td class="px-6 py-2">
                                <div class="flex justify-start items-center">
                                    <div class="w-[50px] h-[60px] flex justify-center items-center pr-2">
                                        <v-img :src="item.image"></v-img>
                                    </div> 
                                    <div class="flex flex-col">
                                        <span class="text-lg font-medium">{{ item.title }}</span>
                                        <span class="text-sm">{{ item.detail }}</span>
                                    </div>
                                </div>
                            </td>
                            <td class="px-6 py-4">{{ item.open }}</td>
                            <td class="px-6 py-4">{{ item.name }}</td>
                            <td class="px-6 py-4">{{ item.status }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div v-show="share" class="w-full h-screen">
            <div class="bg-white h-[70px] flex justify-start items-center px-4 border-b-2">
                <div class="text-xl px-3 text-white h-[40px] bg-teal-600 flex justify-center items-center rounded-xl">
                    <span>Được chia sẻ với bạn</span>
                </div>
                <div class="px-4 text-xl flex justify-center items-center hover:rounded-3xl hover:bg-slate-300 h-[40px]">
                    <span>Do bạn chia sẻ</span>
                </div>
            </div>
            <div class="px-8 pt-10">
                <span class="text-2xl">Gần đây</span>
                <div class="flex justify-start items-center py-6">
                    <div class="pr-3">
                        <div class="w-[100px] h-[40px] bg-gray-200 rounded-3xl flex items-center justify-center">
                            <v-icon>mdi-view-headline</v-icon>
                            <span class="pl-2">Tất cả</span>
                        </div>
                    </div>
                    <div class="pr-3">
                        <div class="w-[100px] h-[40px] bg-gray-200 rounded-3xl flex items-center justify-center">
                            <div class="w-[30px] h-[40px] flex justify-center items-center pr-2">
                                <v-img :src="require('@/assets/image/word.png')"></v-img>
                            </div>  
                            <span>Word</span>
                        </div>
                    </div>
                    <div class="pr-3">
                        <div class="w-[100px] h-[40px] bg-gray-200 rounded-3xl flex items-center justify-center">
                            <div class="w-[30px] h-[40px] flex justify-center items-center pr-2">
                                <v-img :src="require('@/assets/image/excel.png')"></v-img>
                            </div> 
                            <span>Excel</span>
                        </div>
                    </div>
                    <div class="pr-3">
                        <div class="w-[150px] h-[40px] bg-gray-200 rounded-3xl flex items-center justify-center">
                            <div class="w-[30px] h-[40px] flex justify-center items-center pr-2">
                                <v-img :src="require('@/assets/image/pp.png')"></v-img>
                            </div> 
                            <span>Powerpoint</span>
                        </div>
                    </div>
                    <div class="pr-3">
                        <div class="w-[100px] h-[40px] bg-gray-200 rounded-3xl flex items-center justify-center">
                            <div class="w-[30px] h-[40px] flex justify-center items-center pr-2">
                                <v-img :src="require('@/assets/image/pdf.png')"></v-img>
                            </div> 
                            <span>PDF</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="relative overflow-auto table-reponsive px-8 pt-4">
                <table class="w-full border-2 shadow-sm text-left text-gray-500">
                    <thead class="sticky top-[-20px] z-50 text-base text-gray-700 bg-gray-100">
                        <tr>
                            <th scope="col" class="px-6 py-3">Tên</th>
                            <th scope="col" class="px-6 py-3">Đã mở</th>
                            <th scope="col" class="px-6 py-3">Chủ sở hữu</th>
                            <th scope="col" class="px-6 py-3">Hoạt động</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in documents" :key="item.id" class="bg-white border-b ">
                            <td class="px-6 py-2">
                                <div class="flex justify-start items-center">
                                    <div class="w-[50px] h-[60px] flex justify-center items-center pr-2">
                                        <v-img :src="item.image"></v-img>
                                    </div> 
                                    <div class="flex flex-col">
                                        <span class="text-lg font-medium">{{ item.title }}</span>
                                        <span class="text-sm">{{ item.detail }}</span>
                                    </div>
                                </div>
                            </td>
                            <td class="px-6 py-4">{{ item.open }}</td>
                            <td class="px-6 py-4">{{ item.name }}</td>
                            <td class="px-6 py-4">{{ item.status }}</td>
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
import jwtDecode from 'jwt-decode'
const File = {
    data(){
        return{
            home: true,
            file: false,
            share: false,
            classdata: [],
            data: [],
            documents: [
                {image: 'https://png.pngtree.com/element_our/sm/20180627/sm_5b33460fe6357.jpg', title: 'Project Apply Otani', detail: 'Tệp của tôi', open: '4 thg 8', name: 'Mai Tiến Đạt', status:'Đã chỉnh sửa'},
                {image: 'https://images.freeimages.com/fic/images/icons/2795/office_2013_hd/2000/excel.png', title: 'Tiểu luận CNĐH', detail: 'Công nghệ điện hóa', open: '1 thg 8', name: 'Lê Long Vũ', status:''},
                {image: 'https://i.pinimg.com/474x/ab/22/6b/ab226b187fb0ae19473680a22bf0f45d.jpg', title: 'BTL ĐHBM', detail: 'Điện hóa bề mặt', open: '17 thg 7', name: 'Nguyễn Thùy Trang', status:'Đã chỉnh sửa'},
                {image: 'https://www.citypng.com/public/uploads/preview/pdf-file-document-red-icon-png-11664499159d22efvkxoy.png', title: 'BTN CN Mạ', detail: 'Công nghệ mạ', open: '15 thg 7', name: 'Mai Tiến Đạt', status:'Đã chỉnh sửa'},
                {image: 'https://images.freeimages.com/fic/images/icons/2795/office_2013_hd/2000/excel.png', title: 'Đồ án chuyên ngành', detail: 'Đã chia sẻ', open: '1 thg 6', name: 'Mai Tiến Đạt', status:'Đã chỉnh sửa'},
                {image: 'https://www.citypng.com/public/uploads/preview/pdf-file-document-red-icon-png-11664499159d22efvkxoy.png', title: 'BTL Javascrip', detail: 'Tệp của tôi', open: '15 thg 5', name: 'Mai Tiến Đạt', status:''},
                {image: 'https://images.freeimages.com/fic/images/icons/2795/office_2013_hd/2000/excel.png', title: 'BTL Python', detail: 'Đã chia sẻ', open: '3 thg 5', name: 'Mai Tiến Đạt', status:'Đã chỉnh sửa'},
                {image: 'https://png.pngtree.com/element_our/sm/20180627/sm_5b33460fe6357.jpg', title: 'BTL VueJS', detail: 'Tệp của tôi', open: '24 tg 4', name: 'Mai Tiến Đạt', status:'Đã chỉnh sửa'},
                {image: 'https://images.freeimages.com/fic/images/icons/2795/office_2013_hd/2000/excel.png', title: 'Fast API SQLALchemy', detail: 'Tệp của tôi', open: '6 thg  4', name: 'Mai Tiến Đạt', status:''},
                {image: 'https://images.freeimages.com/fic/images/icons/2795/office_2013_hd/2000/excel.png', title: 'Vue Vuetify2', detail: 'Đã chia sẻ', open: '27 thg 3', name: 'Mai Tiến Đạt', status:'Đã chỉnh sửa'},
                {image: 'https://www.citypng.com/public/uploads/preview/pdf-file-document-red-icon-png-11664499159d22efvkxoy.png', title: 'CSS Tailwind', detail: 'Tệp của tôi', open: '28 thg 2', name: 'Mai Tiến Đạt', status:'Đã chỉnh sửa'},
                {image: 'https://png.pngtree.com/element_our/sm/20180627/sm_5b33460fe6357.jpg', title: 'Database Postgresql', detail: 'Tệp của tôi', open: '1 thg 2', name: 'Mai Tiến Đạt', status:'Đã chỉnh sửa'},
            ]
        }
    },
    methods: {
        async getTeacher(){
            const token = localStorage.getItem('token')
            try{
                const decodedToken = jwtDecode(token)
                this.data = decodedToken
            }catch(error){
                console.log(error)
            }
        },
        async getCourses() {
            try{
                const teacher_id = this.data.id
                const {data} =await axios.get(`${API_URL_SUBJECT}${'subject_of_user'}${'/'}${teacher_id}`)
                this.classdata = data[0].subject
            }catch(error){
                console.log(error)
            }
        },
        Home(){
            this.home = true
            this.file = false
            this.share = false
        },
        File(){
            this.home = false
            this.file = true
            this.share = false
        },
        Share(){
            this.home = false
            this.file = false
            this.share = true
        },
    },
    mounted(){
        this.getTeacher()
        this.getCourses()
    }
}
export default File
</script>

<style scoped>
.v-text-field {
    padding-top: 0px;
    margin-top: 0px;
}
.table-reponsive {
    max-height: calc(100vh - 300px);
}
.table-reponsive1 {
    max-height: calc(100vh - 220px);
}
</style>