# import torch
# import torchvision.transforms as transforms
# from torchvision.models import resnet50
# from PIL import Image

# # Загрузка предобученной модели ResNet
# model = resnet50(pretrained=True)
# model.eval()
# from badwords.image_obscenity import ImageClassifier 

# image_classifier = ImageClassifier()

# image_path = 'test_img4.png'

# result = image_classifier.classify_image(image_path)

# if result:
#     print("Obscenity found in the image.")
# else:
#     print("No obscenity found in the image.")









# # Преобразование изображения перед подачей на вход модели
# transform = transforms.Compose([
#     transforms.Resize(256),
#     transforms.CenterCrop(224),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
# ])

# # Загрузка изображения
# image_path = 'test_img1.png'
# image = Image.open(image_path)

# # Преобразование и нормализация изображения
# input_image = transform(image).unsqueeze(0)

# # Предсказание класса изображения
# with torch.no_grad():
#     output = model(input_image)

# # Получение вероятностей для каждого класса
# probabilities = torch.nn.functional.softmax(output[0], dim=0)

# # Определение класса с наибольшей вероятностью
# if probabilities[1] > probabilities[0]:
#     print("Изображение содержит контент для взрослых")
# else:
#     print("Изображение не содержит контента для взрослых")



# import os
# import shutil

# def extract_files_from_folders(source_folder, destination_folder):
#     # Проверяем, существует ли папка назначения, и создаем ее, если необходимо
#     if not os.path.exists(destination_folder):
#         os.makedirs(destination_folder)

#     # Перебираем все элементы в исходной папке
#     for root, dirs, files in os.walk(source_folder):
#         for dir_name in dirs:
#             # Проверяем, оканчивается ли имя папки на "gz_extracted"
#             if dir_name.endswith("gz_extracted"):
#                 source_path = os.path.join(root, dir_name)

#                 # Перебираем все файлы внутри этой папки и копируем их в папку назначения
#                 for file_name in os.listdir(source_path):
#                     file_path = os.path.join(source_path, file_name)
#                     destination_path = os.path.join(destination_folder, file_name)
#                     shutil.copy(file_path, destination_path)

# # Замените 'source_folder' и 'destination_folder' на свои реальные пути
# source_folder = r'F:\prf'
# destination_folder = r'F:\prf'

# extract_files_from_folders(source_folder, destination_folder)


# import os

# def remove_profanity_from_filenames(folder_path):
#     # Получаем список файлов в указанной папке
#     files = os.listdir(folder_path)

#     for filename in files:
#         # Проверяем, содержится ли "filter_profanity_" в имени файла
#         if "filter_profanity_" in filename:
#             # Строим новое имя файла, убирая "filter_profanity_"
#             new_filename = filename.replace("filter_profanity_", "")
            
#             # Составляем полные пути к старому и новому файлам
#             old_path = os.path.join(folder_path, filename)
#             new_path = os.path.join(folder_path, new_filename)
            
#             # Переименовываем файл
#             os.rename(old_path, new_path)
            
#             print(f"Файл {filename} переименован в {new_filename}")

# # Укажите путь к папке, в которой нужно удалить "filter_profanity_" из имен файлов
# folder_path = r'F:\prf'
# remove_profanity_from_filenames(folder_path)




# from badwords.image_check import ProfanityFilter

# profanity_filter = ProfanityFilter()

# image_path = 'test_img2.png'

# profanity_found = profanity_filter.filter_profanity_from_image(image_path, language='pl')

# if profanity_found:
#     print("Profanity found in the image.")
# else:
#     print("No profanity found in the image.")


# from PIL import Image
# import pytesseract
# import datetime
# import time

# # Загрузите изображение
# image_path = r'F:\bdw\test_img1.png'
# image = Image.open(image_path).convert('RGB')

# # Начнем замер времени выполнения
# start_time = time.time()

# # Используйте pytesseract для распознавания текста
# text = pytesseract.image_to_string(image)

# # Закончим замер времени выполнения
# end_time = time.time()

# # Выведите результат и время выполнения
# print("Результат распознавания текста:")
# print(text)
# print("Время выполнения: {:.4f} секунд".format(end_time - start_time))


# from badwords.image_check import ProfanityFilter 


# profanity_filter = ProfanityFilter()

# image_path = r'F:\bdw\test_img1.png'

# profanity_found = profanity_filter.filter_profanity_from_image(image_path, language='en')

# if profanity_found:
#     print("Profanity found in the image.")
# else:
#     print("No profanity found in the image.")


# # Вызов функции и вывод результата
# result = is_adult_content(image_path, threshold)
# print('Contains adult content:', result)




# import easyocr
# reader = easyocr.Reader(['en'])
# result = reader.readtext('img.png')
# print(result)  \

# 1. **"Проект с GitHub: Manim"**
#    Представим вам проект Manim, библиотеку для создания анимаций в Python, особенно полезную для образовательных видео. [Ссылка на проект](https://github.com/ManimCommunity/manim).

# 2. **"Интересная библиотека: Typer"**
#    Расскажем о Typer, библиотеке для создания красивых командной строки приложений в Python. [Ссылка на проект](https://github.com/tiangolo/typer).

# 3. **"Приложение для управления зависимостями: Poetry"**
#    Поделимся опытом использования Poetry, инструмента для управления зависимостями и сценариями в Python. [Ссылка на проект](https://github.com/python-poetry/poetry).

# 4. **"Многозадачный менеджер: Huey"**
#    Расскажем о Huey, минималистичном и легковесном менеджере для создания очередей задач и их выполнения в фоне в приложениях Python. [Ссылка на проект](https://github.com/coleifer/huey).

# 5. **"Автоматизация браузера: Pyppeteer"**
#    Представим вам Pyppeteer, библиотеку для автоматизации работы с браузером Chrome (порт Puppeteer) в Python. [Ссылка на проект](https://github.com/pyppeteer/pyppeteer).

# 6. **"Работа с API: HTTPX"**
#    Расскажем о HTTPX, альтернативе requests с поддержкой асинхронных запросов и HTTP/1.1, HTTP/2. [Ссылка на проект](https://github.com/encode/httpx).

# 7. **"Метапрограммирование: Black"**
#    Поделимся опытом использования Black, инструмента для автоматического форматирования кода в Python с уникальным подходом. [Ссылка на проект](https://github.com/psf/black).

# 8. **"Асинхронные веб-фреймворки: FastAPI"**
#    Расскажем о FastAPI, современном веб-фреймворке для Python с поддержкой асинхронного программирования и автоматической генерацией документации. [Ссылка на проект](https://github.com/tiangolo/fastapi).

# 9. **"Библиотека для работы с графами: NetworkX"**
#    Представим вам NetworkX, библиотеку для анализа и визуализации сложных сетей и графов в Python. [Ссылка на проект](https://github.com/networkx/networkx).

# 10. **"Модуль для автоматического тестирования: Hypothesis"**
#     Расскажем о Hypothesis, библиотеке для автоматического тестирования в Python с использованием стратегий и свойств. [Ссылка на проект](https://github.com/HypothesisWorks/hypothesis).
