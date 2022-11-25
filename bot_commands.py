from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import model 


# Определите несколько обработчиков команд. Обычно они принимают два аргумента update и 
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправит сообщение, когда будет введена команда /start."""
    user = update.effective_user
    await update.message.reply_html(
        f"""\
        Hi {user.mention_html()}!
        /echo - Повторяет сообщение пользователя\n\
        /calc - Калькулятор\n\
        /help - Справка по командам""",
        reply_markup=ForceReply(selective=True),
    )

    
async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправит сообщение, когда будет введена команда /calc"""
    await update.message.reply_text(f'{update.message.text[6:]} = {model.run(model.parsing(update.message.text[6:]))}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправит сообщение, когда будет введена команда /help"""
    await update.message.reply_text(f'''\
                /start - Приветствие пользователя\n\
                /echo - Повторяет сообщение пользователя\n\
                /calc - Калькулятор\n\
                /help - Справка по командам''')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Повторит сообщение пользователя."""
    await update.message.reply_text(update.message.text[6:])


def main() -> None:
    """Запустите бота."""
    # Создайте приложение и передайте ему токен вашего бота.
    application = Application.builder().token(model.read_data()).build()

    # по разным командам - ответ в Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("calc", calc))
    application.add_handler(CommandHandler("echo", echo))

    # повторит сообщение в Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запуск бота до тех пор, пока пользователь не нажмет Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()

    