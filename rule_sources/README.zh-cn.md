# 规则源文件维护说明

**语言选择：[English](README.md) | 简体中文**

这里是手动维护规则条目的入口。需要改规则时，先改本目录里的 `*.rules`。推送后，GitHub Actions 会构建 Clash / Surge 产物并提交。

## 基本格式

```text
## ApplicationService
### google
cable.ua5v.com # Google Authenticator.
doodles.google # Currently blocked.
+.jotform.com # Form builder.

## Game
### pokemonmasters
! 3b8d4a717682c1cc5839b50bc93667cf.baas.nintendo.com # Disabled note.
```

## 写法约定

- `## <category>` 表示顶层分类，生成时会变成 `# /*<category>*/`。
- `### <group>` 表示分组，生成时会变成 `# <group>`。
- 普通行表示启用条目，支持域名、IP、`PROCESS-NAME,...`。
- `! <entry>` 表示禁用条目。
- 行尾 `# note` 是维护备注，只会输出到 Clash；Surge 只输出规则本体。
- `+.` 在 Clash 中原样保留，在 Surge 中会转换为 `.domain`。
- 不要直接手改生成产物；需要改规则就改这里的源文件。

## 本地校验

```powershell
python workflow_scripts/build_rules.py
python workflow_scripts/build_rules.py --check
```

这些命令不是日常流程的必需步骤。推送前想检查生成结果，或排查构建问题时再运行。
