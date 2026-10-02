# Third-Party Rules

**Select your Language: English | [简体中文](README.zh-cn.md)**

## Introduction

Synchronizes every third-party provider used by the Mihomo override in Clash, Surge and sing-box formats. Custom rules remain in the existing `artifact/` directories.

**Update frequency**: one scheduled sync per day, at **03:23** Hong Kong time (UTC+8, the same as Beijing time), corresponding to **19:23 UTC on the previous day**.

The schedule takes effect after the [workflow](../.github/workflows/sync-third-party-rules.yml) is published to `main`. 03:23 is the scheduled trigger time; [GitHub Actions scheduling can be delayed](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows#scheduled-workflows-running-at-unexpected-times). Check the Actions run history for actual start and completion times; updated rule files are not guaranteed to be available at 03:23.

## Repository Maintenance

The provider inventory is read directly from `ruleProviders` in `client_conf/mihomo_override/mihomo_override.js`. The workflow runs `python workflow_scripts/sync_third_party_rules.py`, downloads readable upstream sources, reuses the existing converter for all three formats, and updates the source manifest. License files remain fixed copies and are maintained through manual review.

All sources and conversions are validated before outputs are updated. A download, content or conversion failure prevents publication and preserves the previously published files. Unchanged contents create no commit. Run Sync Third-Party Rules manually from Actions when needed.

Maintain third-party rules upstream rather than editing generated files. Conversion preserves matching categories and adds no routing policies.

## Third-Party Licenses

Rules retain their upstream copyright and license terms; this repository does not replace those terms. See [NOTICE.md](NOTICE.md) and [licenses/](licenses/) for complete notices and original texts. AdRules aggregates multiple sources; its 0BSD script license does not license all rule data. Entries without a stated license retain the upstream declaration.

## Related documents and links

**Note**: CDN links can lag because of caching. Use the original links for the latest files.

### For sing-box Kernel - Choose your TYPE

Remote rule sets use the original URL with `type: remote` and `format: source`. The applications provider contains process rules and requires an environment that supports process identification.

<table>
  <tr align="center">
    <td><b>TYPE</b></td>
    <td><b>View or Download by an Original Link</b></td>
    <td><b>View or Download by a CDN Link</b></td>
  </tr>
  <tr align="center">
    <td>adrules</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/adrules_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/adrules_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>private</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/private_IP.json">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/private_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/private_IP.json">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/private_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Steam</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Steam_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Steam_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Copilot</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Copilot_IP.json">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Copilot_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Copilot_IP.json">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Copilot_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>google-gemini</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/google-gemini_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/google-gemini_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>adobe-activation</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/adobe-activation_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/adobe-activation_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>googlefcm</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/googlefcm_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/googlefcm_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>z-library</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/z-library_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/z-library_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>linuxdo</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/linuxdo_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/linuxdo_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>twitter</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/twitter_IP.json">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/twitter_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/twitter_IP.json">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/twitter_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>github</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/github_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/github_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>gitlab</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/gitlab_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/gitlab_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>onedrive</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/onedrive_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/onedrive_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Microsoft</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Microsoft_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Microsoft_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>openai</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/openai_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/openai_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>anthropic</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/anthropic_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/anthropic_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>discord</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/discord_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/discord_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>aliyun</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/aliyun_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/aliyun_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>cloudflare</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/cloudflare_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/cloudflare_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>docker</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/docker_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/docker_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>homebrew</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/homebrew_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/homebrew_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>python</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/python_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/python_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>icloud</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/icloud_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/icloud_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>apple</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/apple_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/apple_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>youtube</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/youtube_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/youtube_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Google</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Google_IP.json">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Google_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Google_IP.json">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Google_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>twitch</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/twitch_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/twitch_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>niconico</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/niconico_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/niconico_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Pixiv</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Pixiv_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Pixiv_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>netflix</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/netflix_IP.json">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/netflix_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/netflix_IP.json">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/netflix_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>disney</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/disney_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/disney_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>bilibili</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/bilibili_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/bilibili_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>spotify</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/spotify_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/spotify_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>dmm</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/dmm_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/dmm_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Telegram</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Telegram_IP.json">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/Telegram_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Telegram_IP.json">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/Telegram_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>gfw</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/gfw_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/gfw_Domain.json">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>applications</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/applications.json">Process Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/applications.json">Process Only</a></td>
  </tr>
  <tr align="center">
    <td>cn</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/sing-box/cn_Domain.json">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/sing-box/cn_Domain.json">Domain Only</a></td>
  </tr>
</table>

### For Clash Kernel - Choose your TYPE

Use `behavior: domain` for Domain files, `behavior: ipcidr` for IP files and `behavior: classical` for applications. All files use YAML.

<table>
  <tr align="center">
    <td><b>TYPE</b></td>
    <td><b>View or Download by an Original Link</b></td>
    <td><b>View or Download by a CDN Link</b></td>
  </tr>
  <tr align="center">
    <td>adrules</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/adrules_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/adrules_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>private</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/private_IP.yaml">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/private_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/private_IP.yaml">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/private_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Steam</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Steam_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Steam_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Copilot</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Copilot_IP.yaml">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Copilot_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Copilot_IP.yaml">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Copilot_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>google-gemini</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/google-gemini_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/google-gemini_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>adobe-activation</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/adobe-activation_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/adobe-activation_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>googlefcm</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/googlefcm_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/googlefcm_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>z-library</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/z-library_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/z-library_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>linuxdo</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/linuxdo_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/linuxdo_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>twitter</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/twitter_IP.yaml">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/twitter_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/twitter_IP.yaml">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/twitter_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>github</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/github_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/github_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>gitlab</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/gitlab_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/gitlab_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>onedrive</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/onedrive_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/onedrive_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Microsoft</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Microsoft_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Microsoft_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>openai</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/openai_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/openai_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>anthropic</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/anthropic_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/anthropic_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>discord</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/discord_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/discord_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>aliyun</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/aliyun_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/aliyun_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>cloudflare</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/cloudflare_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/cloudflare_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>docker</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/docker_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/docker_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>homebrew</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/homebrew_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/homebrew_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>python</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/python_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/python_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>icloud</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/icloud_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/icloud_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>apple</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/apple_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/apple_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>youtube</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/youtube_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/youtube_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Google</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Google_IP.yaml">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Google_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Google_IP.yaml">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Google_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>twitch</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/twitch_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/twitch_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>niconico</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/niconico_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/niconico_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Pixiv</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Pixiv_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Pixiv_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>netflix</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/netflix_IP.yaml">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/netflix_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/netflix_IP.yaml">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/netflix_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>disney</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/disney_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/disney_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>bilibili</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/bilibili_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/bilibili_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>spotify</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/spotify_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/spotify_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>dmm</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/dmm_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/dmm_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Telegram</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Telegram_IP.yaml">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/Telegram_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Telegram_IP.yaml">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Telegram_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>gfw</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/gfw_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/gfw_Domain.yaml">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>applications</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/applications.yaml">Process Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/applications.yaml">Process Only</a></td>
  </tr>
  <tr align="center">
    <td>cn</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/clash/cn_Domain.yaml">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/cn_Domain.yaml">Domain Only</a></td>
  </tr>
</table>

### For Surge Kernel - Choose your TYPE

Use `DOMAIN-SET` for domain files and `RULE-SET` for IP and applications files. IP files contain `IP-CIDR` / `IP-CIDR6` entries with `no-resolve`.

<table>
  <tr align="center">
    <td><b>TYPE</b></td>
    <td><b>View or Download by an Original Link</b></td>
    <td><b>View or Download by a CDN Link</b></td>
  </tr>
  <tr align="center">
    <td>adrules</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/adrules_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/adrules_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>private</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/private_IP.list">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/private_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/private_IP.list">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/private_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Steam</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Steam_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Steam_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Copilot</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Copilot_IP.list">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Copilot_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Copilot_IP.list">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Copilot_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>google-gemini</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/google-gemini_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/google-gemini_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>adobe-activation</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/adobe-activation_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/adobe-activation_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>googlefcm</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/googlefcm_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/googlefcm_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>z-library</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/z-library_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/z-library_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>linuxdo</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/linuxdo_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/linuxdo_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>twitter</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/twitter_IP.list">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/twitter_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/twitter_IP.list">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/twitter_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>github</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/github_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/github_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>gitlab</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/gitlab_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/gitlab_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>onedrive</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/onedrive_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/onedrive_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Microsoft</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Microsoft_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Microsoft_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>openai</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/openai_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/openai_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>anthropic</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/anthropic_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/anthropic_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>discord</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/discord_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/discord_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>aliyun</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/aliyun_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/aliyun_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>cloudflare</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/cloudflare_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/cloudflare_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>docker</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/docker_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/docker_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>homebrew</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/homebrew_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/homebrew_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>python</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/python_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/python_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>icloud</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/icloud_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/icloud_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>apple</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/apple_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/apple_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>youtube</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/youtube_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/youtube_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Google</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Google_IP.list">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Google_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Google_IP.list">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Google_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>twitch</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/twitch_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/twitch_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>niconico</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/niconico_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/niconico_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Pixiv</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Pixiv_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Pixiv_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>netflix</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/netflix_IP.list">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/netflix_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/netflix_IP.list">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/netflix_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>disney</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/disney_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/disney_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>bilibili</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/bilibili_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/bilibili_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>spotify</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/spotify_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/spotify_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>dmm</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/dmm_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/dmm_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>Telegram</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Telegram_IP.list">IP Only</a><br><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/Telegram_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Telegram_IP.list">IP Only</a><br><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/Telegram_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>gfw</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/gfw_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/gfw_Domain.list">Domain Only</a></td>
  </tr>
  <tr align="center">
    <td>applications</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/applications.list">Process Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/applications.list">Process Only</a></td>
  </tr>
  <tr align="center">
    <td>cn</td>
    <td><a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/third_party/surge/cn_Domain.list">Domain Only</a></td>
    <td><a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/surge/cn_Domain.list">Domain Only</a></td>
  </tr>
</table>
