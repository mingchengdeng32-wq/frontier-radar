# 前沿雷达 · Frontier Radar

一份由 AI agent 每天自动生成的 AI 前沿日报。读者是企业高管、投资人和技术负责人。

每期固定三块：
- **A 一手精读**：把顶级人物的访谈、播客逐字稿通读一遍，整理成十个带时间戳的要点，附观察、深挖和启发。
- **B 今日信号**：当天的重要事件，每条附深挖。
- **C 论断追踪**：权威人物的预测和承诺，到期后回头复查。

最新一期：`issues/2026-10-10-issue-006.html`（第 6 期：基辛格、AWS Garman、ASML Fouquet 三篇精读，加五条信号）。

## 仓库结构
```
prompts/daily-task.md        定时任务的完整指令（与线上任务同步）
skills/frontier-radar/       可在任意 Claude 环境中复用的 skill
docs/writing-standard.md     写作标准，以 Muse 精读为样板，含读者反馈形成的规则
docs/sources.md              信息源、发现路径、踩过的坑
docs/design-system.md        版式组件与禁用样式
issues/                      往期 HTML 存档（最新一期即版式模板）
scripts/check_page.py        发布前检查：截图、移动端横向溢出
config/radar.json            线上资源 ID：页面链接、学习文档、定时任务
```

## 当前线上运行方式
- **定时任务**：每天北京时间 09:30 运行，指令见 `prompts/daily-task.md`。
- **页面**：每期发布到同一个固定链接（`config/radar.json` 中的 `html_artifact_url`）。
- **归档**：写入 Claude Docs「前沿雷达 · 每日学习」，包括每期一个子页和论断追踪表。

## 换电脑或换环境后复用
1. 克隆仓库：`git clone <本仓库地址> && cd frontier-radar`
2. **在 Claude 里使用**：把 `skills/frontier-radar/` 作为 skill 添加，然后说“出今天的前沿雷达”。
3. **重建定时任务**：新建一个定时任务（`CRON_TZ=Asia/Shanghai 30 9 * * *`），把 `prompts/daily-task.md` 的全文作为指令。
4. **线上资源归属**：页面链接、学习文档和定时任务都属于原 Claude 账号。
   - 同一账号下换电脑：无需任何改动。
   - 换了账号：首次运行会生成新的页面和文档，生成后把新 ID 写回 `config/radar.json`，并替换 `prompts/daily-task.md` 中对应的链接和 ID。
5. **本地检查依赖**：`pip install playwright && playwright install chromium`

## 维护约定
- 每次调整写法或版式时，同步更新 `docs/` 和 `prompts/daily-task.md`，并在线上任务中粘贴同样的内容。
- 每期发布后，把 HTML 存到 `issues/`，它同时作为下一期的版式模板。
