settings = {"service_id": 1}

def use_config(id=None):
    global settings
    if id:
        settings["service_id"] = id
        print("Обновлен config")
    return settings["service_id"]