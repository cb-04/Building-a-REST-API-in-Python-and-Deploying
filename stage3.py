from fastapi import FastAPI
from typing import Optional

app = FastAPI()

courses = [
    {"course_name": "Python"},
    {"course_name": "NodeJS"},
    {"course_name": "Machine Learning"}
]
subjects = [
    {"name": "Maths"},
    {"name": "Science"},
    {"name": "Programming"}
]

@app.get("/")
def root():
    return {"message":"Hello world"}


@app.get("/courses")
def read_course(start:int=0, end:int=10):
    return courses[start:start+end]
    
@app.get("/subjects/{subject_id}")
def read_subjects(subject_id:int, q:Optional[str]=None):
    if q is not None:
        return {"subject_name": subjects[subject_id], "q": q}
    return {"subject_name": subjects[subject_id]}
