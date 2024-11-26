# Модель

## Общая информация

Работа с данными книг реализована с помощью файла **models.py**. В нем реализован основной **API** для взаимодействия с данными книг и хранилищем данных книг. В файле реализован лишь один класс, описывающий отдельно взятую книгу: **Book**. Хранение данных модели реализовано с помощью **.json** файла, название которого можно указать в глобальном поле **file_name** класса **Book**.

## Основные моменты
### Поля класса

Класс содержит только 2 глобальных поля - **pk** и **filename** с модификатором **private**:
- **pk** определяет идентификатор, присваивающийся следующему добавленному объекту книги.
- **filename** определяет название файла, который хранит в себе данные книг.
### Инициализатор

Инициализатор имеет в себе 1 интересную вещь: параметры вида ключ-значение, следующие после параметра **deserializing**, они нужны при загрузке данных из файла хранилища:

- **deserializing** - булево значение, которое определяет, происходит ли десериализация или это просто создание объекта книги
- **id** - идентификатор десериализуемого объекта
- **status** - статус десериализуемого объекта

При инициализации метод __init__ по сути просто решает, происходит ли создание объекта модели в процессе сериализации или это просто создание нового объекта модели.
### Геттер книги

Метод **get_by_id** извлекает объект книги из хранилища по переданному методу идентификатору. Возвращает объект класса **Book**.
### Сериализация/десериализация

Сериализация/десериализация производится методами: **get_serialized**, **deserialize**, **deserialize_object**:

- **get_serialized** вызывается локально для объекта класса. Возвращает сериализованные данные объекта, для которого метод был вызван
- **deserialize** по сути производит выборку из хранилища, десериализуя каждую запись о книге. Принимает на вход **filter_data** - данные для фильтрации тех объектов, значения которых были указаны при выборке; если он пуст, значит возвращаются все записи из хранилища. Возвращает список объектов класса **Book**
- **deserialize_object** десериализует конкретную запись, возвращая объект класса **Book**.
### Инициализация файла хранилища

Метод **initialize** вызывается при каждому запуске программы. Метод нужен для создания файла хранилища, если вдруг он ещё не создан, и установления значения поля **pk**.
### CRUD методы

API модели предоставляет самые типичные CRUD операции:

- **save()** - сохраняет объект класса в хранилище(**CREATE**)
- **list_objects()** - перечисляет все объекты из хранилища по определенному фильтру(**READ**) 
- **delete()** - удаляет объект класса из хранилища(**DELETE**)

# Исполнители
## Общая информация

Для исполнения всех необходимых пользователю действий отдельно используется файл **executors.py**. Можно сказать, исполнители - некая прослойка между пользователем и **CRUD** интерфейсом. В целом, так как операции относительно простые, функции просто используют уже реализованные методы класса, кроме функции **change_status**(id): эта функция меняет статус книги и сохраняет изменения в хранилище.

# Роутеры и хендлеры
## Общая информация

Распознавание комманд и оперирование вводом пользователя берут на себя 2 файла: **routers.py** и **handlers.py**. Файл роутеров, по сути, просто, в зависимости от введенной команды, направляет пользователя на различных хендлеры, где пользователь получает интерфейс для работы с **API** модели.

## Обработка ввода

Все, что происходит в хэндлерах - это ввод данных, преобразование их в удобный для функций-исполнителей вид и делегирование работы на функции-исполнители. Происходит строгое разграничение между хэндлерами и исполнителями, чтобы хэндлер не работал с **CRUD** модели напрямую.

# Точка входа

## Общая информация

В точке входа происходит инициализация модели Book, предоставляется ввод команды и происходит перенаправление введенной команды на файл роутеров. А также в самом начале в переменной **ALLOWED_COMMAND_LIST** прописывается список разрешенных команд.