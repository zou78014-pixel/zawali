import asyncio
import datetime

from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

API_ID = 32266719
API_HASH = "454bca8c3651d4f4977555e420f4d212"
BASE_NAME = "• 𝐇𝐀𝐋𝐊 ⌯"

client = TelegramClient("session_name", API_ID, API_HASH)


def to_fancy_digits(text):
    digits_map = str.maketrans(
        "0123456789",
        "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
    )
    return str(text).translate(digits_map)


async def update_time_name():
    await client.start()

    last_time = ""

    while True:
        try:
            raw_time = datetime.datetime.now().strftime("%H:%M")
            fancy_time = to_fancy_digits(raw_time)

            if fancy_time != last_time:
                new_name = f"{BASE_NAME} {fancy_time}"

                await client(
                    UpdateProfileRequest(first_name=new_name)
                )

                last_time = fancy_time
                print(f"تم التحديث إلى: {new_name}")

            await asyncio.sleep(30)

        except Exception as e:
            print(f"حدث خطأ: {e}")
            await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(update_time_name())