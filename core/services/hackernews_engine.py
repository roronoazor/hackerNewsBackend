from django.db import transaction
import requests
import asyncio
from timeit import default_timer
from concurrent.futures import ThreadPoolExecutor
from core.models import Item
from timeit import default_timer
from asgiref.sync import sync_to_async

"""
    This class is to be responsible for all communication
    between the server and hackerNews api
"""

HACKER_NEWS_BASE_URL = 'https://hacker-news.firebaseio.com'
MAX_ITEM_URL = '/v0/maxitem.json?print=pretty'


class HackerNewsEngine:
    
    def __init__(self, *args, **kwargs):
        self.base_url = HACKER_NEWS_BASE_URL
        self.pipeline_data = []
        
    def request_item(self, request_obj, id):
        url = f"{self.base_url}/v0/item/{id}.json?print=pretty"
        with request_obj.get(url) as response:
            data = response.json()

            if response.status_code != 200:
                print("FAILURE::{0}".format(url))

            elapsed_time = default_timer() - self.start_time
            completed_at = "{:5.2f}s".format(elapsed_time)
            print("{0:<30} {1:>20}".format(id, completed_at))
            return data
            
        
    async def start_hackernews_sync(self, last_item_id):
        # asynchronous process to make api calls for speed 
        # get the highest reference id in the db
        # get the max id from the hacker news site
        # find the offset between the 2, those are the id we need to sync
        
        with requests.get(self.base_url + MAX_ITEM_URL) as response:
            max_item_id = int(response.text)
        
        # a list to hold all the items fetched from the db
        items_list = []
        self.start_time = default_timer()
            
        # offset to synchronize
        synchronize_offset = max_item_id - last_item_id  if ((max_item_id - last_item_id) > 0 and (max_item_id - last_item_id) < 5000)   else 5000
        synchronize_offset = 500
            
        with ThreadPoolExecutor(max_workers=10) as executor:
            with requests.Session() as session:
                loop = asyncio.get_event_loop()
                tasks = [
                    loop.run_in_executor(
                        executor,
                        self.request_item,
                        *(session,i)
                    )
                    for i in range(last_item_id, (last_item_id + synchronize_offset))
                ]
                for response in await asyncio.gather(*tasks):
                    print(response)
                    items_list.append(response)
        
        self.pipeline_data = items_list
        
    def persist_data(self):
        Item.objects.bulk_create(list(map(
            lambda data: Item(reference_id=data.get("id"), **data),
            self.pipeline_data
        )), 
        1000, # batch size 
        ignore_conflicts=True
        )
        
    @transaction.atomic
    def run(self, **kwargs):
        """
        Run fetching and saving services as a pipeline (synchronization)
        """
        last_item_from_hackernews = Item.objects.filter(reference_id__isnull=False).order_by('-reference_id').first()
        last_item_id = last_item_from_hackernews.reference_id if last_item_from_hackernews else 1
        
        
        # loop = asyncio.get_event_loop()
        # future = asyncio.ensure_future(self.start_hackernews_sync(last_item_id))
        # loop.run_until_complete(future)
        # loop.close()
        
        asyncio.run(self.start_hackernews_sync(last_item_id))
        
        self.persist_data()




