import asyncio
from pyustc import CASClient
from config import STUDENT_ID, PASSWORD


async def async_login():
    async with CASClient.login_by_pwd(STUDENT_ID, PASSWORD) as cas_client:
        return cas_client


def login():
    return asyncio.run(async_login())


if __name__ == "__main__":
    login()
    print("登录成功")