import pytest
import requests
from utils import get_token


def test_jaga_login():

    jwt_token = get_token.get_login_token()

    headers = {
        'accept': '*/*',
        'Authorization': f'Bearer {jwt_token}',
    }

    response = requests.get('https://test2-jaga.lukit.ru/esmp-integrator/jaga/project/serviceList', headers=headers)
    print('  ')
    print('response=',response)

    projectId = 1657
    serviceId = 1
    print('---------------------------------------------------  ')
    response = requests.delete(f'https://test2-jaga.lukit.ru/esmp-integrator/jaga/project/service?projectId={projectId}&serviceId={serviceId}', headers=headers)
    print(f'projectId={projectId}  serviceId={serviceId}  ')
    print('response=',response)
    projectId = 16570
    serviceId = 3
    print('---------------------------------------------------  ')
    response = requests.delete(f'https://test2-jaga.lukit.ru/esmp-integrator/jaga/project/service?projectId={projectId}&serviceId={serviceId}', headers=headers)
    print(f'projectId={projectId}  serviceId={serviceId}  ')
    print('response=',response)


