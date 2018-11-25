# Source: https://twitter.com/JaneScott_/status/1065995260554170369

curl "https://crt.sh/?q=%.example.com&output=json" | jq '.name_value' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u
