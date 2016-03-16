import asyncio
import pyquery

if config.MYSQL:
    import aiomysqlS

@asyncio.coroutine
def processData(data):
    '''
    data is from the http response in main module.
    '''
    pass

if __name__ == '__main__':
    processData('<a>hello</a>')