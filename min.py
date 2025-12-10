import os
import aiohttp
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)


BOT_TOKEN = os.getenv("8215531557:AAGYtHi_62InVtodJj1gFafvftBGt_XARV0")
GOOGLE_API_KEY = os.getenv("AIzaSyAnVYTf_A9LKEfP1Ely5b0fyt_SjSHNMN0")


# --------------------------
# Generate 4 Images
# --------------------------
async def generate_images(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateImages?key={GOOGLE_API_KEY}"

    payload = {
        "prompt": {"text": prompt},
        "numImages": 4
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            data = await response.json()

            images = []
            try:
                for item in data["images"]:
                    img_bytes = item["imageBytes"]
                    images.append(img_bytes)
            except:
                return None

            return images


# --------------------------
# Start Command
# --------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌟 **BD Ultra Image Generator** এ স্বাগতম!\n"
        "যে কোনো প্রম্পট লিখুন — আমি ৪টি AI ছবি বানিয়ে দেব।\n\n"
        "উদাহরণ:\n👉 *A girl standing beside river*\n👉 *Future city skyline*\n👉 *Bangladeshi village at sunset*"
    )


# --------------------------
# Prompt Handler
# --------------------------
async def handle_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text

    msg = await update.message.reply_text("⏳ ছবি তৈরি করা হচ্ছে, একটু অপেক্ষা করুন...")

    images = await generate_images(prompt)

    if images is None:
        await msg.edit_text("❌ ছবি তৈরি করতে সমস্যা হয়েছে। আবার চেষ্টা করুন।")
        return

    await msg.edit_text("✨ আপনার AI ছবি প্রস্তুত!")

    # Send all 4 images
    for img in images:
        await update.message.reply_photo(photo=img)


# --------------------------
# Main Function
# --------------------------
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_prompt))

    print("BD Ultra Image Generator Bot Running...")
    app.run_polling()


if __name__ == "__main__":
    main()