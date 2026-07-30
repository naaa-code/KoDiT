from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters, CommandHandler
import os
import re

TOKEN = "8458357251:AAEq6two8WV6prxU1Xq9NZ7D9wCBg7oZVns"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
"""🌟 Selamat Datang ke KoDiT

📚 Kamus Digital Isyarat

Sila taip perkataan yang ingin dicari.

Contoh:
• Alif
• Islam
• Solat
• Gua Thur
• Air Mutlak

KoDiT akan menghantar video isyarat yang berkaitan.

Selamat belajar! 🤟
""")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()
    text = re.sub(r"\s+", "_", text)

    video_path = f"videos/{text}.mp4"

    if os.path.exists(video_path):
        await update.message.reply_video(video=open(video_path, "rb"))
    else:
        await update.message.reply_text(f"Maaf, video '{text}' belum ada.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start",start))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("KoDiT Bot sedang berjalan...")

app.run_polling() 

