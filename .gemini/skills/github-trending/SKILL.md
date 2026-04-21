---
name: github-trending
description: GitHub Trendingから週間トレンドのAI/MLリポジトリを収集し、HTML形式のメールで送信する。
---

# GitHub Trending Weekly Digest

## Step 1

Search for this week's trending GitHub repositories in the AI/ML space.

Visit or search for trending repositories with these topics/keywords:
- artificial-intelligence, machine-learning, deep-learning, llm, generative-ai
- Look at https://github.com/trending?since=weekly

For each repository, collect:
- Repository name (owner/repo)
- Description
- Primary language
- Stars count (total)
- Stars gained this week
- URL (https://github.com/{owner}/{repo})

Aim for the top 10 repositories.

## Step 2

Write the digest as a beautiful HTML email to `/tmp/github-trending.html`.

Use the following template and fill in the repositories:

```html
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
  body { font-family: Arial, sans-serif; background: #0d1117; margin: 0; padding: 20px; }
  .container { max-width: 660px; margin: auto; background: #161b22; border-radius: 10px; overflow: hidden; border: 1px solid #30363d; }
  .header { background: #21262d; padding: 28px 32px; border-bottom: 1px solid #30363d; }
  .header h1 { margin: 0; font-size: 20px; color: #e6edf3; }
  .header p { margin: 6px 0 0; color: #8b949e; font-size: 12px; }
  .content { padding: 20px 24px; }
  .repo { border: 1px solid #30363d; border-radius: 8px; padding: 16px; margin-bottom: 12px; background: #0d1117; }
  .repo-name { font-size: 15px; font-weight: bold; margin: 0 0 6px; }
  .repo-name a { color: #58a6ff; text-decoration: none; }
  .repo-desc { font-size: 13px; color: #8b949e; margin: 0 0 10px; line-height: 1.5; }
  .repo-meta { display: flex; gap: 16px; font-size: 12px; color: #8b949e; }
  .repo-meta .stars { color: #f0c040; }
  .repo-meta .week-stars { color: #3fb950; }
  .footer { background: #21262d; text-align: center; padding: 16px; font-size: 11px; color: #8b949e; border-top: 1px solid #30363d; }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>GitHub Trending · AI/ML</h1>
    <p>週間トレンド · {current_date}</p>
  </div>
  <div class="content">
    <!-- 各リポジトリを .repo div で挿入 -->
    <div class="repo">
      <p class="repo-name"><a href="{repo_url}">{owner}/{repo}</a></p>
      <p class="repo-desc">{description}</p>
      <div class="repo-meta">
        <span class="stars">★ {total_stars}</span>
        <span class="week-stars">↑ {week_stars} this week</span>
        <span>{language}</span>
      </div>
    </div>
  </div>
  <div class="footer">GitHub Trending Digest · 自動配信</div>
</div>
</body>
</html>
```

## Step 3

Run this command to send the HTML email:

```
python send_gmail.py --to a.takahashi@visualhawaii.com --subject "GitHub Trending AI/ML {current_date}" --body-file /tmp/github-trending.html --html
```
