import asyncio

async def getLeaderboard(parameters): # searches the directory "Cache" based on the parameters for the right leaderboard to return
    filePath = f"cache/{parameters['region']}/{parameters['track']}.xml"
    with open(filePath, 'rb') as leaderboard: # makes sure that the file handle gets closed
        return leaderboard.read()


