from pydantic import BaseModel, HttpUrl, Field


class URLCreate(BaseModel):
    url: HttpUrl = Field(description="Ссылка", examples=["https://example.com"])


class ShortURLSchema(BaseModel):
    short_url: str = Field(description="Короткая ссылка")


class UrlSchema(BaseModel):
    short_id: str = Field(description="Идентификатор ссылки", examples=["sj32Ls"])
    full_url: str = Field(description="Оригинальная ссылка", examples=["https://example.com"])

    class Config:
        from_attributes = True
