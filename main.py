from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = '6768881871:AAEJJPPpCQHgk1Grq53HS5kX095nVhIRiUQ'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Приветствие
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    discount_code_btn = types.KeyboardButton('Получить -10% на первый заказ!')
    order_btn = types.KeyboardButton('Заказать')
    new_in_btn = types.KeyboardButton('Посмотреть новинки')
    track_order_btn = types.KeyboardButton('Отследить заказ')
    customer_service_btn = types.KeyboardButton('Написать в поддержку')
    markup.add(discount_code_btn)
    markup.add(order_btn, new_in_btn)
    markup.add(track_order_btn, customer_service_btn)

    await message.answer(f'Привет, {message.from_user.first_name}!\n'
                         'Если ты в поиске необычных украшений, которых ни у кого нет - '
                         'то ты в правильном месте! Мы постоянно в поиске новых интересных дизайнеров по всему миру, чтобы твои украшения всегда привлекали внимание и становились поводом для разговора.\n\n', reply_markup=markup)

@dp.message_handler(lambda message: message.text == 'Получить -10% на первый заказ!')
async def discount_code(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Зарегистрироваться', web_app=WebAppInfo(url='https://elinaavon.github.io/')))
    await message.answer('Получи скидку -10% на первый заказ при регистрации.', reply_markup=markup)

@dp.message_handler(lambda message: message.text == 'Заказать')
async def order(message: types.Message):
    await message.answer('Напиши название украшения, которое хочешь заказать:')

@dp.message_handler(lambda message: message.text == 'Отследить заказ')
async def track_order(message: types.Message):
    await message.answer('Напиши номер заказа:')

@dp.message_handler(lambda message: message.text == 'Написать в поддержку')
async def contact_customer_service(message: types.Message):
    await message.answer('Пожалуйста, обращайся со всеми вопросами в личные сообщения к @elinaavon')

@dp.message_handler(lambda message: message.text == 'Посмотреть новинки')
async def new_in(message: types.Message):
    justine_clenquet_collage = open('./photos/collage.png', 'rb')
    await bot.send_photo(message.chat.id, justine_clenquet_collage.read())
    justine_clenquet_collage.close()

    markup_justine = types.InlineKeyboardMarkup()
    button_justine = types.InlineKeyboardButton('Посмотреть всю коллекцию Justine Clenquet на нашем сайте',
                                                url='https://justineclenquet.com/en-us')
    markup_justine.add(button_justine)

    await message.answer('Jusine Clenquet - французский дизайнер. Все ее украшения - это результат кропотливой ручной работы, сделанной с высоким качеством и большим вниманием к деталям.',
                         reply_markup=markup_justine)

    panconesi = open('./photos/collage1.png', 'rb')
    await bot.send_photo(message.chat.id, panconesi.read())
    panconesi.close()

    markup_panconesi = types.InlineKeyboardMarkup()
    button_panconesi = types.InlineKeyboardButton('Посмотреть всю коллекцию Panconesi на нашем сайте',
                                                  url='https://marcopanconesi.com/')
    markup_panconesi.add(button_panconesi)

    await message.answer(
        'Marco Panconesi, создавая свои работы, ищет вдохновение в природе, в особенности в камнях и металлах. Проработав в ювелирных мастерских Givenchy, Balenciaga, а также главным дизайнером в Fendi и директором отдела ювелирного дизайна в Swarowski, он продолжает создавать прекрасные украшения для своего неповторимого бренда Panconesi.',
        reply_markup=markup_panconesi
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
