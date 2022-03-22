# tkinter_with_stock_line


## crawler
```python
crawStock()
```
- 目標網站：
     - www.twse.com
- 目標資料：
     - 日收盤價
- 趨勢線圖呈現

     可能需要事先下載字體
     
     ```
     # 下載台北思源黑體並命名taipei_sans_tc_beta.ttf
     !wget -O TaipeiSansTCBeta-Regular.ttf
     ```

## tkinter 
```
main()
```

>  生成前

![image](./pic/pic1.png)

>  生成後

![image](./pic/pic2.png)



# 打包

## pyinstaller 

- 問題
OSError: Python library not found: Python3, Python, libpython3.8.dylib, .Python, libpython3.8m.dylib
解決：https://www.wandouip.com/t5i295394/