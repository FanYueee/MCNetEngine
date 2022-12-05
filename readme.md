# DiscordBot MCNetEngine
一個可藉由 Discord 查詢 Minecraft 伺服器或 IP 網路資訊的機器人。

## 必需函式庫
僅代表開發時使用版本，不代表其他版本無法部署。

|函式庫名稱 |版本|
|-----|--------|
|py-cord|2.3.1|
|requests|2.28.1|

## 設定
[MCNetEngine/config.json](https://github.com/FanYueee/MCNetEngine/blob/main/config.json)
```yaml
{  
  "token": ""  # Discord Bot Token
}
```

## 功能
* /mcs \<IP>  - 查詢 Minecraft 伺服器資訊（限 Java 版本）
	* 人數
	* MOTD
	* 伺服器版本
	* Protocol 版本
	* 原始IP/Port
	* 主機名稱
	* IP 國家
	* ASN
	* ISP
	* 組織

## 使用的 API
查詢 Minecraft 伺服器相關資訊－https://api.mcsrvstat.us/

查詢 IP 相關資訊－http://ip-api.com/

