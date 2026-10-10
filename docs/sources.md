# 信息源与发现路径

## 一手访谈和播客（A 板块）
| 用途 | 地址 | 说明 |
|---|---|---|
| 查近期单集 | `https://www.teahose.com/podcast/<节目名>` | 节目名用 URL 编码，例如 `The%20a16z%20Show`。页面上有发布日期和摘要。 |
| 读全文逐字稿 | `https://ceointerviews.ai/entity/<id>-<人名>-<公司>/` → `https://ceointerviews.ai/interview/<id>/` | 逐字稿带时间戳，最适合精读。 |
| 补充摘要 | `https://finance.biggo.com/podcast` | 只给相对日期（如“昨天”），需要交叉核实。 |
| 原始节目 | YouTube、Simplecast、节目官网 | 用于核实日期和时长。 |

**常查节目**：The a16z Show、Dwarkesh Podcast、Lex Fridman、No Priors、Latent Space、BG2、20VC、Sources、Lenny's Podcast、Big Technology、Hard Fork、Decoder、Cognitive Revolution、Stratechery、Acquired、All-In、Training Data、Invest Like the Best、A Bit Personal、Y Combinator。

**已验证可用的逐字稿示例**：
- Gelsinger × a16z（2026-10-09）：https://ceointerviews.ai/interview/3016166/
- Garman × a16z（2026-10-08）：https://ceointerviews.ai/interview/3009574/
- Fouquet × A Bit Personal（2026-10-08）：https://ceointerviews.ai/interview/3015177/

## 今日信号（B 板块）
- **官方博客与研究页**：Anthropic（/news、/research）、OpenAI（/index）、Google DeepMind、Meta、NVIDIA、DeepSeek、Qwen。
- **媒体**：Reuters、FT、The Verge、TechCrunch、The Information。其中 Reuters 在当前环境中可能被拦截，被拦截时注明“原文无法访问”。
- **日更汇总**：只用于发现线索，必须打开原文核实。
  - `https://aisdg.substack.com/p/ai-news-for-<month>-<day>-<year>`
  - `https://github.com/duanyytop/agents-radar/issues`（每日官方内容报告）
  - Latent Space AINews
  - `https://www.nocode.mba/ai-release-tracker/<yyyy>/<mm>`（模型发布追踪）

## 踩过的坑
- 把 9 月 10 日发布的 DeepSeek V4.1 Flash 当成当天新闻，被读者指出。以后每条都要核实事件本身的日期。
- OpenAI 的 run rate 先按流传的 700 亿美元写了，后经 FT 更正为约 500 亿（毛额与净额口径不同）。凡是营收数字，都要核实口径。
- Teahose 摘要里的时间戳有误差，时间戳一律以 ceointerviews 的逐字稿为准。
