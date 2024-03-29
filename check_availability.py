import logging
import requests

from pytube import YouTube
from TEXTS import  EXAMPLES, ERRORS


logger_avaliability = logging.getLogger('Перехват ошибок при проверке доступности Youtube.')


class Checker:
    def __init__(self, url: str):
        if len(url) < 131:
            for example in EXAMPLES:
                if url.startswith(example):
                    self.base_check = (True, url)
                    break
            else:
                self.base_check = (False, ERRORS[2])
        else:
            self.base_check = (False, ERRORS[2])

    def check_status_code(self, url) -> tuple[bool, str]:
        try:
            response = requests.get(url)
        except Exception as err:
            logger_avaliability.exception(err)
            return (False, ERRORS[0])
        if response.status_code != 200:
            return (False, ERRORS[1].format(self.url, response.status_code))
        return (True, url)

    def check_access(self, url: str) -> tuple[bool, str | YouTube]:
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).last()
        except Exception as err:
            logger_avaliability.exception(err)
            return (False, ERRORS[3].format(url))
        return (True, yt)
