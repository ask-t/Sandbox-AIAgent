---
name: arxiv-digest
description: arXivから当日の新着AI・機械学習論文を収集し、HTML形式のメールで送信する。
---

# arXiv AI Papers Digest

## Step 1

Search arXiv for today's new papers in the following categories:
- cs.AI (Artificial Intelligence)
- cs.LG (Machine Learning)
- cs.CL (Computation and Language / NLP)

Find papers submitted or cross-listed today. For each paper, collect:
- Title
- Authors (first 3 authors)
- Abstract (summarized in 2-3 sentences in Japanese)
- arXiv URL (format: https://arxiv.org/abs/{id})

Aim for the top 8-10 most impactful or interesting papers.

## Step 2

Write the digest as a beautiful HTML email to `/tmp/arxiv-digest.html`.

Use the following template and fill in the papers:

```html
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
  body { font-family: Arial, sans-serif; background: #f0f2f5; margin: 0; padding: 20px; }
  .container { max-width: 660px; margin: auto; background: #fff; border-radius: 10px; overflow: hidden; }
  .header { background: linear-gradient(135deg, #1a1a2e, #16213e); color: #fff; padding: 28px 32px; }
  .header h1 { margin: 0; font-size: 20px; letter-spacing: 1px; }
  .header p { margin: 6px 0 0; color: #7ec8e3; font-size: 12px; }
  .content { padding: 24px 32px; }
  .paper { border: 1px solid #e8edf3; border-radius: 8px; padding: 16px; margin-bottom: 16px; }
  .paper h2 { margin: 0 0 6px; font-size: 14px; color: #1a1a2e; line-height: 1.4; }
  .paper .authors { font-size: 11px; color: #888; margin-bottom: 8px; }
  .paper p { margin: 0 0 10px; font-size: 13px; color: #444; line-height: 1.6; }
  .paper a { display: inline-block; font-size: 11px; color: #4f8ef7; text-decoration: none; border: 1px solid #4f8ef7; padding: 3px 10px; border-radius: 4px; }
  .footer { background: #f0f2f5; text-align: center; padding: 16px; font-size: 11px; color: #999; }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>arXiv AI Papers Digest</h1>
    <p>{current_date} · cs.AI / cs.LG / cs.CL</p>
  </div>
  <div class="content">
    <!-- 各論文を .paper div で挿入 -->
    <div class="paper">
      <h2>{paper_title}</h2>
      <div class="authors">{authors}</div>
      <p>{abstract_japanese}</p>
      <a href="{arxiv_url}">arXivで読む →</a>
    </div>
  </div>
  <div class="footer">arXiv Digest · 自動配信</div>
</div>
</body>
</html>
```

## Step 3

Run this command to send the HTML email:

```
python send_gmail.py --to a.takahashi@visualhawaii.com --subject "arXiv AI Papers {current_date}" --body-file /tmp/arxiv-digest.html --html
```
