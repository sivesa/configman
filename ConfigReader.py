import os
import xml.etree.ElementTree as ET

class ConfigReader:
    def __init__(self, config_filename="config_simple.xml"):
        # Dynamically determine the base directory (compatible across OS)
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_file = os.path.join(self.config_dir, config_filename)
        
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")

    def read_config(self):
        pass

    def _parse_xml_to_dict(self, element):
        pass
        
# Usage
if __name__ == "__main__":
    try:
        config_reader = ConfigReader()
        print("try has been executed")
    except Exception as e:
        print(f"Error: {e}")

