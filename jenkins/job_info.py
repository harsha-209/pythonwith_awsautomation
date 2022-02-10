import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='harshad', password='harshad')
build = server.get_job_info('ccfg')['lastBuild']['number']
print(build)

