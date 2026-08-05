# CommonRules Collection - Security Series

**Select your Language: English | [简体中文](README.zh-cn.md)**

## Type Ⅰ - DOMAIN ONLY

 **If you would like to use `anonymityservice_domainonly.yaml`, you can get it with following links:**

- Original: [View or Download](https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/security/clash/anonymityservice_domainonly.yaml)
- CDN(maybe 24-hour-delaying sync): [View or Download](https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/security/clash/anonymityservice_domainonly.yaml)

### Note

**To use `anonymityservice_domainonly.yaml`, `behavior` property should be `domain`.**

### Example

```yaml
rule-providers:
  blacklistrules-security_domain:
    {
      type: http,
      interval: 86400,
      format: yaml,
      behavior: domain,
      url: "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/security/clash/anonymityservice_domainonly.yaml",
      path: "./ruleset/Paloexiz/anonymityservice_domainonly.yaml",
    }
```

## Type Ⅱ - PROCESS NAME ONLY

 **If you would like to use `anonymityservice_processnameonly.yaml`, you can get it with following links:**

- Original: [View or Download](https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/security/clash/anonymityservice_processnameonly.yaml)
- CDN(maybe 24-hour-delaying sync): [View or Download](https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/security/clash/anonymityservice_processnameonly.yaml)

### Note

**To use `anonymityservice_processnameonly.yaml`, `behavior` property should be `classical`.**

### Example

```yaml
rule-providers:
  blacklistrules-security_process:
    {
      type: http,
      interval: 86400,
      format: yaml,
      behavior: classical,
      url: "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/security/clash/anonymityservice_processnameonly.yaml",
      path: "./ruleset/Paloexiz/anonymityservice_processnameonly.yaml",
    }
```
