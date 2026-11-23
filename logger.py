from datetime import datetime


class Logger:
    def __init__(self,log_path):
        self.log_path = log_path

    def log(self,file,is_correct,filter):
        with open(self.log_path, 'a') as f:
            current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status = "Успешно" if is_correct else "Ошибка Доступа"
            f.write(f"{current_date_time} Файл: {file} | Фильтр: {filter} | Статус: {status} \n")

