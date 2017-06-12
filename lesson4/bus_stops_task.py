import csv


def get_most_common_value_per_column(file, column_name):
    with open(file, 'r', encoding='cp1251') as f:
        reader = csv.DictReader(f, delimiter=';')
        street_station_count_map = {}
        for row in reader:
            if row[column_name] in street_station_count_map.keys():
                value = set(street_station_count_map[row[column_name]])
                value.add(row['StationName'])
                street_station_count_map.update({row[column_name]: value})
            else:
                street_station_count_map.update({row[column_name]: []})
    return sorted(street_station_count_map.items(), key=lambda x: len(x[1]), reverse=True)[0][0]


if __name__ == '__main__':
    csv_file = 'data-398-2017-06-05.csv'
    most_common_street = get_most_common_value_per_column(csv_file, "Street")
    print("Улица, на которой больше всего остановок: {street}".format(street=most_common_street))
