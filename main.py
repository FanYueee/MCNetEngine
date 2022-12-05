import discord
from discord.commands import option
import json
import requests
import datetime

intents = discord.Intents.default()
client = discord.Bot(intents=intents)

print("  __  __  _____ _   _      _   ______             _             ")
print(" |  \/  |/ ____| \ | |    | | |  ____|           (_)            ")
print(" | \  / | |    |  \| | ___| |_| |__   _ __   __ _ _ _ __   ___  ")
print(" | |\/| | |    | . ` |/ _ \ __|  __| | '_ \ / _` | | '_ \ / _ \ ")
print(" | |  | | |____| |\  |  __/ |_| |____| | | | (_| | | | | |  __/ ")
print(" |_|  |_|\_____|_| \_|\___|\__|______|_| |_|\__, |_|_| |_|\___| ")
print("                                             __/ |              ")
print("DiscodBot-MCNetEngine Create By FanYueee    |___/        Ver 1.0")
print("Required API: api.mcsrvstat.us, ip-api.com")

# 讀取 config.json
with open('config.json', mode='r',encoding='utf8') as config:
    config = json.load(config)

# 控制台啟動通知
@client.event
async def on_ready():
    print(f"\n已成功啟動 {client.user}")

# 指令主體
@client.slash_command(description = "查詢Minecraft伺服器資訊")
@option("ip",description = "輸入欲查詢的伺服器IP")
async def mcs(ctx, ip: str):
    # 偵測前三個字是否為127開頭，如果是直接回應錯誤
    if ip[0:3] != "127":
        response_check = str("<Response [200]>")
        game = requests.get('https://api.mcsrvstat.us/2/' + ip)
        response_mcsrv = str(game)
        # 判斷 mcsrvstat 是否正常回應數值
        if response_mcsrv == response_check:
            game_data = game.json()
            ipaddress = game_data['ip']
            net = requests.get('http://ip-api.com/json/' + ipaddress)
            response_ip = str(net)
            # 判斷 ip-api 是否正常回應數值
            if response_ip == response_check:
                net_data = net.json()
                # 伺服器在線
                if game_data['online'] == True:

                    embed = discord.Embed(title=f"Minecraft 伺服器檢查工具",
                              description=f"**__人數: {game_data['players']['online']}/{game_data['players']['max']}__**```{game_data['motd']['clean'][0]}\n{game_data['motd']['clean'][1]}```", color=0x43cbff, timestamp=datetime.datetime.now())
                    embed.set_author(name=f"{ip}", url=f"https://mcsrvstat.us/server/{game_data['ip']}",
                         icon_url=f"https://api.mcsrvstat.us/icon/{ip}")
                    embed.add_field(name=f"➼ 版本資訊", value=f"**Minecraft版本:** {game_data['version']}\n**Protocol版本:** {game_data['protocol']}", inline=False)
                    embed.add_field(name="➼ 網路資訊",
                        value=f"**原始IP:** {game_data['ip']}:{game_data['port']}\n**主機名稱:** {game_data['hostname']}\n**國家:** {net_data['country']}\n**ASN:** {net_data['as']}\n**ISP:** {net_data['isp']}\n**組織:** {net_data['org']}",
                        inline=False)
                    await ctx.respond(embed=embed)
                    # 伺服器不在線，但回應的IP非127.0.0.1
                elif game_data['ip'] != "127.0.0.1" and game_data['online'] == False:
                    embed = discord.Embed(title=f"Minecraft 伺服器檢查工具",
                              description=f"**__該伺服器離線或並未運行伺服器__**", color=0xea5455, timestamp=datetime.datetime.now())
                    embed.set_author(name=f"{ip}", url=f"https://mcsrvstat.us/server/{game_data['ip']}",
                         icon_url=f"https://api.mcsrvstat.us/icon/{ip}")
                    embed.add_field(name="➼ 網路資訊",
                        value=f"**原始IP:** {game_data['ip']}:{game_data['port']}\n**主機名稱:** {game_data['hostname']}\n**國家:** {net_data['country']}\n**ASN:** {net_data['as']}\n**ISP:** {net_data['isp']}\n**組織:** {net_data['org']}",
                        inline=False)
                    await ctx.respond(embed=embed)
                    # 伺服器不在線，且回應的是127.0.0.1(無法解析網域或其他錯誤)
                else:
                    await ctx.respond("錯誤: 您輸入的IP有誤，無法解析")
            else:
                await ctx.respond("錯誤: http://ip-api.com/json/ 無法正常回傳資料")
        else:
            await ctx.respond("錯誤: https://api.mcsrvstat.us/2/ 無法正常回傳資料")
    else:
        await ctx.respond("錯誤: 無法使用內網IP查詢")

client.run(config['token'])
