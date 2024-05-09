import xml.etree.ElementTree as ET
import json

class Adapter:
    def __init__(self, xml_file):
        with open(xml_file, 'r') as file:
            xml_file = file.read()
        self.root = ET.fromstring(xml_file)

    def xml_to_json(self, element):
        node = {}
        for child in element:
            if child.tag == 'hijos':
                node[child.tag] = [{'tipo': grandchild.text} for grandchild in child]
            elif child.text.strip():
                node[child.tag] = child.text
            elif list(child):
                node[child.tag] = [self.xml_to_json(grandchild) for grandchild in child]
        return node

    def get_json(self):
        json_data = self.xml_to_json(self.root)
        transformed_data = {
            "laberinto": [{"tipo": child.get('tipo', ''), "num": int(child.get('num', 0)), "hijos": child.get('hijos', [])} for child in json_data['laberinto']],
            "puertas": [[int(child.get('num1', 0)), child.get('direccion1', ''), int(child.get('num2', 0)), child.get('direccion2', '')] for child in json_data['puertas']],
            "bichos": [{"modo": child.get('modo', ''), "hab": int(child.get('hab', 0))} for child in json_data['bichos']],
            "compis": [{"modo": child.get('modo', ''), "hab": int(child.get('hab', 0))} for child in json_data['compis']]
        }
        return json.dumps(transformed_data)

