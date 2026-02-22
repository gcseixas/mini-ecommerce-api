import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnY3NlaXhhczAxQGdtYWlsLmNvbSIsImV4cCI6MTc3MTcwMjEwMX0.d95R6KnCy96z6Eh9yX7wIietthQ2lkc7SfpbqVRpRHs"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/me", headers=headers)
print(requisicao)
dados = requisicao.json()

print(dados)