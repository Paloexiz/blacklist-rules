# mihomo_configuration

**Select your Language: English | [简体中文](README.zh-cn.md)**

Version 7.01.

You can leave a comment here if you found any problem or have any suggestion.

## Note

This file is mainly designed to proxy these following:

- Known IPs or domain that banned by the illegal Firewall you may know;
- Some application service that not available yet at your current region.
- Due to slow connection of some application service in current Internet provided by your ISP, cannot load all resources successfully for a long time.

## About "Proxy Groups"

- Node selection Groups
  - Proxy: Your main switch, choose a mode first to access most of IPs or domains that banned by the Firewall.
  - All Nodes: You can see all nodes of subscription(s), choose a node (or choose a node in other "[Region] Nodes").
  - HK/TW/JP/US/SG/UK Nodes: You only can see HK/TW/JP/US/SG/UK nodes of subscription(s), choose a node (otherwise, choose a node in "All Nodes" or other "[Region] Nodes").
  - Minimum delay: Automatically choose a node which has a minimum delay in "All Nodes".
  - Load Balancing (Hashing): It will assign requests with the same target address to the same proxy node within "All Nodes".
  - Load Balancing (Round Robin): It will distribute all requests among different proxy nodes within within "All Nodes".
- Contact
  - Discord: Include text, picture and game resources, exclude voice channel service. "Proxy" in default.
  - Telegram: "Proxy" in default.
- AI
  - ChatGPT: "Proxy" in default.
  - Claude: "Proxy" in default.
  - Copilot: "DIRECT" in default. Attention, if you choose proxy mode node in this proxy group, "www.bing.com" will be proxied. It will affect your experience when you search something in bing search engine.
  - Gemini: "Proxy" in default.
- Media
  - Bilibili: "DIRECT" in default.
  - Disney: "Proxy" in default.
  - DMM: "Proxy" in default.
  - Netflix: "Proxy" in default.
  - Niconico: "Proxy" in default.
  - Pixiv: "Proxy" in default.
  - Spotify: "Proxy" in default.
  - Twitch: "Proxy" in default.
  - Youtube: "Proxy" in default.
  - Z-Library: "Proxy" in default.
- Social
  - Bluesky: "Proxy" in default.
  - LINUX DO: "Proxy" in default.
  - Twitter: "Proxy" in default.
- Cloud Storage
  - iCloud: "DIRECT" in default.
  - OneDrive: "DIRECT" in default.
- Tech
  - Aliyun: "DIRECT" in default.
  - Cloudflare: "DIRECT" in default.
  - Docker: "Proxy" in default.
  - GitHub: "Proxy" in default.
  - GitLab: "Proxy" in default.
- Services Provider
  - Apple: "DIRECT" in default.
  - Google: "Proxy" in default.
  - Microsoft: "DIRECT" in default.
- Other Groups
  - Adobe Activation Service: "REJECT" in default. You can choose "DIRECT" mode if you're using truly licensed Adobe software.
  - AdBlock: It will block spy connections and advertisements. "REJECT" in default.
  - Domestic: Include CN domains & IPs. "DIRECT" in default.
  - Game Boosting: Boost some game that may not stably connect to the internet provided by your ISP. "DIRECT" in default.
  - Game Unlocking: Unlock some game that not serve for some regions. "Proxy" in default.
  - Google FCM: "Proxy" in default.
  - Others: "DIRECT" in default. If you choose proxy mode in this proxy group, it will proxy all services that are not listed in above proxy groups. It won't affect domestic connections.
  - Safe Browse: "Proxy" in default.
