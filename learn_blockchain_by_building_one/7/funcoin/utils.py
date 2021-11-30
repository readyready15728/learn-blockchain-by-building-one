import aiohttp
import structlog

logger = structlog.getLogger(__name__)

async def get_external_ip():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://ipinfo.io', headers={'User-Agent': 'curl/7.68.0'}) as response:
            response_json = await response.json(content_type=None)
            ip = response_json['ip']
            logger.info(f'Found external IP: {ip}')
            return ip
