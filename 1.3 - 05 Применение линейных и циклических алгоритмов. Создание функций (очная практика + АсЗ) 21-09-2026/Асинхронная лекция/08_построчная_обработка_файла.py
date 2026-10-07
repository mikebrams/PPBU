def analise_log(file_name):
    counter = {'INFO': 0, 'ERROR': 0, 'WARNING': 0}
    try:
        with open(file_name, encoding='utf-8') as file:
            for line in file:
                if "[INFO]" in line:
                    counter['INFO'] += 1
                elif "[ERROR]" in line:
                    counter['ERROR'] += 1
                elif "[WARNING]" in line:
                    counter['WARNING'] += 1
        for k, v in counter.items():
            print(f'{k}: {v}')


    except FileNotFoundError:
        print(f'Файл {file_name} не найден')
    except Exception as e:
        print(f'Неизвестная ошибка: {e}')

analise_log('log_file.txt')