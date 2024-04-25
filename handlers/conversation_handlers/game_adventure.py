from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ConversationHandler, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

from handlers.base_handler import BaseHandler

COMAND, POSITION_1, POSITIONSP_1,POSITION_2,POSITIONSP_2 = range(5)


class GameAdventure(BaseHandler):
    @classmethod
    def register(cls, app):
        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('startgame', cls.startgame)],
            states={
                COMAND: [MessageHandler(filters.Regex('^(Терористи|Спецназ)$'), cls.comand)],
                POSITION_1: [MessageHandler(filters.Regex('^(A|B|Mid)$'), cls.position_1)],
                POSITIONSP_1: [MessageHandler(filters.Regex('^(A|B|Mid)$'), cls.positionsp_1)],
                POSITION_2:[MessageHandler(filters.Regex('^(A|B|Mid)$'), cls.position_2)],
                POSITIONSP_2:[MessageHandler(filters.Regex('^(A|B|Mid)$'), cls.positionsp_2)],

            },
            fallbacks=[CommandHandler('exit', cls.exit)]
        )

        app.add_handler(conversation_handler)

    @staticmethod
    async def startgame(update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [KeyboardButton('Терористи'), KeyboardButton('Спецназ')],
        ]
        reply_text = ReplyKeyboardMarkup(keyboard)
        await update.message.reply_text(f'Привіт {update.effective_user.first_name}! За яку команду будеш грати?', reply_markup=reply_text)

        return COMAND

    @staticmethod
    async def exit(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'Exit from conversation')

        return ConversationHandler.END

    @staticmethod
    async def comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
        comand = update.message.text
        keyboard = [
            [KeyboardButton('A'), KeyboardButton('B'), KeyboardButton('Mid')],
        ]
        reply_text = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        await update.message.reply_text(f'Добре ти граєш за комунду {comand}.Вибери куда ти підеш: ', reply_markup=reply_text)

        if comand == 'Терористи':
            return POSITION_1
        elif comand == 'Спецназ':
            return POSITIONSP_1


    @staticmethod
    async def position_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
        position = update.message.text

        if position == 'A':
            await update.message.reply_text(f"Ви вирішили вийти з ями та стати тетріс, ви вбили всіх спецназовців та встигли поставити пачку!")
            await update.message.reply_text(f'Ви попали в другий раунд: ')
        elif position == 'B':
            await update.message.reply_text(f"Ви вирішили вибігти на +w вбити всіх та поставити пачку, вас вбили.")
            await update.message.reply_text(f'Ви попали в другий раунд: ')
        elif position == 'Mid':
            await update.message.reply_text(f"Ви вирішили вибігти на мід, вас вбили.", reply_markup=ReplyKeyboardRemove())
            await update.message.reply_text(f'Ви попали в другий раунд: ')

        reply_text = ReplyKeyboardMarkup(keyboard)

        if comand == 'Терористи':
            return POSITION_1
        elif comand == 'Спецназ':
            return POSITIONSP_1



    @staticmethod
    async def positionsp_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
        positionsp = update.message.text
        if positionsp == 'A':
            await update.message.reply_text(f"Ви вирішили стати на дефолт, ви згоріли від молотова.")
            await update.message.reply_text(f'Ви попали в другий раунд: ')
        elif positionsp == 'B':
            await update.message.reply_text(f"Вирішили піти на шорт, ви вбили терориста в міді!")
            await update.message.reply_text(f'Ви попали в другий раунд: ')
        elif positionsp == 'Mid':
            await update.message.reply_text(f"Ви вирішили вікно, вас вбили з AWP.")
            await update.message.reply_text(f'Ви попали в другий раунд: ')

        reply_text = ReplyKeyboardMarkup(keyboard)


        return POSITION_2



    @staticmethod
    async def position_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
        positionsp = update.message.text
        if positionsp == 'A':
            await update.message.reply_text(f"Ви вирішили вийти через палас і вас вбив спецназовець.")
        elif positionsp == 'B':
            await update.message.reply_text(f"Ви запушили б і змогли поставити бомбу але вас вбили.")
        elif positionsp == 'Mid':
            await update.message.reply_text(f"Ви вийшли через мід і вбили спецназовця.")

        reply_text = ReplyKeyboardMarkup(keyboard)


    @staticmethod
    async def positionsp_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
        positionsp = update.message.text
        if positionsp == 'A':
            await update.message.reply_text(f"Ви вирішили стати на стейрс, ви почали перестрілюватися з терористом і попали йому в голову.")
        elif positionsp == 'B':
            await update.message.reply_text(f"Ви вирішили встати кар, це був пуш б і ви змогли вбити 3 терористів, але вмерли.")
        elif positionsp == 'Mid':
            await update.message.reply_text(f"Ви вирішили вийти в вікно, там нікого не було.")

        reply_text = ReplyKeyboardMarkup(keyboard)
        return POSITIONSP_2







