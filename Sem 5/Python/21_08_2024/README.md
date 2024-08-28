# COVID-19 Data Processing Script

This Python script processes COVID-19 data from multiple JSON files and generates a summary report. The summary includes average confirmed cases, deaths, recovered cases, and the date with the maximum number of cases for each country. The script also ranks the countries based on confirmed cases and outputs the top 5 and bottom 5 countries.

## File Structure

- `jsonHandling.py`: The main script that processes the data.
- `data/`: Directory containing the country-specific JSON files.
- `covid19_summary.json`: The output summary file.

## Example of a Country JSON File

Each country JSON file in the `data/` directory should have the following structure:

```json
{
    "country": "USA",
    "data": [
        {
            "date": "2024-08-26",
            "confirmed_cases": {
                "total": 1222732
            },
            "deaths": {
                "total": 54300
            },
            "recovered": {
                "total": 919307
            }
        },
        ...
    ]
}
```

## Script Overview

`readJson(datadir)`
- Reads all JSON files in the specified directory (excluding `covid19_summary.json`).
- Returns a list of country data.

`statisticsJson(countries)`
- Processes the list of country data.
- Calculates average confirmed cases, deaths, and recovered cases.
- Finds the date with the maximum number of confirmed cases.
- Returns a list of statistics for each country.

`countries_ranking(country_ranking)`
- Sorts the countries based on confirmed cases in descending order.
- Returns the top 5 and bottom 5 countries.

`summary_report(datadir)`
- Reads the country data.
- Generates statistics for each country.
- Ranks the countries and writes the summary to `covid19_summary.json`.

## Running the Script

To run the script, execute the following command in your terminal:
```bash
python jsonHandling.py
```

Make sure the `data/` directory contains the country-specific JSON files.

## Example Output
The script generates a `covid19_summary.json` file with the following structure:
```json
[
    {
        "country": "USA",
        "confirmed_cases": 1116123.0,
        "deaths": 54300.4,
        "recovered": 919307.6,
        "max_cases": 1222732,
        "max_date": "2024-08-26"
    },
    ...
]
```