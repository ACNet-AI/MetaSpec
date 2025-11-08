# Templates 目录结构差异分析

## ❌ 问题：文档与实现不一致

### 📄 文档建议的结构 (`spec-template.md.j2` Line 415-429)

**按 specification system source 组织**:

```
templates/
├── [library-spec-1]/       # 例如: generic/
│   ├── commands/           # Slash Commands from this specification system
│   │   └── [command-name].md
│   └── templates/          # Entity/workflow templates from this system
│       └── [template-name].yaml
├── [library-spec-2]/       # 例如: spec-kit/
│   ├── commands/
│   └── templates/
└── [custom]/               # 例如: mcp/ (from protocol)
    ├── commands/
    └── templates/
```

**设计理念**:
- ✅ 按来源分组（library vs custom）
- ✅ 清晰的命名空间隔离
- ✅ 体现规范组合性（Specification Composability）
- ✅ 易于理解来源和用途

**文档示例 (MCP-Speckit)**:
```
templates/
├── generic/               # From library/generic
│   ├── commands/
│   │   ├── init.md
│   │   └── validate.md
│   └── templates/
│       └── basic-spec.yaml
├── spec-kit/              # From library/sdd/spec-kit
│   ├── commands/
│   │   ├── plan.md
│   │   └── implement.md
│   └── templates/
│       └── toolkit-spec.yaml
└── mcp/                   # Custom (from protocol/001-mcp-protocol)
    ├── commands/
    │   ├── show-protocol.md
    │   ├── get-template.md
    │   └── validate-server.md
    └── templates/
        ├── basic-server.yaml
        ├── advanced-server.yaml
        └── tool-definition.yaml
```

---

### 💻 实际实现的结构 (`generator.py` Line 257-269)

**扁平化组织**:

```python
# Line 260: 模板文件直接在 templates/ 根目录
output_template = f"templates/{template_name}"

# Line 266: 命令文件在 templates/commands/ 统一目录
output_command = f"templates/commands/{command_name}"
```

**实际生成的结构**:
```
templates/
├── specify-template.md      # 直接在根目录，没有 source 分组
├── plan-template.md         # 直接在根目录
├── validate-template.md     # 直接在根目录
└── commands/                # 所有命令混在一起
    ├── specify.md           # 来自 generic/greenfield
    ├── plan.md              # 来自 spec-kit
    ├── proposal.md          # 来自 openspec
    └── validate.md          # 来自 generic/greenfield
```

**问题**:
- ❌ 无法区分来源（generic vs spec-kit vs custom）
- ❌ 命名冲突风险（不同 source 可能有同名命令）
- ❌ 与文档承诺的结构不符
- ❌ 不符合"按 specification system source 组织"的设计原则

---

## 📊 具体差异对比

| 方面 | 文档建议 | 实际实现 | 影响 |
|------|---------|---------|------|
| **组织原则** | 按 source 分组 | 扁平化 | ❌ 不符合设计理念 |
| **目录结构** | `templates/{source}/commands/` | `templates/commands/` | ❌ 无法区分来源 |
| **模板位置** | `templates/{source}/templates/` | `templates/` | ❌ 混在根目录 |
| **命名冲突** | 隔离（不同 source 可同名） | 可能冲突 | ❌ 风险增加 |
| **可组合性** | 体现规范组合 | 无法体现 | ❌ 设计理念丢失 |
| **用户理解** | 清晰来源和职责 | 混乱不清 | ❌ 学习曲线增加 |

---

## 🔍 根本原因

### generator.py 中的简化逻辑

```python
# Line 248-269: 循环处理 slash_commands
for sc in meta_spec.slash_commands:
    source = f"library/{sc.source}"
    
    # 从 source 读取
    source_template = f"{source}/templates/{template_name}.j2"
    source_command = f"{source}/commands/{command_name}.j2"
    
    # 但输出时丢弃了 source 信息！
    output_template = f"templates/{template_name}"      # ❌ 扁平化
    output_command = f"templates/commands/{command_name}"  # ❌ 扁平化
```

**问题**: 输出路径没有保留 `source` 信息。

---

## ✅ 建议的修复方案

### 方案 1: 保留 source 层次结构（推荐）

**修改 generator.py**:

```python
for sc in meta_spec.slash_commands:
    source = f"library/{sc.source}"
    
    # 保留 source 信息
    output_template = f"templates/{sc.source}/templates/{template_name}"
    output_command = f"templates/{sc.source}/commands/{command_name}"
```

**修复后的结构**:
```
templates/
├── generic/
│   ├── commands/
│   │   ├── specify.md
│   │   └── validate.md
│   └── templates/
│       ├── specify-template.md
│       └── validate-template.md
├── spec-kit/
│   ├── commands/
│   │   ├── plan.md
│   │   └── implement.md
│   └── templates/
│       ├── plan-template.md
│       └── implement-template.md
└── custom/                # 如果有 protocol-derived commands
    ├── commands/
    │   └── show-protocol.md
    └── templates/
        └── server-template.yaml
```

**优点**:
- ✅ 符合文档设计
- ✅ 清晰的命名空间
- ✅ 体现规范组合性
- ✅ 避免命名冲突

**风险**:
- ⚠️ 破坏性变更（需要更新版本）
- ⚠️ 已有 speckit 的迁移

---

### 方案 2: 更新文档以匹配实现

**修改 spec-template.md.j2**:

将推荐结构改为：
```
templates/
├── {command1}-template.md     # 模板文件
├── {command2}-template.md
└── commands/                  # 所有 Slash Commands
    ├── {command1}.md
    └── {command2}.md
```

**优点**:
- ✅ 简单快速
- ✅ 不破坏现有代码

**缺点**:
- ❌ 放弃设计理念
- ❌ 无法体现规范组合性
- ❌ 可能有命名冲突

---

## 🎯 推荐决策

### 建议：采用方案 1（保留 source 层次结构）

**理由**:
1. **设计一致性**: 文档描述的"按 specification system source 组织"是核心设计理念
2. **可扩展性**: 支持多个 library 的组合使用
3. **清晰性**: 用户可以清楚地看到每个命令来自哪个 specification system
4. **避免冲突**: 不同 source 可以有同名命令而不冲突

**实施步骤**:
1. ✅ 修改 `generator.py` (Line 260, 266)
2. ✅ 更新测试用例
3. ✅ 添加版本升级指南
4. ✅ 更新 CHANGELOG (MAJOR version bump: 0.3.0 → 1.0.0)

---

## 📝 相关文件

- `src/metaspec/generator.py` (Line 257-269) - 实现代码
- `src/metaspec/templates/meta/templates/spec-template.md.j2` (Line 409-455) - 文档规范
- `src/metaspec/templates/meta/sdd/commands/specify.md.j2` (Line 1468-1494) - 开发指南

---

## ⏰ 发现时间

2025-11-08 (Version 0.3.0 发布后)

---

## 🚨 影响评估

**当前状态**:
- ✅ 功能正常工作（能生成 speckit）
- ❌ 结构与文档不符
- ❌ 可能导致用户困惑
- ❌ 无法体现核心设计理念

**修复优先级**: **P0 (Critical)**

**原因**: 这是核心架构设计问题，影响框架的可理解性和可扩展性。

