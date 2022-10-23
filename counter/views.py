from django.shortcuts import render


def home(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'Qpk9GGPQ1UK7DmjVKHJSKQ==sM84QDEd94iDBP2u'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'counter/home.html', {'api': api})
    else:
        return render(request, 'counter/home.html', {'query': 'Enter a valid query'})