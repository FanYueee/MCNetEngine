import discord
from discord.commands import option
import requests
import datetime
import base64

intents = discord.Intents.default()
client = discord.Bot(intents=intents)

# 設定
token = "MTEzNzI2MzY4NzgwNDEyOTI5MA.G7uhzj.wJGelcA1V_idBVWPCPOjr6kzhHWETh0_NmTGEY"
ver = "1.3.1"
Name = "MCNetEngine"

print("  __  __  _____ _   _      _   ______             _             ")
print(" |  \/  |/ ____| \ | |    | | |  ____|           (_)            ")
print(" | \  / | |    |  \| | ___| |_| |__   _ __   __ _ _ _ __   ___  ")
print(" | |\/| | |    | . ` |/ _ \ __|  __| | '_ \ / _` | | '_ \ / _ \ ")
print(" | |  | | |____| |\  |  __/ |_| |____| | | | (_| | | | | |  __/ ")
print(" |_|  |_|\_____|_| \_|\___|\__|______|_| |_|\__, |_|_| |_|\___| ")
print("DiscodBot-MCNetEngine Create By FanYueee     __/ |              ")
print(f"Required API: api.mcsrvstat.us, ip-api.com  |___/       Ver {ver}")


# 控制台啟動通知
@client.event
async def on_ready():
    print(f"\n已成功啟動 {client.user}")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="你打的指令"),status=discord.Status.idle)

# header, encoded_image = icon.split(",", 1)
# datacc = base64.b64decode(encoded_image)
# with open("temp_image.png", "wb") as f:
#     f.write(datacc)
# file = discord.File("temp_image.png")

# 指令主體
@client.slash_command(description = "查詢 Minecraft 伺服器資訊")
@option("ip",description = "輸入欲查詢的伺服器 IP")
async def mcs(ctx, ip: str):
        await ctx.respond("<a:loading:1108348027221065758> 正在查詢中...")
        IPStatus = requests.get('https://api.mcsrvstat.us/2/' + ip)
        IPStatus = IPStatus.json()
        IP = IPStatus['ip']
        Port = IPStatus['port']
        if 'icon' in IPStatus:
            ICONJE = IPStatus['icon']
            header, ICONJE = ICONJE.split(",", 1)
            ICONJE = base64.b64decode(ICONJE)
            with open("ICONJE.png", "wb") as f:
                f.write(ICONJE)
            file = discord.File("ICONJE.png")
        Hostname = IPStatus['hostname'] if 'hostname' in IPStatus else '無'
        IPInfo = requests.get('http://ip-api.com/json/' + IP)
        IPInfo = IPInfo.json()

        if IPInfo['status'] != "fail":

            Location = IPInfo['country'] + ", " + IPInfo['city']
            AS = IPInfo['as']
            ISP = IPInfo['isp']

        if IP[0:3] != "127":
            if IPStatus['online'] == True:

                PlayerOnline = IPStatus['players']['online']
                PlayerMax = IPStatus['players']['max']
                Version = IPStatus['version']
                Protocol = IPStatus['protocol']
                Motd1 = IPStatus['motd']['clean'][0]
                Motd2 = IPStatus['motd']['clean'][1] if 'motd' in IPStatus and 'clean' in IPStatus['motd'] and len(IPStatus['motd']['clean']) > 1 else None
                Motd = Motd1 + "\n" + Motd2 if Motd2 != None else Motd1
                Status = f"<:accept:1045921746219450389> **__在線__** \n> 伺服器人數：{PlayerOnline}/{PlayerMax}\n> 伺服器版本：{Version}\n> 真實 IP：{IP}:{Port}\n> Protocol 版本：{Protocol}\n```{Motd}```"
                Color = 0x55ff55

            else:
                Status = "<:cancel:1045921758215163924> **__離線__**"
                Color = 0xff5555

            embedJE = discord.Embed(title=f"{ip}",description=f"> {Status}",color=Color)
            embedJE.set_thumbnail(url="attachment://temp_image.png")
            embedJE.set_author(name=f"Minecraft 通用伺服器查詢 ➼ Java ➼ {ip}", url=f"https://mcsrvstat.us/server/{ip}",icon_url="https://cdn-vproxy.pages.dev/vproxy_logo.png")

            IPBEStatus = requests.get('https://api.mcsrvstat.us/bedrock/2/' + ip)
            IPBEStatus = IPBEStatus.json()

            ICONBE = IPBEStatus['icon'] if 'icon' in IPBEStatus else None
            IPBE = IPBEStatus['ip']
            PortBE = IPBEStatus['port']

            if IPBEStatus['online'] == True:

                PlayerOnlineBE = IPBEStatus['players']['online']
                PlayerMaxBE = IPBEStatus['players']['max']
                VersionBE = IPBEStatus['version']
                ProtocolBE = IPBEStatus['protocol']
                Motd1BE = IPBEStatus['motd']['clean'][0]
                Motd2BE = IPBEStatus['motd']['clean'][1] if 'motd' in IPBEStatus and 'clean' in IPBEStatus['motd'] and len(IPBEStatus['motd']['clean']) > 1 else None
                MotdBE = Motd1BE + "\n" + Motd2BE if Motd2BE != None else Motd1BE
                StatusBE = f"<:accept:1045921746219450389> **__在線__** \n> 伺服器人數：{PlayerOnlineBE}/{PlayerMaxBE}\n> 伺服器版本：{VersionBE}\n> 真實 IP：{IPBE}:{PortBE}\n> Protocol 版本：{ProtocolBE}\n```{MotdBE}```"
                Color = 0x55ff55

            else:

                StatusBE = "<:cancel:1045921758215163924> **__離線__**"
                Color = 0xff5555

            embedBE = discord.Embed(title=f"{ip}",description=f"> {StatusBE}",color=Color)
            embedBE.set_author(name=f"Minecraft 通用伺服器查詢 ➼ Bedrock ➼ {ip}",url=f"https://mcsrvstat.us/bedrock/{ip}",icon_url="https://cdn-vproxy.pages.dev/vproxy_logo.png")

            embedIPINFO = discord.Embed(title=f"", description=f"", color=0x2b2d31,timestamp=datetime.datetime.now())
            embedIPINFO.set_author(name=f"Minecraft 通用伺服器查詢 ➼ IP 資訊 ➼ {ip}",url=f"https://mcsrvstat.us/bedrock/{ip}",icon_url="https://cdn-vproxy.pages.dev/vproxy_logo.png")
            embedIPINFO.add_field(name=f"真實 IP：{IP}", value="", inline=False)
            embedIPINFO.add_field(name=f"位置：{Location}", value="", inline=False)
            embedIPINFO.add_field(name=f"主機名稱 ：{Hostname}", value="", inline=False)
            embedIPINFO.add_field(name=f"AS：{AS}", value="", inline=False)
            embedIPINFO.add_field(name=f"ISP：{ISP}", value="", inline=False)
            embedIPINFO.set_footer(text=f"{Name}")

            await ctx.edit(file=file,content="<a:icon_yes_animated:1067441695769239552> 查詢成功",embeds=[embedJE,embedBE,embedIPINFO])

        else:
            await ctx.edit(content="<a:icon_no_animated:1067441718506565642> 查詢失敗，請重新檢查您的 IP 是否有誤。")

# 機器人資訊&多此一舉的設計
@client.slash_command(description = "機器人資訊")
async def debug(ctx):
    author = str(base64.b64decode("ZmFueXVlZWU="), "utf-8")
    embed = discord.Embed(title="Soruce Code Link", url="https://github.com/FanYueee/MCNetEngine", color=0x69ff97, timestamp=datetime.datetime.now())
    embed.set_author(name="Debug Information")
    embed.add_field(name="Required Library", value="py-cord\nrequests", inline=True)
    embed.add_field(name="Author", value=f"{str(author)}",inline=True)
    embed.add_field(name="Ping", value=f"{int(client.latency*1000)}ms", inline=True)
    embed.add_field(name="Bot Version", value=f"{ver}", inline=True)
    embed.set_footer(text="MCNetEngine")
    await ctx.respond(embed=embed)

client.run(token)