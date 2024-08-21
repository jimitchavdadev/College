import os
import json

# Function to read JSON data from files in a directory
def read_covid_data(directory):
    covid_data = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    covid_data.append(data)
    return covid_data

# Function to calculate country-wise statistics
def calculate_statistics(covid_data):
    country_stats = {}
    
    for record in covid_data:
        country = record['country']
        confirmed_cases = record['confirmed_cases']['total']
        deaths = record['deaths']['total']
        recovered = record['recovered']['total']
        active_cases = confirmed_cases - (deaths + recovered)
        
        if country not in country_stats:
            country_stats[country] = {
                'total_confirmed': 0,
                'total_deaths': 0,
                'total_recovered': 0,
                'total_active': 0
            }
        
        country_stats[country]['total_confirmed'] += confirmed_cases
        country_stats[country]['total_deaths'] += deaths
        country_stats[country]['total_recovered'] += recovered
        country_stats[country]['total_active'] += active_cases
    
    return country_stats

# Function to get top 5 countries by confirmed cases
def get_top_countries_by_confirmed_cases(country_stats, top=True):
    sorted_countries = sorted(country_stats.items(), key=lambda x: x[1]['total_confirmed'], reverse=top)
    return sorted_countries[:5]

# Function to generate summary report and save to JSON file
def generate_summary_report(country_stats, output_file="covid19_summary.json"):
    with open(output_file, 'w') as f:
        json.dump(country_stats, f, indent=4)
    print(f"Summary report saved to {output_file}")

# Main function
def main(directory):
    covid_data = read_covid_data(directory)
    country_stats = calculate_statistics(covid_data)
    
    # Display statistics
    for country, stats in country_stats.items():
        print(f"{country} - Confirmed: {stats['total_confirmed']}, Deaths: {stats['total_deaths']}, Recovered: {stats['total_recovered']}, Active: {stats['total_active']}")
    
    # Get top 5 countries with highest and lowest confirmed cases
    top_5_highest = get_top_countries_by_confirmed_cases(country_stats, top=True)
    top_5_lowest = get_top_countries_by_confirmed_cases(country_stats, top=False)
    
    print("\nTop 5 countries with the highest confirmed cases:")
    for country, stats in top_5_highest:
        print(f"{country} - Confirmed: {stats['total_confirmed']}")
    
    print("\nTop 5 countries with the lowest confirmed cases:")
    for country, stats in top_5_lowest:
        print(f"{country} - Confirmed: {stats['total_confirmed']}")
    
    # Generate summary report
    generate_summary_report(country_stats)

# Example usage
if __name__ == "__main__":
    directory = "path_to_json_files"
    main(directory)
