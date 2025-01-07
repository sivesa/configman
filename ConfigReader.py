import os
import xml.etree.ElementTree as ET

class ConfigReader:
    def __init__(self, config_filename="config_simple.xml"):
        # Dynamically determine the base directory
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_file = os.path.join(self.config_dir, config_filename)
        
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")

    def read_config(self):
        """Reads and parses the XML configuration file."""
        try:
            tree = ET.parse(self.config_file)
            root = tree.getroot()
            return self._parse_xml_to_dict(root)
        except ET.ParseError as e:
            raise ValueError(f"Error parsing XML configuration file: {e}")

    def _parse_xml_to_dict(self, element):
        """Recursively parses an XML element into a dictionary."""
        config = {}
        for child in element:
            if len(child):  # If the child has children, recurse
                config[child.tag] = self._parse_xml_to_dict(child)
            else:  # Otherwise, just get the text
                config[child.tag] = child.text
        return config

        
# Usage
if __name__ == "__main__":
    try:
        config_reader = ConfigReader()
        config = config_reader.read_config()
        print("Configuration Loaded:")
        print(config)
    except Exception as e:
        print(f"Error: {e}")

