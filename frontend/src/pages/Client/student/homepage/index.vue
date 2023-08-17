<template>
  <div class="flex w-full">
    <div class="bg-slate-200 w-[30%] h-[calc(100vh-60px)]">
        <div class="h-[90px] flex justify-between items-center px-6 border-b-2 border-[#cbd5e1]">
            <div class="text-2xl font-bold">Thông tin quan trọng</div>
            <div>
                <v-icon> mdi-compass-rose</v-icon>
            </div>
        </div>
        <div class="pt-6 pb-4 px-6">
            <div>
                <v-icon>mdi-compass-rose</v-icon>
                <span class="font-base pl-2">Chưa đọc</span>
            </div>
        </div>
        <div class="pt-3 px-1 relative top-0 left-0 overflow-auto table-reponsive w-[100%]">
            <div class="flex justify-start items-center h-[120px] pl-6 bg-white rounded-lg">
                <div>
                  <v-icon color="green" :size="50">mdi-bag-personal-outline</v-icon>
                </div>
                <div>
                  <span class="pl-2 text-lg">Mai Tiến Đạt</span>
                  <p class="pl-2">Đã cập nhật bài tập mới</p>
                  <p class="pl-2">Ngày 9/8/2023</p>
                  <p class="pl-2">Lớp PHP</p>
                </div>
            </div>
            <div class="flex justify-start items-center h-[120px] pl-6 hover:bg-white rounded-lg">
                <div>
                  <v-icon color="green" :size="50">mdi-bag-personal-outline</v-icon>
                </div>
                <div>
                  <span class="pl-2 text-lg">Trần Xuân Bảng</span>
                  <p class="pl-2">Đã cập nhật bài tập mới</p>
                  <p class="pl-2">Ngày 8/8/2023</p>
                  <p class="pl-2">Lớp Javascript</p>
                </div>
            </div>
            <div class="flex justify-start items-center h-[60px] py-2 pl-6 hover:bg-white rounded-lg">
                <div>
                  <v-img class="w-[45px] h-[45px] rounded-full" :src="require('@/assets/nam.jpg')"></v-img>
                </div>
                <div>
                  <span class="pl-2 text-lg">Lê Hoàng Nam</span>
                  <p class="pl-2">Lol không?</p>
                </div>
            </div>
            <div class="flex justify-start items-center h-[120px] pl-6 hover:bg-white rounded-lg">
                <div>
                  <v-icon color="green" :size="50">mdi-bag-personal-outline</v-icon>
                </div>
                <div>
                  <span class="pl-2 text-lg">Trần Xuân Bảng</span>
                  <p class="pl-2">Đã cập nhật bài tập mới</p>
                  <p class="pl-2">Ngày 8/8/2023</p>
                  <p class="pl-2">Lớp Javascript</p>
                </div>
            </div>
            <div class="flex justify-start items-center h-[120px] pl-6 hover:bg-white rounded-lg">
                <div>
                  <v-icon color="green" :size="50">mdi-bag-personal-outline</v-icon>
                </div>
                <div>
                  <span class="pl-2 text-lg">Trần Xuân Bảng</span>
                  <p class="pl-2">Đã cập nhật bài tập mới</p>
                  <p class="pl-2">Ngày 8/8/2023</p>
                  <p class="pl-2">Lớp Javascript</p>
                </div>
            </div>
            <div class="flex justify-start items-center h-[60px]py-2 pl-6 hover:bg-white rounded-lg">
                <div>
                  <v-img class="w-[45px] h-[45px] rounded-full" :src="require('@/assets/nam.jpg')"></v-img>
                </div>
                <div>
                  <span class="pl-2 text-lg">Lê Hoàng Nam</span>
                  <p class="pl-2">Đi ăn không?</p>
                </div>
            </div>
            <div class="flex justify-start items-center h-[120px] pl-6 hover:bg-white rounded-lg">
                <div>
                  <v-icon color="green" :size="50">mdi-bag-personal-outline</v-icon>
                </div>
                <div>
                  <span class="pl-2 text-lg">Mai Tiến Đạt</span>
                  <p class="pl-2">Đã cập nhật bài tập mới</p>
                  <p class="pl-2">Ngày 9/8/2023</p>
                  <p class="pl-2">Lớp PHP</p>
                </div>
            </div>
            <div class="flex justify-start items-center h-[60px] py-4 pl-6 hover:bg-white rounded-lg">
                <div>
                  <v-img class="w-[45px] h-[45px] rounded-full" :src="require('@/assets/hoang.jpg')"></v-img>
                </div>
                <div>
                  <span class="pl-2 text-lg">Phạm Long Hoàng</span>
                  <p class="pl-2">Play Lol KHÔNG?</p>
                </div>
            </div>
            <div class="flex justify-start items-center h-[60px] py-2 pl-6 hover:bg-white rounded-lg">
                <div>
                  <v-img class="w-[45px] h-[45px] rounded-full" :src="require('@/assets/nam.jpg')"></v-img>
                </div>
                <div>
                  <span class="pl-2 text-lg">Lê Hoàng Nam</span>
                  <p class="pl-2">Ăn lẩu Sơn Tùng nhá.</p>
                </div>
            </div>
        </div>
    </div>
    <div class="w-full h-[calc(100vh-60px)]">
        <div class="h-[90px] flex justify-between items-center px-6 border-b-2 border-[#cbd5e1]">
          <div class="flex justify-start items-center h-[120px] pl-6">
                <div>
                  <v-icon color="green" :size="50">mdi-bag-personal-outline</v-icon>
                </div>
                <div>
                  <span class="pl-2 text-2xl font-bold">Bài tập</span>
                </div>
            </div>
        </div>
        <div class="flex flex-col justify-center items-center w-full h-[calc(100vh-150px)]">
          <div class="pl-[80px]">
            <v-img class="w-[568px] h-[489px]" :src="require('@/assets/good.jpg')"></v-img>
          </div>
          <span class="text-3xl font-bold">Thật tuyệt vời</span>
          <p class="text-lg">Bạn đã hoàn thành hết bài tập, giờ thì chơi LOL thôi nào</p>
          <p class="text-lg">Welcome to summerit!</p>
        </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.v-application p {
    margin-bottom: 0px;
}
</style>