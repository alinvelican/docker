import docker
client = docker.from_env()

def listAllContainers():
    for container in client.containers.list():
        print(container.name)


def killAllContainers():
    for container in client.containers.list():
        container.kill()
def removeAllContainers():
    for container in client.containers.list("all"):
        container.remove()
def listImages():
    for image in client.images.list():
        print(image)
def deleteAllImages():
    for image in client.images.list():
        client.images.remove(image.id,True)

# listAllContainers()
# killAllContainers()
# removeAllContainers()
# deleteAllImages()
# listImages()

# client.containers.run('myserver',detach=True,ports = {'8080/tcp': 8080})

client.images.get('myserver').tag('alinvelican/myserver')
client.images.push('alinvelican/myserver')


import docker
client = docker.from_env()
client.images.build(path = "./",tag = "myserver")
