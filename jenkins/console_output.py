import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='harshad', password='harshad')
build = server.get_build_console_output('ccfg',6)
print(build)
