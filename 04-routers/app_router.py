from fastapi import APIRouter


page_router = APIRouter()


@page_router.get("/about")
def about():
    return {"message":"Welcome To About Page"}

@page_router.get("/contact")
def contact():
    return {"message":"Welcome To Contact Page"}

@page_router.get("/services")
def services():
    return {"message":"Welcome To Services Page"}