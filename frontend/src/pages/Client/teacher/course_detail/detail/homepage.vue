<template>
    <div>
        <div class="h-[90px] flex justify-start items-center px-8 border-b-2 border-[#cbd5e1]">
            <div class="flex">
                <v-icon color="#0f766e" class="pr-3" :size="50">mdi-home-heart</v-icon>
                <span class="font-bold text-2xl flex justify-start items-center">Trang chủ</span>
            </div>
        </div>
        <div class="relative top-0 left-0 table-reponsive overflow-x-hidden w-full h-full">
            <div class="m-12">
                <div>
                    <v-img class="w-[1400px] h-[350px] rounded-md" :src="require('@/assets/nen.jpg')"></v-img>
                </div>
                <div class="absolute top-[250px] left-[100px] text-4xl font-bold text-white border-2 border-teal-900 bg-teal-900 rounded-lg py-6 px-3 flex justify-center items-center w-[420px]">
                    Welcome to the class!
                </div>
            </div>
            <div class="mx-12">
                <h1 class="text-4xl font-bold text-gray-500 py-8">Educators can add a heading or announcement here</h1>
                <h3 class="text-2xl font-normal text-gray-500">Educators: Use this space to share class descriptions, announcements, updates, or whatever you want.</h3>
            </div>
            <div class="flex m-12">
                <div class="h-[700px] w-[50%]">
                    <div>
                        <span class="text-2xl">Resources</span>
                        <div class="flex py-8 justify-between items-center">
                            <a class="flex w-[50%] hover:border-2 hover:rounded-lg py-3" target="_blank" href="https://support.microsoft.com/vi-vn/topic/thi%E1%BA%BFt-l%E1%BA%ADp-trang-ch%E1%BB%A7-trong-nh%C3%B3m-l%E1%BB%9Bp-c%E1%BB%A7a-b%E1%BA%A1n-74cd3e26-f63a-41e7-be31-a54b5a6b0a8d">
                                <v-icon class="flex justify-center items-center px-3" :size="50">mdi-web</v-icon>
                                <span class="text-xl text-gray-500 px-3">Learn more about homepage</span>
                            </a>
                            <a class="flex w-[50%] hover:border-2 hover:rounded-lg py-3" target="_blank" href="https://support.microsoft.com/vi-vn/topic/b%E1%BA%AFt-%C4%91%E1%BA%A7u-trong-nh%C3%B3m-l%E1%BB%9Bp-c%E1%BB%A7a-b%E1%BA%A1n-6b5fd708-35b9-4caf-b66e-d8f2468e4fd5">
                                <v-icon class="flex justify-center items-center px-3" :size="50">mdi-web</v-icon>
                                <span class="text-xl text-gray-500 px-3">Get started with Teams for Education</span>
                            </a>
                        </div>
                    </div>
                    <div>
                        <span class="text-2xl">Assignments</span>
                        <div class="h-[600px] flex flex-col justify-center items-center">
                            <v-icon :size="200">mdi-book-open-variant</v-icon>
                            <p class="text-3xl w-[420px]">Có vẻ như bạn không có bất kỳ nhiệm vụ nào.</p>
                        </div>
                    </div>
                </div>
                <div class="h-[700px] w-[50%]">
                    <div>
                        <span class="text-2xl">Class schedule</span>
                        <div class="flex py-8 justify-start items-center">
                           <span class="px-3 py-2 text-lg hover:border-b-4 hover:border-teal-600">Sắp tới</span>
                           <span class="py-2 text-lg border-b-4 border-teal-600">Đã qua</span>
                        </div>
                        <div class="bg-gray-100 h-[720px] rounded-lg shadow-lg">
                            <div class="flex py-10 border-b-2">
                                <div class="flex flex-col justify-center items-center px-6">
                                    <span class="text-2xl">THÁNG</span>
                                    <span class="text-2xl">08</span>
                                </div>
                               <div class="flex flex-col pl-[120px] justify-start">
                                    <span class="text-xl">Không có cuộc họp nào</span>
                                    <span class="text-lg">Các cuộc họp sắp tới sẽ hiển thị ở đây</span>
                               </div>
                            </div>
                            <div class="flex py-10 border-b-2">
                                <div class="flex flex-col justify-center items-center px-6">
                                    <span class="text-2xl">THÁNG</span>
                                    <span class="text-2xl">08</span>
                                </div>
                               <div class="flex flex-col pl-[120px] justify-start">
                                    <span class="text-xl">Không có cuộc họp nào</span>
                                    <span class="text-lg">Các cuộc họp sắp tới sẽ hiển thị ở đây</span>
                               </div>
                            </div>
                            <div class="flex py-10 border-b-2">
                                <div class="flex flex-col justify-center items-center px-6">
                                    <span class="text-2xl">THÁNG</span>
                                    <span class="text-2xl">08</span>
                                </div>
                               <div class="flex flex-col justify-start pl-[120px]">
                                    <span class="text-xl">Không có cuộc họp nào</span>
                                    <span class="text-lg">Các cuộc họp sắp tới sẽ hiển thị ở đây</span>
                               </div>
                            </div>
                            <div class="flex py-10 border-b-2">
                                <div class="flex flex-col justify-center items-center px-6">
                                    <span class="text-2xl">THÁNG</span>
                                    <span class="text-2xl">08</span>
                                </div>
                               <div class="flex flex-col justify-start pl-[120px]">
                                    <span class="text-xl">Không có cuộc họp nào</span>
                                    <span class="text-lg">Các cuộc họp sắp tới sẽ hiển thị ở đây</span>
                               </div>
                            </div>
                            <div class="flex py-10 border-b-2">
                                <div class="flex flex-col justify-center items-center px-4">
                                    <span class="text-2xl">THÁNG</span>
                                    <span class="text-2xl">08</span>
                                </div>
                               <div class="flex flex-col justify-start pl-[120px]">
                                    <span class="text-xl">Không có cuộc họp nào</span>
                                    <span class="text-lg">Các cuộc họp sắp tới sẽ hiển thị ở đây</span>
                               </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

</script>
<style scoped>
.table-reponsive {
    max-height: calc(100vh - 150px);
}
</style>