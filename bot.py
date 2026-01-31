import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
TOKEN = "8462581706:AAFmBtyX2dcs46XonGDHbQWTAdTAedXjJWw"  # <-- BotFather se naya token yahan paste karo
BOT_USERNAME = "Hghhgjvvbot"        # <-- @ ke bina

users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in users:
        users[user_id] = {"points": 50}

    keyboard = [
        [InlineKeyboardButton("Balance", callback_data="balance")],
        [InlineKeyboardButton("Pricing", callback_data="pricing")],
        [InlineKeyboardButton("Get Service", callback_data="service")],
        [InlineKeyboardButton("Referral", callback_data="referral")]
    ]

    await update.message.reply_text(
        "Welcome to AI Service Bot",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == "balance":
        await query.edit_message_text(
            f"Your Balance: {users[user_id]['points']} Points"
        )

    elif query.data == "pricing":
        await query.edit_message_text(
            "Pricing\n\n"
            "50 Points = 20 INR\n"
            "250 Points = 90 INR\n"
            "500 Points = 190 INR\n\n"
            "Payment via UPI"
        )

    elif query.data == "service":
        if users[user_id]["points"] >= 50:
            users[user_id]["points"] -= 50
            await query.edit_message_text(
                "Service request accepted.\nAdmin will contact you."
            )
        else:
            await query.edit_message_text(
                "Not enough points."
            )

    elif query.data == "referral":
        await query.edit_message_text(
            "Invite & Earn\n\n"
            f"https://t.me/{BOT_USERNAME}?start={user_id}"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.run_polling()

if __name__ == "__main__":
    main()
