import requests

HOST = "https://release-gs.qa-playground.com/api/v1"

# response = requests.post(
#     url=f"{HOST}/setup",
#     headers={
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRB"
#                          "Q0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJhdWQiO"
#                          "iJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzEzODU0MzYyL"
#                          "CJpYXQiOjE3MTMyNTQzNjIsImlzcyI6Imh0dHBzOi8vbX"
#                          "lrb3RxYm9ja3p2emFjY2N1Ynouc3VwYWJhc2UuY28vYXV0"
#                          "aC92MSIsInN1YiI6ImE0ZmM2NjI5LTZkYWEtNGJmMC04YmJ"
#                          "hLTI1ODg4YzU5YWQ5YyIsImVtYWlsIjoiZXZnZW5paS50c3"
#                          "RAZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhd"
#                          "GEiOnsicHJvdmlkZXIiOiJlbWFpbCIsInByb3ZpZGVycyI6"
#                          "WyJlbWFpbCJdfSwidXNlcl9tZXRhZGF0YSI6eyJmdWxsX25h"
#                          "bWUiOiLQldCy0LPQtdC90LjQuSJ9LCJyb2xlIjoiYXV0aGV"
#                          "udGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGh"
#                          "vZCI6InBhc3N3b3JkIiwidGltZXN0YW1wIjoxNzEyNjE2MzY"
#                          "yfV0sInNlc3Npb25faWQiOiI3YWM1YzFmYi1lZmRlLTRmNjc"
#                          "tYjg3My02NGIxZmUyMWRkZjIiLCJpc19hbm9ueW1vdXMiOm"
#                          "ZhbHNlfQ.QHdQfapvwBtMY6ry91AdOVjJVfxUV104fBKcd85vqTQ"}
# )
# print(response.status_code)

response = requests.get(
    url=f"{HOST}/users",
    headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzEzODU0MzYyLCJpYXQiOjE3MTMyNTQzNjIsImlzcyI6Imh0dHBzOi8vbXlrb3RxYm9ja3p2emFjY2N1Ynouc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6ImE0ZmM2NjI5LTZkYWEtNGJmMC04YmJhLTI1ODg4YzU5YWQ5YyIsImVtYWlsIjoiZXZnZW5paS50c3RAZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJlbWFpbCIsInByb3ZpZGVycyI6WyJlbWFpbCJdfSwidXNlcl9tZXRhZGF0YSI6eyJmdWxsX25hbWUiOiLQldCy0LPQtdC90LjQuSJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6InBhc3N3b3JkIiwidGltZXN0YW1wIjoxNzEyNjE2MzYyfV0sInNlc3Npb25faWQiOiI3YWM1YzFmYi1lZmRlLTRmNjctYjg3My02NGIxZmUyMWRkZjIiLCJpc19hbm9ueW1vdXMiOmZhbHNlfQ.QHdQfapvwBtMY6ry91AdOVjJVfxUV104fBKcd85vqTQ"}
)
print(response.json())
