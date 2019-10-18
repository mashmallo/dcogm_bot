#/usr/bin/python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, CallbackQueryHandler, MessageHandler
	
def rak(update, context):
	rpict = open('rak.jpg', 'rb')
	update.message.reply_photo(photo=rpict)

def subnet(update, context):
	spict = open('subnet.jpg', 'rb')
	update.message.reply_photo(photo=spict)

def jadwal(update, context):
	keyboard = [[InlineKeyboardButton("Oktober 2019", callback_data='1'),
                 InlineKeyboardButton("November 2019", callback_data='2')],
                [InlineKeyboardButton("Desember 2019", callback_data='3')]]
	reply_markup = InlineKeyboardMarkup(keyboard)
	update.message.reply_text('Jadwal bulan apa?', reply_markup=reply_markup)

def button(update, context):
	query = update.callback_query
	caption = ["Oktober 2019","November 2019","Desember 2019"]
	if query.data == '1':
		jadwal1 = open('1019.png', 'rb')
		query.edit_message_text(text="Jadwal bulan {}".format(caption[0]))
		query.message.reply_photo(photo=jadwal1)
	elif query.data == '2':
		jadwal2 = open('1119.png', 'rb')
		query.edit_message_text(text="Jadwal bulan {}".format(caption[1]))
		query.message.reply_photo(photo=jadwal2)
	elif query.data == '3':
		jadwal3 = open('1219.png', 'rb')
		query.edit_message_text(text="Jadwal bulan {}".format(caption[2]))
		query.message.reply_photo(photo=jadwal3)
		
def main():
	# Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
	updater = Updater(token='YOUR TELEGRAM BOT TOKEN', use_context=True)
	dp = updater.dispatcher
	
	#list of allowed group id
	allowed_groups = ["Insert your Telegram Group ID"]
	filters = Filters.chat(allowed_groups)
	dp.add_handler(CommandHandler('rak', rak, filters))
	dp.add_handler(CommandHandler('subnet', subnet, filters))
	dp.add_handler(CommandHandler('jadwal', jadwal, filters))
	dp.add_handler(CallbackQueryHandler(button))
	
	#Start the Bot
	updater.start_polling()
	
	# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
	updater.idle()

if __name__ == '__main__':
    main()
