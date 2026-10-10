# 版式规范

完整模板见 `template/radar-template.html`。每期只替换内容，不改 CSS 和结构。

## 视觉基调
- 深海军蓝渐变封面，橙色重点，白纸正文，阅读栏最大宽度 820px。
- 字体：Noto Sans SC，回退依次为 PingFang SC、Microsoft YaHei。
- 颜色 token 定义在 `:root`。深色模式写两处：一处是 `@media (prefers-color-scheme: dark)` 配合 `:root:not([data-theme="light"])`，另一处是 `:root[data-theme="dark"]`。

## 组件（class）
| class | 用途 |
|---|---|
| `.cover` `.badge` `h1` `.sub` `blockquote` `.meta` | 封面：徽章「前沿雷达 · 第 N 期 · 日期」、标题、副标题、两句原话、节目元信息 |
| `.tldr` | 深色「一句话总结」框 |
| `.thread` | 今日主线（橙色左边线），标「本刊推断」 |
| `.toc` | 目录卡片，链接到各板块 id |
| `.part` `.tag` `.t` | 板块分隔：A1/A2/A3（id 为 a、a2、a3）、B（b）、C（c） |
| `.sec h2 .n` | 编号小标题，编号可写 01–10、S1、深挖、启发、快讯 |
| `.ts` | 时间戳胶囊（灰） |
| `.dt` | 日期胶囊（橙色描边），用于信号和快讯 |
| `.q` | 原话引语框（蓝色左边线） |
| `.note .k` | 「雷达观察」框（橙底、橙色左边线） |
| `.tbl table` | 表格 |
| `dl.dig .r dt dd .inf` | 深挖五步网格；`.inf` 是「推断」小标签；`.r.no` 用于反方行（灰字） |
| `ol.take` | 启发列表 |
| `ul.flash` | 快讯列表 |
| `.st.new` `.st.due` | 论断状态标签：「今日录入」「即将到期」 |
| `.watch` | 「接下来盯」 |
| `.src` `.foot` | 来源列表、页脚 |

## 禁用
不要再加「他说 / 解读」小标签、「信号 / 趋势」双栏卡、`.theses` 大判断色块、`.verdict` 判断条。这些样式读者已经否决过。

## 发布前检查
运行 `python3 scripts/check_page.py <html>`，会做两件事：
- 截取桌面版首屏；
- 检查 390px 宽度下有没有横向滚动。
