# character in string has index number
          # 01234567890123
infoA = ' Hi PIZZA MK SUSHI '
          # 43240987654321 ติดลบ ( - )
print(infoA[6])
print(infoA[-9])

# เข้าถึงตัวอักษรหลายๆ ตัวใน string เราจะใช้วิธี slingcing ด้วย index number
# Z M
print(infoA[6:9])
print(infoA[-8:-5])

# ZZA K S
print(infoA[4:12])
#PIZZA MK
# string Method
print(infoA.upper()) #ทำให้ string เป็นตัวพิมพ์ใหญ่
print(infoA.lower()) #ทำให้ string เป็นตัวพิมพ์เล็ก
print(infoA.capitalize()) #ทำให้หน้าประโยคเป็นพิมพ์ใหญ่
print(infoA.count("S")) #นับstring
print(infoA.isdigit()) #Method is เอาไว้พิสูจน์บางใดบางอย่าง
print(infoA.isupper()) #พิสูจน์ ว่าตัวพิมพ์ใหญ่หมดมั้ย
print(infoA.title()) #ทำให้ตัวหน้าเป็นพิมพ์ให้
infoB = infoA.replace("PIZZA","SUSHI") #ใช้แทน string ที่อยากแทนที่
print(infoB)
print(infoA.replace('Hi','MK'))

#string function
print(len(infoA)) #ใช้นับตัวอักษรทั้งหมด ใน info ที่ต้องการให้แสดง

print('PIZZA',35) #PIZZA 35
print('PIZZA'+str(35)) #PIZZA35
print('PIZZA',35,sep='') #PIZZA35
print('10','06','2003',sep='/')
print(10,'มิถุนายน',2003,sep='-')
