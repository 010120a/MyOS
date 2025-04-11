import flet as ft
import os


# Функция для открытия ярлыка
def open_file(path):
    os.startfile(path)


# Функция для создания иконок на рабочем столе
def create_icon(name, icon_color, path, x, y):
    icon = ft.Container(
        width=80,
        height=80,
        left=x,  # Позиционирование иконки по оси X
        top=y,  # Позиционирование иконки по оси Y
        content=ft.Column(
            controls=[
                ft.Icon(ft.icons.BEACH_ACCESS, size=40, color=icon_color),
                ft.Text(name, size=12, color="white", text_align="center"),
            ],
            horizontal_alignment="center",
            spacing=5,
        ),
        on_click=lambda _: open_file(path),  # Привязка иконки к открытому ярлыку
    )
    return icon


# Функция для поиска ярлыков по всему устройству
def find_shortcuts(root_dir):
    shortcut_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".lnk"):  # Ярлыки имеют расширение .lnk
                shortcut_paths.append(os.path.join(dirpath, filename))
    return shortcut_paths


# Создание приложения Flet
def main(page: ft.Page):
    page.title = "Рабочий стол Flet"
    page.window_width = 800
    page.window_height = 600
    page.bgcolor = "#1e1e1e"
    page.window_resizable = True

    # Используем Stack для размещения иконок без прокрутки
    desktop = ft.Stack(
        width=page.window_width,
        height=page.window_height,
    )

    # Путь для поиска ярлыков (например, Рабочий стол и другие директории)
    root_directories = [
        "C:/Users/Local/Desktop",  # Рабочий стол пользователя
    ]

    shortcut_paths = []

    # Поиск ярлыков во всех указанных каталогах
    for root_dir in root_directories:
        shortcut_paths.extend(find_shortcuts(root_dir))

    # Позиции для иконок на рабочем столе
    icon_colors = [
        ft.colors.BLUE_400, ft.colors.BLUE_400, ft.colors.BLUE_400, ft.colors.BLUE_400, ft.colors.BLUE_400,
        ft.colors.BLUE, ft.colors.BLUE_400, ft.colors.BLUE_400, ft.colors.BLUE_400, ft.colors.BLUE_400,
        ft.colors.BLUE_400, ft.colors.BLUE_400, ft.colors.BLUE_400, ft.colors.BLUE_400, ft.colors.BLUE_400,
        ft.colors.BLUE_400
    ]

    # Позиции для иконок
    x_pos, y_pos = 50, 50
    icon_width = 90  # Ширина иконки + отступ
    icon_height = 90  # Высота иконки + отступ

    # Создаем иконки
    icon_count = 0  # Счетчик для позиционирования иконок
    for file_path in shortcut_paths:
        # Получаем имя ярлыка без пути и расширения
        file_name = os.path.basename(file_path).split('.')[0]

        # Делаем имя ярлыка коротким, если оно слишком длинное
        short_name = file_name

        # Получаем цвет для иконки (просто циклично используем цвета)
        icon_color = icon_colors[icon_count % len(icon_colors)]

        # Создаем иконку для ярлыка
        icon = create_icon(short_name, icon_color, file_path, x_pos, y_pos)

        # Добавляем иконку на рабочий стол
        desktop.controls.append(icon)

        # Обновляем позицию для следующей иконки
        x_pos += icon_width
        if x_pos > page.window_width - icon_width:
            x_pos = 50
            y_pos += icon_height

        # Увеличиваем счетчик иконок
        icon_count += 1

    # Добавляем Stack с иконками на страницу
    page.add(desktop)


ft.app(target=main)

