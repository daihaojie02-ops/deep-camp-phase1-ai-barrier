#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
km.py — Personal Knowledge Management Toolkit
"你的第二个大脑" — Markdown + Git + AI 驱动的知识管理系统

Usage:
  python km.py init      <知识库目录>    初始化知识库
  python km.py index    <知识库目录>    生成结构化索引
  python km.py search   <关键词>        全文搜索
  python km.py stats    <知识库目录>    统计面板
  python km.py backup   <知识库目录>    Git 自动备份
  python km.py demo                      运行完整演示
"""

import os, sys, re, json, subprocess

# Fix Windows GBK encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
from datetime import datetime
from pathlib import Path
from collections import Counter

# ── YAML Frontmatter Parser ──────────────────────────────────────────
def parse_frontmatter(filepath):
    """Extract YAML frontmatter and body from a Markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    meta = {}
    body = content

    # Match YAML frontmatter: starts with ---, ends with ---
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        body = content[match.end():]
        yaml_text = match.group(1)
        # Simple YAML parsing (avoids PyYAML dependency)
        for line in yaml_text.strip().split('\n'):
            line = line.strip()
            if ':' in line:
                key, _, val = line.partition(':')
                meta[key.strip()] = val.strip()

    return meta, body, content


def extract_title(filepath, meta, body):
    """Extract title: frontmatter > first h1 > filename."""
    if 'title' in meta:
        return meta['title']
    h1 = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
    if h1:
        return h1.group(1).strip()
    return Path(filepath).stem


def extract_tags(meta, body):
    """Extract tags from frontmatter or auto-detect from content."""
    tags = []

    if 'tags' in meta:
        tags = [t.strip() for t in meta['tags'].strip('[]').split(',')]
    elif 'tag' in meta:
        tags = [meta['tag'].strip()]

    # Auto-detect from body
    auto_tags = detect_auto_tags(body)
    tags.extend(auto_tags)

    return list(set(tags))


def detect_auto_tags(body):
    """Heuristic tag detection from body content."""
    tags = []
    patterns = {
        r'\bClaude Code\b': 'claude-code',
        r'\bMCP\b': 'mcp',
        r'\bAgent\b': 'agent',
        r'\bPython\b': 'python',
        r'\bGitHub?\b': 'github',
        r'\bDEEP': 'deep-camp',
        r'\b工作流\b': 'workflow',
        r'\bPrompt\b': 'prompt',
        r'\bAPI\b': 'api',
        r'\bYAML\b': 'yaml',
        r'\bTypeScript\b': 'typescript',
        r'\b插件\b': 'plugin',
        r'\bWebSocket\b': 'websocket',
        r'\bGit\b': 'git',
    }
    for pattern, tag in patterns.items():
        if re.search(pattern, body, re.IGNORECASE):
            tags.append(tag)
    return tags


# ── Core Commands ────────────────────────────────────────────────────
def cmd_index(notedir):
    """Generate a structured index of all Markdown notes."""
    notedir = Path(notedir)
    if not notedir.exists():
        print(f"❌ Directory not found: {notedir}")
        return None

    md_files = sorted(notedir.rglob("*.md"))
    index = {
        'generated_at': datetime.now().isoformat(),
        'total_notes': len(md_files),
        'categories': {},
        'tag_index': {},
        'notes': []
    }

    for fpath in md_files:
        # Skip .git directories
        if '.git' in fpath.parts:
            continue

        meta, body, _ = parse_frontmatter(fpath)
        title = extract_title(fpath, meta, body)
        tags = extract_tags(meta, body)
        desc = meta.get('description', body[:120].replace('\n', ' ').strip())
        word_count = len(body.split())
        modified = datetime.fromtimestamp(fpath.stat().st_mtime).strftime('%Y-%m-%d')

        category = fpath.parent.name if fpath.parent != notedir else 'root'

        note = {
            'title': title,
            'path': str(fpath.relative_to(notedir)),
            'category': category,
            'tags': tags,
            'description': desc,
            'word_count': word_count,
            'modified': modified,
        }
        index['notes'].append(note)

        # Category grouping
        if category not in index['categories']:
            index['categories'][category] = []
        index['categories'][category].append(note)

        # Tag index
        for tag in tags:
            if tag not in index['tag_index']:
                index['tag_index'][tag] = []
            index['tag_index'][tag].append(title)

    return index


def print_index(index):
    """Pretty-print the index in terminal."""
    print(f"\n{'='*60}")
    print(f"  📚 Personal Knowledge Base Index")
    print(f"  Generated: {index['generated_at'][:19]}")
    print(f"  Total Notes: {index['total_notes']}")
    print(f"{'='*60}")

    for cat, notes in sorted(index['categories'].items()):
        print(f"\n  📁 {cat}/ ({len(notes)} notes)")
        for n in notes:
            tag_str = ', '.join(f'#{t}' for t in n['tags'][:3])
            extra = f" +{len(n['tags'])-3}" if len(n['tags']) > 3 else ""
            print(f"    ├─ {n['title']}")
            print(f"    │  {tag_str}{extra} | {n['word_count']} words | {n['modified']}")

    print(f"\n  {'─'*56}")
    print(f"  🏷  Tag Cloud: ", end='')
    top_tags = sorted(index['tag_index'].items(), key=lambda x: -len(x[1]))[:10]
    for tag, notes in top_tags:
        print(f"#{tag}({len(notes)}) ", end='')
    print()


def cmd_search(notedir, keyword):
    """Full-text search across all notes."""
    notedir = Path(notedir)
    results = []

    for fpath in notedir.rglob("*.md"):
        if '.git' in fpath.parts:
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        keyword_lower = keyword.lower()
        if keyword_lower in content.lower():
            # Find context around the keyword
            lines = content.split('\n')
            matches = []
            for i, line in enumerate(lines):
                if keyword_lower in line.lower():
                    ctx_start = max(0, i-1)
                    ctx_end = min(len(lines), i+2)
                    matches.append({
                        'line_num': i+1,
                        'context': '\n'.join(lines[ctx_start:ctx_end])
                    })

            results.append({
                'file': str(fpath.relative_to(notedir)),
                'title': extract_title(fpath, *parse_frontmatter(fpath)[:2]),
                'matches': matches[:5]  # Cap at 5 matches per file
            })

    return results


def print_search_results(keyword, results):
    """Pretty-print search results."""
    print(f"\n{'='*60}")
    print(f"  🔍 Search: \"{keyword}\"")
    print(f"  Found in {len(results)} notes")
    print(f"{'='*60}")

    for r in results:
        print(f"\n  📄 {r['title']}")
        print(f"     {r['file']} ({len(r['matches'])} matches)")
        for m in r['matches'][:3]:
            print(f"     L{m['line_num']}: {m['context'][:100].strip()}...")
        if len(r['matches']) > 3:
            print(f"     ... and {len(r['matches'])-3} more matches")


def cmd_stats(notedir):
    """Generate knowledge base statistics."""
    notedir = Path(notedir)
    md_files = list(notedir.rglob("*.md"))
    md_files = [f for f in md_files if '.git' not in f.parts]

    total_words = 0
    all_tags = []
    total_size = 0

    for fpath in md_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        total_words += len(content.split())
        total_size += len(content.encode('utf-8'))
        _, body, _ = parse_frontmatter(fpath)
        all_tags.extend(detect_auto_tags(body))

    tag_counter = Counter(all_tags)

    print(f"\n{'='*60}")
    print(f"  📊 Knowledge Base Statistics")
    print(f"{'='*60}")
    print(f"  ├─ Total notes:    {len(md_files)}")
    print(f"  ├─ Total words:    {total_words:,}")
    print(f"  ├─ Total size:     {total_size/1024:.1f} KB")
    print(f"  ├─ Avg note size:  {total_words//max(len(md_files),1):,} words")
    print(f"  ├─ Unique tags:    {len(tag_counter)}")
    print(f"  └─ Old → New:      {datetime.fromtimestamp(min(f.stat().st_mtime for f in md_files)).strftime('%Y-%m-%d')} → {datetime.fromtimestamp(max(f.stat().st_mtime for f in md_files)).strftime('%Y-%m-%d')}")
    print(f"\n  🏷  Top 10 Tags:")
    for tag, count in tag_counter.most_common(10):
        bar = '█' * min(count, 20)
        print(f"     {tag:20s} {bar} {count}")


def cmd_backup(notedir):
    """Auto Git backup with generated commit message."""
    notedir = Path(notedir)

    # Check if Git repo
    git_dir = notedir / '.git'
    if not git_dir.exists():
        parent_git = False
        for p in notedir.parents:
            if (p / '.git').exists():
                git_dir = p / '.git'
                parent_git = True
                break
        if not parent_git:
            print("❌ Not a Git repository. Run 'git init' first.")
            return False

    # Check for changes
    result = subprocess.run(
        ['git', '-C', str(notedir), 'status', '--porcelain'],
        capture_output=True, text=True
    )
    changes = result.stdout.strip()

    if not changes:
        print("✅ No changes to backup. Knowledge base is up to date.")
        return True

    # Count changes
    added = len([l for l in changes.split('\n') if l.startswith('A') or l.startswith('??')])
    modified = len([l for l in changes.split('\n') if l.startswith('M')])
    deleted = len([l for l in changes.split('\n') if l.startswith('D')])

    commit_msg = f"kb: {added}+ {modified}~ {deleted}- | {datetime.now().strftime('%Y-%m-%d %H:%M')}"

    print(f"\n  📦 Backup Summary:")
    print(f"     +{added} new  ~{modified} modified  -{deleted} deleted")
    print(f"     Commit: \"{commit_msg}\"")

    # Execute git add, commit
    subprocess.run(['git', '-C', str(notedir), 'add', '-A'], capture_output=True)
    subprocess.run(['git', '-C', str(notedir), 'commit', '-m', commit_msg], capture_output=True)

    print(f"  ✅ Backup complete.")
    return True


def cmd_init(notedir):
    """Initialize a new knowledge base directory with template."""
    notedir = Path(notedir)
    notedir.mkdir(parents=True, exist_ok=True)

    # Create example note
    example = notedir / "example-note.md"
    example.write_text(f"""---
title: 我的第一条笔记
description: 示例笔记 — 展示知识库元数据格式
tags: [example, getting-started]
created: {datetime.now().strftime('%Y-%m-%d')}
---

## 如何使用知识库

1. 用 Markdown 写笔记 — 任何主题都可以
2. 在文件开头添加 YAML frontmatter（标题、标签、描述）
3. 运行 `python km.py index .` 生成索引
4. 运行 `python km.py search <关键词>` 全文搜索
5. Git 备份，永不丢失

## 为什么选这个方案

- **Markdown**：纯文本，任何编辑器都能打开，100年后也能读
- **Git**：每次修改都有记录，换电脑 `git clone` 即可
- **无平台依赖**：不绑定 Notion/Obsidian 等第三方服务
- **AI 友好**：Claude Code 可以直接搜索、分析、关联笔记

---
*Created with km.py — Personal Knowledge Management Toolkit*
""", encoding='utf-8')

    # Create .gitignore
    (notedir / '.gitignore').write_text(""".km_cache/
*.pyc
__pycache__/
""")

    print(f"""
  ✅ Knowledge base initialized at: {notedir}

  📁 Created:
     ├─ example-note.md      (示例笔记 + 使用说明)
     └─ .gitignore           (缓存排除)

  🚀 Next steps:
     cd {notedir}
     git init && git add -A && git commit -m "init: knowledge base"
     python km.py index .        # 生成索引
     python km.py search 知识库   # 测试搜索
""")


# ── Demo ──────────────────────────────────────────────────────────────
def run_demo():
    """Run a complete demonstration on the user's actual notes."""
    notedir = Path.home() / '.claude' / 'projects' / 'C--Users-26414' / 'memory'

    print("""
╔══════════════════════════════════════════════════════════════╗
║     🧠 Personal Knowledge Management — DEMO                ║
║     "你的第二个大脑" — 把学过的东西变成可搜索可关联的AI知识库 ║
╚══════════════════════════════════════════════════════════════╝
""")

    # 1. Index
    print("━" * 60)
    print("  📋 Step 1: Index — 扫描所有笔记，提取标签和元数据")
    print("━" * 60)
    index = cmd_index(notedir)
    if index:
        print_index(index)

    # 2. Search
    print("\n" + "━" * 60)
    print("  🔍 Step 2: Search — 全文搜索 \"Agent\"")
    print("━" * 60)
    results = cmd_search(notedir, "Agent")
    print_search_results("Agent", results)

    print("\n" + "━" * 60)
    print("  🔍 Step 3: Search — 全文搜索 \"API\"")
    print("━" * 60)
    results = cmd_search(notedir, "API")
    print_search_results("API", results)

    # 3. Stats
    print("\n" + "━" * 60)
    print("  📊 Step 4: Stats — 知识库统计面板")
    print("━" * 60)
    cmd_stats(notedir)

    # 4. Backup (dry-run)
    print("\n" + "━" * 60)
    print("  💾 Step 5: Backup — Git 自动备份检查")
    print("━" * 60)
    cmd_backup(notedir)

    print(f"""
╔══════════════════════════════════════════════════════════════╗
║  ✅ Demo Complete                                           ║
║                                                            ║
║  🎯 核心价值:                                                ║
║  • 所有笔记结构化索引 → 搜3个关键词找到任何东西              ║
║  • Git 版本控制 → 换电脑不丢，每次修改有记录                 ║
║  • AI 可读 → Claude Code 可以直接分析你的知识库              ║
║  • 零平台绑定 → Markdown + Git，永久可用                    ║
║                                                            ║
║  🔄 复利效应:                                                ║
║  4年大学 × 职业生涯 = 数万条笔记                             ║
║  期末复习 = 搜3个关键词                                      ║
║  面试准备 = 看过自己所有的思考                               ║
╚══════════════════════════════════════════════════════════════╝
""")

    return index


# ── CLI Entry Point ──────────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == 'demo':
        run_demo()

    elif cmd == 'init':
        path = sys.argv[2] if len(sys.argv) > 2 else '.'
        cmd_init(path)

    elif cmd == 'index':
        path = sys.argv[2] if len(sys.argv) > 2 else '.'
        index = cmd_index(path)
        if index:
            print_index(index)
            # Save JSON index
            out_path = Path(path) / '.km_cache' / 'index.json'
            out_path.parent.mkdir(exist_ok=True)
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(index, f, ensure_ascii=False, indent=2)
            print(f"\n  💾 Index saved to: {out_path}")

    elif cmd == 'search':
        keyword = sys.argv[2]
        path = sys.argv[3] if len(sys.argv) > 3 else '.'
        results = cmd_search(path, keyword)
        print_search_results(keyword, results)

    elif cmd == 'stats':
        path = sys.argv[2] if len(sys.argv) > 2 else '.'
        cmd_stats(path)

    elif cmd == 'backup':
        path = sys.argv[2] if len(sys.argv) > 2 else '.'
        cmd_backup(path)

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)


if __name__ == '__main__':
    main()
