# Third-party notices

**Select your Language: English | [简体中文](NOTICE.zh-cn.md)**

This directory contains conversions and native Surge mirrors from the fixed upstream inventory in `workflow_scripts/sync_third_party_rules.py`. Rules retain their upstream copyright and license terms; the repository's own license does not replace those terms.

| Source repository                                                      | Upstream terms                                                           | Local copy                                                                                      |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| [MetaCubeX/meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat) | GNU GPL version 3; upstream also acknowledges its data contributors      | [LICENSE](licenses/MetaCubeX/LICENSE)                                                            |
| [peiyingyao/Rule-for-OCD](https://github.com/peiyingyao/Rule-for-OCD)   | GNU GPL version 2                                                        | [LICENSE](licenses/Rule-for-OCD/LICENSE)                                                         |
| [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | GNU GPL version 2 | [LICENSE](licenses/blackmatrix7-LICENSE) |
| [Loyalsoldier/clash-rules](https://github.com/Loyalsoldier/clash-rules) | GNU GPL version 3                                                        | [LICENSE](licenses/Loyalsoldier/LICENSE)                                                         |
| [Cats-Team/AdRules](https://github.com/Cats-Team/AdRules)               | Generated rules retain the licenses of their respective upstream authors | [Script LICENSE](licenses/AdRules/SCRIPT-LICENSE) |

AdRules' [0BSD script license](licenses/AdRules/SCRIPT-LICENSE) covers its `script` branch, not a blanket relicensing of the aggregated rule data. Its [upstream source list](https://github.com/Cats-Team/AdRules/blob/script/Source.md) records multiple licenses and entries marked unknown, and warns that some information may be outdated. No license is assigned here to those entries.

[sources.json](sources.json) records each provider's exact source URL, source SHA-256, output paths and corresponding notices. Only upstream license files are stored locally as fixed copies; the daily workflow does not download, update or commit them. Any license change requires manual review. Domain/IP/Process sources generate three readable formats; native Surge sources retain their complete upstream text and comments in the Surge mirror.
