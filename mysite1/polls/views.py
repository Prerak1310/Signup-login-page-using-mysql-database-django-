from django.shortcuts import render,redirect
from django.contrib import messages
import mysql.connector as mysqlcon
import cv2 as cv
mydb=mysqlcon.connect(host='localhost',user='root',password='123456789',database='profile')
mycursor=mydb.cursor() 


def index(request):
    if request.method=='POST':
        user=request.POST['username']
        passw=request.POST['password']
        if user and passw is not None:
          if Profile.objects.filter(username=user,password=passw).exists():
            return redirect('checkout')         
                
          else:
            messages.info(request,'pls enter correct credentials')
            return redirect('/')
        else:
            messages.info(request, 'pls fill all the details')
            return redirect('/')
    return render(request,'home.html')



def checkout(request):
    vid=cv.VideoCapture(0)
    while True:
        isTrue, frame=vid.read()
        cv.imshow('Webcam',frame)
        if cv.waitKey(20) & 0xFF==ord('q'):
            break
    vid.release()
    cv.destroyAllWindows() 
    return redirect('/')
    
  


    
def signup(request):   
    if request.method=='POST':
        d=request.POST
        for key,value in d.items():
            if key=='username':
                namet=value
            if key=='email':
                emailt=value
            if key=='password':
                passwt=value
            if key=='password1':
                passwt1=value
        mycursor.execute("select * from profile_table where name='{}' or email='{}'".format(namet,emailt))
        a=mycursor.fetchall() 
        t=tuple(a)    
        print(t) 
         
        if passwt == passwt1:     
            if t==():
               mycursor.execute("insert into profile_table values('{}','{}','{}','{}')".format(emailt,namet,passwt,passwt1))
               mydb.commit()
               return redirect('/')
            if t!=() :  
                if f"{namet}" in t[0]:       
                    messages.info(request, 'Username Taken')
                    return redirect('signup')
                elif f"{emailt}" in t[0]:
                    messages.info(request, 'Email Taken')
                    return redirect('signup')                            
                
        else:
            messages.info(request,'passwords dont match')

    return render(request, 'signup.htm')



def webcam(request):
    return render(request,'webcam.html')