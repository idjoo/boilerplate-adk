from google.genai.types import Content, Part

from src.dependencies import Agent, Config
from src.schemas import ReplyRequest


class ChatService:
    config: Config
    agent: Agent

    def __init__(
        self,
        config: Config,
        agent: Agent,
    ) -> None:
        self.config = config
        self.agent = agent

    async def reply(
        self,
        data: ReplyRequest,
    ):
        session = await self.agent.async_get_session(
            user_id=data.user_id,
            session_id=data.session_id,
        )
        if session is None:
            await self.agent.async_create_session(
                user_id=data.user_id,
                session_id=data.session_id,
                state={"base_phone_number": data.mdn},
            )

        content = Content(role="user", parts=[Part(text=data.content)])

        response = "No Response!"
        async for event in self.agent.async_stream_query(
            user_id=data.user_id,
            session_id=data.session_id,
            message=content,
        ):
            if (
                event.is_final_response()
                and event.content
                and event.content.parts
            ):
                response = event.content.parts[0].text

        return response
