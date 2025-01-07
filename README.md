# ConfigReader

## Introduction
After working on a couple of projects that required various configuration needs, I decided to create a dynamic configuration class. `ConfigReader` is designed to make handling configuration files seamless and flexible. This class supports multiple file formats, making it an essential tool for projects requiring versatile configuration management.

## Features
- **Multi-Format Support**: Reads configuration files in `.xml`, `.properties`, and `.json` formats.
- **Dynamic Parsing**: Automatically detects file type based on its extension.
- **Cross-Platform Compatibility**: Designed to work on Windows, macOS, and Linux.
- **Error Handling**: Provides clear error messages for missing or malformed files.
- **Hierarchical Parsing**: Supports nested structures for `.xml` and `.json` files.

## Directory Structure
Place your configuration files in a `config/` directory within your project:

```
project/
|-- config/
|   |-- config_simple.xml
|   |-- config_simple.properties
|   |-- config_simple.json
|-- ConfigReader.py
```

## Usage

### Installation
No external libraries are required. `ConfigReader` relies on Python's standard library.

### Example Code
Here is an example of how to use the `ConfigReader`:

```python
from ConfigReader import ConfigReader

if __name__ == "__main__":
    try:
        # Initialize ConfigReader with the desired file
        config_reader = ConfigReader(config_filename="config_simple.json")

        # Read and parse the configuration
        config = config_reader.read_config()

        # Print the loaded configuration
        print("Configuration Loaded:")
        print(config)
    except Exception as e:
        print(f"Error: {e}")
```

### Configuration File Examples
#### Simple `.properties` File:
```properties
app_name=SimpleApp
version=1.0.0
debug=true
```

#### Complex `.json` File:
```json
{
    "database": {
        "host": "127.0.0.1",
        "port": 5432,
        "user": "admin",
        "password": "super_secret_password"
    },
    "application": {
        "name": "ComplexApp",
        "version": "2.5.1",
        "maintenance_mode": false
    }
}
```

## Future Plans
- Add support for additional formats like YAML or INI.
- Introduce schema validation to enforce configuration structure.
- Enable environment variable substitution for dynamic settings.

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request for new features or bug fixes.

---
Thank you for using `ConfigReader`. Feedback and suggestions are always appreciated!


