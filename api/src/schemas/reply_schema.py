from pydantic import BaseModel


class ReplyRequest(BaseModel):
    user_id: str
    session_id: str
    mdn: str
    content: str
