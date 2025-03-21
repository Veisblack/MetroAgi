# MetroAgi
Proje adı : MetroAgi

Geliştirici Adı Soyadı : Serkan GEDİKLİ

Projeye bulunduğum katkı : BFS ve A* algoritması geliştirilmesi.

Kullanılan Kütüphaneler : collections,heapq,typing

Metro Ağı projesi 

En az aktarmayı bulmak için arama algoritmaları arasında BFS kullandım.

BFS algoritmasının kullanılmasının nedeni: 
En az aktarmayı yüksek doğrulukta bulmamı sağlayan bir algoritma olması nedeniyle.
Her durak arasını eşit uzaklıkta kabul edip ulaşılacak hedefe giderken katman katman ilerler ve
tüm komşuları dener deneme tamamladıktan sonra hedef noktaya ulaşabilecek en az düğüm sayısını tercih eder.
Bu sebeple BFS algoritmasının kullanılması en ideal çözümdür.

BFS kodumda nasıl çalışır
1-başlangıç istasyonunu kuyruğa ekler ve ziyaret_edildi listesine alır.
2-Kuyruğun başındaki istasyonu çıkartır bu istasyon hedefse rota döndürülür.
3-istasyonun komşuları kontrol edilr.
4-komşu daha önce ziyaret edilmediyse kuyruğa eklenir.
5-hedefe ulaşana kadar devam eder.


En hızlı rotayı bulmak için arama algoritmaları arasında A* kullandım.

A* algoritmasının kullanılmasının nedeni:
En az süreyle ve en az maliyetle belirlenen hedefe ulaşmamı sağlayan algoritma olması nedeniyle.
Her düğümün ve komşu düğümler arası tahmini maliyetle yola çıkarak gerçek maliyetle toplayarak toplam maliyete ulaşır.
Gereksiz düğümleri ziyaret etmez ve zaman kazanır.
En hızlı ve en az maliyetli yolu belirler.

A* kodumda nasıl çalışır
1-Kuyruk oluşturur ilk düğüm pq içine eklenir.
2-En düşük f(n) değerine sahip istasyon seçilir.
3-Eğer istasyon hedef sonuca eşit olmuşsa sonuc döndürülür.
4-Değilse tüm komşular için heutiristik fonksiyonu hesaplanır ve kuyruğa eklenir.
5-hedefe ulaşana kadar süreç devam eder.
