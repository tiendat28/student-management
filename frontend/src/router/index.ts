import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'page',
    component: () => import('@/pages/index.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/pages/Login/index.vue'),
  },
  {
    path: '/admin',
    name: 'admin',
    component: () => import('@/pages/Admin/index.vue'),
    children: [
      {
        path: '/admin/member',
        name: 'member',
        component: () => import('@/pages/Admin/member/index.vue'),
      },
      {
        path: '/admin/class',
        name: 'class',
        component: () => import('@/pages/Admin/class/index.vue'),
      }
    ]
  },
  {
    path: '/S_home',
    name: 'S_home',
    component: () => import('@/pages/Client/student/index.vue'),
    children: [
      {
        path: '/S_home/homepage',
        name: 'S_homepage',
        component: () => import('@/pages/Client/student/homepage/index.vue'),
      },
      {
        path: '/S_home/courses',
        name: 'S_courses',
        component: () => import('@/pages/Client/student/courses/index.vue'),
      },
      {
        path: '/S_home/chat',
        name: 'S_chat',
        component: () => import('@/pages/Client/student/chat/index.vue'),
      },
      {
        path: '/S_home/assignment',
        name: 'S_assignment',
        component: () => import('@/pages/Client/student/assignment/index.vue'),
      },
      {
        path: '/S_home/file',
        name: 'S_file',
        component: () => import('@/pages/Client/student/file/index.vue'),
      },
      {
        path: '/S_home/assignment_result',
        name: 'S_assignment_result',
        component: () => import('@/pages/Client/student/assignment/result.vue'),
      },
      {
        path: '/S_home/courses/:id/homepage',
        name: 'S_course_homepage',
        component: () => import('@/pages/Client/student/course_detail/index.vue'),
        children: [
          {
            path: '/S_home/courses/:id/homepage',
            name: 'S_course_id_homepage',
            component: () => import('@/pages/Client/student/course_detail/detail/homepage.vue'),
          },
          {
            path: '/S_home/courses/:id/attendance',
            name: 'S_attendance',
            component: () => import('@/pages/Client/student/course_detail/detail/attendance.vue'),
          },
        ]
      }
    ]
  },
  {
    path: '/T_home',
    name: 'T_home',
    component: () => import('@/pages/Client/teacher/index.vue'),
    children: [
      {
        path: '/T_home/homepage',
        name: 'T_homepage',
        component: () => import('@/pages/Client/teacher/homepage/index.vue'),
      },
      {
        path: '/T_home/courses',
        name: 'T_courses',
        component: () => import('@/pages/Client/teacher/courses/index.vue'),
      },
      {
        path: '/T_home/chat',
        name: 'T_chat',
        component: () => import('@/pages/Client/teacher/chat/index.vue'),
      },
      {
        path: '/T_home/assignment',
        name: 'T_assignment',
        component: () => import('@/pages/Client/teacher/assignment/index.vue'),
      },
      {
        path: '/T_home/assignment/:id',
        name: 'T_assignment_edit',
        component: () => import('@/pages/Client/teacher/assignment/id/index.vue'),
      },
      {
        path: '/T_home/file',
        name: 'T_file',
        component: () => import('@/pages/Client/teacher/file/index.vue'),
      },
      {
        path: '/T_home/courses/:id/homepage',
        name: 'T_course_homepage',
        component: () => import('@/pages/Client/teacher/course_detail/index.vue'),
        children: [
          {
            path: '/T_home/courses/:id/homepage',
            name: 'T_course_id_homepage',
            component: () => import('@/pages/Client/teacher/course_detail/detail/homepage.vue'),
          },
          {
            path: '/T_home/courses/:id/attendance',
            name: 'T_attendance',
            component: () => import('@/pages/Client/teacher/course_detail/detail/attendance.vue'),
          },
        ]
      }
    ]
  },
  {
    path: '/S_home/assignment_done',
    name: 'S_assignment_done',
    component: () => import('@/pages/Client/student/assignment/done.vue'),
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
