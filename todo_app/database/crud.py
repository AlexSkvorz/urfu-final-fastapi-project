from fastapi import HTTPException, status

from .core import get_db
from app.schemes.todo_schemes import TodoItem
from database.models import TodoItem as TodoItemModel


class CRUD:
    @staticmethod
    async def read_item_list() -> list[TodoItem]:
        with get_db() as db:
            return db.query(TodoItemModel).all()

    @staticmethod
    async def read_item_by_id(item_id: int) -> TodoItem:
        with get_db() as db:
            item = db.query(TodoItemModel).filter(TodoItemModel.id == item_id).first()
            if not item:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

            return item

    @staticmethod
    async def create_item(
            title: str,
            description: str,
            completed: bool
    ) -> TodoItem:
        with get_db() as db:
            new_item = TodoItemModel(
                title=title,
                description=description,
                completed=completed
            )
            db.add(new_item)
            db.commit()
            db.refresh(new_item)

            return new_item

    @staticmethod
    async def update_item(
            item_id: int,
            title: str,
            description: str,
            completed: bool
    ) -> TodoItem:
        with get_db() as db:
            db_item = db.query(TodoItemModel).filter(TodoItemModel.id == item_id).first()
            if not db_item:
                raise HTTPException(status_code=404, detail="Item not found")
            db_item.title = title
            db_item.description = description
            db_item.completed = completed
            db.commit()
            db.refresh(db_item)

            return db_item

    @staticmethod
    async def change_item(
            item_id: int,
            title: str = None,
            description: str = None,
            completed: bool = None
    ) -> TodoItem:
        with get_db() as db:
            db_item = db.query(TodoItemModel).filter(TodoItemModel.id == item_id).first()
            if not db_item:
                raise HTTPException(status_code=404, detail="Item not found")

            if title:
                db_item.title = title
            if description:
                db_item.description = description
            if completed:
                db_item.completed = completed
            db.commit()
            db.refresh(db_item)

            return db_item

    @staticmethod
    async def delete_item(item_id: int):
        with get_db() as db:
            db_item = db.query(TodoItemModel).filter(TodoItemModel.id == item_id).first()
            if not db_item:
                raise HTTPException(status_code=404, detail="Item not found")
            db.delete(db_item)
            db.commit()
