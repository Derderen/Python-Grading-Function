def grade(nilai):
    if nilai > 80 :
      return "A"
    elif nilai >= 73 and nilai <= 79:
      return "B+"
    elif nilai >= 69 and nilai <= 72:
      return "B"
    elif nilai >= 57 and nilai <= 68:
      return "C+"
    elif nilai >= 52 and nilai <= 56:
      return "C"
    elif nilai >= 42 and nilai <= 51:
      return "D"
    elif nilai < 42:
      return "E"
    if nilai > 100:
      grade(int(input("Masukkan Nilai : ")))

grade(int(input("Masukkan Nilai : ")))