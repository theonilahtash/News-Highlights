import urllib.request,json
from .models import Source

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['results']:
            source_results_list = get_sources_response['results']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('original_name')
        description = source_item.get('description')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if poster:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)
            print(source_results)

    return source_results

def get_source(id):
    get_source_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)
        source_object = None
        if source_details_response:
            id = source_details_response.get('id')
            name = source_details_response.get('name')
            description = source_details_response.get('description')
            category = source_details_response.get('category')
            language = source_details_response.get('language')
            country = source_details_response.get('country')
        

            source_object = Source(id,name,description,url,category,language,country)

    return source_object

def search_source(source_name):
    search_source_url = 'https://newsapi.org/v2/sources?api_key={}&query={}'.format(api_key,source_name)
    with urllib.request.urlopen(search_source_url) as url:
        search_source_data = url.read()
        search_source_response = json.loads(search_source_data)

        search_source_results = None

        if search_source_response['results']:
            search_source_list = search_source_response['results']
            search_source_results = process_results(search_source_list)


    return search_source_results