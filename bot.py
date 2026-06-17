from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN=import os

TOKEN = os.getenv("TOKEN")
CHANNEL="@CC1kTrading"
CHANNEL_LINK="https://t.me/CC1kTrading"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb=[[InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("✅ I've Joined", callback_data="check")]]
    text=("👋 *Welcome to CC TRADE*\n\n"
          "Please join our official channel and then press *I've Joined*.")
    await update.message.reply_text(text,parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(kb))

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q=update.callback_query
    await q.answer()
    member=await context.bot.get_chat_member(CHANNEL,q.from_user.id)
    if member.status in ["member","administrator","creator","owner"]:
        await q.edit_message_text("✅ Verification successful! Welcome to CC TRADE.")
    else:
        kb=[[InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)]]
        await q.edit_message_text("❌ You must join the channel first.",
            reply_markup=InlineKeyboardMarkup(kb))

app=Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(CallbackQueryHandler(check))
app.run_polling()
