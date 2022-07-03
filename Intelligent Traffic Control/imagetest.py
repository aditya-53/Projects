import os
from imageai.Detection import ObjectDetection
from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)
import random    
@app.route('/success')
def success():
    pathvehicles = r"static\inputs"
    randomimg1=random.choice([x for x in os.listdir(pathvehicles) if os.path.isfile(os.path.join(pathvehicles, x))])
    execution_path = os.getcwd()
    #pathvehicles=os.path.join(execution_path , "static\inputs\image1.jpg")
    detector1 = ObjectDetection()
    detector1.setModelTypeAsTinyYOLOv3()
    detector1.setModelPath( os.path.join(execution_path , "yolo-tiny (1).h5"))
    detector1.loadModel()
    k1=pathvehicles
    k1+="/"
    k1+=randomimg1
    detections1 = detector1.detectObjectsFromImage(input_image=k1, output_image_path=os.path.join(execution_path , "static\outputs34\imagenew1.jpg"))
    c1=0
    print("1st random image:",randomimg1)
    for eachObject in detections1:
        if(eachObject["name"]=="bus" or eachObject["name"]=="truck" or eachObject["name"]=="car" or eachObject["name"]=="motorcycle" or eachObject["name"]=="person"):
            c1+=1
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    print(c1)
    randomimg2=random.choice([x for x in os.listdir(pathvehicles) if os.path.isfile(os.path.join(pathvehicles, x))])
    print("2st random image:",randomimg2)
    k2=pathvehicles
    k2+="/"
    k2+=randomimg2
    detector2 = ObjectDetection()
    detector2.setModelTypeAsTinyYOLOv3()
    detector2.setModelPath( os.path.join(execution_path , "yolo-tiny (1).h5"))
    detector2.loadModel()
    detections2 = detector2.detectObjectsFromImage(input_image=k2, output_image_path=os.path.join(execution_path , "static\outputs34\imagenew2.jpg"))
    c2=0
    for eachObject in detections2:
        if(eachObject["name"]=="bus" or eachObject["name"]=="truck" or eachObject["name"]=="car" or eachObject["name"]=="motorcycle" or eachObject["name"]=="person"):
            c2+=1
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    print(c2)
    randomimg3=random.choice([x for x in os.listdir(pathvehicles) if os.path.isfile(os.path.join(pathvehicles, x))])
    print("3st random image:",randomimg3)
    k3=pathvehicles
    k3+="/"
    k3+=randomimg3
    detector3 = ObjectDetection()
    detector3.setModelTypeAsTinyYOLOv3()
    detector3.setModelPath( os.path.join(execution_path , "yolo-tiny (1).h5"))
    detector3.loadModel()
    detections3 = detector3.detectObjectsFromImage(input_image=k3, output_image_path=os.path.join(execution_path , "static\outputs34\imagenew3.jpg"))
    c3=0
    for eachObject in detections3:
        if(eachObject["name"]=="bus" or eachObject["name"]=="truck" or eachObject["name"]=="car" or eachObject["name"]=="motorcycle" or eachObject["name"]=="person"):
            c3+=1
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    print(c3)
    randomimg4=random.choice([x for x in os.listdir(pathvehicles) if os.path.isfile(os.path.join(pathvehicles, x))])
    print("4st random image:",randomimg4)
    k4=pathvehicles
    k4+="/"
    k4+=randomimg4
    detector4 = ObjectDetection()
    detector4.setModelTypeAsTinyYOLOv3()
    detector4.setModelPath( os.path.join(execution_path , "yolo-tiny (1).h5"))
    detector4.loadModel()
    detections4 = detector3.detectObjectsFromImage(input_image=k4, output_image_path=os.path.join(execution_path , "static\outputs34\imagenew4.jpg"))
    c4=0
    for eachObject in detections4:
        if(eachObject["name"]=="bus" or eachObject["name"]=="truck" or eachObject["name"]=="car" or eachObject["name"]=="motorcycle" or eachObject["name"]=="person"):
            c4+=1
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    print(c4)
    
    return render_template('imagetest.html',c1=c1,c2=c2,c3=c3,c4=c4,k1=k1,k2=k2,k3=k3,k4=k4)
'''@app.route('/login',methods = ['POST', 'GET'])
def login():
    return redirect(url_for('success'))'''
   
if __name__=='__main__':
    app.run(debug=True)
