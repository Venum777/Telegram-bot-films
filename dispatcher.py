# Python
from aiogram import (
    Dispatcher,
    Router, 
    types
)
from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Local
from database.models.genres import Genre
from database.models.films import Film
from database.connection import my_connection


dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    await message.answer(f"""
    Все доступные команды:
    Посмотреть список жанров - /genres
    Посмотреть список всех фильмов - /all_films
    """)


@dp.message(Command("genres"))
async def get_genres(message: types.Message):
    genres = Genre.get_all(conn=my_connection.conn)
    builder_genre = InlineKeyboardBuilder()
    for genre in genres:
        builder_genre.button(text=f"{genre[1]}", callback_data=f"set:{genre[0]}")

    builder_genre.adjust(5, 5)
    
    await message.answer("Выберите жанр:", reply_markup=builder_genre.as_markup())


@dp.callback_query(lambda c: c.data.startswith('set:'))
async def get_films(callback: types.CallbackQuery):
    genre = callback.data.replace('set:', '')
    films = Film.get_all_by_genre(conn=my_connection.conn, genre_id=genre)
    for film in films:
        await callback.message.answer(f"""
        -------------------------------------------------
        Название: {film[0]}
        Описание: {film[1]}
        Рейтинг: {film[3]} ⭐
        -------------------------------------------------
        """)


@dp.message(Command("all_films"))
async def get_all_films(message: types.Message):
    films = Film.get_all(conn=my_connection.conn)
    for film in films:
        await message.answer(f"""
            -------------------------------------------------
            Название: {film[0]}
            Описание: {film[1]}
            Рейтинг: {film[3]} ⭐
            -------------------------------------------------
        """)
