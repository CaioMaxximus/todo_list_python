import asyncio

async def minha_tarefa_assincrona():
    print("Executando minha tarefa assíncrona...")
    await asyncio.sleep(5)  # Simulando uma tarefa demorada

async def run_schedules():
    while True:
        await minha_tarefa_assincrona()
        print("laco2")

async def main():
    task1 = asyncio.create_task(run_schedules())
    # await task1  # Aguarda a conclusão da tarefa run_schedules

    while True:
        await asyncio.sleep(3)
        print("laco1")


# Executando o loop principal
asyncio.run(main())
