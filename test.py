from requests import delete

'''
print(get('http://127.0.0.1:5000/api/jobs').json())
print(get('http://127.0.0.1:5000/api/jobs/1').json())
print(get('http://127.0.0.1:5000/api/jobs/100').json())
print(get('http://127.0.0.1:5000/api/jobs/kyrkuma').json())

print(post('http://127.0.0.1:5000/api/jobs').json())

print(post('http://127.0.0.1:5000/api/jobs',
           json={'id': 'Заголовок'}).json())

print(post('http://127.0.0.1:5000/api/jobs',
           json={'id': 10, 'job': 'doctor doctor', 'team_leader': 1, 'work_size': 45,
                 'collaborators': '6, 7, 9', 'is_finished': False}).json())
'''

print(delete('http://127.0.0.1:5000/api/jobs/999').json())
print(delete('http://127.0.0.1:5000/api/jobs/kurkuma').json())
print(delete('http://127.0.0.1:5000/api/jobs/1').json())