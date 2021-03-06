import aiohttp
import asyncio
import config
import processData as pd

async def fetchData(url, callback = pd.processData, params=None):
    #set request url and parameters here or you can pass from outside.
    
    
    conn = aiohttp.TCPConnector(limit=config.REQ_AMOUNTS)    
    s = aiohttp.ClientSession(headers = config.HEADERS, connector=conn)
    #use s.** request a webside will keep-alive the connection automaticaly,
    #so you can set multi request here without close the connection 
    #while in the same domain.
    #i.e. 
    #await s.get('***/page1')
    #await s.get('***/page2')
    ########################################################################
    async with s.get(url, params = params) as r:
        #here the conection closed automaticly.
        data = await r.text()
        return await callback(data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    #coroutine in tasks will run 
    calendar_url= 'http://ec.cn.forexprostools.com/?ecoDayFontColor=%23c5c5c5&amp;ecoDayBackground=%23ffffff&amp;innerBorderColor=%23edeaea&amp;borderColor=%23edeaea&amp;columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&amp;category=_employment,_economicActivity,_inflation,_credit,_centralBanks,_confidenceIndex,_balance,_Bonds&amp;importance=1,2,3&amp;features=datepicker,timezone,timeselector,filters&amp;countries=29,25,54,145,34,163,32,70,6,27,37,122,15,113,107,55,24,121,59,89,72,71,22,17,51,39,93,106,14,48,33,23,10,35,92,57,94,97,68,96,103,111,42,109,188,7,105,172,21,43,20,60,87,44,193,125,45,53,38,170,100,56,80,52,36,90,112,110,11,26,162,9,12,46,85,41,202,63,123,61,143,4,5,138,178,84,75&amp;calType=week&amp;timeZone=28&amp;lang=1'
    tasks = [
        fetchData('http://www.xm.com', pd.Xm),
        fetchData('http://biz.aetoscg.com/content/get-ratio!callback.json?ln=0&group=TOOL&callback=showToolsLAS&_=1458550863266', pd.Asto),
        fetchData(calendar_url, pd.Calendar)
    ]    
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close() 