# 其它规则 - Bluesky

**语言选择：[English](README.md) | 简体中文**

## 仅适用于 Clash 内核

**如果您需要使用 `bluesky.yaml` 文件，可以通过以下链接获取：**

- 原始链接：[查看或下载](https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/other/clash/bluesky/bluesky.yaml)
- 镜像链接（同步可能延迟 24 小时）：[查看或下载](https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/other/clash/bluesky/bluesky.yaml)

### 注意事项

**为了正常调用 `bluesky.yaml` 文件，`behavior` 属性应为 `domain`。**

### 示例代码

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
