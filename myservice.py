settings = {"service_id": None}

def get_congif(id=None):
    global settings
    if id:
        settings["service_id"] = id
        print("Config update!")
    return settings["service_id"]
