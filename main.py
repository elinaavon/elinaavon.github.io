from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = '6768881871:AAEJJPPpCQHgk1Grq53HS5kX095nVhIRiUQ'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Приветствие
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    discount_code_btn = types.KeyboardButton('Get 10% Off Your First Order!')
    order_btn = types.KeyboardButton('Order')
    new_in_btn = types.KeyboardButton('New In')
    track_order_btn = types.KeyboardButton('Track Order')
    customer_service_btn = types.KeyboardButton('Contact Customer Service')
    markup.add(discount_code_btn)
    markup.add(order_btn, new_in_btn)
    markup.add(track_order_btn, customer_service_btn)

    await message.answer(f'Hi, {message.from_user.first_name}!\n'
                         'If you\'re looking for jewelry pieces that everybody is going to ask you about  - '
                         'then you\'re in a right place! We\'re always looking for new new unordinary designers around the world so that you can be the center of attention.\n\n', reply_markup=markup)

@dp.message_handler(lambda message: message.text == 'Get 10% Off Your First Order!')
async def discount_code(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Sign Up', web_app=WebAppInfo(url='https://elinaavon.github.io/')))
    await message.answer('Get 10% Off For Your First Order.', reply_markup=markup)

@dp.message_handler(lambda message: message.text == 'Order')
async def order(message: types.Message):
    await message.answer('Напиши название украшения, которое хочешь заказать:')

@dp.message_handler(lambda message: message.text == 'Track Order')
async def track_order(message: types.Message):
    await message.answer('Напиши номер заказа:')

@dp.message_handler(lambda message: message.text == 'Contact Customer Service')
async def contact_customer_service(message: types.Message):
    await message.answer('Пожалуйста, обращайся со всеми вопросами в личные сообщения к @elinaavon')

@dp.message_handler(lambda message: message.text == 'New In')
async def new_in(message: types.Message):
    justine_clenquet_collage = open('./photos/collage.png', 'rb')
    await bot.send_photo(message.chat.id, justine_clenquet_collage.read())
    justine_clenquet_collage.close()

    markup_justine = types.InlineKeyboardMarkup()
    button_justine = types.InlineKeyboardButton('Check out Justine Clenquet\'s full collection',
                                                url='https://justineclenquet.com/en-us')
    markup_justine.add(button_justine)

    await message.answer('Jusine Clenquet - французский дизайнер. Все ее украшения - это результат кропотливой ручной работы, сделанной с высоким качеством и большим вниманием к деталям.',
                         reply_markup=markup_justine)

    panconesi = open('./photos/collage1.png', 'rb')
    await bot.send_photo(message.chat.id, panconesi.read())
    panconesi.close()

    markup_panconesi = types.InlineKeyboardMarkup()
    button_panconesi = types.InlineKeyboardButton('Check out Marco Panconesi\'s full collection',
                                                  url='https://marcopanconesi.com/')
    markup_panconesi.add(button_panconesi)

    await message.answer(
        'Marco Panconesi, создавая свои работы, ищет вдохновение в природе, в особенности в камнях и металлах. Проработав в ювелирных мастерских Givenchy, Balenciaga, а также главным дизайнером в Fendi и директором отдела ювелирного дизайна в Swarowski, он продолжает создавать прекрасные украшения для своего неповторимого бренда Panconesi.',
        reply_markup=markup_panconesi
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
