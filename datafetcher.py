import asyncio
import aiofiles
import aiohttp
import parsing
import mkleaderboards

mkl_course = {49: 8, 50: 1, 51: 2, 52: 4, 53: 0, 54: 5, 55: 6, 56: 7, 57: 9, 58: 15, 60: 3, 59: 11, 62: 10, 61: 14, 63: 12, 64: 13, 65: 16, 66: 20, 67: 25, 68: 26, 69: 27, 70: 31, 71: 23, 72: 18, 73: 21, 74: 30, 75: 29, 76: 17, 77: 24, 78: 22, 79: 19, 80: 28}

async def updateCache(region):
    for i in range(49, 81):
        leaderboard = await mkleaderboards.requestLeaderboard(i, region)
        parsedLeaderboard = await parsing.parseLeaderboard(leaderboard)
        async with aiofiles.open(f'cache/{region}/{str(mkl_course[i])}.bin', 'wb') as f:
            await f.write(parsedLeaderboard)
            await f.close()
async def run():
    await updateCache("world")
    await updateCache("americas")
    await updateCache("europe")
    await updateCache("asia")
    await updateCache("oceania")
    await asyncio.sleep(300)

while True:
    asyncio.run(run())
