import requests
import json
from pymongo import MongoClient
from flask import abort


class DbService(object):
    def __init__(self):
        self.conn_addr = ''
        self.__mongo_client, self.conn_addr = self.__connect_to_mongo_db()

    def __connect_to_mongo_db(self):
        available_dbs = DbService.__get_available_db_services()

        not_used_dbs = list(filter(lambda o: o['Address'] != self.conn_addr.split(':')[0],
                                   available_dbs))

        if len(not_used_dbs) == 0:
            abort(503)

        db = not_used_dbs[0]
        addr, port = db['Address'], db['ServicePort']

        return MongoClient(host=addr, port=port,
                           connectTimeoutMS=1000,
                           serverSelectionTimeoutMS=5000), \
               '{}:{}'.format(addr, port)

    @staticmethod
    def __get_available_db_services():
        return json.loads(
            requests.get('http://localhost:8500/v1/catalog/service/mongodb?passing').text
        )

    def get_books(self):
        return self.get_mongo_client()['bookstore']['books']

    def get_mongo_client(self):
        return self.__mongo_client


# --------------------------------------------------------------------------------------------


class Paging(object):
    values = None

    @staticmethod
    def calculate_number_of_pages(cnt):
        return cnt // 10 + int(cnt % 10 != 0)

    @staticmethod
    def init_paging_obj(db_service):
        if Paging.values is None:
            cnt = db_service.get_books().count()
            last = Paging.calculate_number_of_pages(cnt)
            Paging.values = {
                'curr_page': 1,
                'last_page': last,
                'range': 5,
            }

    @staticmethod
    def set_curr_page(p):
        Paging.values['curr_page'] = p


# --------------------------------------------------------------------------------------------
