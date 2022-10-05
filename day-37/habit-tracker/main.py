import requests
from datetime import datetime

USERNAME = "junpak"
TOKEN = "i9l4u0v3h2e3r!"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
users_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    }
# response = requests.post(url=pixela_endpoint, json=users_params)


graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Studying graph",
    "unit": "commit",
    "type": "int",
    "color": "sora",
    }

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graphs_endpoint, json=graph_config, headers=headers)


today = datetime.now().strftime("%Y%m%d")

graphs_post_endpoint = f"{graphs_endpoint}/{GRAPH_ID}"
graph_post_config = {
    "date": today,
    "quantity": input("How many times did you study today?: "),
    }
response = requests.post(url=graphs_post_endpoint, json=graph_post_config, headers=headers)

graphs_put_endpoint = f"{graphs_post_endpoint}/{today}"
graph_put_config = {
    "quantity": "7",
    }
# response = requests.put(url=graphs_put_endpoint, json=graph_put_config, headers=headers)

graphs_delete_endpoint = f"{graphs_post_endpoint}/{today}"
# response = requests.delete(url=graphs_put_endpoint, json=graph_put_config, headers=headers)

print(response.text)
