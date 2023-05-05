from fastapi import FastAPI
from sqladmin import Admin, ModelView

from utils.db_api.models import (
    User, School, 
    College, Texnikum, Lyceum
    )

from loader import db

engine = db.get_engine()

app = FastAPI()
admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.user_id, User.username, User.first_name, User.last_name]
    can_create = False
    can_edit = False
    can_delete = False
    icon = "fa-solid fa-user"


class SchoolAdmin(ModelView, model=School):
    column_list = [
        School.id, School.malumot, School.rahbariyat, 
        School.yonalish, School.qabul, School.savollar, School.boglanish
    ]
    icon = "fa-solid fa-university"

   
class CollegeAdmin(ModelView, model=College):
    column_list = [
        College.id, College.malumot, College.rahbariyat, 
        College.yonalish, College.qabul, College.savollar, College.boglanish
    ]
    icon = "fa-solid fa-university"

   
class TexnikumAdmin(ModelView, model=Texnikum):
    column_list = [
        Texnikum.id, Texnikum.malumot, Texnikum.rahbariyat, 
        Texnikum.yonalish, Texnikum.qabul, Texnikum.savollar, Texnikum.boglanish
    ]
    icon = "fa-solid fa-university"


class LyceumAdmin(ModelView, model=Lyceum):
    column_list = [
        Lyceum.id, Lyceum.malumot, Lyceum.rahbariyat, 
        Lyceum.yonalish, Lyceum.qabul, Lyceum.savollar, Lyceum.boglanish
    ]
    icon = "fa-solid fa-university"

   

admin.add_view(UserAdmin)
admin.add_view(SchoolAdmin)
admin.add_view(CollegeAdmin)
admin.add_view(TexnikumAdmin)
admin.add_view(LyceumAdmin)