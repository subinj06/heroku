from django.shortcuts import render

from django.http import HttpResponse
import pymongo
from pymongo import MongoClient
from datetime import datetime

connecip = 'mongodb+srv://graduate:graduate@graduate.gw2nh.mongodb.net/<dbname>?retryWrites=true&w=majority'
# connecip = 'mongodb+srv://graduate:graduate@graduate-pri.gw2nh.mongodb.net/Graduate?retryWrites=true&w=majority'

cluster = MongoClient(connecip)
db = cluster["graduate"]

pill=db["pill"]
reception=db["reception"]
sell = db["sell"]

allpill = pill.find()
allsell= sell.find()
allrecep = reception.find()


def index(request):
    str1= ' <html><head> <style> header{ background-color:darkcyan; position: fixed; left: 0px; top: 0px; width: 100%; height: 20%; text-align: center; z-index: 3; } header p{ color: white; font-size: 50px; font-weight: 500; text-align: center; } section{ font-size: 30px; position:absolute; top:22%; margin-left:10%; width:90%; z-index: 1; padding-bottom: 10%;} section hr{ width:90%; margin-left: 0; } section p{ font-weight:700; } section table{ width:90%; } section table th{ color:teal; font-size:23px; font-weight: 600; width:25%; text-align: center; } section table td{ width:25%; font-size:20px; font-weight: lighter; color:black; text-align: center; } </style> <title> YG </title> </head> <body> <header><p> Pill Dispenser </p> </header> <section> <p>Pills</p> <hr> <table> <tr> <th>ID</th> <th>Name</th> <th>Stock</th> <th>Unit Price</th> </tr>'
    pillstr=' '
    for pills in allpill:
        pillstr = pillstr+ ' <tr><td> '+ str( pills["_id"] ) + '</td><td>' + pills["name"] + '</td><td> ' + str( pills["stock"] ) + '</td><td>' + str(pills["price"]) +'</td></tr>'

    str2='</table> <p>Sells</p> <hr> <table> <tr> <th>Prescription</th> <th>Pill ID</th> <th>Numbers</th> </tr>'

    sellstr= ' '
    for sells in allsell:
        sellstr = sellstr+ ' <tr><td> '+ str( sells["_id"]['pre_id'] ) + '</td><td>' + str(sells["_id"]["pill"] )+ '</td><td> ' + str( sells["num"] ) + '</td></tr>'

    str3=' </table> <p>Receptions</p> <hr> <table> <tr> <th>ID</th> <th>Prescripted Date</th> <th>Selling Date</th> <th>Total</th> </tr>'
    
    recstr=' '
    for receps in allrecep:
        recstr = recstr+ ' <tr><td> '+ str( receps["_id"] ) + '</td><td>' + receps["pre_date"]+ '</td><td>' + receps["sell_date"] + '</td><td> ' + str( receps["total"] ) + '</td></tr>'

    str4= ' </table> </section> </body> </html>'
    return HttpResponse(str1+pillstr+str2+sellstr+str3+recstr+str4)