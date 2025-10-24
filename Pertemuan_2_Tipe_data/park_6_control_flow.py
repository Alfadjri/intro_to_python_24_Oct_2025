#case
nilai = 60
print("=====if=====")
if nilai >= 100:
    print("Nilai Kamu lulus dengan Sempurna")
print("Tetap masuk sekolah")
print("====if-else===")
nilai = 50
if nilai >= 70:
    print("Kamu lulus dalam ujian ini")
else:
    print("kamu tidak lulus dalam ujian ini")
print("===if-elif-else=====")
nilai = 85
if nilai >= 90:
    print("nilai kamu A")
elif nilai >=80 and nilai < 90:
    print("nilai kamu B")
elif nilai >= 70 and nilai < 80:
    print("Kamu hampir tidak lulus")
else:
    print("Kamu tidak lulus")

print("=====Switch Case======")
print("======Menu=====")
print("1.Start Game")
print("2.Exit")
selection = input("Select => ")
match selection:
    case "1":
        print("Start Game")
    case "2":
        print("Exit Game")
    case _:
        print("invalid input type !!! please select 1 or 2!!!!")