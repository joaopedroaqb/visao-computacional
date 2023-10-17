import cv2
import face_recognition as fr

imgJP = fr.load_image_file('jp.jpg')
imgJP = cv2.cvtColor(imgJP, cv2.COLOR_BGR2RGB)
imgJPTest = fr.load_image_file('jpTest.jpg')
imgJPTest = cv2.cvtColor(imgJPTest, cv2.COLOR_BGR2RGB)


face_locations = fr.face_locations(imgJP)

if face_locations:  
    faceLoc = face_locations[0]
    cv2.rectangle(imgJPTest, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 255, 0), 2)

    encodeJP = fr.face_encodings(imgJP)[0]
    encodeJPTest = fr.face_encodings(imgJPTest)[0]

    comparacao = fr.compare_faces([encodeJP], encodeJPTest)
    distancia = fr.face_distance([encodeJP], encodeJPTest)

    print(comparacao, distancia)
else:
    print("No faces found in the image.")

cv2.imshow('JP', imgJP)
cv2.imshow('JPTest', imgJPTest)
cv2.waitKey(0)
