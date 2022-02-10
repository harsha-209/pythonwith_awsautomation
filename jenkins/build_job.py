import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='harshad', password='harshad')
build = server.build_job('ccfg')
lastest_buildnumber = server.get
print(build)
