import asyncio
import websockets

# Зберігаємо список підключених клієнтів
connected_clients = set()

async def handle_connection(websocket, path):
    # Додаємо нового клієнта до списку
    connected_clients.add(websocket)
    print("Новий користувач підключився!")
    
    try:
        # Читаємо повідомлення від клієнта
        async for message in websocket:
            print(f"Отримано повідомлення: {message}")
            # Пересилаємо повідомлення всім підключеним клієнтам
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.ConnectionClosed:
        print("Клієнт відключився.")
    finally:
        # Видаляємо клієнта зі списку
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(handle_connection, "0.0.0.0", 8080)
    print("WebSocket сервер запущений на Jonny104.pythonanywhere.com:8080")
    await server.wait_closed()
    
# Запуск основного циклу подій
if __name__ == "__main__":
    asyncio.run(main())
