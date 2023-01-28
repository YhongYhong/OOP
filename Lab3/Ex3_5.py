record_collection = {
  2548: {
    'albumTitle': 'Slippery When Wet',
    'artist': 'Bon Jovi',
    'tracks': ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    'albumTitle': '1999',
    'artist': 'Prince',
    'tracks': ['1999', 'Little Red Corvette']
  },
  1245: {
    'artist': 'Robert Palmer',
    'tracks': []
  },
  5439: {
    'albumTitle': 'ABBA Gold'
  }
}

def update_records(record, id, property, value):
    if property != 'tracks' and value != '':
        record[id].update({property : value})

    elif property == 'tracks' and property not in record_collection[id]:
        record[id].update({'tracks' : []})
        record[id]['tracks'].append(value)

    elif property == 'tracks' and record_collection[id][property] != '':
        record[id]['tracks'].append(value)

    elif value == '':
        del record[id][property]

    else: pass

    return record_collection

print(update_records(record_collection, 2548, "albumTitle", "Have a Nice Day"))
