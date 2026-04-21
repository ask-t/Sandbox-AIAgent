---
name: tech-blog-digest
description: 主要AIラボの公式ブログ新着記事を収集し、HTML形式のメールで送信する。
---

# Tech Blog Digest

## Step 1

Check the following official AI company blogs for new articles published in the last 24 hours:

- **Anthropic**: https://www.anthropic.com/news
- **OpenAI**: https://openai.com/news
- **Google DeepMind**: https://deepmind.google/discover/blog/
- **Meta AI**: https://ai.meta.com/blog/

For each new article found, collect:
- Company name
- Article title
- Publication date
- 2-3 sentence summary in Japanese
- URL

If no new articles were published in the last 24 hours for a given blog, skip it.
If no new articles are found across all blogs, write a message saying "本日は新着記事はありませんでした。" and still send the email.

## Step 2

Write the digest as a beautiful HTML email to `/tmp/tech-blog-digest.html`.

Use the following template and fill in the articles:

```html
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
  body { font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 20px; }
  .container { max-width: 660px; margin: auto; background: #fff; border-radius: 10px; overflow: hidden; }
  .header { background: #1a1a2e; color: #fff; padding: 28px 32px; }
  .header h1 { margin: 0; font-size: 20px; }
  .header p { margin: 6px 0 0; color: #aaa; font-size: 12px; }
  .content { padding: 24px 32px; }
  .company-section { margin-bottom: 24px; }
  .company-label { font-size: 11px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; color: #fff; background: #4f8ef7; display: inline-block; padding: 2px 10px; border-radius: 4px; margin-bottom: 10px; }
  .article { border-left: 3px solid #e0e7ff; padding: 10px 14px; margin-bottom: 10px; background: #f8f9ff; border-radius: 0 6px 6px 0; }
  .article h2 { margin: 0 0 6px; font-size: 14px; color: #1a1a2e; }
  .article p { margin: 0 0 8px; font-size: 13px; color: #555; line-height: 1.6; }
  .article a { font-size: 12px; color: #4f8ef7; text-decoration: none; }
  .footer { background: #f4f4f4; text-align: center; padding: 16px; font-size: 11px; color: #999; }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>Tech Blog Digest</h1>
    <p>{current_date} · Anthropic / OpenAI / DeepMind / Meta AI</p>
  </div>
  <div class="content">
    <!-- 各企業のセクションを挿入。記事がない企業はスキップ -->
    <div class="company-section">
      <span class="company-label">{company_name}</span>
      <div class="article">
        <h2>{article_title}</h2>
        <p>{summary_japanese}</p>
        <a href="{article_url}">記事を読む →</a>
      </div>
    </div>
  </div>
  <div class="footer">Tech Blog Digest · 自動配信</div>
</div>
</body>
</html>
```

## Step 3

Run this command to send the HTML email:

```
python send_gmail.py --to a.takahashi@visualhawaii.com --subject "Tech Blog Digest {current_date}" --body-file /tmp/tech-blog-digest.html --html
```
