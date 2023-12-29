# Credit scoring package

## Общая информация

Данный проект представляет собой пакет Python, предназначенный для работы с данными, связанный с кампаниями прямого маркетинга (телефонными звонками) португальского банковского учреждения и используется для предсказания вероятности дефолта клиента в этом банке.

## Структура кода 
### Configs

Параметры модели задаются через configs. Конфиги представлены файлами yaml. Ценности для параметров можно установить в файле `credit_scoring_model/config.yml`. Configs анализируются и проверяются в `credit_scoring_model/config/core.py` модуль, использующий библиотеку [StrictYaml](https://github.com/crdoconnor/strictyaml) для разбора и [Pydantic](https://pydantic-docs.helpmanual.io/) для проверки типов значений. 

## Настройка пайплайна и обучение

Pipeline установлен в credit_scoring_model/pipeline.py файл. Обучение проходит в файле `credit_scoring_model/train_pipeline.py`. Все этапы обработки данных выполняются в [Scikit-learn](https://scikit-learn.org/stable/), включая пользовательские преобразования, хранящиеся в файле `credit_scoring_model/processing/features.py`. 


### Как делать прогнозы

Код для предсказания устанавливается из файла `credit_scoring_model/predict.py`. Перед каждым предсказанием производится проверка входных данных. Код для проверки можно найти в файле `credit_scoring_model/processing/validation.py`. 


## Как запустить код 

Код можно запустить с помощью инструмента [Tox](https://pypi.org/project/tox/). Tox — это удобный способ автоматической настройки среды и путей Python и запуска необходимых команд из командной строки. Файл с описанием tox можно найти в файле `tox.ini`. Следующие команды можно запустить из командной строки используя Tox:

* Запустить обучение: сначала создайте каталог для сохранения моделей, если такового нет `mkdir ./credit_scoring_model/trained_models`, а затем запустите `tox -e train`
* Запустить тестирование (через [pytest](https://docs.pytest.org/en/6.2.x/)): `tox -e test_package`
* Запустить проверку типов (через [mypy](https://mypy.readthedocs.io/en/stable/)): `tox -e typechecks`
* Запустить проверку стиля (через [black](https://github.com/psf/black), [isort](https://github.com/PyCQA/isort), [mypy](https://mypy.readthedocs.io/en/stable/)
и [flake8](https://pypi.org/project/flake8/)): `tox -e stylechecks`

## Описание признаков
Общие атрибуты: 1-8; последний контакт с банком: 9-12; другие атрибуты: 13-16; таргет: 17
1) age (numeric)
2) job : тип работы (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur","student", "blue-collar","self employed","retired","technician","services")
3) marital : семейное положение (categorical: "married","divorced","single"; примечание: "divorced" означает разведенный или овдовевший)
4) education : образование (categorical: "unknown","secondary","primary","tertiary")
5) default : есть ли дефолт по кредиту (binary: "yes","no")
6) balance : среднегодовой баланс, в евро (numeric)
7) housing : есть ли жилищный кредит (binary: "yes","no")
8) loan : есть ли личный заем (binary: "yes","no")
9) contact : тип контактной связи (categorical: "unknown","telephone","cellular")
10) day : последний контактный день месяца (numeric)
11) month : месяц последнего контакта в году (categorical: "jan", "feb", "mar", ..., "nov", "dec")
12) duration : продолжительность последнего контакта, в секундах (numeric)
13) campaign : количество контактов, осуществленных в ходе данной кампании и для данного клиента (numeric, включает последний контакт)
14) pdays : количество дней, прошедших с момента последнего обращения к клиенту в рамках предыдущей кампании (numeric, -1 означает, что с клиентом ранее не связывались)
15) previous : количество контактов, осуществленных до начала данной кампании и для данного клиента (numeric)
16) poutcome : результат предыдущей маркетинговой кампании (categorical: "unknown","other","failure","success")
17) y : был ли одобрен кредит (binary: "yes","no")

## Соответствия исходных значений кодам
1) age: положительные числа - 20, 27, 40
2) job:
'admin.': 0,
'blue-collar': 1,
'entrepreneur': 2,
'housemaid': 3,
'management': 4,
'retired': 5,
'self-employed': 6,
'services': 7,
'student': 8,
'technician': 9,
'unemployed': 10,
'unknown': 11},
3) marital:'divorced': 0, 'married': 1, 'single': 2
4) education: 'primary': 0, 'secondary': 1, 'tertiary': 2, 'unknown': 3
5) default: 'no': 0, 'yes': 1
6) housing': 'no': 0, 'yes': 1
7) loan: 'no': 0, 'yes': 1
8) contact: 'cellular': 0, 'telephone': 1, 'unknown': 2
9) day: от 1 до 30 в зависимости от месяца
10) month:
'apr': 0,
'aug': 1,
'dec': 2,
'feb': 3,
'jan': 4,
'jul': 5,
'jun': 6,
'mar': 7,
'may': 8,
'nov': 9,
'oct': 10,
'sep': 11},
11) duration: положительные числа - 261, 302, 563
12) campaign: положительные числа - 1, 6, 10
13) pdays: положительные числа - 1, 2, 4 и отрицательное -1
14) previous: положительные числа - 2, 5, 6
15) poutcome:
'failure': 0,
'other': 1,
'success': 2,
'unknown': 3
16) y: 'no': 0, 'yes': 1

## Как установить пакет

Для установки пакета запустите 

```
pip install pandas
pip install credit-scoring-model
```

После этого вы можете делать прогнозы, используя пакет: 

```
from credit_scoring_model.predict import make_prediction
import pandas as pd

# Пример входных данных
input_dict = {'age': [20], 'job': [8], 'marital': [2], 'education': [1], 'default': [0], 
              'balance': [502], 'housing': [0], 'loan': [0], 'contact': [0], 'day': [30], 
              'month': [0], 'duration': [261], 'campaign': [1], 'pdays': [-1], 'previous': [0],
              'poutcome': [3]}

input_dict = pd.DataFrame(input_dict)

result = make_prediction(input_data=input_dict)

print(result)
```
