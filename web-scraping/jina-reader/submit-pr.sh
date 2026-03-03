#!/bin/bash
# JinaAI Reader Skill - PR 提交指南

echo "🚀 JinaAI Reader Skill - PR 提交步骤"
echo "======================================"
echo ""

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}步骤 1: Fork 仓库${NC}"
echo "------------------------------"
echo "1. 访问: https://github.com/josecookai/awesome-openclaw-skills"
echo "2. 点击右上角 'Fork' 按钮"
echo "3. 等待 Fork 完成"
echo ""

echo -e "${GREEN}步骤 2: 克隆你的 Fork${NC}"
echo "------------------------------"
echo "git clone https://github.com/<你的用户名>/awesome-openclaw-skills.git"
echo "cd awesome-openclaw-skills"
echo ""

echo -e "${GREEN}步骤 3: 创建目录结构${NC}"
echo "------------------------------"
echo "mkdir -p web-scraping/jina-reader"
echo ""

echo -e "${GREEN}步骤 4: 复制文件${NC}"
echo "------------------------------"
echo "cp ~/.openclaw/workspace/skills/jina-reader-for-openclaw/* web-scraping/jina-reader/"
echo ""

echo -e "${GREEN}步骤 5: 检查文件${NC}"
echo "------------------------------"
echo "ls -la web-scraping/jina-reader/"
echo ""
echo "应该包含:"
echo "  - jina-reader.py"
echo "  - SKILL.md"
echo "  - README.md"
echo "  - LICENSE"
echo ""

echo -e "${GREEN}步骤 6: 提交更改${NC}"
echo "------------------------------"
echo "git add web-scraping/jina-reader/"
echo 'git commit -m "Add skill: jina-reader - Web content extraction using Jina AI"
echo ""

echo -e "${GREEN}步骤 7: 推送到你的 Fork${NC}"
echo "------------------------------"
echo "git push origin main"
echo ""

echo -e "${GREEN}步骤 8: 创建 PR${NC}"
echo "------------------------------"
echo "1. 访问: https://github.com/<你的用户名>/awesome-openclaw-skills"
echo "2. 点击 'Contribute' → 'Open pull request'"
echo "3. 填写 PR 标题和描述:"
echo ""
echo "标题:"
echo "Add skill: jina-reader - Web content extraction using Jina AI"
echo ""
echo "描述:"
cat << 'PRDESC'
## Skill: Jina AI Reader

Extract clean, readable content from any webpage using Jina AI's free service.

### Features
- ✅ No API key required
- ✅ Clean Markdown output
- ✅ Twitter/X support
- ✅ Lightweight & fast

### Use Cases
- Reading articles without paywalls
- Extracting Twitter/X content
- Research and documentation
- Data collection

### Files Added
- `SKILL.md` - OpenClaw specification
- `README.md` - Documentation
- `jina-reader.py` - Main script
- `LICENSE` - MIT License

### Testing
- [x] Tested with various websites
- [x] Tested with Twitter/X URLs
- [x] Works in OpenClaw sessions

Author: @chainblackbox
PRDESC
echo ""

echo -e "${GREEN}一键复制命令:${NC}"
echo "------------------------------"
cat << 'COMMANDS'
# 1. Fork 仓库 (在浏览器中完成)
# https://github.com/josecookai/awesome-openclaw-skills

# 2. 克隆并设置
git clone https://github.com/<你的用户名>/awesome-openclaw-skills.git
cd awesome-openclaw-skills

# 3. 创建目录并复制文件
mkdir -p web-scraping/jina-reader
cp ~/.openclaw/workspace/skills/jina-reader-for-openclaw/* web-scraping/jina-reader/

# 4. 提交
git add web-scraping/jina-reader/
git commit -m "Add skill: jina-reader - Web content extraction using Jina AI"
git push origin main

# 5. 去 GitHub 创建 PR
COMMANDS

echo ""
echo "✅ 准备完成！按照上述步骤提交 PR。"
