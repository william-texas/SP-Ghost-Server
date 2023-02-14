import asyncio
import aiohttp

API_URL = "https://www.mkleaderboards.com/api/charts/mkw_nonsc_"
async def requestLeaderboard(track, region):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{API_URL}{region}/{track}') as res:
            leaderboard = await res.json()

    return leaderboard

