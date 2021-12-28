import random, os, shutil, json

settings = json.load(open('settings.json'))

for x in range(settings["amount"]):
    random_filename = random.choice([
    x for x in os.listdir(settings["path"])
    if os.path.isfile(os.path.join(settings["path"], x))
    ])
    shutil.copyfile(os.path.join(settings["path"], random_filename), os.path.join(settings["target"], random_filename))