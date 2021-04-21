# Veeam-Software_Junior-Developer-in-QA

Тестовые решения на задачи из [блока](https://github.com/fattybobcat/Veeam-Software_Junior-Developer-in-QA/blob/main/QA%20Automation%20Engineer%20(update%202020-03-15).docx):
* Задача 1 - [task_1.py](https://github.com/fattybobcat/Veeam-Software_Junior-Developer-in-QA/blob/main/task_1.py);
* Задача 2 - [task_2.py](https://github.com/fattybobcat/Veeam-Software_Junior-Developer-in-QA/blob/main/task_2.py).


## task_1.py
Представлен в виде функции. В качестве входного аргумента функции указываем конфигурационного файла. 
Перед запуском функции, мы должны быть в дериктории с конфигурационным файлом
Если кофигурационный файл отсутствует - выведится list с ошибкой об отсутствии файла. 

Если отсутствуют файлы для копирования - выведится list c ошибками об отсутствии файлов для копирования.

Если все в порядке - выведится list со значением "Copy completed successfully "


## task_2.py
Пример запуска в консоли:
`python task_2.py "C:\project_python\test_task\test_2_ex.txt" "C:\project_python\test_task\test"`

При вызове программы - на вход требуется 2 агрумента. При несовпадении количества аргументов: выведится ошибка в консоли о не совпадении количества аргументов.

Если не дан файл, содержащий имена файлов, алгоритм хэширования - выведится ошибка.

При успешном запуске - будет выводится информация о проверке целостности файлов

```(пример)
file_01.bin OK
file_02.bin FAIL
file_03.bin NOT FOUND
file_04.txt OK
```
