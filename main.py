"""
เขียนโปรแกรมสร้างเกม RPG โดยใช้ dict 
เก็บข้อมูลของตัวละครผู้เล่น โดยใช้ for loop วนซ้ำเพื่อแสดงข้อมูลของตัวละครผู้เล่นออกมา
"""
# กำหนดค่าให้ตัวแปรเป็นประเภท Dict เครื่องหมาย ? ให้ใส่ข้อมูลเข้าไปแทนที่เอง
player = {
     "name": "Andy",
     "Level": 99,
     "Life Points": 99,
     "Attack Points": 99,
     "Defense Points": 99,
}

# วนซ้ำเพื่อเข้าถึงรายการใน Dict ใช้ .items()
for k,v in player.items():
    print(f"{k} is {v}")