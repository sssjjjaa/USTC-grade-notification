import asyncio
from pyustc import CASClient, EAMSClient
from pyustc.eams._grade import GradeManager
from config import STUDENT_ID, PASSWORD


async def async_get_grade(latest_only=False):
    async with CASClient.login_by_pwd(STUDENT_ID, PASSWORD) as cas_client:
        async with await EAMSClient.create(cas_client) as eams_client:
            grade_manager = GradeManager.__new__(GradeManager)
            await GradeManager.__init__(grade_manager, eams_client._client_pool)

            semesters = await grade_manager.get_semesters()
            
            if latest_only:
                semester_ids = [max(semesters.keys())]
            else:
                semester_ids = list(semesters.keys())

            train_types = await grade_manager.get_train_types()
            train_type_id = next(iter(train_types.keys()))

            grade_sheet = await grade_manager.get_grade_sheet(
                train_type=train_type_id, semesters=semester_ids
            )

            grade_dict = {}
            for course in grade_sheet.courses:
                grade_dict[course.name] = course.score

            return grade_dict


def get_grade(latest_only=False):
    return asyncio.run(async_get_grade(latest_only))


if __name__ == "__main__":
    print(get_grade(latest_only=True))