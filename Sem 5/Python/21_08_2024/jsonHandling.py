import os
import json


def readJson(datadir):
    """
    Reads all JSON files in the specified directory except for 'covid19_summary.json'
    and returns a list of country data.

    :param datadir: The directory containing the JSON files.
    :return: A list of dictionaries, each containing data for a specific country.
    """
    countries = []
    for root, _, files in os.walk(datadir):
        for file in files:
            if file.endswith('.json') and file != 'covid19_summary.json':
                with open(os.path.join(root, file), 'r') as f:
                    try:
                        data = json.load(f)
                        countries.append(data)
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON from file {file}: {e}")
    return countries


def statisticsJson(countries):
    """
    Processes the list of country data and calculates average statistics for each country.

    :param countries: A list of dictionaries, each containing data for a specific country.
    :return: A list of dictionaries, each containing summarized statistics for a country.
    """
    country_stats = []
    for country in countries:
        country_name = country['country']
        avg_confirmed_cases = 0
        avg_deaths = 0
        avg_recovered = 0
        max_cases = 0

        # Calculate statistics for each country
        for i in range(len(country['data'])):
            avg_confirmed_cases += country['data'][i]['confirmed_cases']['total']
            avg_deaths += country['data'][i]['deaths']['total']
            avg_recovered += country['data'][i]['recovered']['total']

            if country['data'][i]['confirmed_cases']['total'] > max_cases:
                max_cases = country['data'][i]['confirmed_cases']['total']
                max_cases_date = country['data'][i]['date']

        # Calculate averages
        avg_confirmed_cases /= len(country['data'])
        avg_deaths /= len(country['data'])
        avg_recovered /= len(country['data'])

        # Append summarized data for each country
        country_stats.append({
            'country': country_name,
            'confirmed_cases': avg_confirmed_cases,
            'deaths': avg_deaths,
            'recovered': avg_recovered,
            'max_cases': max_cases,
            'max_date': max_cases_date
        })
    return country_stats


def countries_ranking(country_ranking):
    """
    Ranks countries based on average confirmed cases and returns the top 5 and bottom 5.

    :param country_ranking: A list of summarized statistics for each country.
    :return: Two lists containing the top 5 and bottom 5 countries.
    """
    country_ranking.sort(key=lambda x: x['confirmed_cases'], reverse=True)
    return country_ranking[:5], country_ranking[-5:]


def summary_report(datadir):
    """
    Generates a summary report from the JSON files in the specified directory.

    :param datadir: The directory containing the JSON files.
    """
    countries = readJson(datadir)
    stats = statisticsJson(countries)
    top5, bottom5 = countries_ranking(stats)

    # Write the report to a summary JSON file
    with open('covid19_summary.json', 'w') as f:
        json.dump(stats, f, indent=4)

    # Interactive loop for querying country data
    while True:
        country_name = input("Enter a country name to see its COVID-19 data (or type 'exit' to quit): ").strip()

        if country_name.lower() == 'exit':
            print("Exiting the program.")
            break

        found_country = next((country for country in stats if country['country'].lower() == country_name.lower()), None)

        if found_country:
            print(json.dumps(found_country, indent=4))
        else:
            print(f"No data found for country: {country_name}. Please try again.")


if __name__ == "__main__":
    # Set the current working directory and the data directory path
    getcwd = os.getcwd()
    datadir = os.path.join(getcwd, "data")

    # Generate the summary report
    summary_report(datadir)
