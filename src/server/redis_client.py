import asyncio

class RedisClient:
    async def connect(self, host, port):
        self.r, self.w = await asyncio.open_connection(host, port)

    async def set(self, key, value):
        self.w.write(f"SET {key} {value}\r\n".encode())
        await self.w.drain()
        return await self._read_reply() 

    async def get(self, key):
        self.w.write(f"GET {key}\r\n".encode())

    
    async def _read_reply(self):
        tag = await self.r.read(1)

        if tag == b'+':
            result = b''
            characters = b''
            while characters != b'\n':
                characters = await self.r.read(1)
                result += characters
            return result[:-1].decode()
        else:
            msg = await self.r.read(100)
            raise Exception(f"Unknow tag: {tag}, msg: {msg}")


async def main():
    print("Hello asyncio!")
    client = RedisClient()
    await client.connect("localhost", 6379)
    print(await client.set("s", "hello"))

if __name__ == "__main__":
    asyncio.run(main())
