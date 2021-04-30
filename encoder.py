import base64



CLIENT_ID = "5j14aDZDG1y35124iAoAH5o5z2hr8DHzEYoubmOy"
CLIENT_SECRET = "K2t96X0bNzMnEtvNVLogndSqdPkD89Gr05O5JgX4mVad5XRqu9Vd0816S2CY2997MVnEoNaZDkIJXe589mGz05MW7r7Bnht7RtNQUWUS5oQXRlXYu2Tif32ZdwSehS7g"

def main(client_id,client_secret):
    credentials = f"{client_id}:{client_secret}"
    print(credentials)
    encrypted_credentials = base64.b64encode(credentials.encode("utf-8"))
    print(encrypted_credentials)




if __name__ == "__main__":
    main(CLIENT_ID,CLIENT_SECRET)