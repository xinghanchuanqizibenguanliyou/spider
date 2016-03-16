import aiohttp
import asyncio
import config
import processData as pd


@asyncio.coroutine
def fetchData(url):
    #set request url and parameters here or you can pass from outside.
    
    
    conn = aiohttp.TCPConnector(limit=config.REQ_AMOUT)    
    s = aiohttp.ClientSession(headers = config.HEARDERS, connector=conn)
    #use s.** request a webside will keep-alive the connection automaticaly,
    #so you can set multi request here without close the connection 
    #while in the same domain.
    #i.e. 
    #await s.get('***/page1')
    #await s.get('***/page2')
    ########################################################################
    async with s.get(url) as r:
        #here the conection closed automaticly.
        data = await r.text()
        return await pd.processData(data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    #coroutine in tasks will run 
    tasks = [
        fetchData(),
        fetchData(),
        fetchData()
    ]    
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


