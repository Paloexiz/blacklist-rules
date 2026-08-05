# CommonRules Collection - Boost Series

**Select your Language: English | [简体中文](README.zh-cn.md)**

## Type Ⅰ - NO GAME & DOMAIN ONLY

 **If you would like to use `slowdomains_nogame_domainonly.yaml`, you can get it with following links:**

- Original: [View or Download](https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/boost/clash/slowdomains_nogame_domainonly.yaml)
- CDN(maybe 24-hour-delaying sync): [View or Download](https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/boost/clash/slowdomains_nogame_domainonly.yaml)

### Note

**To use `slowdomains_nogame_domainonly.yaml`, `behavior` property should be `domain`.**

### Example

```yaml
rule-providers:
  blacklistrules-boost:
    {
      type: http,
      interval: 86400,
      format: yaml,
      behavior: domain,
      url: "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/boost/clash/slowdomains_nogame_domainonly.yaml",
      path: "./ruleset/Paloexiz/slowdomains_nogame_domainonly.yaml",
    }
```

# CommonRules Collection - Boost Series

**Select your Language: English | [简体中文](README.zh-cn.md)**

## Type Ⅱ - GAME ONLY & DOMAIN ONLY

 **If you would like to use `slowdomains_gameonly_domainonly.yaml`, you can get it with following links:**

- Original: [View or Download](https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/boost/clash/slowdomains_gameonly_domainonly.yaml)
- CDN(maybe 24-hour-delaying sync): [View or Download](https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/boost/clash/slowdomains_gameonly_domainonly.yaml)

### Note

**To use `slowdomains_gameonly_domainonly.yaml`, `behavior` property should be `domain`.**

### Example

```yaml
rule-providers:
  blacklistrules-boost:
    {
      type: http,
      interval: 86400,
      format: yaml,
      behavior: domain,
      url: "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/boost/clash/slowdomains_gameonly_domainonly.yaml",
      path: "./ruleset/Paloexiz/slowdomains_gameonly_domainonly.yaml",
    }
```
