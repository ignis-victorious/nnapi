#  ##   ###
#  Import LIBRARIES
from typing import Literal
from fastapi import FastAPI
#  Import FILES
#  ##   ###


api = FastAPI()


all_todos: list[dict[str, str | int]] = [
    {"todo_id": 1, "name": "Sports", "description": "Go to the gym"},
    {"todo_id": 2, "name": "Read", "description": "Read 10 pages"},
    {"todo_id": 3, "name": "Shop", "description": "Go shopping"},
    {"todo_id": 4, "name": "Study", "description": "Study for exam"},
    {"todo_id": 5, "name": "Meditate", "description": "Meditate 20 minutes"},
]

# for todo in all_todos:
#     print(todo)
# print(max(todo["todo_id"] for todo in all_todos))


@api.get("/")
def index():
    return {"message": "Hi mum!"}


@api.get("/todos/{todo_id}")
def get_todo(todo_id: int) -> dict[str, dict[str, str | int]] | None:
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            return {"result": todo}
    return None  # If no todo is found, return None


@api.get("/todos")
def get_todos(last_n: int | None = None) -> list[dict[str, str | int]]:
    """usage: localhost:xxxx/todos?last_n=2 return only the last 2 records"""
    if last_n:
        return all_todos[-last_n:]
    else:
        return all_todos


# def get_todos(first_n: int = None) -> list[dict[str, str | int]]:
#     """usage: localhost:xxxx/todos?first_n=3 return only the first 3 records"""
#     if first_n:
#         return all_todos[-first_n:]
#     else:
#         return all_todos


@api.post("/todos")
def create_todo(todo: dict) -> None:
    new_todo_id: int = 1 + int(max(todo["todo_id"] for todo in all_todos))

    new_todo: dict[str, str | int] = {
        "todo_id": new_todo_id,
        "name": todo["name"],
        "description": todo["description"],
    }
    all_todos.append(new_todo)


@api.put("/todos/{todo_id}")
def update_todo(
    todo_id: int, updated_todo: dict
) -> dict[str, str | int] | Literal["Error, not found"]:
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            todo["name"] = updated_todo["name"]
            todo["description"] = updated_todo["description"]
            return todo
    return "Error, not found"


@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int) -> dict[str, str | int] | Literal["Error, not found"]:
    for index, todo in enumerate(all_todos):
        if todo["todo_id"] == todo_id:
            deleted_todo: dict[str, str | int] = all_todos.pop(index)
            return deleted_todo
    return "Error, not found"


####
# {
# "name": "New todo",
# "description": "New todo Description"
# }
###
