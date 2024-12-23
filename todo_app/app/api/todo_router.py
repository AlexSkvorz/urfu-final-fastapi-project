from fastapi import APIRouter, Path, Body, status
from typing import Annotated

from app.schemes.todo_schemes import TodoItem, TodoCreate, TodoUpdate
from database.crud import CRUD

todo_router = APIRouter(
    prefix="/todo",
    tags=["todo"]
)


@todo_router.get(
    path="/list",
    response_model=list[TodoItem]
)
async def read_item_list() -> list[TodoItem]:
    return await CRUD.read_item_list()


@todo_router.post(
    path="/create",
    response_model=TodoItem
)
async def create_item(
        item: Annotated[TodoCreate, Body(...)]
) -> TodoItem:
    return await CRUD.create_item(title=item.title, description=item.description, completed=item.completed)


@todo_router.put(
    path="/update/{item_id}",
    response_model=TodoItem
)
async def update_item(
        item_id: Annotated[int, Path(title="ID задачи")],
        item: Annotated[TodoCreate, Body(...)]
) -> TodoItem:
    return await CRUD.update_item(
        item_id=item_id,
        title=item.title,
        description=item.description,
        completed=item.completed
    )


@todo_router.delete(
    path="/delete/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_item(item_id: Annotated[int, Path(title="ID задачи")]):
    await CRUD.delete_item(item_id=item_id)


@todo_router.patch(
    path="/change/{item_id}",
    response_model=TodoItem
)
async def change_item(
        item_id: Annotated[int, Path(title="ID задачи")],
        item: Annotated[TodoUpdate, Body(...)]
) -> TodoItem:
    return await CRUD.change_item(
        item_id=item_id,
        title=item.title,
        description=item.description,
        completed=item.completed
    )


@todo_router.get(
    path="/{item_id}",
    response_model=TodoItem
)
async def read_item_by_id(item_id: Annotated[int, Path(title="ID задачи")]) -> TodoItem:
    return await CRUD.read_item_by_id(item_id=item_id)
