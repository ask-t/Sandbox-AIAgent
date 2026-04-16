# Gmail自動送信 (Python)

このリポジトリには、`send_gmail.py` で Gmail を自動送信する最小構成のサンプルを入れています。

## 1. 事前準備

1. Googleアカウントで 2 段階認証を有効化
2. Google の「アプリパスワード」を発行
3. 以下の環境変数を設定

### PowerShell

```powershell
$env:GMAIL_ADDRESS = "your_address@gmail.com"
$env:GMAIL_APP_PASSWORD = "xxxx xxxx xxxx xxxx"  # 発行された16桁
```

## 2. 実行

```powershell
python .\send_gmail.py --to "to@example.com" --subject "テスト送信" --body "これは自動送信メールです"
```

成功すると `メール送信に成功しました。` と表示されます。

## 3. 補足

- Gmailの通常パスワードではなく、アプリパスワードを使用してください。
- 認証情報はコードに直書きせず、環境変数で管理してください。
