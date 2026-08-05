# Other Rules - Bluesky

**Select your Language: English | [简体中文](README.zh-cn.md)**

## For Clash Kernel Only

**If you would like to use `bluesky.yaml`, you can get it with the following links:**

- Original: [View or Download](https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/other/clash/bluesky/bluesky.yaml)
- CDN (may have a 24-hour sync delay): [View or Download](https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/other/clash/bluesky/bluesky.yaml)

### Note

**To use `bluesky.yaml`, the `behavior` property should be `domain`.**

### Example

```yaml
rule-providers:
  bluesky:
    {
      type: http,
      interval: 86400,
      format: yaml,
      behavior: domain,
      url: "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/other/clash/bluesky/bluesky.yaml",
      path: "./ruleset/paloexiz/bluesky.yaml",
    }
```
