from fastapi import APIRouter, status, HTTPException, Path
from fastapi.responses import RedirectResponse
from typing import Annotated

from app.schemes.url_schemes import URLCreate, ShortURLSchema, UrlSchema
from app.services.url_service import UrlService
from database.crud import CRUD

url_router = APIRouter(
    prefix="/url",
    tags=["url"]
)


@url_router.get(
    path="/list",
    response_model=list[UrlSchema]
)
async def read_shorten_url_list() -> list[UrlSchema]:
    return await CRUD.read_shorten_url_list()


@url_router.post(
    path="/shorten",
    response_model=ShortURLSchema
)
async def create_shorten_url(item: URLCreate) -> ShortURLSchema:
    for _ in range(10):
        short_id = await UrlService.generate_short_id()
        existing = await CRUD.is_exist_url_short_id(short_id=short_id)
        if not existing:
            await CRUD.create_short_url(short_id=short_id, url=str(item.url))
            return ShortURLSchema(short_url=f"http://localhost:8001/{short_id}")
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Не удалось сгенерировать короткую ссылку"
    )


@url_router.get("/stats/{short_id}")
async def get_stats(short_id: str):
    url_item = await CRUD.read_short_url(short_id=short_id)
    return {
        "short_id": url_item.short_id,
        "full_url": url_item.full_url
    }


@url_router.delete(
    path="/delete/{short_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_url_by_short_id(short_id: Annotated[str, Path(title="ID ссылки")]):
    await CRUD.delete_url_by_short_id(short_id=short_id)


@url_router.get("/{short_id}")
async def redirect_to_full(short_id: str):
    url_item = await CRUD.read_short_url(short_id=short_id)
    print(f"Redirecting to: {url_item.full_url}")  # Логирование
    return RedirectResponse(url=url_item.full_url)
