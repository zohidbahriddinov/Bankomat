import os
os.system("cls")
from datetime import datetime
import psycopg2

# s1 = '''CREATE TABLE Bankomat(
#     id SERIAL PRIMARY KEY,            
#     Karta_raqami VARCHAR(16) NOT NULL, 
#     Parol VARCHAR(10) NOT NULL,       
#     Egasining_ismi VARCHAR(100) NOT NULL, 
#     Telifon_r VARCHAR(20) NOT NULL,    
#     Balans NUMERIC(12, 2)
# );'''

# s2 = """
# INSERT INTO Bankomat (Karta_raqami, Parol, Egasining_ismi, Telifon_r, Balans)
# VALUES
# ('8600123456789012', '1234', 'Ali Valiyev', '+998901112233', 150000.50),
# ('9860123456789012', '5678', 'Dilshod Karimov', '+998933334455', 250000.00),
# ('8600987654321098', '4321', 'Madina Rasulova', '+998935556677', 75000.75),
# ('9860765432109876', '8765', 'Javlonbek Umarov', '+998977778899', 500000.00),
# ('8600654321987654', '1111', 'Sevara Xolmatova', '+998941112244', 10000.00);
# """

# Bankomat
          
class Bankomat:
      def __init__(self):
          self.conn = psycopg2.connect(
                dbname="dorixona",
                user = "postgres",
                password = "123",
                host = "localhost",
                port = "5432"
          )
          self.cur = self.conn.cursor()

      def kar_add(self):
          while True:
            Karata_raqami = input("Karta raqamini kiriting: ")
            Parol = input("Parolni kiriting: ")
            Egasining_ismi = input("Egasining ismini kiriting: ")
            Telifon_r = input("Telefon raqamini kiriting (+998778889911): ")
            Balans = input("Balansni kiriting: ")

            if (
                Karata_raqami.isdigit() and len(Karata_raqami) == 16 and
                Parol.isdigit() and len(Parol) == 4 and
                Egasining_ismi.isalpha() and
                Balans.isdigit() and
                Telifon_r.startswith("+998") and len(Telifon_r) == 13 and Telifon_r[1:].isdigit()):
                self.cur.execute("""
                INSERT INTO Bankomat (Karta_raqami, Parol, Egasining_ismi, Telifon_r, Balans)
                VALUES (%s, %s, %s, %s, %s)
                """, (Karata_raqami, Parol, Egasining_ismi, Telifon_r, Balans))
                self.conn.commit()
                print("Ma'lumotlar qo'shildi.")
                break               
            else:
                print("Xato kiritildi! Qaytadan kiriting.")

      def Kartani_tekshir(self, seria):
          self.cur.execute("SELECT 1 FROM Bankomat WHERE Karta_raqami = %s" , (seria,))
          return self.cur.fetchone() is not None
      
      def PIN_tekshirish(self , seria, pin):
          self.cur.execute("SELECT 1 FROM Bankomat WHERE Karta_raqami = %s and Parol = %s" , (seria , pin))
          return self.cur.fetchone() is not None
      
      
      def SMS_xizmati(self , seria):
          print("1. SMS xizmatini yoqish")
          print("2. SMS xizmatini o'chirish")
          tanlov1 = input("Tanlov (1 - 2): ")

        
          if tanlov1 == "1":
               Telifon = input("Telefon raqamingizni kiriting: ")
               if Telifon.startswith("+998") and len(Telifon) == 13 and Telifon[1:].isdigit():
                  self.cur.execute("update Bankomat set Telifon_r = %s where Karta_raqami = %s" , (Telifon , seria))
                  self.conn.commit()
                  print("Telefon raqamingiz muvaffaqiyatli o'zgartirildi.")
               else:
                 print("Telefon raqam noto'g'ri.")
          elif tanlov1 == "2":
               self.cur.execute("update Bankomat set Telifon_r = '' where Karta_raqami = %s" , (seria,))
               self.conn.commit()
               print("SMS xizmati o'chirildi")
          else:
                print("Xato Tanlov?")

      def balance_xizmati(self , seria):
          print("1. Hozirgi balansni ko'rish")
          print("2. Pul yechish")
          print("3. Pul qo'shish")

          hozirgi_vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
          tanlov = input("Tanlov (1 - 3): ")

          if tanlov == "1":
             self.cur.execute("select Balans from Bankomat where Karta_raqami = %s", (seria,))
             balans = self.cur.fetchone()[0]
             print(f"Balans: {balans} so'm")
          elif tanlov == "2":
           miqdor = int(input("Qancha yechmoqchisiz kiriting: "))
           self.cur.execute("select Balans from Bankomat where Karta_raqami = %s", (seria,))
           balans = float(self.cur.fetchone()[0])


           if balans >= miqdor:
                    xizmat_haqi = round(miqdor * 0.01)
                    yangi_b  = balans - (miqdor + xizmat_haqi)
                    self.cur.execute("update Bankomat set balans  = %s where  Karta_raqami = %s" , (yangi_b , seria))
                    self.conn.commit()
                    print(f"{miqdor} so'm yechildi, xizmat haqi: {xizmat_haqi} so'm.")
                    print(f"Yangi balans: {yangi_b} so'm.")
                    print(hozirgi_vaqt)
                    print("Marhamat, pulni oling.")
           else:
                    print("Pul yetarli emas")
                
          elif tanlov == "3":
                miqdor = int(input("Balansga qo'shiladigan summani kiriting: "))
                xizmat_haqi = round(miqdor * 0.01)
                self.cur.execute("select balans from Bankomat where Karta_raqami = %s" , (seria,))
                balans = float(self.cur.fetchone()[0])
                yangi_b = balans + miqdor - xizmat_haqi
                self.cur.execute("update Bankomat set balans  = %s where  Karta_raqami = %s" , (yangi_b , seria))
                self.conn.commit()
                print("Pul muvaffaqiyatli qo'shildi.")
          else:
                print("Xato tanlov?")
      def PIN_ozgartirish(self , seria):
                 while True:
                   yangi = input("Yangi PIN-kodni kiriting (faqat raqamlar): ")
                   if yangi.isdigit() and len(yangi) == 4:
                      self.cur.execute("UPDATE Bankomat SET PAROL = %s WHERE Karta_raqami = %s" , (yangi, seria))
                      self.conn.commit()
                      print("PIN muvaffaqiyatli o'zgartirildi.")
                      break
                   else:
                    print("PIN faqat raqamlardan iborat bo'lishi kerak. Qayta urinib ko'ring.")
      def close(self):
          self.cur.close()
          self.conn.close()
   
       
def menyu(b , seria):
    while True:
        print("\n--- Bankomat menyusi ---")
        print("1. Telefon raqamini o'zgartirish")
        print("2. Balans xizmatlari")
        print("3. PIN kodni o'zgartirish")
        print("4. Chiqish")

        tanlov = input("Tanlov (1 - 4): ")

        if tanlov == "1":
            b.SMS_xizmati(seria)
        elif tanlov == "2":
            b.balance_xizmati(seria)
        elif tanlov == "3":
            b.PIN_ozgartirish(seria)
        elif tanlov == "4":
            print("Bankomatdan chiqildi.")
            break
        else:
            print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")

if __name__ == "__main__":
    
    b = Bankomat()
    n = int(input("Yaratmoqchi bo'lgan kartalar sonini kiriting: "))

    for i in range(n):
        print(f"{i + 1} karta")
        b.kar_add()
        
    print("<<<<<<<<<<<< Bankomatga hush kelibsiz >>>>>>>>>>>>>>")
    seria = input("Karta raqamini kiriting: ")

    if not b.Kartani_tekshir(seria):
        print("Karta mavjud emas")
        exit()

    h = False
    i = 0
    while i < 3:
        pin = input("PIN kodni kiriting: ")
        if b.PIN_tekshirish(seria, pin):
            print("PIN to'g'ri.")
            h = True
            break
        else:
            print("Xato PIN kod!")
            i += 1

    if not h:
        print("3 marta noto'g'ri PIN. Xayr!")
        exit()

    menyu(b , seria)
    b.close()

