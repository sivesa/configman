import os
import json
import xml.etree.ElementTree as ET

class ConfigReader:
    def __init__(self, config_filename="config_complex.xml"):
        # Dynamically determine the base directory
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_file = os.path.join(self.config_dir, config_filename)
        
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")

    def read_config(self):
        """Reads and parses the configuration file based on its extension."""
        file_extension = os.path.splitext(self.config_file)[1].lower()
        
        try:
            if file_extension == ".xml":
                tree = ET.parse(self.config_file)
                root = tree.getroot()
                return self._parse_xml_to_dict(root)
            elif file_extension == ".properties":
                return self._parse_properties_to_dict(self.config_file)
            elif file_extension == ".json":
                return self._parse_json_to_dict(self.config_file)
            else:
                raise ValueError(f"Unsupported configuration file format: {file_extension}")
        except Exception as e:
            raise ValueError(f"Error reading configuration file: {e}")

    def _parse_xml_to_dict(self, element):
        """Recursively parses an XML element into a dictionary."""
        config = {}
        for child in element:
            if len(child):  # If the child has children, recurse
                config[child.tag] = self._parse_xml_to_dict(child)
            else:  # Otherwise, just get the text
                config[child.tag] = child.text
        return config

    def _parse_properties_to_dict(self, properties_file):
        """Parses a .properties file into a dictionary."""
        config = {}
        try:
            with open(properties_file, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith('#'):  # Skip empty lines and comments
                        key, value = line.split('=', 1)
                        config[key.strip()] = value.strip()
        except Exception as e:
            raise ValueError(f"Error parsing properties file: {e}")
        return config

    def _parse_json_to_dict(self, json_file):
        """Parses a JSON file into a dictionary."""
        try:
            with open(json_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing JSON file: {e}")
        except Exception as e:
            raise ValueError(f"Error reading JSON file: {e}")

# Usage
if __name__ == "__main__":
    try:
        config_reader = ConfigReader()
        config = config_reader.read_config()
        print("Configuration Loaded:")
        print(config)
    except Exception as e:
        print(f"Error: {e}")


