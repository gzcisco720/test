def convert_single_quotes_json(json_text):
    # Replace single quotes around keys with double quotes
    json_text = re.sub(r"'(\w+)':", r'"\1":', json_text)
    
    # Replace single quotes around values with double quotes
    def replace_value_quotes(match):
        value = match.group(1)
        value = value.replace('"', '\\"')  # Escape existing double quotes in the value
        return f'"{value}"'
    
    json_text = re.sub(r":\s*'([^']*?)'\s*(?=,|\})", lambda m: ':"' + m.group(1).replace("'", "\\'") + '"', json_text)
    
    # Now replace single quotes with double quotes for the remaining unmatched single quotes
    json_text = re.sub(r"'", '"', json_text)

    # Convert the modified string to a JSON object
    return json.loads(json_text)
