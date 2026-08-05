# BlacklistRules Collection

**Select your Language: English | [简体中文](README.zh-cn.md)**

## For Clash Kernel

 **If you would like to use `blacklistrules_domainonly.yaml`, you can get it with following links:**

- Original: [View or Download](https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/common/clash/blacklistrules_domainonly.yaml)
- CDN(maybe 24-hour-delaying sync): [View or Download](https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/common/clash/blacklistrules_domainonly.yaml)

### Note

**To use `blacklistrules_domainonly.yaml`, `behavior` property should be `domain`.**

### Example

```yaml
rule-providers:
  blacklistrules:
    {
      type: http,
      interval: 86400,
      format: yaml,
      behavior: domain,
      url: "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/common/clash/blacklistrules_domainonly.yaml",
      path: "./ruleset/Paloexiz/blacklistrules_domainonly.yaml",
    }
```
