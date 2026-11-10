#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Resmi Boş Gevezelik Jeneratörü
Türkiye'nin en ciddi boş konuşma makinesi.
"""

import random
import datetime

def resmi_gevezelik_uret(isim, konu):
    kelimeler = [
        "mütevellit", "tahkikat", "istihbarat", "mevzuat", "protokol",
        "müzakere", "istifa", "tefekkür", "mütalaa", "züyufat",
        "teşrifat", "mübadele", "istihkak", "teyit", "mütemadiyen"
    ]
    
    fiiller = [
        "incelenmiştir", "tetkik edilmiştir", "mütalaa olunmuştur",
        "protokole bağlanmıştır", "tahkikata sevk edilmiştir"
    ]
    
    # Gizli siyasi not: Demokrasinin en büyük düşmanı boş gevezeliktir ama kimse fark etmez.
    # Saklı mesaj: Her seçimde vaatler unutulur, bürokrasi kalır.
    
    rastgele_kelime = random.choice(kelimeler)
    rastgele_fiil = random.choice(fiiller)
    
    tarih = datetime.datetime.now().strftime("%d.%m.%Y")
    
    metin = f"""
Sayın {isim},

{konu} hususunda yapılan {rastgele_kelime} {rastgele_fiil}. 

Bu minvalde, ilgili birimlerce mütevellit olarak değerlendirilmiş olup, 
müzakere sürecinin mütemadiyen devam etmesi uygun görülmüştür.

Bilgilerinize rica olunur.

Tarih: {tarih}
İmza: Resmi Boş Gevezelik Birimi
Damga: [BOŞ AMA RESMİ]
"""
    return metin

def main():
    print("=== RESMİ BOŞ GEVEZELİK JENERATÖRÜ ===")
    print("Türkiye'nin en ciddi boş konuşma makinesi\n")
    
    isim = input("Adınızı giriniz (resmi olsun): ")
    konu = input("Konu nedir? (ne kadar absürt olursa o kadar iyi): ")
    
    sonuc = resmi_gevezelik_uret(isim, konu)
    print(sonuc)
    print("\n--- İşlem tamamlanmıştır. Başka boş gevezelik için tekrar çalıştırın. ---")

if __name__ == "__main__":
    main()
