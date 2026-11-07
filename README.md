# Tool for Games

[MIT](LICENSE) · v0.2.0

当游戏开发者提出工具需求时，让 agent 理解对方正在完成什么工作、需要凭什么作判断，再把这项工作做成容易操作、结果可信、后续内容也能接入的工具。

An agent skill for building game-production tools around the work people actually do and the decisions they need to make.

## Install / 安装

```bash
npx skills add Th-Hjj/tool-for-games
```

Add `-g` to install globally. / 加上 `-g` 可安装到用户级。

## 怎么用

使用上方命令安装，或手动将 `skills/tool-for-games` 复制到所用 agent 的 skills 目录，保留其中的 `SKILL.md`、`agents/` 和 `references/`。安装后直接描述工作和遇到的问题，也可以明确要求使用 `tool-for-games`。

例如：

- “每次测试 Boss 的第二阶段都要重新打四分钟，帮我把这个流程缩短。”
- “这个声音滑杆改了听不出来，帮我查清楚并修好。”
- “系统和美术都要批量改敌人。帮我们做个能看清影响范围、保留特例的编辑工具。”
- “本地化表导回游戏经常漏内容，帮我改进导入和检查流程。”

已有工程、样例资产、截图或一次实际操作的记录，都能帮助 agent 更快开始。无需先写完整需求文档。

## 它会怎样工作

先还原一次真实任务，读懂现有数据怎样被编辑、预览、保存和使用，再选择合适的改法。先跑通最容易出错、也最能证明工具有用的操作，最后用实际生产任务验收。小修直接处理，不要求走完整设计流程。

适用于关卡、系统、战斗、技术策划、美术、动画、特效、音频、叙事、程序、QA、本地化、制作管理和运营等工作。岗位名称帮助理解背景；实际任务决定工具需要什么。同一个人切换任务时，需要的输入、状态和保存范围也可能不同。

工具可以是现有编辑器里的一个按钮、调参面板、导入脚本、表格、命令或独立应用。它会比较复用、扩展和新建的成本，并保留人的创作判断。只要求改一条台词、一个数值或实现普通玩法时，直接完成对应工作。

## 内容

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](skills/tool-for-games/SKILL.md) | 自动调用描述、技术策划思路与按规模调整的工作流程 |
| [work-patterns.md](skills/tool-for-games/references/work-patterns.md) | 跨岗位任务、共用流程与差异化反馈 |
| [production-checks.md](skills/tool-for-games/references/production-checks.md) | 修改内容的工具、预览与保存、继承覆盖、批量导入、异步结果和验收 |
| [research.md](skills/tool-for-games/references/research.md) | 一手来源、适用边界，以及作者经验如何转成方法 |
| [integration-points.md](skills/tool-for-games/references/integration-points.md) | Unity、Unreal、Godot 与表格/命令行工具的界面、撤销、导入和校验接入点 |
| [evals](evals/README.md) | 维护者使用的场景与验证记录，不作为日常执行步骤 |

主文件使用英文指令，要求 agent 使用用户的语言和项目已有术语。工作方法不绑定引擎；具体实现需要相应工程、工具权限和运行环境。
