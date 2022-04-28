# pfSense_tools_mikprin
This python code allow you to add static DHCP to XML configuration from CSV file. That might be usefull when you need to add a massive list of servers to DHCP binding. Example of format of CSV can be found in `examples/staticmap.csv`. Also you will need your current PfSence XML configuration which you can download from backup page.

# Installation

1. Download whl  [release](https://github.com/mikprin/pfSense_tools_mikprin/releases).
1. Install it from wheel file with `pip3 install pfsence_tools_mikprin-0.0.1-py3-none-any.whl`

# Build:
You can build it as a package if you have problem with release wheel. This is an alternative option.

1. Install setuptools for python. (`pip install setuptools`)
1. Build with `python3 -m build`.
1. Get output in `dist` directory.

# Use as python file
Actually all code is in one file under `src/pfsense_tools_mikprin/add_static_map_to_file.py`. You can import it directly.

# Usage

 [Usage guide in notebook](https://github.com/mikprin/pfSense_tools_mikprin/blob/master/guide.ipynb) 

This python code allow you to add static DHCP to XML configuration from CSV file. And here I will show you how:

```
## Preparation
### Import module
from pfsense_tools_mikprin.add_static_map_to_file import add_static_map_to_file

### Set path for your configuration file. Can be downloaded from your PfSence web interface in backup.
configuration_file = "examples/example_pf_config.xml" 

### Set your CSV file with all hosts to add to static map
static_map_file = "examples/staticmap.csv" 

### Add enteries
add_static_map_to_file(configuration_file, static_map_file, interface = "lan", output_file = "./output_config.xml")
```




## Setting file path

`static_map_file = "examples/staticmap.csv"` - Staticmap file is a list of static hosts you want to add.
`output_file = "output_config.xml"` - Output configuration file. You can use `output_file = "SAME_AS_INPUT"` to owerwrite your configuration.
`configuration_file = "examples/example_pf_config.xml" ` - Current pfsence configuration

`target_lan_interface = 'lan'` - target local network interface you want to use

## Running the script

`add_static_map_to_file(configuration_file, static_map_file, interface = "lan", output_file = "./output_config.xml")`



# Other material

Bash script with the similar functionality.

https://carl.idv.hk/migrate-windows-dhcp-to-pfsense/
