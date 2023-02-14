import asyncio

leaderboard = [] #global variable that gets set by datafetcher.py once it finishes fetching data, should be a nested dict with region, then track

async def setLeaderboards(leaderboards):
    leaderboard = leaderboards
async def getLeaderboard(parameters): # searches the directory "Cache" based on the parameters for the right leaderboard to return
    region = parameters['region']
    track = parameters['track']
    return leaderboard[region][track]


