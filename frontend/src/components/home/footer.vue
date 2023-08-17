<template>
    <footer id="contact" class="bg-slate-900">
        <div class="container text-black mx-auto w-full max-w-screen-xl p-4 py-6 lg:py-8">
            <div class="w-full lg:flex lg:w-full lg:justify-between lg:items-center mx-auto ">
                <div class="w-full lg:w-[30%] pr-3">
                    <div class="text-xl font-bold py-3 uppercase text-[#06b6d4]">Về chúng tôi</div>
                    <hr>
                    <div class="py-3">
                        <p class="text-[#cbd5e1]">A dedicated group of experts continually working to create programming resources that is accurate and easier to understand.</p>
                    </div>
                </div>
                <div class="w-full lg:w-[20%] lg:px-3">
                    <div class="text-xl font-bold py-3 text-[#06b6d4] uppercase">Danh mục</div>
                    <hr>
                    <ul class="py-3 list-none pl-0">
                        <a class="hover:text-[#86efac]"><li href="#about">Giới thiệu</li></a>
                        <a class="hover:text-[#86efac]"><li href="#courses">Khóa học</li></a>
                        <a class="hover:text-[#86efac]"><li href="#new">Tin tức</li></a>
                        <a class="hover:text-[#86efac]"><li href="#contact">Liên hệ</li></a>
                    </ul>
                </div>
                <div class="w-full lg:w-[25%] lg:px-3">
                    <div class="text-xl font-bold py-3 text-[#06b6d4] uppercase">Cam kết</div>
                    <hr>
                    <div class="py-3 text-[#cbd5e1]">
                        <h1>Chuẩn đầu ra</h1>
                        <h1>Không mất phí học khi thi lại</h1>
                        <h1>Chính xác</h1>
                        <h1>Giảng viên nhiệt tình, chu đáo</h1>
                    </div>
                </div>
                <div class="w-full lg:w-[25%] lg:pl-2">
                    <div class="text-xl font-bold py-3 text-[#06b6d4] uppercase">Liên hệ</div>
                    <hr>
                    <ul class="py-3 text-[#cbd5e1] list-none pl-0">
                        <li>Địa chỉ: TP. Hà Nội</li>
                        <li>SĐT: 0948900833</li>
                        <li>Email: fivedream@gmail.com</li>
                        <a class="hover:text-[#86efac]" target="_blank" href="https://www.facebook.com/kddarkill"><li>Facebook: Tiến Đạt</li></a>
                    </ul>
                </div>
            </div>
        </div>
        <div class="bg-slate-900">
            <div class="flex justify-center items-center py-2 text-[#06b6d4]">
                <span>© Bản quyền thuộc về FiveDream</span>
                <div class="px-4">|</div>
                <span>Thiết kế bởi Fivedream.vn</span>
            </div>
        </div>
    </footer>
</template>
<script>
const Footer = {

}
export default Footer
</script>
<style scoped>
.v-application a {
    color: #cbd5e1;
}
.v-application a :hover{
    color: #06b6d4;
}
</style>