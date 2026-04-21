---
name: AI-News
description: 最近のAIニュースを検索し、HTML形式のメールで送信するための手順。
---

# AI News Letter

## Step 1

Search for the latest AI news from the past 24 hours. Focus on major announcements, new model releases, and notable research.

## Step 2

Write the news summary as a beautiful HTML email to `/tmp/ai-news.html`.

Use the following template and fill in the articles:

```html
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
  body { font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 20px; }
  .container { max-width: 640px; margin: auto; background: #fff; border-radius: 8px; overflow: hidden; }
  .header { background: #1a1a2e; color: #fff; padding: 24px 32px; }
  .header h1 { margin: 0; font-size: 22px; }
  .header p { margin: 4px 0 0; color: #aaa; font-size: 13px; }
  .content { padding: 24px 32px; }
  .article { border-left: 4px solid #4f8ef7; padding: 12px 16px; margin-bottom: 20px; background: #f9fbff; border-radius: 0 6px 6px 0; }
  .article h2 { margin: 0 0 6px; font-size: 15px; color: #1a1a2e; }
  .article p { margin: 0; font-size: 13px; color: #555; line-height: 1.6; }
  .footer { background: #f4f4f4; text-align: center; padding: 16px; font-size: 11px; color: #999; }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>AI News</h1>
    <p>{current_date}</p>
  </div>
  <div class="content">
    <!-- ニュース記事をここに挿入 (各記事を .article div で囲む) -->
    <div class="article">
      <h2>{article_title}</h2>
      <p>{article_summary}</p>
    </div>
  </div>
  <div class="footer">AI News · 自動配信</div>
</div>
</body>
</html>
```

## Step 3

Run this command to send the HTML email:

```
python send_gmail.py --to a.takahashi@visualhawaii.com --subject "AI News {current_date}" --body-file /tmp/ai-news.html --html
```
