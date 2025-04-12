# Система управления контрактами

**Система управления контрактами** — это веб-приложение на базе Django, предназначенное для управления контрактами, платежами и связанными документами. Оно позволяет пользователям создавать, редактировать и удалять контракты, отслеживать платежные документы и поручения, управлять лимитами бюджета (КБК/КОСГУ) и экспортировать данные в Excel. Система поддерживает аутентификацию пользователей и предоставляет удобный интерфейс.

## Возможности

- **Управление контрактами**:
  - Создание, редактирование и удаление контрактов.
  - Прикрепление файлов контрактов и дополнительных соглашений.
  - Просмотр детальной информации о контракте, включая суммы, платежи и остатки.
- **Учет платежей**:
  - Добавление и управление платежными документами и поручениями.
  - Отслеживание выставленных и оплаченных сумм по каждому контракту.
- **Лимиты бюджета (КБК/КОСГУ)**:
  - Управление лимитами бюджета по кодам КБК и КОСГУ.
  - Мониторинг законтрактованных сумм и остатков.
- **Журнал и отчеты**:
  - Просмотр журнала зарегистрированных контрактов.
  - Экспорт данных контрактов в Excel.
- **Аутентификация пользователей**:
  - Безопасный вход и выход из системы.
  - Доступ на основе ролей (авторизованные пользователи могут добавлять/редактировать записи).
- **Интуитивный интерфейс**:
  - Удобное меню навигации.
  - Поддержка загрузки файлов (контракты, платежи, соглашения).

## Технологический стек

- **Бэкенд**: Django 5.0, Python 3.x
- **База данных**: PostgreSQL (настраивается через переменные окружения)
- **Фронтенд**: HTML, CSS, JavaScript, шаблоны Django
- **Статические файлы**: Пользовательский CSS (`style.min.css`)
- **Зависимости**: Управляются через `requirements.txt`

## Установка

Следуйте этим шагам для локальной установки проекта:

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/evlx87/contract_control.git
cd contract_control
```

### 2. Создайте виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```

### 3. Установите зависимости
```bash
pip install -r requirements.txt
```

### 4. Настройте переменные окружения
Скопируйте файл env.sample в .env и заполните его:
```bash
cp env.sample .env
```
Отредактируйте .env с вашими настройками:
```bash
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_NAME=contract_control
DB_PORT=5432
ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_SECRET_KEY=your-secure-secret-key
```
Сгенерируйте безопасный `DJANGO_SECRET_KEY` с помощью функции `django.core.management.utils.get_random_secret_key()`.

### 5. Примените миграции базы данных
```bash
python manage.py migrate
```

### 6. Создайте суперпользователя
```bash
python manage.py createsuperuser
```
### 7. Заполните справочные данные (опционально)
Выполните команды для заполнения таблиц (например, КБК, КОСГУ, типы контрактов):
```bash
python manage.py fill_contract_lib
python manage.py fill_kbk_kosgu
```
### 8. Запустите сервер разработки
```bash
python manage.py runserver
```
По умолчанию приложение доступно по адресу http://127.0.0.1:8000.

## Использование
### Вход в систему:
Перейдите на `/registration/login/` и войдите с вашими учетными данными.
Суперпользователи могут получить доступ к админ-панели по адресу `/admin/`.
### Главная страница:
Домашняя страница (`/`) содержит ссылки на контракты, закупки, журнал и лимиты.
### Контракты:
Просмотр всех контрактов: `/contracts/purchases_list/`.
Добавление нового контракта: `/contracts/add_contract/`.
Редактирование или удаление через страницу деталей: `/contracts/contract-detail/<id>/`.
### Платежи:
Добавление платежных документов или поручений со страницы деталей контракта.
Загрузка файлов (например, PDF) для контрактов, платежей и соглашений.
### Лимиты:
Управление лимитами: `/limits/limits_list/`.
Просмотр контрактов по КБК/КОСГУ: `/limits/card_limit/<kbk>/<kosgu>/<year>/`.
### Экспорт:
Экспорт данных контрактов в Excel из `/contracts/journal_list/` с помощью кнопки "Экспорт в Excel".

```text
contract_control/
├── config/                 # Настройки проекта Django
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── contracts/              # Основное приложение для управления контрактами
│   ├── templates/contracts/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
├── limits/                 # Приложение для управления лимитами
│   ├── templates/limits/
│   ├── forms.py
│   ├── models.py
│   ├── views.py
├── lib_ccportal/           # Утилитарное приложение для справочных данных
│   ├── management/commands/
│   ├── models.py
├── users/                  # Приложение для аутентификации пользователей
│   ├── templates/registration/
│   ├── models.py
│   ├── views.py
├── static/                 # Статические файлы (CSS)
├── media/                  # Загруженные файлы (контракты, платежи)
├── env.sample              # Шаблон переменных окружения
├── manage.py               # Скрипт управления Django
├── README.md               # Документация проекта
```

## Модели
### Contract (contracts.models.Contract):
- Поля: `contract_number`, `supplier`, `contract_amount`, `contract_file` и др.
- Связи: Внешние ключи к `PurchaseType`, `ContractType`, `KBK`, `KOSGU`.
### PaymentDocument (contracts.models.PaymentDocument):
- Учет платежных документов, связанных с контрактами.
### PaymentOrder (contracts.models.PaymentOrder):
- Управление платежными поручениями с суммами и файлами.
### AdditionalAgreement (contracts.models.AdditionalAgreement):
- Хранение дополнительных соглашений к контрактам.
### Limit (limits.models.Limit):
- Управление лимитами бюджета по КБК, КОСГУ и году.
### User (users.models.User):
- Пользовательская модель, расширяющая `AbstractUser`.

## Внесение изменений
Мы приветствуем любые улучшения! Чтобы внести вклад:
- Сделайте форк репозитория.
- Создайте новую ветку (`git checkout -b feature/your-feature`).
- Внесите изменения и зафиксируйте их (`git commit -m "Добавлена новая функция"`).
- Отправьте ветку в репозиторий (`git push origin feature/your-feature`).
- Создайте Pull Request.

Пожалуйста, добавляйте тесты для новых функций и следуйте стандартам PEP 8.

## Тестирование
В настоящее время тесты отсутствуют. Для их добавления:
- Создайте тесты в файлах `contracts/tests.py`, `limits/tests.py` и др.
- Запустите тесты командой:
```bash
python manage.py test
```

Пример теста для модели Contract:
```python
from django.test import TestCase
from contracts.models import Contract

class ContractModelTest(TestCase):
    def test_contract_str(self):
        contract = Contract.objects.create(
            contract_number="123",
            supplier="Тестовый поставщик",
            contract_amount=1000.00
        )
        self.assertEqual(str(contract), "123")
```
Лицензия
Проект распространяется под лицензией `GNU General Public License v3.0`. 
Подробности см. в файле [LICENSE](https://github.com/evlx87/contract_control/blob/main/LICENSE).