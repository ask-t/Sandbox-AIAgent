"""
Gmail自動送信用スクリプト。

使い方:
1) 環境変数を設定
   - GMAIL_ADDRESS: 送信元Gmailアドレス
   - GMAIL_APP_PASSWORD: Googleアカウントで発行したアプリパスワード
2) 実行
   python send_gmail.py --to example@example.com --subject "テスト" --body "本文です"
"""

from __future__ import annotations
from dotenv import load_dotenv
import argparse
import os
import smtplib
from email.message import EmailMessage

load_dotenv()

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


def build_message(from_addr: str, to_addr: str, subject: str, body: str) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = subject
    msg.set_content(body)
    return msg


def send_gmail(to_addr: str, subject: str, body: str) -> None:
    gmail_address_env = os.getenv("GMAIL_ADDRESS")

    if not gmail_address_env or ":" not in gmail_address_env:
        raise ValueError(
            "環境変数 GMAIL_ADDRESS を 'email:password' 形式で設定してください。"
        )

    gmail_address, app_password = gmail_address_env.split(":", 1)
    message = build_message(gmail_address, to_addr, subject, body)

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.login(gmail_address, app_password)
        smtp.send_message(message)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Gmail自動送信スクリプト")
    parser.add_argument("--to", required=True, help="送信先メールアドレス")
    parser.add_argument("--subject", required=True, help="メール件名")
    parser.add_argument("--body", required=True, help="メール本文")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    send_gmail(args.to, args.subject, args.body)
    print("メール送信に成功しました。")


if __name__ == "__main__":
    main()
