import json


class JsonSource():
    def __init__(self, json_path):
        with open(json_path, "r") as f:
            json_data = json.load(f)

        self.data = json_data


    def split(self,arr, size):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr   = arr[size:]
        arrs.append(arr)
        return arrs

    
    def get_options(self,lang):
        options = self.data[lang]["options"].keys() 
        options = list(options)
        formatted_options = self.split(options,2)
        return formatted_options       