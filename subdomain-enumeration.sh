# Source: https://twitter.com/JaneScott_/status/1065995260554170369

# NOT WORKING
# curl "https://crt.sh/?q=%.example.com&output=json" | jq '.name_value' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u

# WORKING
# Just replacte the example.com with any domain and you will get a list  of sub/domains.
$curl 'https://crt.sh/?q=%.example.com&output=json' | jq -r '.[] | .name_value' | sort -u
