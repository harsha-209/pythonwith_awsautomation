import jenkins
import datetime
import time
job_name = "ccfg"
server = jenkins.Jenkins('http://localhost:8080', username='harshad', password='harshad')

################################### build jenkins job###############################

build_job = server.build_job(job_name)
print(build_job)
########################################waiting#########################################
print("waiting to get job build completed")
time.sleep(50)

######################### getting last build number#####################################
build_number = server.get_job_info(job_name)['lastBuild']['number']
print('the build number for this job is', build_number)

############################ console output job for latest build##############################
console_output = server.get_build_console_output(job_name, build_number)
print("this is the console output for", build_number)
print(console_output)
