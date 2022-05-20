'''A simple program that creates a Plotly Express bar chart showing the number of
repositories for the chosen languages on GitHub currently. When hovering over a bar,
it will tell you the most-starred repository for that language.'''

from ghl_functions import get_data, show_plot

# A list of the languages we want to compare
languages = ['python', 'c#', 'dart', 'java', 'go',
             'php', 'html', 'c++', 'javascript', 'ruby']

github_data = get_data(languages)
show_plot(github_data)
