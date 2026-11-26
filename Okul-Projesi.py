#------------------------------------------------------------
#------------------FULL ADDER SİMÜLATER----------------------
#--(SANAL KAPILARI KULLANARAK İKİ 4-BİT TAM SAYI TOPLAYICI)--
#------------------------------------------------------------
#---MANTIK KAPILARI---
def AND(a,b):
    return (a and b)#"VE" mantık kapısı için Python fonksiyonu

def OR(a,b):        #"VEYA" mantık kapısı için Python fonksiyonu
    return (a or b)

def XOR(a,b):       #"YADA" mantık kapısı için Python fonksiyonu
    return(a ^ b)

#---HALF ADDER--- #İKİ BİTİ TOPLAYAN FONKSİYON
def half_adder(a,b):                   
  
  toplam_Biti = XOR(a,b)   #İki bit'in toplanıp sonucu değişkende tutulduğu kısım
  elde_Biti = AND(a,b)     #Eldeyi oluşuyorsa sonucu değişkende tutulduğu kısım
  
  return toplam_Biti,elde_Biti

#---FULL ADDER---#ELDE BİTİNİDE TOPLAMA ALABİLEN BİT TOPLAMA FONKSİYONU
def full_adder(a,b,elde):

    toplam1,elde1 = half_adder(a,b)         #Bitlerin toplandığı ve elde bitinin bulunduğu ilk half adder toplama işlemi   
    toplam2,elde2 = half_adder(toplam1,elde)#Bitlerin toplama sonucuna elde bitininde katıldığı ikinci half adder toplama işlemi
    
    elde = OR(elde1,elde2)
    return toplam2,elde

#---KULLANICIDAN SAYILARI İSTEME---
sayi1 = input("Birinci sayiyi giriniz (4-Bitlik ikilik sayi): ") #Kullanıcıdan iki tane 4-bitlik 2'lik sayı istenir
sayi2 = input("İkinci sayiyi giriniz (4-Bitlik ikilik sayi): ")

#---YANLIŞLIK KONTROLÜ---   
if (OR((len(sayi1) != 4),(len(sayi2) != 4))):                                     
    print("Lütfen 4 bitlik sayilar giriniz!!(Programi baştan başlatin)")
    exit()            
#Sayılar 4 bit'lik mi kontrol edilir eğer değilse programdan çıkılır ve baştan başlatma istenir

for bit in sayi1:
    if (AND((bit != '1'),(bit != '0'))):
        print("Sayi1 hatali Sadece 1 ve 0 rakamlarini kullaniniz!!(Programi baştan başlatin)")
        exit()
for bit in sayi2:
    if (AND((bit != '1'),(bit != '0'))):
        print("Sayi2 hatali Sadece 1 ve 0 rakamlarini kullaniniz!!(Programi baştan başlatin)")
        exit()
#Sayılarda uygun rakamlar kullanılmış mı kontrol edilir eğer değilse programdan çıkılır ve baştan başlatma istenir


#---TOPLAMA İŞLEMİ---

eldeBiti_Final = 0   #Final eldesini ve Toplama işlemi final sonucunu saklamak için iki değişken
sonuc = ""

for t in range(3,-1,-1):#İki 4-bitlik tam sayıyı sağdan başlayarak döngü ile aynı bitteki sayıları toplama işlemine alınan kısım
    toplamFinal,eldeBiti_Final = (full_adder(int(sayi1[t]),int(sayi2[t]),eldeBiti_Final))
    sonuc = str(toplamFinal)+sonuc


#---SONUÇLARI YAZDIRMA--- 
print("Toplama İşleminizin Sonucu: ",sonuc) #Sonuç değişkeni ile toplama işleminin final sonucunun yazılması
if(eldeBiti_Final == 1):
    print("Oluşan Nihai Sonucunuz: ",str(eldeBiti_Final)+sonuc) #Eğer elde biti varsa nihai bitle sonucun yazılması
    print("Oluşan Nihai Elde(TAŞMA) Bitimiz: ",str(eldeBiti_Final)) #Nihai bitin yazılması(gösterimi)