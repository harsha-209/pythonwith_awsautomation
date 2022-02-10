import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='harshad', password='harshad')
jobs = server.get_jobs()

for i in jobs:
  print(i['name'])
