
from fastapi import APIRouter
from endpoint import teacher, student, subject, attendance, user, token, questions, answer, todolist

api_router = APIRouter()

api_router.include_router(
    user.router,
    prefix='/user',
    tags=['user']
)

api_router.include_router(
    teacher.router,
    prefix='/teacher',
    tags=['teacher']
)


api_router.include_router(
    student.router,
    prefix='/student',
    tags=['student']
)

api_router.include_router(
    subject.router,
    prefix='/subject',
    tags=['subject']
)

api_router.include_router(
    attendance.router,
    prefix='/attendance',
    tags=['attendance']
)

api_router.include_router(
    token.router,
    prefix='/token',
    tags=['token']
)

api_router.include_router(
    questions.router,
    prefix='/questions',
    tags=['questions']
)

api_router.include_router(
    answer.router,
    prefix='/answer',
    tags=['answer']
)

api_router.include_router(
    todolist.router,
    prefix='/todolist',
    tags=['todolist']
)
