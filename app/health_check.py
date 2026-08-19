import requests
from requests.exceptions import RequestException, Timeout

print("DevOps Health Check Dashboard starting...")

url ="https://httpbin.org/status/200"

try:

	response = requests.get(url, timeout=5)

	print(f"Checked URL: {url}")
	print(f"Status code: {response.status_code}")

	if response.status_code == 200:
		print("Health check result: PASS")
	else:
		print("Health check result: FAIL")

except Timeout:
	print(f"Checked URL:{url}")
	print("Health check result: FAIL")
	print("Reason: Request timed out")

except RequestException as error:
	print(f"Checked URL: {url}")
	print("Health check result: FAIL")
	print(f"Reason: Request error: {error}")
