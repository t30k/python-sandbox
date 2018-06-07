import yaml

def import_yml():
    with open('../test.yaml') as file:
        data = yaml.load(file)
        myeip = data['MyEIP']
        type = myeip['Type']
        print(type)
        properties = myeip['Properties']
        instanceid = properties['InstanceId']
        print(instanceid)

if __name__ == "__main__":
    import_yml()