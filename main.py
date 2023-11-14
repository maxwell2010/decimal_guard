import os
import asyncio
import platform
from dotenv import load_dotenv, set_key
import shutil


patch_dsc_guard = "/home/user/candyguard/dsc-guard/cmd/dsc-guard/"
patch_gentx = "/home/user/candyguard/dsc-guard/cmd/gentx/"


async def set_offline_tx(new_tx: str) -> str:
    dsc_guard = load_dotenv(patch_dsc_guard + '.env')
    if dsc_guard:
        os.environ["SET_OFFLINE_TX"] = new_tx
        set_key(patch_dsc_guard, "SET_OFFLINE_TX", os.environ["SET_OFFLINE_TX"], quote_mode='never')
        return f"🖥 Платформа: {platform.system()} {platform.node()}" \
               f"\n✅ Транзакция отключения обновлена!"
    return "🚨 Проверьте правильность пути до dsc-guard/ .env!"


async def get_offline_tx():
    dsc_guard = load_dotenv(patch_dsc_guard + '.env')
    if dsc_guard:
        print("SET_OFFLINE_TX:", os.environ["SET_OFFLINE_TX"])
    else:
        print('!!!!!!!!!!!!!!!')


async def get_free_mem() -> str:
    total_mem, used_mem, free_mem = shutil.disk_usage('/')
    gb = 10 ** 9
    return f"Всего: {round(total_mem/gb, 2)}\n" \
           f"Занято: {round(used_mem/gb, 2)}\n" \
           f"Свободно: {round(free_mem/gb, 2)}\n"


async def create_offline_tx() -> str:
    os.chdir(patch_gentx)
    os.system(f"ls -l")
    my_cmd = os.popen(f'./gentx').read()
    if my_cmd != "":
        await set_offline_tx(my_cmd)
        return f"🔋 Транзакция отключения:\n\n<code>{my_cmd}</code>"
    return f"🪫 Транзакция отключения НЕ СОЗДАНА!"
