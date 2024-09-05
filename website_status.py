import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict

def check_status(url :str) -> None:
    try:
        response :Responce = requests.get(url)

        status_code :int = response.status_code
        header: CaseInsensitiveDict[str] = response.headers
        content_type :str = header.get('Content-Type', 'Unknown')
        server:str = header.get('Server','Unknown')
        response_time :float = response.elapsed.total_seconds()

        print(f'URL: {url}')
        print(f'Status Code: {status_code}')
        print(f'Content Type: {content_type}')
        print (f'Server: {server}' )
        print (f'Response Time: {response_time:.2f} seconds')
        
    except RequestException as e:
        print(f'Error: {e}')

def main() ->None:
    url_to_check :str = input("Enter the URL to check: ")
    check_status(url_to_check)

if __name__ == '__main__':
    main()
    
    
