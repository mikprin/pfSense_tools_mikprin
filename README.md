# pfSense_static_dhcp_from_csv
This python code allow you to add static DHCP to XML configuration from CSV file.

# Usage

## Getting data set

`staticmap_file = "../staticmap/staticmap.csv"` - Staticmap file is a list of static hosts you want to add.
`output_file = "out.xml"` - Output configuration file. You can use `output_file = "SAME_AS_INPUT"` to owerwrite your configuration.
`configuration_file = "../bkup_configs/current_config.xml"` - Current pfsence configuration

`target_lan_interface = 'lan'` - targer local network interface you want to use

## Running the script:

`add_static_map_to_file(configuration_file, staticmap_file, interface = "lan"  , static_template = "DEFAULT" , output_file = "out.xml")`



# Other material

Bash script with the same functionality.

https://carl.idv.hk/migrate-windows-dhcp-to-pfsense/
