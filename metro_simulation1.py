from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        #Geliştirilen BFS algoritması
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar: #Başlangıç ve hedef istasyonların varlığını kontrol ediyorum belirlenen parametre yoksa None döndürüyorum.
           return None
        
        baslangic = self.istasyonlar[baslangic_id] #Başlangıç ve hedef istasyonları belirliyorum.
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = {baslangic}               #Ulaşılan istasyonları ziyaret edildi setine ekliyorum.
        kuyruk = deque([(baslangic, [baslangic])]) #Kuyruk oluşturuyorum.
        
        while kuyruk:                           #Kuyruk boş olana kadar döngüyü devam ettiriyorum. boş ise None döndürüyorum.
            istasyon, rota = kuyruk.popleft()   #kuyruğun başındaki elemanı kuyruktan çıkartıyorum.Belirlenen parametrelere tanımlıyorum.
            
            if istasyon == hedef:               #Eğer istasyon hedefe eşitse rotayı döndürüyorum.
                return rota
            for komsu, _ in istasyon.komsular:  #İstasyonun komşularını dolaşıyorum. _ süre olduğu için süreyi kullanmıyorum.
                if komsu not in ziyaret_edildi: #Eğer komşu ziyaret edilmediyse ziyaret edildi setine ekliyorum ve kuyruğa ekliyorum.
                    ziyaret_edildi.add(komsu)
                    kuyruk.append((komsu, rota + [komsu]))
        return None
    
    #Heuristik fonksiyonu
    def heuristik(self, istasyon: Istasyon, hedef: Istasyon) -> int:   #istasyon ve hedef istasyon aynı hat üzerinde mi kontrol ediyorum.
        return 0 if istasyon.hat == hedef.hat else 2                   #Eğer aynı hat üzerinde ise 0 döndürüyorum değilse 2 döndürüyorum.
    
    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        #Geliştirilen A* algoritması
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = set()
        pq = [(0, id(baslangic), baslangic, [baslangic])] #Öncelikli kuyruk oluşturdum başlangaç düğümünün bilgilerini ekledim.

        while pq:
            sure, _, istasyon, rota = heapq.heappop(pq)   #En düşük süreye sahip düğümü alır. _ parametresi id(istasyon) için kullanılır burada gereksizdir.
            if istasyon == hedef:                         #İstasyon ve hedef eşitse rotayı ve süreyi döndürür
                return rota, sure
            if istasyon in ziyaret_edildi: 
                continue
            ziyaret_edildi.add(istasyon)                  #mevcut istasyonu ziyaret edildi olarak işaretliyorum
            for komsu, komsu_sure in istasyon.komsular:   #her komşunun bağlantı süresini alıyorum
                if komsu not in ziyaret_edildi:           #komşu daha önce ziyaret edilmediyse Heuristik değeri hesaplar ve öncelikli kuyruğa yeni güzergah ekler.
                    heuristik_deger = self.heuristik(komsu, hedef)
                    heapq.heappush(pq, (sure + komsu_sure + heuristik_deger, id(komsu), komsu, rota + [komsu]))
        return None

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 