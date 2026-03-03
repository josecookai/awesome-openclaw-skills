#!/usr/bin/env python3
"""
Jina AI 网页阅读器工具
使用 r.jina.ai 服务获取任意网页正文
支持 Twitter/X、新闻网站、博客等
"""

import requests
import sys
import json
import argparse

def fetch_with_jina(url):
    """
    使用 Jina AI 阅读器获取网页内容
    
    Args:
        url: 目标网页 URL
    
    Returns:
        dict: 包含标题、内容、元数据的字典
    """
    jina_url = f"https://r.jina.ai/http://{url.replace('https://', '').replace('http://', '')}"
    
    try:
        response = requests.get(jina_url, timeout=30)
        response.raise_for_status()
        
        content = response.text
        
        # 解析 Jina AI 返回的格式
        lines = content.split('\n')
        result = {
            'title': '',
            'url': url,
            'published_time': '',
            'markdown_content': '',
            'raw_content': content
        }
        
        in_markdown = False
        markdown_lines = []
        
        for line in lines:
            if line.startswith('Title:'):
                result['title'] = line.replace('Title:', '').strip()
            elif line.startswith('URL Source:'):
                result['url'] = line.replace('URL Source:', '').strip()
            elif line.startswith('Published Time:'):
                result['published_time'] = line.replace('Published Time:', '').strip()
            elif line.startswith('Markdown Content:'):
                in_markdown = True
            elif in_markdown:
                markdown_lines.append(line)
        
        result['markdown_content'] = '\n'.join(markdown_lines).strip()
        
        return result
        
    except requests.RequestException as e:
        return {'error': str(e), 'url': url}


def fetch_tweet(tweet_url):
    """专门获取 Twitter/X 推文"""
    result = fetch_with_jina(tweet_url)
    
    if 'error' in result:
        return result
    
    # Twitter 特殊处理
    content = result.get('markdown_content', '')
    
    # 提取推文文本（通常在标题后面）
    lines = content.split('\n')
    tweet_text = []
    capture = False
    
    for line in lines:
        if capture and line.strip():
            tweet_text.append(line)
        if 'x.com' in line or 'twitter.com' in line:
            capture = True
    
    result['tweet_text'] = '\n'.join(tweet_text[:20])  # 限制长度
    return result


def main():
    parser = argparse.ArgumentParser(description='使用 Jina AI 获取网页内容')
    parser.add_argument('url', help='目标网页 URL')
    parser.add_argument('--tweet', '-t', action='store_true', help='Twitter/X 推文模式')
    parser.add_argument('--json', '-j', action='store_true', help='JSON 格式输出')
    parser.add_argument('--save', '-s', help='保存到文件')
    
    args = parser.parse_args()
    
    print(f"🔍 获取: {args.url}")
    print("-" * 50)
    
    if args.tweet or 'x.com' in args.url or 'twitter.com' in args.url:
        result = fetch_tweet(args.url)
    else:
        result = fetch_with_jina(args.url)
    
    if 'error' in result:
        print(f"❌ 错误: {result['error']}")
        sys.exit(1)
    
    # 输出
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"📰 标题: {result.get('title', 'N/A')}")
        print(f"🔗 URL: {result.get('url', 'N/A')}")
        if result.get('published_time'):
            print(f"🕐 发布时间: {result['published_time']}")
        print("-" * 50)
        print("📝 内容:")
        print(result.get('markdown_content', result.get('tweet_text', 'N/A'))[:2000])
        if len(result.get('markdown_content', '')) > 2000:
            print("\n... (内容已截断)")
    
    # 保存到文件
    if args.save:
        with open(args.save, 'w', encoding='utf-8') as f:
            if args.json:
                json.dump(result, f, ensure_ascii=False, indent=2)
            else:
                f.write(f"Title: {result.get('title', 'N/A')}\n")
                f.write(f"URL: {result.get('url', 'N/A')}\n")
                f.write(f"Time: {result.get('published_time', 'N/A')}\n")
                f.write("-" * 50 + "\n")
                f.write(result.get('markdown_content', 'N/A'))
        print(f"\n💾 已保存到: {args.save}")


if __name__ == "__main__":
    main()
