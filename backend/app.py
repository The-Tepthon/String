
from flask import Flask, render_template, request
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

app = Flask(__name__)

# تحميل القيم من متغيرات البيئة
API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "")
SESSION_STRING = os.getenv("SESSION_STRING", "")

if not SESSION_STRING:
    raise Exception("SESSION_STRING is required and must be set in environment variables.")

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@app.route("/")
def index():
    return "تطبيق تليجرام جاهز للعمل!"

@app.route("/send", methods=["POST"])
def send_message():
    phone = request.form.get("phone")
    message = request.form.get("message")
    async def main():
        await client.send_message(phone, message)
    with client:
        client.loop.run_until_complete(main())
    return "تم الإرسال"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
