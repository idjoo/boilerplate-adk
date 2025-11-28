from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.dependencies import Logger, tracer
from src.schemas import ReplyRequest, Response
from src.services import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)


@router.post("/reply")
@tracer.observe
async def reply(
    logger: Logger,
    chat_service: Annotated[ChatService, Depends()],
    data: ReplyRequest,
) -> Response[str]:
    data = await chat_service.reply(data)
    return Response(
        status=status.HTTP_200_OK,
        message="Message replied successfully",
        data=data,
    )
