# 通用规则合集 - 安全系列

**语言选择：[English](README.md)  | 简体中文**

## 类型 Ⅰ - 仅域名

 **如果您需要使用 `anonymityservice_domainonly.yaml` 文件，您可以通过如下超链接进行获取：**

- 原始链接：[查看或下载](https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/security/clash/anonymityservice_domainonly.yaml)
- 镜像链接（可能会有24小时的延迟）：[查看或下载](https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/security/clash/anonymityservice_domainonly.yaml)

### 注意事项

**为了能够正常调用 `anonymityservice_domainonly.yaml` 文件，`behavior` 属性应为 `domain` 字项。**

### 示例代码

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

## 类型 Ⅱ - 仅程序名

 **如果您需要使用 `anonymityservice_processnameonly.yaml` 文件，您可以通过如下超链接进行获取：**

- 原始链接：[查看或下载](https://raw.githubusercontent.com/Paloexiz/blacklist-rules/main/artifact/individual/security/clash/anonymityservice_processnameonly.yaml)
- 镜像链接（可能会有24小时的延迟）：[查看或下载](https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/security/clash/anonymityservice_processnameonly.yaml)

### 注意事项

**为了能够正常调用 `anonymityservice_processnameonly.yaml` 文件，`behavior` 属性应为 `classical` 字项。**

### 示例代码

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
