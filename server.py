import asyncio
import quart
from hypercorn.config import Config
from hypercorn.asyncio import serve
from quart import Quart
from quart import request
import parsing
import datafetcher

config = Config()
app = Quart('server')


# Need an endpoint for ghost downloads, for leaderboards, and for ghost uploads
@app.route("/Leaderboards", methods=['GET'])
async def leaderboardRequest():
    requestBody = await request.data  # raw request data received by the server
    parameters = await parsing.parseLeaderboardRequest(requestBody)  # should return a list or a dict of parameters
    leaderboard = await cache.getLeaderboard(parameters)  # this function grabs the latest cached version of the leaderboard which is already converted to XML format
    return leaderboard


config.bind = ["localhost:8080"]
loop = asyncio.get_event_loop()
loop.create_task(datafetcher.updateCache(300))  # cache will update every 300 seconds or 5 minutes
loop.create_task(serve(app, config))
loop.run_forever()
