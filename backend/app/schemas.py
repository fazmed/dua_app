from pydantic import BaseModel, Field

# Schema for reading a Dua


class DuaBase(BaseModel):
    title: str
    content: str

# Schema for creating a Dua


class DuaCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    content: str = Field(..., min_length=1)

# Schema for response (includes ID)


class DuaResponse(DuaBase):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True
