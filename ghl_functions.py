import requests
import plotly.express as px


def get_data(languages):
    '''Loop through the languages and make an API call for each language to get the
    total number of repositories, and the name of the most-starred repository for
    each.'''
    # Empty list for our dictionaries of data
    github_data = []
    for language in languages:
        # Make the API call
        print(f'Getting data for {language}...')
        # This returns only the most-starred repository for the language as well as
        # general data such as the total count
        url = (f'https://api.github.com/search/repositories?q=language:{language}'
               '&per_page=1&sort=stars')
        r = requests.get(url)
        # If the request was successful
        if r.status_code == 200:
            # Store the data as JSON
            data = r.json()
            # Add the language, count and top repo (most-starred) as a dict to the list
            github_data.append({
                'language': language,
                'count': data['total_count'],
                'top_repo': f'Top Repo: {data["items"][0]["name"]}'
            })
        # If the request was unsuccessful
        else:
            # Print an error and add the language to the error list
            print(f'Status code error {r.status_code} for {language}')

    # Sort data by count and return the list of dictionaries
    print('Data download complete.')
    return sorted(github_data, key=lambda x: x['count'], reverse=True)


def show_plot(github_data):
    '''Create a Plotly Express bar chart of the github data'''
    # If there is at least one item in the list
    if len(github_data) > 0:
        print('Launching plot in web browser.')
        fig = px.bar(github_data,
                     x='language',
                     y='count',
                     hover_name='top_repo',
                     title='Number of Repositories on GitHub',
                     labels={'language': 'Language', 'count': 'Repositories'},
                     template='seaborn',
                     )
        fig.show()
    # If the list is empty
    else:
        print('Could not display plot - no data to plot!')
