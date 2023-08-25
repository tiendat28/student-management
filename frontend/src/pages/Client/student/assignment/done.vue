<template>
    <div class="bg-gray-300 w-full h-screen">
        <div class="w-[60%] absolute top-0 left-[360px]">
            <div class="px-8 pt-4">
                <div class="h-[270px]">
                    <div class="bg-green-500 h-[70px] rounded-t-lg flex items-center px-6 text-xl text-white">
                        <div>PHẦN TRẮC NGHIỆM --- MÔN TIẾNG ANH</div>
                    </div>
                    <div class="bg-white h-[200px] rounded-b-lg border-gray-300 border-2 items-center px-6 text-xl">
                        <div class="py-8">
                            <v-icon :size="40" color="green">mdi-check-outline</v-icon>
                            <span class="px-3">Nộp bài thành công</span>
                        </div>
                        <div>
                            <router-link to="/S_home/assignment_result">
                                <span class="px-3">Xem kết quả</span>
                            </router-link>
                        </div>
                        <div class="py-4">
                            <router-link to="/S_home/homepage">
                                <span class="px-3">Trang chủ</span>
                            </router-link>
                        </div>
                    </div>
                </div>
                <div class="flex flex-col justify-center items-center py-8">
                    <span class="text-lg">Cảm ơn bạn đã tin tưởng chúng tôi! FiveDream trân thành cảm ơn!</span>
                    <span class="py-8 text-2xl"><b>FiveDream</b> Form</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>