"""
Gmail自動送信用スクリプト。

使い方:
1) 環境変数を設定
   - GMAIL_ADDRESS: 送信元Gmailアドレス (例: user@gmail.com:app_password)
2) 実行（プレーンテキスト）
   python send_gmail.py --to example@example.com --subject "テスト" --body "本文です"
3) 実行（HTMLファイル）
   python send_gmail.py --to example@example.com --subject "テスト" --body-file /tmp/mail.html --html
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


def build_message(
    from_addr: str, to_addr: str, subject: str, body: str, html: bool
) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = subject
    if html:
        msg.set_content("このメールはHTML形式です。HTMLに対応したメールクライアントでご覧ください。")
        msg.add_alternative(body, subtype="html")
    else:
        msg.set_content(body)
    return msg


def send_gmail(to_addr: str, subject: str, body: str, html: bool = False) -> None:
    gmail_address_env = os.getenv("GMAIL_ADDRESS")

    if not gmail_address_env or ":" not in gmail_address_env:
        raise ValueError(
            "環境変数 GMAIL_ADDRESS を 'email:password' 形式で設定してください。"
        )

    gmail_address, app_password = gmail_address_env.split(":", 1)
    message = build_message(gmail_address, to_addr, subject, body, html)

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.login(gmail_address, app_password)
        smtp.send_message(message)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Gmail自動送信スクリプト")
    parser.add_argument("--to", required=True, help="送信先メールアドレス")
    parser.add_argument("--subject", required=True, help="メール件名")
    body_group = parser.add_mutually_exclusive_group(required=True)
    body_group.add_argument("--body", help="メール本文（文字列）")
    body_group.add_argument("--body-file", help="メール本文ファイルパス（HTMLファイルなど）")
    parser.add_argument("--html", action="store_true", help="HTML形式で送信する")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.body_file:
        with open(args.body_file, encoding="utf-8") as f:
            body = f.read()
    else:
        body = args.body
    send_gmail(args.to, args.subject, body, html=args.html)
    print("メール送信に成功しました。")


if __name__ == "__main__":
    main()
