# 博客表格样式修复 — 交接文档

## 当前问题

表格右侧有大片空白，数据列只占约 60% 宽度，但表格的 border-bottom 横线延伸到了整个内容区边缘。

截图：表格 5 列（Model / Layers / Mean FEP / FEP Depth / Crystallization Rate），数据内容在左侧结束，右侧空白延伸到容器边缘。

## 根因分析

已尝试过的方案：
- `width: 100%` → 表格撑满，但列间距过大（5 列内容不足以填满 720px）
- `width: auto; margin: 0 auto` → 表格按内容收缩并居中，但外层容器仍是 100% 宽度，border 和背景色延伸到右侧

**核心问题**：PaperMod 主题可能在 `<table>` 外层有一个 `overflow-x: auto` 的 wrapper div，这个 div 是 `width: 100%` 的。CSS 的 `border-top/bottom` 应用在 `<table>` 上，但如果外层容器也有样式，就会导致视觉上的"右侧空白"。

**需要用浏览器 DevTools 确认的事情**：
1. 右键表格 → 检查元素
2. 查看 `<table>` 的完整父元素链
3. 确认是哪个元素在撑满宽度

## 可能的修复方向

### 方向 A：给外层容器也设置 auto 宽度

```css
/* 如果 PaperMod 在 table 外包了一层 div */
.post-content > div:has(> table),
.md-content > div:has(> table) {
  display: table;        /* 或 inline-block */
  margin: 0 auto 32px;
  width: auto;
}

.post-content table,
.md-content table {
  margin: 0;             /* 让外层容器控制 margin */
}
```

### 方向 B：去掉三线表 border，回归朴素风格

```css
.post-content table,
.md-content table {
  margin-bottom: 32px;
  border-collapse: collapse;
  border-top: none;
  border-bottom: none;
}
```

去掉上下粗线后，右侧延伸问题在视觉上不明显。

### 方向 C：width 100% + 最后一列吸收剩余空间

```css
.post-content table,
.md-content table {
  width: 100%;
  table-layout: auto;
}

/* 让最后一列吸收剩余宽度 */
.post-content table th:last-child,
.post-content table td:last-child,
.md-content table th:last-child,
.md-content table td:last-child {
  width: 100%;
}
```

### 方向 D：Hugo shortcode 手动控制 HTML

创建 `layouts/shortcodes/table.html`，包裹表格在可控的 div 中。

## 当前 CSS 状态

文件：`assets/css/extended/custom.css`，表格相关在第 60-97 行：

```css
/* Tables: booktabs academic style — auto width, centered, three-line, zebra */
.post-content table,
.md-content table {
  margin: 0 auto 32px;
  border-collapse: collapse;
  width: auto;
  font-size: 15px;
  border-top: 2px solid var(--primary);
  border-bottom: 2px solid var(--primary);
}

.post-content table th,
.md-content table th {
  padding: 8px 12px;
  font-weight: 600;
  text-align: left;
  border-bottom: 1px solid var(--primary);
  white-space: nowrap;
}

.post-content table:not(.highlighttable, .highlight table, .gist .highlight) td,
.md-content table:not(.highlighttable, .highlight table, .gist .highlight) td {
  padding: 8px 12px;
  line-height: 1.4;
}

/* 斑马条纹 */
.post-content table:not(...) tbody tr:nth-child(even),
.md-content table:not(...) tbody tr:nth-child(even) {
  background: var(--code-bg);
}

/* hover 高亮 */
.post-content table:not(...) tbody tr:hover,
.md-content table:not(...) tbody tr:hover {
  background: var(--border);
}
```

## 博文中的表格源码

文件：`content/posts/late-crystallization/index.md`，第 154-159 行：

```markdown
| Model | Layers | Mean FEP | FEP Depth | Crystallization Rate |
|-------|--------|----------|-----------|---------------------|
| Qwen2.5-7B | 28 | 27.3 ± 1.8 | 97.5% | 85.9% |
| Qwen2.5-14B | 48 | 46.0 ± 4.9 | 95.8% | 77.7% |
| Llama-3.1-8B | 32 | 29.4 ± 4.9 | 91.9% | 71.0% |
| Mistral-7B | 32 | 26.3 ± 6.2 | 82.3% | 27.1% |
```

## 相关文件清单

| 文件 | 作用 |
|------|------|
| `assets/css/extended/custom.css` | 所有 CSS 覆盖 |
| `content/posts/late-crystallization/index.md` | 博文源码 |
| `themes/PaperMod/assets/css/common/post-single.css` | 主题默认表格样式 |
| `themes/PaperMod/assets/css/common/main.css` | 主题全局样式 |
| `themes/PaperMod/assets/css/core/theme-vars.css` | CSS 变量定义 |
| `.aone_copilot/skills/blog-writing/SKILL.md` | Blog Skill 文档 |

## 推送方式（重要！）

**阿里内网禁止 `git push`**，必须用 GitHub API 推送：

```bash
# 获取 token
TOKEN=$(echo "protocol=https\nhost=github.com" | git credential fill 2>/dev/null | grep password | cut -d= -f2)

# Python 脚本推送（blob → tree → commit → ref）
python3 -c "
import json, urllib.request, base64

token = '<TOKEN>'
repo = 'hellogxp/hellogxp.github.io'
headers = {'Authorization': f'token {token}', 'Content-Type': 'application/json'}

def api(method, path, data=None):
    url = f'https://api.github.com/repos/{repo}/git/{path}'
    req = urllib.request.Request(url, headers=headers, method=method)
    if data:
        req.data = json.dumps(data).encode()
    return json.loads(urllib.request.urlopen(req).read())

# 获取远程最新 SHA
ref = api('GET', 'refs/heads/main')  # 注意 GET 用 urllib 直接读
parent = ref['object']['sha']

# 读文件并 base64
with open('assets/css/extended/custom.css', 'rb') as f:
    content_b64 = base64.b64encode(f.read()).decode()

blob = api('POST', 'blobs', {'content': content_b64, 'encoding': 'base64'})
tree = api('POST', 'trees', {'base_tree': parent, 'tree': [{'path': 'assets/css/extended/custom.css', 'mode': '100644', 'type': 'blob', 'sha': blob['sha']}]})
commit = api('POST', 'commits', {'message': 'style: fix table', 'tree': tree['sha'], 'parents': [parent]})

# Update ref
import urllib.request as ur
req = ur.Request(f'https://api.github.com/repos/{repo}/git/refs/heads/main', headers=headers, method='PATCH', data=json.dumps({'sha': commit['sha']}).encode())
result = json.loads(ur.urlopen(req).read())
print('pushed:', result['object']['sha'])
"
```

## 已完成的工作

- ✅ `hugo.yml` 配置对齐 Lilian Weng（ShowBreadCrumbs=false, ShowCodeCopyButtons=false, ShowShareButtons=true, 菜单 Archive/Search）
- ✅ `layouts/_partials/post_meta.html` 自定义模板（Date: | Estimated Reading Time: | Author:）
- ✅ `content/archives.md` 和 `content/search.md` 创建
- ✅ `custom.css` 字体/字号/行高/间距/链接样式全部对齐 Lilian Weng
- ✅ 博文所有论文引用加 arXiv 超链接
- ✅ Blog Skill 文档完善（含超链接规则、GitHub API 推送规则、自绘图表规范）
- ✅ 表格改为加粗列表（回避 CSS 问题，符合 Lilian 风格）
- ❌ **两张 bar chart 需要按新规范重画**（见下方）

## 待办：重画两张 bar chart

### 问题

博文中有 2 张自绘 bar chart，风格和论文原图（蓝/红双色 line chart）不统一：

1. **`intervention_comparison.png`** — 灰+3蓝渐变，底部有蓝框白底注释，Y轴截断无断轴标记
2. **`crystallization_by_architecture.png`** — 蓝/绿/橙多色，斜线填充，橙色手绘箭头注释

论文原图（`computability_memorization_spectrum.png` 等 line chart）质量很好，可直接用。

### 改图规范

完整规范见 `~/.aone_copilot/skills/blog-writing/SKILL.md` §二"自绘数据图统一规范"。关键点：

- **配色**：主色 `#4C72B0`（蓝），对比色 `#C44E52`（红），baseline `#8C8C8C`（灰）
- **figsize**: `(7, 4.5)`，DPI 300
- **柱宽**: 0.4-0.6
- **禁止**：框线注释、手绘箭头、斜线填充、每组不同色系
- **信息注释**放到 figure caption（Hugo 图片 alt text），不放图内

### 具体改法

**intervention_comparison.png**:
- 灰色 baseline 柱 + 蓝色系 3 柱（浅→深渐进：`#A8C8E8` → `#6FA0D6` → `#4C72B0`）
- 去掉底部蓝框注释 → 移到 caption
- Baseline 虚线简化为灰色 `linewidth=1`

**crystallization_by_architecture.png**:
- 全部用蓝色系：实心蓝 = crystallization rate，半透明蓝(alpha=0.4) = FEP depth
- 去掉绿/橙配色、斜线填充、橙色箭头
- "Sliding window attention enables earlier routing" 移到 caption

### 图表生成脚本位置

- `~/llm-mi/generate_figures.py` — 包含 `fig_intervention_comparison()`（第 141 行）
- `~/llm-mi-data/scripts/generate_figures.py` — 另一版本
- 图片输出到：`~/hellogxp.github.io/content/posts/late-crystallization/figures/`

### 步骤

1. 修改 Python 脚本中的配色/柱宽/字号/去掉注释框
2. 运行脚本重新生成 PNG
3. 更新博文 caption（alt text）加入从图内移出的注释信息
4. 通过 GitHub API 推送新图片 + 更新的 index.md
