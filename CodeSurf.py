import webbrowser
from plyer import notification
import random

end_tags_coding = [': GeeksforGeeks', ': Stack Overflow', ': leetcode', ': python.org', ': github']

notification.notify(
    title = 'Code:Surf',
    message = 'Welcome to CodeSurf',
    app_icon = None,
    timeout = 3,
)

surf_Search = input('\n\nSurf the web: ')
surf_Search_formed = surf_Search + random.choice(end_tags_coding)
webbrowser.open('https://www.google.com/search?q= ' + surf_Search_formed + '&oq= ' + surf_Search_formed + '&aqs=chrome..69i57.30j0j7&sourceid=chrome&ie=UTF-8' + random.choice(end_tags_coding) + '')

