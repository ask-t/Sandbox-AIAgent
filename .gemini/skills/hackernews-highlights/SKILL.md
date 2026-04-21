---
name: hackernews-highlights
description: Hacker NewsのトップストーリーからAI/Tech関連記事をフィルタしてHTML形式のメールで送信する。
---

# Hacker News Highlights

## Step 1

Fetch today's top stories from Hacker News.

You can use the official HN API:
- Top stories list: https://hacker-news.firebaseio.com/v0/topstories.json
- Item detail: https://hacker-news.firebaseio.com/v0/item/{id}.json

Fetch the top 50 story IDs, then retrieve details for each. Filter for stories that are relevant to:
- AI / Machine Learning / LLM
- Software engineering / programming
- Startups / tech industry news
- Science / research

For each selected story, collect:
- Title
- URL
- Points (score)
- Number of comments
- HN discussion URL (https://news.ycombinator.com/item?id={id})
- 1-sentence summary in Japanese (based on the title/context)

Select the top 10 most interesting and highly-scored stories.

## Step 2

Write the highlights as a beautiful HTML email to `/tmp/hackernews-highlights.html`.

Use the following template and fill in the stories:

```html
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
  body { font-family: Arial, sans-serif; background: #f6f6ef; margin: 0; padding: 20px; }
  .container { max-width: 660px; margin: auto; background: #fff; border-radius: 10px; overflow: hidden; }
  .header { background: #ff6600; padding: 20px 32px; }
  .header h1 { margin: 0; font-size: 20px; color: #fff; }
  .header p { margin: 4px 0 0; color: #ffe0c0; font-size: 12px; }
  .content { padding: 16px 24px; }
  .story { border-bottom: 1px solid #eee; padding: 14px 0; }
  .story:last-child { border-bottom: none; }
  .story-rank { font-size: 20px; font-weight: bold; color: #ff6600; float: left; width: 32px; }
  .story-body { margin-left: 40px; }
  .story-title { font-size: 14px; font-weight: bold; margin: 0 0 4px; }
  .story-title a { color: #1a1a2e; text-decoration: none; }
  .story-summary { font-size: 12px; color: #666; margin: 0 0 6px; line-height: 1.5; }
  .story-meta { font-size: 11px; color: #999; }
  .story-meta a { color: #ff6600; text-decoration: none; }
  .footer { background: #f6f6ef; text-align: center; padding: 14px; font-size: 11px; color: #999; }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>Hacker News Highlights</h1>
    <p>{current_date} · Top AI/Tech Stories</p>
  </div>
  <div class="content">
    <!-- 各ストーリーを .story div で挿入 -->
    <div class="story">
      <span class="story-rank">{rank}</span>
      <div class="story-body">
        <p class="story-title"><a href="{url}">{title}</a></p>
        <p class="story-summary">{summary_japanese}</p>
        <span class="story-meta">▲ {points} points · <a href="{hn_url}">{comments} comments</a></span>
      </div>
    </div>
  </div>
  <div class="footer">Hacker News Highlights · 自動配信</div>
</div>
</body>
</html>
```

## Step 3

Run this command to send the HTML email:

```
python send_gmail.py --to a.takahashi@visualhawaii.com --subject "HN Highlights {current_date}" --body-file /tmp/hackernews-highlights.html --html
```
