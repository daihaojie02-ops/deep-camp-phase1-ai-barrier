# DEEP007 戴昊杰 — 数字身份卡项目记忆

## 项目名称

**第三自习室数字身份卡**（Digital Identity Card for Study Room 3）

## 项目概述

为 DEEP 营入营准备制作个人数字身份卡，包含第三自习室标识、DEEP 编号、个人 ID 等信息。最终方案以深黑基调 + 蜜桃暖色为主视觉，融合 Apple 极简美学与气势感：戏剧化光束、六角徽章、动感强度条、定制蜜桃 Logo SVG。

## 使用工具

| 工具 | 用途 |
|------|------|
| **Claude Code** | 主控 Agent：需求理解 → 设计方案迭代 → 代码生成 → 截图输出 |
| **Puppeteer MCP** | 浏览器自动化：渲染 HTML 身份卡、html2canvas 截取卡片元素 |
| **html2canvas** | 前端截图库：将卡片 DOM 渲染为 Canvas 并导出 PNG |
| **HTML/CSS/SVG** | 身份卡前端实现：磨砂玻璃、CSS 动效、蜜桃矢量 Logo |
| **Node.js** | Base64 解码并写入 PNG 文件 |

## 模型配置

| 配置项 | 值 |
|--------|-----|
| **模型** | Deepseek-v4-pro |
| **API 端点** | `https://api.deepseek.com/anthropic` |
| **权限模式** | `bypassPermissions` |
| **终端** | Git Bash on Windows 11 |
| **主题** | Dark |
| **已启用 MCP** | Puppeteer (browser automation) |

## 制作过程

### 1. 需求理解
- 任务要求：身份卡需包含"第三自习室"、"个人 ID"、"DEEP 编号"
- 用户信息：DEEP007 / 戴昊杰 / 第三自习室 / 入营日期 2026.06.13
- 风格偏好：Apple 高级感 → 追加"气势" → 追加"桃子 Logo"

### 2. 设计迭代

**第一版**（粒子动画 + 金色调）：
- Canvas 粒子背景、动态连线、毛玻璃卡片、旋转渐变边框
- 偏科技/游戏感，用户反馈要 Apple 风

**第二版**（Apple 极简）：
- 磨砂玻璃 `backdrop-filter: blur(60px)`、SF 字体、金色点缀
- Sub Rosa 光晕 + 网点网格背景
- 用户反馈：不够有气势

**第三版 · 最终**（黑金气势 + 蜜桃 Logo）：
- 深黑底 + 戏剧化光束雕塑（金色 → 蜜桃暖色迁移）
- 六角 SVG 徽章（内置 III = 第三自习室）
- 蜜桃矢量 Logo：双瓣桃身 + 径向渐变 + 高光 + 绿叶 + 呼吸发光动画
- 动感强度条（5条渐变竖线，hover 时高度跳动）
- 探索者角标、MMXXVI 罗马数字年份
- 等宽字体 DEEP007 编号（`SF Mono`）

### 3. 身份卡信息

| 字段 | 值 |
|------|-----|
| 姓名 | 戴昊杰 |
| 英文名 | Haojie Dai |
| DEEP 编号 | DEEP007 |
| 个人 ID | DEEP007 |
| 所属自习室 | 第三自习室 |
| 入营日期 | 2026.06.13 |
| 身份标签 | 探索者 |

### 4. 截图输出流程

```
Puppeteer导航 → 加载html2canvas CDN → render Card DOM → 
Canvas.toDataURL() → 返回base64 → Node.js解码 → 写入PNG
```

**遇到的坑**：
- browser-act Chrome 浏览器 IPC 连接反复失败（returncode=21），换用 Puppeteer
- Puppeteer `encoded` 参数截图结果超出 token 限制（52KB base64），改用 html2canvas 方案
- Node.js 读取长行文件需正确 strip JSON 包裹字符

### 5. 技术亮点

- **纯 CSS 磨砂玻璃**：`backdrop-filter: blur(80px) saturate(200%)`，无 JS 依赖
- **蜜桃矢量 Logo**：纯 SVG（径向渐变 + 椭圆拼接 + 高光叠加），HTML 内联零请求
- **呼吸动画**：蜜桃徽章光晕 `@keyframes peach-breathe` 3s ease-in-out 循环
- **气势层次**：光束雕塑 → 磨砂卡片 → 金色分割线 → 信息列表 → 强度条

### 6. 输出文件

| 文件 | 格式 | 说明 |
|------|------|------|
| `DEEP007_戴昊杰_身份卡.html` | HTML | 交互式身份卡页面（4587 bytes） |
| `DEEP007_戴昊杰_身份卡.png` | PNG | html2canvas 渲染截图（62916 bytes, 460×640） |
| `DEEP007_戴昊杰_项目记忆.md` | Markdown | 本文档 |

---

*由 Claude Code + Deepseek-v4-pro 辅助生成 | 2026.06.13*
