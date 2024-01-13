from app.apis.v1.news.list.repositories.news_repositories import \
    NewsListRepository
from app.models.news import ModelNewsRegister


class NewsListService:
    """
    뉴스 리스트 Service
    """

    def __init__(self, news_list_repository: NewsListRepository) -> None:
        self._repository: NewsListRepository = news_list_repository

    async def get_news_list_service(self) -> list[dict] | list:
        """
        Get Service
        """

        # 레파지토리 호출
        news_list: list[dict] | list = await self._repository.get_news_list_repository()
        return news_list

    async def post_news_list_service(self, news_info: ModelNewsRegister) -> list[dict] | list:
        """
        Post Service
        """

        # 레파지토리 호출
        news_list: list[dict] | list = await self._repository.post_news_list_repository(news_info)
        return news_list