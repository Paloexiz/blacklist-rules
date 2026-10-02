# 第三方许可说明

**语言选择：[English](NOTICE.md)  | 简体中文**

## 项目介绍

本目录收录 `client_conf/mihomo_override/mihomo_override.js` 中引用的第三方规则，并提供转换后的格式。规则沿用上游的版权与许可条款，仓库自身的许可证不替代第三方许可。

## 第三方许可

| 来源仓库                                                               | 上游许可说明                                                  | 本地原文                                                                             |
| ---------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [MetaCubeX/meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat) | GNU General Public License v3.0；上游另有数据贡献者的致谢说明 | [LICENSE](licenses/MetaCubeX/LICENSE)                                                 |
| [peiyingyao/Rule-for-OCD](https://github.com/peiyingyao/Rule-for-OCD)   | GNU General Public License v2.0                               | [LICENSE](licenses/Rule-for-OCD/LICENSE)                                              |
| [Loyalsoldier/clash-rules](https://github.com/Loyalsoldier/clash-rules) | GNU General Public License v3.0                               | [LICENSE](licenses/Loyalsoldier/LICENSE)                                              |
| [Cats-Team/AdRules](https://github.com/Cats-Team/AdRules)               | 生成规则沿用各原始作者的许可                                  | [脚本 LICENSE](licenses/AdRules/SCRIPT-LICENSE) |

AdRules 的 [0BSD 脚本许可](licenses/AdRules/SCRIPT-LICENSE) 适用于其 `script` 分支，不能作为全部聚合规则数据的许可。[上游来源清单](https://github.com/Cats-Team/AdRules/blob/script/Source.md) 包含多种许可及标记为未知的条目，并提示部分信息可能已经过时。本目录不为未明确许可的条目另行指定许可。

## 相关文档与链接

[sources.json](sources.json) 记录每项规则的原始来源链接、来源文件 SHA-256、产物路径及对应的许可说明。本地只保留上游许可文件的固定副本；每日 Workflow 不下载、更新或提交这些文件。许可变更需人工审核。原始来源链接指向生成三种可读格式所使用的文本。

**提示**：本页为中文说明，上游许可原文见 [licenses/](licenses/)。规则订阅链接及维护方式见 [README.zh-cn.md](README.zh-cn.md)。
