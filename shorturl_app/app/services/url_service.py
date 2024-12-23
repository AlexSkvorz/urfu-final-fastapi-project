import string
import random


class UrlService:
    @staticmethod
    async def generate_short_id(length: int = 6) -> str:
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
