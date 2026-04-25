import requests
from bs4 import BeautifulSoup

task_id_ = 121
def all_info(task_id):
    url_math = f"https://oge.sdamgia.ru/problem?id={task_id}"
    response = requests.get(url_math)
    soup = BeautifulSoup(response.text, 'html.parser')
    task_block = soup.find('div', class_='pbody')
    if task_block is None:
        return f"❌ Задание с номером {task_id} не найдено. Проверь структуру страницы.\n"
    elif task_block.find('img'):
        return f'{task_id} имеет изображение в себе. \n'
    else:
        tipe_task = soup.find('span', class_='prob_nums')
        type_ = tipe_task.text.split()[0]+ ' ' + tipe_task.text.split()[1] + f'. Тип задания: {task_id}.'
        p_task = task_block.find_all('p')
        task = "Задание:"
        all_task = ''
        for i in p_task:
            all_task += i.get_text().replace('\u00ad', '').replace('&nbsp;', '').replace('\xa0', ' ')
            all_task += '\n'
        ans = "Решение:"
        ans_block = soup.find('div', class_='prob_maindiv')
        ans_block = ans_block.find_all('div', class_='pbody')
        all_ans = ans_block[1].text.replace('\u00ad', '').replace('Решение. ', '').replace('&nbsp;', '').replace('\xa0', ' ')
        return type_ +'\n' + task + '\n'+ all_task + ans  + '\n' + all_ans + '\n'

for i in range(10000):
    with open('tasts.txt', 'a', encoding='utf-8') as f:
        f.write(all_info(i))
        f.write('\n-----------------------------------------------------------------------------------------------------------------')
        f.write('\n')
    print(f'\rОбработано {round(((i+1)/10000)*100, 4) }% заданий', end = '')


