
#抓公開資訊網的資料
import requests
import time
import requests
import json
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties
# 在tkinter 上 作圖
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def crawStock():

     # date&stockNo
     # 從 tkinter 放入變數
     date =  date_input.get() #"20210107" 
     stockNo =  stockNo_input.get() #"2330" 
     df = pd.DataFrame() 
     
     closing_price_price=[]
     closing_price_date=[]  
     
     url="https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date="+ date +"&stockNo="+ stockNo
     
     print(date,stockNo)
     try :

          res=requests.get(url)
          
          print(res)
     except Exception as e :
          pass
          
     else :
          time.sleep(0.5)
          # print("time.sleep 0.5 sec")
     # 資料包成json
     s =json.loads(res.text) #,encoding='utf8') 
     closing_price_values=list(s.values()) 
     
     #日期跟收盤價的dataframe 
     for i in range(len(closing_price_values[4])):
          closing_price_price.append(float(closing_price_values[4][i][6]))
          closing_price_date.append(closing_price_values[4][i][0])
          i +=1 
     
     #公司名
     stock = closing_price_values[2].split(' ',3)  
     title = stock[1]+stock[2] #1是代碼、是公司名
     
     # 收盤價跟日期裝成df
     df = pd.DataFrame(data = closing_price_price,index = closing_price_date, columns= [title])

     # 做圖      
     # 設定趨勢圖中文字
     font_path =  FontProperties(fname='TaipeiSansTCBeta-Regular.ttf',size = 20)
     
     
     crawStock.f.clf() # intital 
     crawStock.a = crawStock.f.add_subplot(111) # 一行一列一個
     # 取當月資料 做趨勢圖
     crawStock.a.plot(df,
          linewidth = 2.0,
          linestyle = '-',
          marker = 'o',
          label = title
          ) 
     # 標題、圖例與調整
     crawStock.a.set_title("{} {}月 趨勢圖".format(title,date[4:6]),fontweight="bold",fontproperties = font_path)
     crawStock.a.legend(prop=font_path)
     crawStock.a.tick_params(axis='both', which='major', labelsize=20)

     import matplotlib.ticker as mticker
     tick_spacing = df.index.size/5 # x軸密集度
     crawStock.a.xaxis.set_major_locator(mticker.MultipleLocator(tick_spacing))   
     
     crawStock.canvas.draw()
     
     


def main():
     global date_input,stockNo_input # 將變數做成全域，之後要丟給crawler

     background = Tk()
     background.title('月股價趨勢圖') #設置視窗標題名稱
               
     background.geometry('515x380') #調整視窗大小
     # 建立 框架一
     frame1 = Frame(background, width = 500, height=100,bg = None)
     frame1.grid(row=0,sticky='ew')
     ## 文字建立 運用 label()

     Label(frame1, text = '請輸入個股代號：', font = ("微軟正黑", 20), fg = 'black',bg = None).grid(column = 0,row=0,padx = 40,sticky=W)  # sticky= WEST 東西南北
     Label(frame1, text = '請輸入日期：', font = ("微軟正黑", 20), fg = 'black',bg = None).grid(column = 0,row=1,padx = 40,sticky=W)

     # 建立 使用者輸入之變數，之後要傳進
     today = datetime.now()
     yyyymmdd = today.strftime("%Y%m%d")
     
     date_input =Entry(frame1)
     date_input.insert(0,yyyymmdd) # 預設值為今天
     stockNo_input =Entry(frame1)
     stockNo_input.insert(0,'2330') # 預設值為2330
          
     ## gird() 設置在畫面上
     stockNo_input.grid(column = 1,row = 0,sticky='e')
     date_input.grid(column = 1,row = 1,sticky='e')


     # 建立 框架二
     frame2 = Frame(background, width = 500, height=250,bg = 'gray')
     frame2.grid(row=1,padx = 3,pady=3,sticky='nsew')
     
     ## 放置圖的地方
     crawStock.f = Figure(figsize = (10, 5),dpi =50) 
     crawStock.canvas = FigureCanvasTkAgg(crawStock.f, frame2)
     crawStock.canvas.draw()
     crawStock.canvas.get_tk_widget().grid(padx = 3,pady=3,sticky=E+W)
          

     # 建立 框架三
     frame3 = Frame(background, width = 500, height=50,bg =None)
     frame3.grid(row=3,sticky='ew')
     
     ## command= crawStock
     fr3_left =Frame(frame3, width = 250, height=50,bg = None).grid(row = 0,column = 0,sticky='e')
     fr3_right =Frame(frame3, width = 250, height=50,bg = None).grid(row = 0,column = 1,sticky='w')
     Button(frame3, text = "生成圖", font = ("微軟正黑", 15) ,width = 15,command= crawStock).grid(row = 0,column = 0,sticky='ns')
     Button(frame3, text = "離開", font = ("微軟正黑", 15),width = 15, command = background.destroy).grid(row = 0,column = 1,sticky='ns')
          

     background.mainloop()






main()