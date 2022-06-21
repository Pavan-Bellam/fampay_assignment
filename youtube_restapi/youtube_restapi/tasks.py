from celery import shared_task
from celery.utils.log import get_task_logger
from dateutil import parser
from app.find import search
from youtube_restapi.settings import (
    SEARCH_QUERY,
    CHECK_INTV,
    BASE_URL
)

logger = get_task_logger(__name__)


@shared_task
def update():
    from app.models import Videos,test
    from app.find import search
    response = search(SEARCH_QUERY, CHECK_INTV, 50)
    logger.info("Successfully Fetched Videos")

    for item in response.get("items", []):
        try:
            
            if all(
                [
                    not Videos.objects.filter(
                        link=BASE_URL + item["id"]["videoId"]
                    ).exists(),
                    item["id"]["kind"] == "youtube#video",
                ]
            ):
                snippet = item["snippet"]
                #print("----------------------------------------------------------------------------")
                #print(item)
                #print(item["id"]["videoId"])
                video = Videos(
                    title=snippet["title"],
                    desc=snippet["description"],
                    publishing_date=parser.parse(snippet["publishedAt"]),
                    url_for_thumnail=snippet["thumbnails"]["default"]["url"],
                    link=BASE_URL + str(item["id"]["videoId"])
                )
                video.save()
           
        except:
            #print("passed")
            pass
    logger.info("Successfully Updated Videos DB")
    b=test(tit="title")


