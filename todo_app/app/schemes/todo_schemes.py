from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    title: str = Field(description="Название задачи", examples=["Приготовить ужин"])
    description: str = Field(default=None, description="Описание задачи", examples=["Не солить"])
    completed: bool = Field(default=False, description="Статус задачи")


class TodoItem(BaseModel):
    id: int = Field(description="Идентификатор задачи", examples=[1])
    title: str = Field(description="Название задачи", examples=["Приготовить ужин"])
    description: str = Field(default=None, description="Описание задачи", examples=["Не солить"])
    completed: bool = Field(default=False, description="Статус задачи")

    class Config:
        from_attributes = True


class TodoUpdate(BaseModel):
    title: str = Field(default=None, description="Название задачи", examples=["Приготовить ужин"])
    description: str = Field(default=None, description="Описание задачи", examples=["Не солить"])
    completed: bool = Field(default=None, description="Статус задачи")
