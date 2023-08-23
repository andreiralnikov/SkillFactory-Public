# SkillFactory
Задание 28.1

Итоговый проект по автоматизации тестирования на курсе QAP в Skillfactory.

Разработать тест-кейсы (не менее 20). Необходимо применить несколько техник тест-дизайна.
Провести обеспеченность тестированием продукта (не менее 20 автотестов).
Оформить описание обнаруженных дефектов. Если дефекты не обнаружены, подумайте и опишите 3 потенциальных дефекта на специализированном ресурсе.

1. Протестированы тербования заказчика, согласно требованиям. 
Требования к тестированию оформлены в виде комментариев в документе по ссылке ниже:
https://docs.google.com/document/d/1bBwogeH-AHdSQj9nsnhO5XvoXC7uvUuK/edit?usp=sharing&ouid=103582970268699073971&rtpof=true&sd=true
2. Разработаны тест-кейсы и обозначены потенциальные баги.
3. Для разработки тест-кейсов были применены следующие техники тест-дизайна: 
- эквивалентное разбиение, 
- анализ граничных значений, 
- таблица принятия решений, 
- диаграмма перехода состояния https://drive.google.com/file/d/1pIseoud6YExoE6NeKPZO8W7_w5yj2PJa/view?usp=share_link
- попарное тестирование (Pairwise) https://drive.google.com/file/d/16IMuoCMtoRIAuYCwSJBBxnz5dOiKTr7m/view?usp=share_link
4. Тест-кейсы оформлены в Google-таблице: https://docs.google.com/spreadsheets/d/14CWfiHra800ketr1XOSLcalC3GG8GhEh/edit?usp=share_link&ouid=103582970268699073971&rtpof=true&sd=true
5. Написаны автотесты.
6. Для тестирования сайта был использован инструмент Selenium.
7. Для определения локаторов были применены: Element Locator, DevTools.
8. Для разработки автотестов, были дополнительно установлены библиотеки: selenium (4.7.2), pytest(7.2.0), pytest-selenium(4.0.0).

Для запуска тестов необходимо:
1) Установить все требования: pip install -r requirements.txt
2) Загрузить Selenium WebDriver с https://chromedriver.chromium.org/downloads (версия драйвера должна быть совместима с версией браузера)
3) Запустить тест: python -m pytest -v --driver Chrome --driver-path /tests/chromedriver.exe tests/test_rostelekom.py