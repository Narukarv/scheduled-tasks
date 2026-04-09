import smtplib
import datetime as dt
import random

#Datetime mini resumen

# hoy_ahora = dt.datetime.now()
# hora = hoy_ahora.hour #Hora
# year = hoy_ahora.year #Año
# month = hoy_ahora.month #Mes
# day = hoy_ahora.day #Día
# dia = hoy_ahora.weekday() #Día de la semana (parte de 0)
# date = hoy_ahora.date() #aaaa-mm-dd
#
# day_of_birth = dt.datetime(year=2001, month=9, day=27) #aaaa-mm-dd hh:mm:ss en 00:00:00
# print(day_of_birth)

#SMTPLIP Resumen
# my_email = "ignacio.urrutia.bustos@gmail.com"
# password = "qptpkyuryyozhoxw"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:   #Dar permisos en seguridad de la cuenta.
#     connection.starttls() #Da seguridad a la conexión (encripta)
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="ignacio.urrutiab@yahoo.com",
#         msg="Subject:Hello\n\nThis is a test message"
#     )

# connection.quit() #Necesario si no se abre como with
# connection.close()

my_email = "ignacio.urrutia.bustos@gmail.com"
password = "qptpkyuryyozhoxw"

to_email = "freddy@guerraperez.cl"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
    # print(quote)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ignacio.urrutiab@yahoo.com",
            msg = f"Subject: Monday Motivation!\n\n{quote}"
        )