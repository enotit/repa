import openai_secret_manager
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Получаем ключи доступа к OpenAI API из переменной окружения
secrets = openai_secret_manager.get_secret("openai")

# Инициализируем API OpenAI
openai.api_key = secrets["api_key"]

# Функция, которая будет вызываться при получении текстового сообщения
def handle_text(update, context):
    # Получаем текст сообщения
    text = update.message.text
    
    # Отправляем запрос в OpenAI API
    response = openai.Completion.create(
        engine="davinci", prompt=text, max_tokens=1024, n=1, stop=None, temperature=0.7
    )
    
    # Получаем ответ из API и отправляем его обратно в Telegram
    answer = response.choices[0].text.strip()
    update.message.reply_text(answer)

# Функция, которая будет вызываться при получении команды /start
def start(update, context):
    update.message.reply_text('Привет! Я готов отвечать на ваши сообщения.')

# Создаем объект Updater и передаем ему токен бота
updater = Updater('1177583422:AAGVvSoNzgqKxaU1aJmDE2s82vFQ2RxCIzw', use_context=True)

# Получаем диспетчер сообщений
dispatcher = updater.dispatcher

# Создаем обработчики команд и сообщений
start_handler = CommandHandler('start', start)
text_handler = MessageHandler(Filters.text, handle_text)

# Регистрируем обработчики в диспетчере
dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)

# Запускаем бота
updater.start_polling()