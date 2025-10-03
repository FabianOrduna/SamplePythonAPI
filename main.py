from fastapi import FastAPI

app = FastAPI()

# In-memory storage
DB = { 
    1: {"id": 1, "name": "John Doe", "age": 30},
    2: {"id": 2, "name": "Jane Smith", "age": 25},
    3: {"id": 3, "name": "Alice Johnson", "age": 28},
    4: {"id": 4, "name": "Bob Brown", "age": 22}
}

# GET: list all persons
@app.get("/")
async def health():
    return {"ok": 1}


# GET: list all persons
@app.get("/persons")
async def get_persons():
    return DB

# GET: get a person by id
@app.get("/person/{person_id}")
async def get_single_person(person_id: int):
    person = DB.get(person_id)
    if not person:
        return {"error": "Person not found"}
    return person


# POST: create a person
@app.post("/person", status_code=201)
async def create_person(person: dict):
    DB[person["id"]] = person
    return {"message": "Person created", "data": person}

# GET: reset the database
@app.get("/reset")
async def reset_db():
    DB.clear()
    return {"message": "Database reset to initial state"}

# POST: procesar clave única
@app.post("/procesar-clave")
async def procesar_clave(clave_unica: int = Form(...)):
    digits = [int(d) for d in str(clave_unica)]
    suma = sum(digits)
    resultado = suma * digits[0] * digits[-1]
    return {
        "clave_unica": clave_unica,
        "resultado_final": resultado
    }
