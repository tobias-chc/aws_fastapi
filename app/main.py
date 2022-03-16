from fastapi import FastAPI

# Create a fastapi object
app = FastAPI()


# Create an endpoint (route)
@app.get("/")
async def root():
    return {"message": "Hello to the EC2 fastappi app!"}


student_list = ['Tobias', 'Mannar', 'Stephan', 'Benjamin']


# Another endpoint with parameter
@app.get("/{number_students}")
async def students_disp(number_students: int):
    amount_students = len(student_list)
    if number_students <= amount_students:
        return {"message": f"This is the list of students: {student_list[0:number_students]} at Sophia Campus."}
    else:
        return {"message": f"There are only {amount_students} students!"}
