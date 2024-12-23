from fastapi import HTTPException, status

from .core import get_db
from .models import URLItem
from app.schemes.url_schemes import UrlSchema


class CRUD:
    @staticmethod
    async def read_shorten_url_list() -> list[UrlSchema]:
        async with get_db() as db:
            return db.query(URLItem).all()

    @staticmethod
    async def is_exist_url_short_id(short_id: str) -> URLItem:
        async with get_db() as db:
            return db.query(URLItem).filter(URLItem.short_id == short_id).first()

    @staticmethod
    async def create_short_url(short_id: str, url: str):
        async with get_db() as db:
            new_item = URLItem(short_id=short_id, full_url=str(url))
            db.add(new_item)
            db.commit()
            db.refresh(new_item)

    @staticmethod
    async def read_short_url(short_id: str) -> URLItem:
        async with get_db() as db:
            url_item = db.query(URLItem).filter(URLItem.short_id == short_id).first()
            if not url_item:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Короткая ссылка не найдена")

            return url_item

    @staticmethod
    async def delete_url_by_short_id(short_id: str):
        async with get_db() as db:
            url_item = db.query(URLItem).filter(URLItem.short_id == short_id).first()
            if not url_item:
                raise HTTPException(status_code=404, detail="URL not found")
            db.delete(url_item)
            db.commit()
