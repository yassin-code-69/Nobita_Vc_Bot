# import discord
# from discord.ext import commands
# import asyncio

# # Intent setup (Bot ke channel er kotha bolar permission deya)
# intents = discord.Intents.default()
# bot = commands.Bot(command_prefix="!", intents=intents)

# # ⚠️ Ekhane tomar Bot Token ar Voice Channel ID dibe
# TOKEN = "TOMAR_BOT_ER_TOKEN_EKHANE_BOSHAO"
# CHANNEL_ID = 123456789012345678  # Tomar VC ID ekhane dao

# @bot.event
# async def on_ready():
#     print(f"✅ Agent online! Logged in as {bot.user}")
#     print("🚀 VC Duty Cycle start hocche...")
#     # Bot chalu holei automatic duty start korbe
#     bot.loop.create_task(vc_duty_cycle())

# async def vc_duty_cycle():
#     await bot.wait_until_ready()
#     channel = bot.get_channel(CHANNEL_ID)

#     while True:
#         if not channel:
#             print("❌ Target VC khuje pai nai! ID ta thik ache kina check koro.")
#             await asyncio.sleep(60) # 1 min por abar khujbe
#             continue

#         try:
#             # 🟢 Duty Shuru: VC-te join kora
#             print("🟢 Agent VC-te join korche 20 ghontar jonno...")
#             vc = await channel.connect(reconnect=True, timeout=None)
            
#             # ⏱️ 20 ghonta (20 * 3600 seconds) VC-te thaka
#             await asyncio.sleep(20 * 3600)
            
#             # 🔴 Duty Break: Disconnect kora
#             print("🔴 20 ghonta shesh! Agent 5 minuter cha-nastar break nicche...")
#             if vc.is_connected():
#                 await vc.disconnect()
            
#             # ⏱️ 5 minute (5 * 60 seconds) break
#             await asyncio.sleep(5 * 60)

#         except Exception as e:
#             print(f"⚠️ Loop-e choto ekta error hoyeche: {e}")
#             await asyncio.sleep(30) # Error hole 30 sec por abar try korbe

# # Agent Run Kora
# bot.run(TOKEN)


# import discord
# from discord.ext import commands
# import asyncio
# import random
# import os
# from dotenv import load_dotenv

# # .env file theke secret data load kora
# load_dotenv()
# USER_TOKEN = os.getenv("USER_TOKEN")
# CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# # ⚠️ ফিক্স: Intents পুরোপুরি বাদ দেওয়া হয়েছে, শুধু self_bot=True থাকবে
# bot = commands.Bot(command_prefix="?", self_bot=True)

# @bot.event
# async def on_ready():
#     print(f"✅ Successful Login! Automated User: {bot.user}")
#     print("🚀 Anti-Detection VC Duty Loop Shuru holo...")
#     bot.loop.create_task(stealth_vc_loop())

# async def stealth_vc_loop():
#     await bot.wait_until_ready()
#     channel = bot.get_channel(CHANNEL_ID)

#     while True:
#         if not channel:
#             print("❌ Channel khuje paowa jayni! ID ta abar check koro.")
#             await asyncio.sleep(60)
#             continue

#         try:
#             print("🟢 Joining VC under stealth mode...")
#             # self_mute=True korle Discord ar automatic kick marbe na
#             vc = await channel.connect(reconnect=True, timeout=None, self_mute=True, self_deaf=False)
            
#             # 🔥 Human Jitter 1: 19.5 theke 20.5 ghontar moddhe random time
#             session_hours = random.uniform(19.5, 20.5)
#             session_seconds = int(session_hours * 3600)
#             print(f"⏳ Session targeted for {session_hours:.2f} hours. Staying active...")
            
#             await asyncio.sleep(session_seconds)
            
#             print("🔴 Session limits hit! Disconnecting for a human-like break...")
#             if vc.is_connected():
#                 await vc.disconnect()
            
#             # 🔥 Human Jitter 2: 4 minute theke 8 minuter moddhe random break
#             break_seconds = random.randint(240, 480)
#             print(f"☕ Taking a break for {break_seconds / 60:.2f} minutes...")
#             await asyncio.sleep(break_seconds)

#         except Exception as e:
#             print(f"⚠️ Error Alert: {e}")
#             await asyncio.sleep(30)

# bot.run(USER_TOKEN)






# import discord
# from discord.ext import commands
# import asyncio
# import random
# import os
# from dotenv import load_dotenv

# # Local PC-r jonno .env load kora (Render e eita auto bypass hoye jabe)
# load_dotenv()
# USER_TOKEN = os.getenv("USER_TOKEN")
# # String theke integer e convert korar aage check kora jate crash na khay
# CHANNEL_ID = int(os.getenv("CHANNEL_ID")) if os.getenv("CHANNEL_ID") else 0

# bot = commands.Bot(command_prefix="?", self_bot=True)

# @bot.event
# async def on_ready():
#     print(f"✅ Successful Login! Automated User: {bot.user}")
    
#     # 🛠️ FIX: Reconnect hole jeno multiple loop toiri na hoy shetar protection
#     if not hasattr(bot, 'loop_started'):
#         print("🚀 ULTRA-DYNAMIC Stealth VC Loop Shuru holo...")
#         bot.loop.create_task(stealth_vc_loop())
#         bot.loop_started = True
#     else:
#         print("🔄 Gateway reconnected, loop already running.")

# async def stealth_vc_loop():
#     await bot.wait_until_ready()
#     channel = bot.get_channel(CHANNEL_ID)

#     while True:
#         if not channel:
#             print("❌ Channel khuje paowa jayni! Render Environment variable check koro.")
#             await asyncio.sleep(60)
#             continue

#         try:
#             print("🟢 Joining VC under stealth mode...")
#             vc = await channel.connect(reconnect=True, timeout=None, self_mute=True, self_deaf=False)
            
#             session_hours = random.uniform(15.0, 65.0)
#             session_seconds = int(session_hours * 3600)
#             print(f"⏳ Dynamic Session targeted for {session_hours:.2f} hours. Staying active...")
            
#             await asyncio.sleep(session_seconds)
            
#             print("🔴 Session limits hit! Disconnecting for a human-like break...")
#             if vc.is_connected():
#                 await vc.disconnect()
            
#             break_seconds = random.randint(600, 2700)
#             print(f"☕ Taking a random break for {break_seconds / 60:.2f} minutes...")
#             await asyncio.sleep(break_seconds)

#         except Exception as e:
#             print(f"⚠️ Error Alert: {e}")
#             for x in bot.voice_clients:
#                 if x.guild.id == channel.guild.id:
#                     await x.disconnect(force=True)
            
#             print("♻️ 1 Minute rest niye abar reconnect korbe...")
#             await asyncio.sleep(60)

# if __name__ == "__main__":
#     if not USER_TOKEN or CHANNEL_ID == 0:
#         print("❌ ERROR: USER_TOKEN ba CHANNEL_ID pawa jayni! .env ba Render setup check koro.")
#     else:
#         bot.run(USER_TOKEN)






# import discord
# from discord.ext import commands
# import asyncio
# import random
# import os
# from dotenv import load_dotenv
# from http.server import BaseHTTPRequestHandler, HTTPServer
# import threading

# load_dotenv()
# USER_TOKEN = os.getenv("USER_TOKEN")
# CHANNEL_ID = int(os.getenv("CHANNEL_ID")) if os.getenv("CHANNEL_ID") else 0

# bot = commands.Bot(command_prefix="?", self_bot=True)

# # 🌐 HACK: Render Free Tier Bypass Dummy Web Server
# class DummyServer(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.end_headers()
#         self.wfile.write(b"Bot is Alive and Running 24/7!")

# def run_dummy_server():
#     # Render automatic $PORT env variable provide kore
#     port = int(os.environ.get("PORT", 8080))
#     server = HTTPServer(("0.0.0.0", port), DummyServer)
#     print(f"🌍 Dummy Web Server started on port {port}")
#     server.serve_forever()

# @bot.event
# async def on_ready():
#     print(f"✅ Successful Login! Automated User: {bot.user}")
#     if not hasattr(bot, 'loop_started'):
#         print("🚀 ULTRA-DYNAMIC Stealth VC Loop Shuru holo...")
#         bot.loop.create_task(stealth_vc_loop())
#         bot.loop_started = True

# async def stealth_vc_loop():
#     await bot.wait_until_ready()
#     channel = bot.get_channel(CHANNEL_ID)
#     while True:
#         if not channel:
#             print("❌ Channel khuje paowa jayni!")
#             await asyncio.sleep(60)
#             continue
#         try:
#             print("🟢 Joining VC under stealth mode...")
#             vc = await channel.connect(reconnect=True, timeout=None, self_mute=True, self_deaf=False)
#             session_hours = random.uniform(15.0, 65.0)
#             session_seconds = int(session_hours * 3600)
#             print(f"⏳ Dynamic Session targeted for {session_hours:.2f} hours. Staying active...")
#             await asyncio.sleep(session_seconds)
#             print("🔴 Session limits hit! Disconnecting...")
#             if vc.is_connected():
#                 await vc.disconnect()
#             break_seconds = random.randint(600, 2700)
#             print(f"☕ Taking a break for {break_seconds / 60:.2f} minutes...")
#             await asyncio.sleep(break_seconds)
#         except Exception as e:
#             print(f"⚠️ Error Alert: {e}")
#             for x in bot.voice_clients:
#                 if x.guild.id == channel.guild.id:
#                     await x.disconnect(force=True)
#             await asyncio.sleep(60)

# if __name__ == "__main__":
#     if not USER_TOKEN or CHANNEL_ID == 0:
#         print("❌ ERROR: Config missing!")
#     else:
#         # Pishone threading diye dummy server chalu kora jate loop block na hoy
#         threading.Thread(target=run_dummy_server, daemon=True).start()
#         bot.run(USER_TOKEN)







import discord
from discord.ext import commands
import asyncio
import random
import os
import sys
from dotenv import load_dotenv
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# 🛠️ WINDOWS 3.14 SOCKET BUG FIX: Local PC-te crash bypass korar jonno
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# .env file theke data load kora (Local PC-r jonno)
load_dotenv()
USER_TOKEN = os.getenv("USER_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID")) if os.getenv("CHANNEL_ID") else 0

bot = commands.Bot(command_prefix="?", self_bot=True)

# 🌐 RENDER FREE TIER BYPASS: Dummy HTTP Web Server jate Render shutdown na kore
class DummyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Nobita VC Bot is Alive and Running 24/7 on Cloud!")

def run_dummy_server():
    # Render dynamic PORT supply kore, na paile default 8080
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), DummyServer)
    print(f"🌍 Dummy Web Server started successfully on port {port}")
    server.serve_forever()

@bot.event
async def on_ready():
    print(f"✅ Successful Login! Automated User: {bot.user}")
    
    # 🛠️ MULTIPLE LOOP PROTECTION: Gateway reconnect hole jeno extra loop toiri na hoy
    if not hasattr(bot, 'loop_started'):
        print("🚀 ULTRA-DYNAMIC Stealth VC Loop Shuru holo...")
        bot.loop.create_task(stealth_vc_loop())
        bot.loop_started = True
    else:
        print("🔄 Gateway reconnected, loop already running seamlessly.")

async def stealth_vc_loop():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)

    while True:
        if not channel:
            print("❌ Channel khuje paowa jayni! Environment variables check koro.")
            await asyncio.sleep(60)
            continue

        try:
            print("🟢 Joining VC under stealth mode...")
            # self_mute=True (anti-kick), self_deaf=False (XP tracking enable)
            vc = await channel.connect(reconnect=True, timeout=None, self_mute=True, self_deaf=False)
            
            # 🔥 ULTRA DYNAMIC TIMING: 15 ghonta theke 65 ghontar jekono random time
            session_hours = random.uniform(15.0, 65.0)
            session_seconds = int(session_hours * 3600)
            print(f"⏳ Dynamic Session targeted for {session_hours:.2f} hours. Staying active...")
            
            await asyncio.sleep(session_seconds)
            
            print("🔴 Session limits hit! Disconnecting for a human-like break...")
            if vc.is_connected():
                await vc.disconnect()
            
            # 🔥 HUMAN JITTER BREAK: 10 minute theke 45 minuter random break
            break_seconds = random.randint(600, 2700)
            print(f"☕ Taking a random break for {break_seconds / 60:.2f} minutes...")
            await asyncio.sleep(break_seconds)

        except Exception as e:
            print(f"⚠️ Error Alert: {e}")
            # FAIL-SAFE: Error khale jor kore purano voice state clear kora
            for x in bot.voice_clients:
                if x.guild.id == channel.guild.id:
                    await x.disconnect(force=True)
            
            print("♻️ 1 Minute rest niye abar automatic reconnect korbe...")
            await asyncio.sleep(60)

if __name__ == "__main__":
    if not USER_TOKEN or CHANNEL_ID == 0:
        print("❌ ERROR: CONFIGURATION MISSING! USER_TOKEN ba CHANNEL_ID khuje paowa jayni।")
    else:
        # Background thread-e dummy server friendly run kora
        threading.Thread(target=run_dummy_server, daemon=True).start()
        # Main thread-e Discord bot client run kora
        bot.run(USER_TOKEN)