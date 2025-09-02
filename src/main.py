from fastapi import FastAPI

# cria a aplicação FastAPI
app = FastAPI()


def soma(a: int, b: int) -> int:
    return a + b


# rota raiz
@app.get("/")
def read_root() -> object:
    return {"message": "Hello, World!"}


# rota com parâmetro
@app.get("/hello/{name}")
def read_item(name: str) -> object:
    return {"message": f"Hello, {name}!"}
