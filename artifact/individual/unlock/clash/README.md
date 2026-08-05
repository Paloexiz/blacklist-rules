# CommonRules Collection - Unlock Series

**Select your Language: English | [简体中文](README.zh-cn.md)**

## Type Ⅰ - NO GAME & DOMAIN ONLY

 **If you would like to use `blockeddomains_nogame_domainonly.yaml`, you can get it with following links:**

- Original: [View or Download](https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/unlock/clash/blockeddomains_nogame_domainonly.yaml)
- CDN(maybe 24-hour-delaying sync): [View or Download](https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/unlock/clash/blockeddomains_nogame_domainonly.yaml)

### Note

**To use `blockeddomains_nogame_domainonly.yaml`, `behavior` property should be `domain`.**

### Example

```yaml
rule-providers:
  blacklistrules-unlock_nogame:
    {
      type: http,
      interval: 86400,
      format: yaml,
      behavior: domain,
      url: "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/unlock/clash/blockeddomains_nogame_domainonly.yaml",
      path: "./ruleset/Paloexiz/blockeddomains_nogame_domainonly.yaml",
    }
```

## Type Ⅱ - GAME ONLY & DOMAIN ONLY

 **If you would like to use `blockedgames_domainonly.yaml`, you can get it with following links:**

- Original: [View or Download](https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/unlock/clash/blockedgames_domainonly.yaml)
- CDN(maybe 24-hour-delaying sync): [View or Download](https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/unlock/clash/blockedgames_domainonly.yaml)

### Note

**To use `blockedgames_domainonly.yaml`, `behavior` property should be `domain`.**

### Example

```yaml
rule-providers:
  blacklistrules-unlock_game:
    {
      type: http,
      interval: 86400,
      format: yaml,
      behavior: domain,
      url: "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/unlock/clash/blockedgames_domainonly.yaml",
      path: "./ruleset/Paloexiz/blockedgames_domainonly.yaml",
    }
```
