import requests
import json


class Host:

    def __init__(self, url):
        self.url = url
        

    def get_all(self):
        response = requests.get(self.url + 'todo/all')
        if response.status_code == 200:
            return print(json.loads(response.text))
        raise Exception('Server offline')
    
    def create(self):
        data_create = {
    'title': str(input('Введите имя: ')),
    'is_done': bool(input('Введите статус True или False: '))
    }
        response = requests.post(self.url + 'todo/create', data=json.dumps(data_create))
        if response.status_code == 200:
            return True
        return False

    def retrieve(self):
        retrieve_id = input('Введите ID для поиска: ')
        response = requests.get(self.url + f'todo/{retrieve_id}')
        if response.status_code == 200:
            return print(json.loads(response.text))
        elif response.status_code == 404:
            raise Exception('Нет такой записи')
        raise Exception('Непредвиденная ошибка')


    def update(self):
        id_input = input('введите ID: ')
        update_input = {
        'title': str(input('Новое имя: ')),
        'is_done': bool(input('Введите статус True или False: '))
        }
        response = requests.put(self.url + f'todo/{id_input}/update', data=json.dumps(update_input))
        if response.status_code == 200:
            return True
        return False


    def delete(self):
        delete_id = input("Введи ID для удаления: ")
        response = requests.delete(self.url + f'todo/{delete_id}/delete', data=delete_id)
        if response.status_code == 200:
            return True
        return False




obj = Host('http://3.67.196.232/')
obj.get_all()
# obj.create()
# obj.retrieve()
# obj.update()
# obj.delete()