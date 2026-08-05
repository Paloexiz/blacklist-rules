# blacklist-rules

**Select your Language: English | [简体中文](README.zh-cn.md)**

## Introduction

Rules for directing outbound packets.

**Update frequency**: *anytime*.

## Disclaimer

Use this repository only in legal and authorized scenarios. The rules are meant for network routing, filtering, research, and maintenance. They are not meant to support unlawful activity, violations of service terms, or violations of third-party rights.

You are responsible for how you use, share, or modify this repository. The maintainers are not responsible for misuse. This repository is provided as-is, without warranty; see the [GNU General Public License v3.0](LICENSE) for license terms.

## Repository Maintenance

Manual rule edits go in `rule_sources/*.rules`. Generated outputs live under `artifact/common/`, `artifact/individual/`, and `artifact/other/`.

To update this repository:

1. Edit the matching source file in `rule_sources/`.
2. Commit and push the source changes.
3. GitHub Actions runs `python workflow_scripts/build_rules.py` and commits the generated outputs.

On pull requests, GitHub Actions checks generated outputs against the source files. Run `python workflow_scripts/build_rules.py --check` locally if you want a quick check before pushing.

See [rule_sources/README.md](rule_sources/README.md) for the source format and maintenance rules.

## Related documents and links

**Note**: CDN links can lag because of caching. Use the original links if you need the latest files.

### For Clash Kernel - Choose your TYPE

<table>
  <tr align="center">
    <td>
      <b>TYPE</b>
    </td>
    <td>
      <b>View or Download by an Oringal Link</b>
    </td>
    <td>
      <b>View or Download by a CDN Link</b>
    </td>
  </tr>
  <tr align="center">
    <td>
      <a href="https://github.com/Paloexiz/blacklist-rules/tree/main/artifact/common/clash">CustomRules Collection</a>
    </td>
    <td>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/common/clash/blacklistrules_domainonly.yaml">Domain Only</a>
    </td>
    <td>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/common/clash/blacklistrules_domainonly.yaml">Domain Only</a>
    </td>
  </tr>
  <tr align="center">
    <td>
      <a href="https://github.com/Paloexiz/blacklist-rules/tree/main/artifact/individual/boost/clash">Common-Boost</a>
    </td>
    <td>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/boost/clash/slowdomains_nogame_domainonly.yaml">No game & Domain Only</a>
      <br>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/boost/clash/slowdomains_gameonly_domainonly.yaml">Game Only & Domain Only</a>
    </td>
    <td>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/boost/clash/slowdomains_nogame_domainonly.yaml">No game & Domain Only</a>
      <br>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/boost/clash/slowdomains_gameonly_domainonly.yaml">Game Only & Domain Only</a>
    </td>
  </tr>
  <tr align="center">
    <td>
      <a href="https://github.com/Paloexiz/blacklist-rules/tree/main/artifact/individual/security/clash">Common-Security</a>
    </td>
    <td>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/security/clash/anonymityservice_domainonly.yaml">Domain Only</a>
      <br>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/security/clash/anonymityservice_processnameonly.yaml">Process Name Only</a>
    </td>
    <td>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/security/clash/anonymityservice_domainonly.yaml">Domain Only</a>
      <br>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/security/clash/anonymityservice_processnameonly.yaml">Process Name Only</a>
    </td>
  </tr>
  <tr align="center">
    <td>
      <a href="https://github.com/Paloexiz/blacklist-rules/tree/main/artifact/individual/unlock/clash">Common-Unlock</a>
    </td>
    <td>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/unlock/clash/blockeddomains_nogame_domainonly.yaml">No game & Domain Only</a>
      <br>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/unlock/clash/blockedgames_domainonly.yaml">Game Only & Domain Only</a>
    </td>
    <td>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/unlock/clash/blockeddomains_nogame_domainonly.yaml">No game & Domain Only</a>
      <br>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/unlock/clash/blockedgames_domainonly.yaml">Game Only & Domain Only</a>
    </td>
  </tr>
</table>

### For Surge Kernel - Choose your TYPE

<table>
  <tr align="center">
    <td>
      <b>TYPE</b>
    </td>
    <td>
      <b>View or Download by an Oringal Link</b>
    </td>
    <td>
      <b>View or Download by a CDN Link</b>
    </td>
  </tr>
  <tr align="center">
    <td>
      <a href="https://github.com/Paloexiz/blacklist-rules/tree/main/artifact/common/surge">CustomRules Collection</a>
    </td>
    <td>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/common/surge/blacklistrules_domainonly.list">Domain Only</a>
    </td>
    <td>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/common/surge/blacklistrules_domainonly.list">Domain Only</a>
    </td>
  </tr>
  <tr align="center">
    <td>
      <a href="https://github.com/Paloexiz/blacklist-rules/tree/main/artifact/individual/boost/surge">Common-Boost</a>
    </td>
    <td>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/boost/surge/slowdomains_nogame_domainonly.list">No game & Domain Only</a>
      <br>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/boost/surge/slowdomains_gameonly_domainonly.list">Game Only & Domain Only</a>
    </td>
    <td>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/boost/surge/slowdomains_nogame_domainonly.list">No game & Domain Only</a>
      <br>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/boost/surge/slowdomains_gameonly_domainonly.list">Game Only & Domain Only</a>
    </td>
  </tr>
  <tr align="center">
    <td>
      <a href="https://github.com/Paloexiz/blacklist-rules/tree/main/artifact/individual/security/surge">Common-Security</a>
    </td>
    <td>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/security/surge/anonymityservice_domainonly.list">Domain Only</a>
      <br>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/security/surge/anonymityservice_processnameonly.list">Process Name Only</a>
    </td>
    <td>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/security/surge/anonymityservice_domainonly.list">Domain Only</a>
      <br>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/security/surge/anonymityservice_processnameonly.list">Process Name Only</a>
    </td>
  </tr>
  <tr align="center">
    <td>
      <a href="https://github.com/Paloexiz/blacklist-rules/tree/main/artifact/individual/unlock/surge">Common-Unlock</a>
    </td>
    <td>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/unlock/surge/blockeddomains_nogame_domainonly.list">No game & Domain Only</a>
      <br>
      <a href="https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/unlock/surge/blockedgames_domainonly.list">Game Only & Domain Only</a>
    </td>
    <td>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/unlock/surge/blockeddomains_nogame_domainonly.list">No game & Domain Only</a>
      <br>
      <a href="https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/unlock/surge/blockedgames_domainonly.list">Game Only & Domain Only</a>
    </td>
  </tr>
</table>
