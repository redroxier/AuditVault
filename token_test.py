from auth import create_token

token = create_token({
    "user_id": "123",
    "tenant_id": "tenant_a"
})

print(token)