# 第三方规则

**语言选择：[English](README.md) | 简体中文**

## 项目介绍

同步 Mihomo override 中使用的全部第三方规则，并提供 Clash、Surge 和 sing-box 三种格式。自有规则仍位于原有 `artifact/` 目录。

**更新频率**：每天定时同步一次，计划在香港时间（UTC+8，与北京时间相同）凌晨 **03:23** 触发，对应前一天 UTC **19:23**。

定时配置随 [Workflow](../.github/workflows/sync-third-party-rules.yml) 发布到 `main` 后生效。03:23 是计划触发时间；[GitHub Actions 调度可能延迟](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows#scheduled-workflows-running-at-unexpected-times)，实际开始与完成时间以 Actions 运行记录为准，不能保证规则文件在 03:23 已更新完成。

## 维护方式

同步清单直接读取 `client_conf/mihomo_override/mihomo_override.js` 的 `ruleProviders`，不另行维护一份应用列表。Workflow 运行 `python workflow_scripts/sync_third_party_rules.py`，从原发布者下载可读文本，复用现有转换器生成三种格式，并更新来源清单。许可文件保留固定副本，变更需人工审核。

全部来源和转换验证成功后才更新产物。任何下载、内容或转换失败都会使 Workflow 失败且不提交新规则，已发布文件继续保留。内容不变时不生成提交。可在 Actions 中手动运行 Sync Third-Party Rules。

请在上游维护第三方规则，不要手动编辑生成文件。转换保留匹配分类，不添加分流出口。

## 第三方许可

规则沿用各来源的版权与许可，仓库自身的许可证不替代第三方许可。完整说明及原文见 [NOTICE.zh-cn.md](NOTICE.zh-cn.md) 和 [licenses/](licenses/)。AdRules 的生成规则是多来源聚合；其脚本的 0BSD 许可不能作为全部规则数据的许可。原始来源表中未明确许可的条目按上游声明保留，不另行指定许可。

## 相关文档与链接

**提示**：CDN 镜像可能因为缓存而滞后。需要最新文件时，请优先使用原始链接。

### 适用于 sing-box 内核 - 选择您的类型

远程规则集填写原始链接，设置 `type: remote`、`format: source`。applications 是客户端进程规则，需使用支持进程识别的运行环境。

<table>
  <tr align="center">
    <td><b>类型</b></td>
    <td><b>通过原始链接以查看或下载</b></td>
    <td><b>通过镜像链接以查看或下载</b></td>
  </tr>
  <tr align="center">
    <td>adrules</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/adrules_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/adrules_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>private</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/private_IP.json">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/private_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/private_IP.json">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/private_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Steam</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Steam_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Steam_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Copilot</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Copilot_IP.json">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Copilot_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Copilot_IP.json">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Copilot_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>google-gemini</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/google-gemini_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/google-gemini_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>adobe-activation</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/adobe-activation_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/adobe-activation_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>googlefcm</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/googlefcm_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/googlefcm_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>z-library</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/z-library_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/z-library_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>linuxdo</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/linuxdo_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/linuxdo_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>twitter</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/twitter_IP.json">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/twitter_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/twitter_IP.json">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/twitter_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>github</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/github_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/github_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>gitlab</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/gitlab_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/gitlab_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>onedrive</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/onedrive_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/onedrive_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Microsoft</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Microsoft_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Microsoft_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>openai</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/openai_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/openai_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>anthropic</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/anthropic_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/anthropic_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>discord</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/discord_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/discord_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>aliyun</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/aliyun_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/aliyun_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>cloudflare</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/cloudflare_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/cloudflare_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>docker</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/docker_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/docker_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>homebrew</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/homebrew_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/homebrew_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>python</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/python_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/python_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>icloud</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/icloud_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/icloud_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>apple</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/apple_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/apple_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>youtube</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/youtube_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/youtube_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Google</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Google_IP.json">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Google_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Google_IP.json">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Google_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>twitch</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/twitch_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/twitch_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>niconico</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/niconico_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/niconico_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Pixiv</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Pixiv_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Pixiv_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>netflix</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/netflix_IP.json">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/netflix_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/netflix_IP.json">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/netflix_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>disney</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/disney_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/disney_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>bilibili</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/bilibili_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/bilibili_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>spotify</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/spotify_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/spotify_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>dmm</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/dmm_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/dmm_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Telegram</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Telegram_IP.json">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Telegram_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Telegram_IP.json">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Telegram_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>gfw</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/gfw_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/gfw_Domain.json">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>applications</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/applications.json">仅进程</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/applications.json">仅进程</a></td>
  </tr>
  <tr align="center">
    <td>cn</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/cn_Domain.json">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/cn_Domain.json">仅域名</a></td>
  </tr>
</table>

### 适用于 Clash 内核 - 选择您的类型

Domain 文件使用 `behavior: domain`，IP 文件使用 `behavior: ipcidr`，applications 使用 `behavior: classical`；格式均为 YAML。

<table>
  <tr align="center">
    <td><b>类型</b></td>
    <td><b>通过原始链接以查看或下载</b></td>
    <td><b>通过镜像链接以查看或下载</b></td>
  </tr>
  <tr align="center">
    <td>adrules</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/adrules_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/adrules_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>private</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/private_IP.yaml">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/private_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/private_IP.yaml">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/private_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Steam</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Steam_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Steam_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Copilot</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Copilot_IP.yaml">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Copilot_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Copilot_IP.yaml">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Copilot_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>google-gemini</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/google-gemini_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/google-gemini_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>adobe-activation</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/adobe-activation_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/adobe-activation_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>googlefcm</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/googlefcm_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/googlefcm_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>z-library</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/z-library_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/z-library_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>linuxdo</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/linuxdo_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/linuxdo_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>twitter</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/twitter_IP.yaml">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/twitter_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/twitter_IP.yaml">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/twitter_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>github</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/github_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/github_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>gitlab</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/gitlab_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/gitlab_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>onedrive</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/onedrive_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/onedrive_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Microsoft</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Microsoft_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Microsoft_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>openai</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/openai_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/openai_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>anthropic</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/anthropic_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/anthropic_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>discord</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/discord_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/discord_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>aliyun</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/aliyun_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/aliyun_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>cloudflare</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/cloudflare_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/cloudflare_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>docker</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/docker_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/docker_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>homebrew</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/homebrew_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/homebrew_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>python</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/python_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/python_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>icloud</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/icloud_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/icloud_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>apple</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/apple_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/apple_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>youtube</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/youtube_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/youtube_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Google</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Google_IP.yaml">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Google_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Google_IP.yaml">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Google_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>twitch</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/twitch_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/twitch_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>niconico</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/niconico_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/niconico_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Pixiv</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Pixiv_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Pixiv_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>netflix</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/netflix_IP.yaml">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/netflix_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/netflix_IP.yaml">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/netflix_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>disney</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/disney_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/disney_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>bilibili</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/bilibili_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/bilibili_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>spotify</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/spotify_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/spotify_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>dmm</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/dmm_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/dmm_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Telegram</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Telegram_IP.yaml">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Telegram_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Telegram_IP.yaml">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Telegram_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>gfw</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/gfw_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/gfw_Domain.yaml">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>applications</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/applications.yaml">仅进程</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/applications.yaml">仅进程</a></td>
  </tr>
  <tr align="center">
    <td>cn</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/cn_Domain.yaml">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/cn_Domain.yaml">仅域名</a></td>
  </tr>
</table>

### 适用于 Surge 内核 - 选择您的类型

域名文件使用 `DOMAIN-SET`；IP 和 applications 文件使用 `RULE-SET`。IP 文件包含 `IP-CIDR` / `IP-CIDR6` 和 `no-resolve`。

<table>
  <tr align="center">
    <td><b>类型</b></td>
    <td><b>通过原始链接以查看或下载</b></td>
    <td><b>通过镜像链接以查看或下载</b></td>
  </tr>
  <tr align="center">
    <td>adrules</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/adrules_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/adrules_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>private</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/private_IP.list">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/private_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/private_IP.list">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/private_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Steam</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Steam_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Steam_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Copilot</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Copilot_IP.list">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Copilot_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Copilot_IP.list">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Copilot_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>google-gemini</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/google-gemini_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/google-gemini_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>adobe-activation</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/adobe-activation_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/adobe-activation_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>googlefcm</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/googlefcm_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/googlefcm_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>z-library</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/z-library_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/z-library_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>linuxdo</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/linuxdo_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/linuxdo_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>twitter</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/twitter_IP.list">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/twitter_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/twitter_IP.list">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/twitter_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>github</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/github_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/github_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>gitlab</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/gitlab_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/gitlab_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>onedrive</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/onedrive_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/onedrive_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Microsoft</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Microsoft_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Microsoft_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>openai</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/openai_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/openai_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>anthropic</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/anthropic_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/anthropic_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>discord</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/discord_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/discord_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>aliyun</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/aliyun_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/aliyun_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>cloudflare</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/cloudflare_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/cloudflare_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>docker</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/docker_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/docker_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>homebrew</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/homebrew_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/homebrew_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>python</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/python_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/python_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>icloud</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/icloud_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/icloud_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>apple</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/apple_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/apple_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>youtube</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/youtube_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/youtube_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Google</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Google_IP.list">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Google_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Google_IP.list">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Google_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>twitch</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/twitch_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/twitch_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>niconico</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/niconico_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/niconico_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Pixiv</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Pixiv_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Pixiv_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>netflix</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/netflix_IP.list">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/netflix_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/netflix_IP.list">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/netflix_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>disney</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/disney_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/disney_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>bilibili</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/bilibili_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/bilibili_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>spotify</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/spotify_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/spotify_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>dmm</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/dmm_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/dmm_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>Telegram</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Telegram_IP.list">仅 IP</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Telegram_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Telegram_IP.list">仅 IP</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Telegram_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>gfw</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/gfw_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/gfw_Domain.list">仅域名</a></td>
  </tr>
  <tr align="center">
    <td>applications</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/applications.list">仅进程</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/applications.list">仅进程</a></td>
  </tr>
  <tr align="center">
    <td>cn</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/cn_Domain.list">仅域名</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/cn_Domain.list">仅域名</a></td>
  </tr>
</table>
