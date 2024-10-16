from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    print("To run open a console and run 'fastapi dev first_steps.py'")
    print("Then open up a browser at address 'localhost:8000' or whatever port is specified in the previous step")
    print("Observe 'hello world' message")
    print("Then open up similar address 'localhost:8000/docs' and observe the Swagger interface")
