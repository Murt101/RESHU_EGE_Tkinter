import asyncio, time, how_many_tasks_universal as tasks

async def fetch_data(delay, name):
    await asyncio.sleep(delay)  # имитация I/O-операции
    print(f"Загружено {name}")
    return f"Данные из {name}"

async def main():
    tasks_ = []
    results = []
    for i in range(500):
        print(i)
        tasks_.append(asyncio.create_task(tasks.gat_tasks(i*2000, (i*2000)+2000, i)))
    for result in tasks_:
        print(await result)

asyncio.run(main())
