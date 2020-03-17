from firebase import firebase
firebase =firebase.FirebaseApplication('https://tesseract-23.firebaseio.com/',None)
result=firebase.get('patient',"")
for i in result:
    if i is not None:
        print(i['id'])
   