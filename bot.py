from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")
CHANNEL = "@CC1kTrading"
CHANNEL_LINK = "https://t.me/CC1kTrading"

# Define valid member statuses
VALID_MEMBER_STATUSES = {"member", "administrator", "creator", "owner"}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)],
          [InlineKeyboardButton("✅ I've Joined", callback_data="check")]]
    text = ("👋 *Welcome to CC TRADE*\n\n"
            "Please join our official channel and then press *I've Joined*.")
    await update.message.reply_text(text, parse_mode="Markdown",
                                    reply_markup=InlineKeyboardMarkup(kb))

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    member = await context.bot.get_chat_member(CHANNEL, q.from_user.id)
    
    if member.status in VALID_MEMBER_STATUSES:
        keyboard = [[
            InlineKeyboardButton(
                "🚀 Open CC TRADE Channel",
                url="https://t.me/CC1kTrading"
            )
        ]]
        await q.edit_message_text(  # Fixed: was 'query' instead of 'q'
            """✅ Verification successful!

🎉 Welcome to CC TRADE!

You now have full access to our official channel.

Click the button below to open the channel and view the latest offers.""",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        kb = [[InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)]]
        await q.edit_message_text("❌ You must join the channel first.",
                                  reply_markup=InlineKeyboardMarkup(kb))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(check))
app.run_polling()
