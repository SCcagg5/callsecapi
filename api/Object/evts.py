import requests
import os
import time

docker = "/mnt/c/Program\ Files/Docker/Docker/resources/bin/docker.exe"
dc = "/mnt/c/Program\ Files/Docker/Docker/resources/bin/docker-compose.exe"#"docker-compose"

class dockers:

    def run(x, login):
        name = "wordpress_n" + str(x)
        commands = [
        "cd ../..",
        "cp -r WP_base/ " + name,
        "cd " + name,
        dc + " up -d > /dev/null",
        "echo $(" + dc + " ps nginx | tail -n 1 | cut -d : -f2 | cut -d - -f1) > port.conf"
        ]
        globalcom = ""
        for i in commands:
            globalcom += str(i) + " ; "
        os.system(globalcom)
        with open("../../" + name + "/port.conf", 'r') as file:
            data = file.read()[:-1]
            file.close()
        return dockers.nginxsteup(data, login, x)

    def nginxsteup(port, login, x):
        with open("../../nginx/site.conf", 'r') as file:
            conf = file.read()[:-2]
            file.close()
        url = "/" + login + "/" + str(x) + "/"
        conf += "\n\
    location /courte_e/1/ {\n\
        proxy_pass http://host.docker.internal:"+port+"/ ;\n\
    }\
}"
        with open("../../nginx/site.conf", 'w') as file:
            file.write(conf)
            file.close()
        os.system("cd ../../ ;" + dc + " restart")
        return [True, {"url": url, "addr": port}]

if __name__ == '__main__':
    print(dockers.run(1, "courte_e")[1])
