<template>
    <div id="news" class="container p-12 mx-auto">
        <div class="flex flex-col justify-center items-center uppercase text-[#06b6d4] text-5xl font-medium p-10">Tin tức</div>
        <div class="flex justify-center">
            <div>
                <div class="bg-white h-[700px] w-[500px] rounded-lg">
                    <div>
                        <v-img class="rounded-t-lg hover:opacity-80 h-[300px]" :src="require('@/assets/image/vue.jpg')"></v-img>
                    </div>
                    <h1 class="uppercase font-bold text-2xl p-6">Chuỗi khóa học framework VueJS bứt phá frontend, phá đảo mọi yêu cầu tuyển dụng</h1>
                    <p class="font-light text-lg px-6">Chuỗi VueJS Đặc Biệt HOÀN TOÀN MIỄN PHÍ "Bứt phá Frontend" vào 20H các ngày 15/9; 18/9; 20/9 và 22/9 này. Hãy cùng tìm hiểu bài viết dưới đây và đăng ký tham gia chuỗi VueJS đặc biệt trong tháng 8 này nha!</p>
                    <div class="text-xl font-medium text-red-600 p-6 pt-[62px] hover:cursor-pointer">Xem chi tiết</div>
                </div>
            </div>
            <div class="px-10">
                <div class="bg-white h-[700px] w-[500px] rounded-lg">
                    <div>
                        <v-img class="rounded-t-lg hover:opacity-80 h-[300px]" :src="require('@/assets/image/python.jpg')"></v-img>
                    </div>
                    <h1 class="uppercase font-bold text-2xl p-6">CUỘC THI "Clear code less bug" - THAM GIA NGAY, NHẬN VÉ XEM PHIM LIỀN TAY</h1>
                    <p class="font-light text-lg px-6">Trong tháng 8 này, FiveDream chính thức khởi động cuộc thi "Clear code less bug" code đẹp ít bug - nhằm giúp các bạn thoả sức đam mê code, sáng tạo trong lập trình kích thích phát triển. Phần thưởng là khóa học Python free cho người thắng cuộc.</p>
                    <div class="text-xl font-medium text-red-600 p-6 pt-9 hover:cursor-pointer">Xem chi tiết</div>
                </div>
            </div>
            <div>
                <div class="bg-white h-[700px] w-[500px] rounded-lg">
                    <div>
                        <v-img class="rounded-t-lg hover:opacity-80 h-[300px]" :src="require('@/assets/image/postgre.jpg')"></v-img>
                    </div>
                    <h1 class="uppercase font-bold text-2xl p-6">Chuỗi khóa học PostgreSQL bứt phá cơ sở dữ liệu, phá đảo mọi yêu cầu tuyển dụng</h1>
                    <p class="font-light text-lg px-6">Chuỗi PostgreSQL Đặc Biệt HOÀN TOÀN MIỄN PHÍ "Bứt phá CSDL" vào 20H các ngày 15/9; 18/9; 20/9 và 22/9 này. Hãy cùng tìm hiểu bài viết dưới đây và đăng ký tham gia chuỗi Database đặc biệt trong tháng 8 này nha!</p>
                    <div class="text-xl font-medium text-red-600 p-6 pt-[62px] hover:cursor-pointer">Xem chi tiết</div>
                </div>
            </div>
        </div>
        <div class="flex justify-center pt-6 hover:cursor-pointer">
            <div class="bg-[#06b6d4] flex justify-center items-center rounded-lg h-[50px] w-[200px] text-white text-xl font-medium p-6">
                Xem toàn bộ
            </div>
        </div>
    </div>
</template>

<script>
const New = {

}
export default New
</script>

<style>

</style>