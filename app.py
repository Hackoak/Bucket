# import json

# import requests

# headers = {"Authorization": "Bearer ya29.a0ARrdaM8h8u89vkmjUgQ8bmpSZG9Jeixp0HmOV3XMunD1rlhTGqx4T541JIUnyUR1o-KMm-Tf8OvXpmHLIBsZMc55BaT5jMZ7BTJ3jkYMAHtp1MKM10kV4qsepN_0g_kdQP-nbrB_1wn9V_4o7bVS0mzZqOYG"}
# para = {
#     "name": "Capture.png",
#     "parents": ['1Z28Y2bB-lKn1zpIf7hAs3NL2eClD_EVB']
# }
# files = {
#     'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
#     'file': open("./Capture.png", "rb")
# }
# r = requests.post(
#     "https://www.googleapis.com/drive/v3/files/",
#     #     "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
#     headers=headers,
#     #     files=files
# )
# print(r.text)

import os

# -------------------------------------------------------------------------------
# Youtube ->  https://www.youtube.com/watch?v=gLyaR3KPYt4
# -------------------------------------------------------------------------------
# Imports
import pyrebase

# -------------------------------------------------------------------------------
# Variables & Setup

# filelist = [ f for f in os.listdir(".") if f.endswith(".JPG") ]
# for f in filelist:
#     os.remove(os.path.join(".", f))

# config = {
# "apiKey": "Your API Key",
# "authDomain": "Your auth domain",
# "databaseURL": "https://connectiontopython.firebaseio.com",
# "projectId": "connectiontopython",
# "storageBucket": "connectiontopython.appspot.com",
# "serviceAccount": "serviceAccountKey.json"
# }
bucket = {
    "type": "service_account",
    "project_id": "bucket-ee4ae",
    "private_key_id": "2c3f8d079038ed9922449d7abe938b3ee343aae6",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQD38yNgfq17vcjq\nXEzqX5DKP2bC22XRRE7JM4MbtcIWrPM1q1vAL4SqRIllbVPVnflgKE954PDvvwUX\nt4gAaQlVBicjYWPWUWhhUnc1s3OESsrn/HP3bBOXe/4xk0fA7a789hqqrkDtrF32\nhhq6PYBVnvMMZqR4CKL1/hXQwC/nqEtnv1aakRjx1M/07gUZu1ThrsTLI7nLw/ur\ncNdB3GCXMoY3SdsCzliOJI15TZnXq8nNIDBKhHOqFH1S+QDM9hha/qq3muYaPl8D\ng3EFCH2EdilnASRaFBQilQlnXKNRJ2PrDLs67rONl6ZLdwhCEPhyQ1PtG8laOxxn\nPrF3dLtBAgMBAAECggEAARZSqDTXchPpDJ7AQtxH3ig/vTFauHuMSOPuHVTmPWwf\ncZxYpo3mDu3MASjZShMinflpdORam44lr3p7iboDc3ZDLAjQ1Sl4OCc1O+EjGkJl\nskbkpo24fbnTL2uN/reR53468bQaFJlwP6w0f27sVH9qvlFEiVnW46HJTz9J8Kq5\n8h3YjN50wjVjN+G8hRw+GVgCkRdnVv9CB9vnkWe086FaUfh7lzQ42ep9oor5SSI8\nc4mS5oQnc4NbXYXH8QijJatB+BjKldutm5BJ0b5OyjCW91mqwx30QPIWip1CUY/U\nW3I6NCuI5nnP0/+c0nEQMNFHM3CS1Ka6HxD95rsfQQKBgQD8HzeKBAUl5vh0V4PS\nNruIphI7yj6J/2ktR3G49eE3YcLBf0542C45ZhOGeJqj8nWoE2i7VmHhckGfb3e4\nqBg2zWhq/tONYFfWqfNV3LksjS8Be/QQqfsZcTlEpci0een83iXlc/ngZ8WJtKfs\nJNf6iohGuRlTxYa+MrgVEBjBqQKBgQD7w34NtnMs14v2YlWs0+d6KBPT6Dh2Tgyh\nA8K6AH/S5nIpQmcASg2l4H5GJIUc1dhQQHTmf4vNZGAirE2vPlkQK/X5WigBFicm\nds+VLTfCjWnsH0pdap7YM1y2HqXPVZwRSE+zfVQ+7png/VnWqPJLMSxWBNVFRjeb\niNBByIXb2QKBgQDlCTbbGmvS0tBCYH5QKYiTysolpsTJeE2D5LNa44OFXDogrhYL\nkdfsLN7v+gABj/Fyjq9GAGNK+xDCVfDcv1e/8To6eOSWOj+RszJrfeh6oIdjQcem\nm8SQiFsOEc0Spu352ZVzrLgDNEIvpv4leBL8d3z1QpHPmFGf11ODTuwugQKBgQDY\nM9GURRIzeAch1uBsQq2OIcylNc8HCY+e1nPq93LN0khHVlbN0MpXoKnP4pzNXncc\ns72wE+giwggsvnsX+xrQ4G+jauDfzf5g8bbiDKrN0FMeCuD5yA4Q7Eq5uyf5HTOh\nQ8/t+7rVMGHE7MyxovQvzlKcrBnaG6q1TpBJbcJGQQKBgQDBoY5uPplKTSynT1by\n8bQ7K3KWZNHvIPlOoffmKiDViONOlyfl+6joTEMhlJKKfw09G1pjLlrIJc6fr67D\nNaJ7X0Ou2VbukpZR8lrCw/yqOnssnOJsvE92x0JIddiarByCyIlIbtbhBnL7FGh8\nyRo0dpzYzZ4YZSErDIxN+jClFQ==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-ed7kx@bucket-ee4ae.iam.gserviceaccount.com",
    "client_id": "117049455184473964802",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ed7kx%40bucket-ee4ae.iam.gserviceaccount.com"
}
config = {

    "apiKey": "AIzaSyCoFYb5VuIdAEh-AJDBn9R8sXpiEXpOzf8",

    "authDomain": "bucket-ee4ae.firebaseapp.com",

    "projectId": "bucket-ee4ae",

    "databaseURL": "https://bucket-ee4ae.appspot.com",

    "storageBucket": "bucket-ee4ae.appspot.com",

    # "serviceAccount": "bucket.json"

    #   messagingSenderId: "103023190629",

    #   appId: "1:103023190629:web:e4e1ce4a6774a873b5dc8c",

    #   measurementId: "G-2QDW75T3PR"

}


firebase_storage = pyrebase.initialize_app(config)
auth = firebase_storage.auth()
storage = firebase_storage.storage()

# -------------------------------------------------------------------------------
# Uploading And Downloading Images
user = auth.sign_in_with_email_and_password("h@g.com", "Pass@1234")
# print(user)
# if f.endswith(".JPG")
filelist = [f for f in os.listdir()]
for f in filelist:
    print(f)
    # os.remove(os.path.join(".", f))
# dl = storage.child().list_files()  # (user["idToken"])
# print(dl)
# .put("Capture.JPG")
# storage.child("PlayingGuitar.JPG").download("PlayingGuitar.JPG")

# all_files = storage.list_files()

# for file in all_files:
#     print(file.name)
# file.download_to_filename(file.name)
