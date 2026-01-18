from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello world"}


@app.get("/courses/{course_id}")
def read_course(course_id:int):
    return {"course_id": course_id}
    