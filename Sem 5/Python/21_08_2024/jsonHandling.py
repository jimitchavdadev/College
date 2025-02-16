import os
import json


def readJson(datadir):
    countries = []
    # Traverse the directory tree starting from the given directory path.
    
    for root, _, files in os.walk(getcwd):
        for file in files:
            # Check if the file is a JSON file and not the summary file.
            
            if file.endswith('.json') and file != 'covid19_summary.json':
                # Open the JSON file and load its content.

                with open(os.path.join(root, file), 'r') as f:
                    data = json.load(f)
                    
                    # Append the data from the file to the list of countries.
                    countries.append(data)
    return countries

def statisticsJson(countries):
    country_stats = []
    # Process each country's data
    
    for country in countries:
        country_name = country['country']
        total_confirmed_cases = 0
        total_deaths = 0
        total_recovered = 0
        
        # Accumulate the statistics from the list of daily data.
        for i in range(0, len(country['data'])):
            total_confirmed_cases += country['data'][i]['confirmed_cases']['total']
            total_deaths += country['data'][i]['deaths']['total']
            total_recovered += country['data'][i]['recovered']['total']
        
        # Append the aggregated statistics for the country.
        country_stats.append({
            'country': country_name,
            'confirmed_cases': total_confirmed_cases,
            'deaths': total_deaths,
            'recovered': total_recovered,
            'active_cases': total_confirmed_cases - total_deaths - total_recovered
        })
    return country_stats

def countries_ranking(country_ranking):
    # Sort countries by the number of confirmed cases in descending order.
    country_ranking.sort(key=lambda x: x['confirmed_cases'], reverse=True)
    
    # Return the top 5 and bottom 5 countries based on confirmed cases.
    return country_ranking[:5],country_ranking[-5:]

def summary_report(datadir):
    # Read JSON data from the specified directory.
    countries = readJson(datadir)
    
    # Calculate statistics for each country.
    stats = statisticsJson(countries)
    
    # Get top 5 and bottom 5 countries based on confirmed cases
    top5, bottom5 = countries_ranking(stats)

    #Write the report to a summary json file
    with open('covid19_summary.json', 'w') as f:
        json.dump(stats, f, indent=4)


if __name__ == "__main__":
    # Get the current working directory.
    getcwd = os.getcwd()
    
    # Calculate statistics for the countries in the data directory.
    datadir = os.path.join(getcwd, "data")
    stats = statisticsJson(readJson(datadir))
    
    # Get top 5 and bottom 5 countries based on confirmed cases
    top5, bottom5 = countries_ranking(stats)
    
    # Generate and save the summary report.
    summary_report(datadir)
    
    # Print the top 5 and bottom 5 countries
    print("Top 5 Countries:")
    for i in top5: 
        print(f"  {i['country']} - {i['confirmed_cases']} cases")
    print("Bottom 5 Countries:")
    for i in bottom5:
        print(f"  {i['country']} - {i['confirmed_cases']} cases")

    # Allow user to query statistics for a specific country
    while True:
        userInput = input("Enter the country name to get the statistics (or type 'exit' to quit): ")
        if userInput.lower() == 'exit':
            break
        
        # Find the statistics for the input country.
        country_stat = next((item for item in stats if item['country'].lower() == userInput.lower()), None)
        if country_stat:
            # Print the statistics for the specified country.
            print(f"Statistics for {country_stat['country']}:")
            print(f"  Confirmed Cases: {country_stat['confirmed_cases']}")
            print(f"  Deaths: {country_stat['deaths']}")
            print(f"  Recovered: {country_stat['recovered']}")
            # print(f"  Max Cases: {country_stat['max_cases']} on {country_stat['max_date']}")
        else:
            print("Country not found. Please try again.")