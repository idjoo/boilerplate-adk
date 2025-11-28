from google.genai.types import Content, Part

from src.dependencies import AdkRunner, AdkSession, Config
from src.schemas import ReplyRequest


class ChatService:
    runner: AdkRunner
    session: AdkSession
    config: Config

    def __init__(
        self,
        runner: AdkRunner,
        session: AdkSession,
        config: Config,
    ) -> None:
        self.runner = runner
        self.session = session
        self.config = config

    async def reply(
        self,
        data: ReplyRequest,
    ):
        session = await self.session.get_session(
            app_name=self.config.service,
            user_id=data.user_id,
            session_id=data.session_id,
        )
        if session is None:
            await self.session.create_session(
                app_name=self.config.service,
                user_id=data.user_id,
                session_id=data.session_id,
                state={"base_phone_number": data.mdn},
            )

        content = Content(role="user", parts=[Part(text=data.content)])

        response = "No Response!"
        async for event in self.runner.run_async(
            user_id=data.user_id,
            session_id=data.session_id,
            new_message=content,
        ):
            if (
                event.is_final_response()
                and event.content
                and event.content.parts
            ):
                response = event.content.parts[0].text

        return response
