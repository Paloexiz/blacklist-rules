# Rule Source Maintenance Guide

**Select your Language: English | [简体中文](README.zh-cn.md)**

This directory is where manual rule edits happen. Change the `*.rules` files here first. After you push those changes, GitHub Actions builds the Clash / Surge outputs and commits them.

## Basic Format

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

## Conventions

- `## <category>` defines a top-level category and is generated as `# /*<category>*/`.
- `### <group>` defines a group and is generated as `# <group>`.
- A normal line is an enabled entry. Domains, IP entries, and `PROCESS-NAME,...` are supported.
- `! <entry>` marks a disabled entry.
- A trailing `# note` is a maintenance note. It is only emitted to Clash outputs; Surge outputs only include the rule body.
- `+.` is kept as-is in Clash outputs and converted to `.domain` in Surge outputs.
- Do not edit generated outputs directly. Edit the source files here instead.

## Local Verification

```powershell
python workflow_scripts/build_rules.py
python workflow_scripts/build_rules.py --check
```

These commands are optional. Use them when you want to check the generated files before pushing or debug a build problem.
