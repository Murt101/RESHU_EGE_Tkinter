import requests, asyncio
from bs4 import BeautifulSoup

task_id_ = 0


async def gat_tasks(start_id, end_id: int, p):
    st = start_id
    start = False
    non_task = ['ЗаданияТакого', 'задания', 'не', 'существует.']
    ans = []
    while start_id != end_id:
        print(f'{p} :)')
        url_math = f"https://oge.sdamgia.ru/problem?id={start_id}"

        response = requests.get(url_math)

        soup = BeautifulSoup(response.text, 'html.parser')
        req = soup.find('div', class_='sgia-main-content').text.split()[:4]

        if req == non_task and start == False:
            pass
        elif req != non_task and start == False:
            ans.append(f'Начинается с задания: {start_id}')
            start = True
        elif req == non_task and start == True:
            ans.append(f"Заканчивается на задании: {start_id}")
            #if task_id == :
            start = False
        start_id += 1
    if ans:
        return ans
    else:
        return f'Ничего в пределе не было с {st} по {end_id}]'


if __name__ == '__main__':
    gat_tasks(1,1)