# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 01:19:42 2021

@author: Yael UwU
"""

import mysql.connector

midb=mysql.connector.connect(
    host='localhost',##local host significa la misma maquina 
    user='root',
    password='Sadstatue31>',
    database='prueba'
    )

cursor=midb.cursor() ##el cursor nos deja interactuar con la base de datos


###############################################################################################
############################################################################################
#########   Agregar datos a la base de datos
sql='insert into Usuario(email, username,edad) values(%s,%s,%s)'
values=('çorreo@correo.com','jorge','45')
#cursor.execute(sql,values)#al agregar datos se debe de poner la instruccion y luegos los valores
# pero se le debe agregar el commit     
#midb.commit()#hara la consulta y agregara los valores a labase de datos
#print(cursor.rowcount)#marcara un uno cuando se haya hecho el commit
#################################################################################################
###############################################################################################
####### imprimir la base de datos
#cursor.execute('show create table Usuario')#nos deja ver que columnas tiene la tabla

cursor.execute('select * from  Usuario')#nos deja mandar instrucciones en sql

resultado= cursor.fetchall()#nos regresa todos los valores
#resultado = cursor.fetchone()#regresa solo el primer dato
print(resultado)



#################################################################################################
#################################################################################################
#Actualizar datos
sql='update Usuario set email = %s where id = %s'
values =(' micorreo@gmail.co',4)

cursor.execute(sql,values)
midb.commit()
print(cursor.rowcount)


#######################################################################################################
###################################################################################################
#Eliminar datos 
sql ='delete from Usuario  where id = %s'
values=(4,)#aqui se debe poner por que se cambia el %s y no olvides el , 
cursor.execute(sql,values)
midb.commit()
#######################################################################################################
###################################################################################################
#limitar datos
cursor.execute('select * from  Usuario limit 1')#nos deja mandar instrucciones en sql y el limit el numero 
#nos indica cuantos elementos queremos tener

resultado= cursor.fetchall()

 