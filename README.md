# Starmap

Starmap yıldızların gökyüzündekini konumlarını istenilen tarihte ve konumda görüntülemeye yarayan bir programdır. Programa dahil olan yıldız haritalarının formatı "[XEphem database file](https://www.mmto.org/obscats/edb.html)" ve dosya uzantısı ".edb"dir. Program şu anda aşağıdaki iki tane katalog dosyasını kullanıyor.
* [Yale Bright Star Catalog](http://tdc-www.harvard.edu/catalogs/bsc5.html) (1991)
* Messier Catalog (2005)

Yıldızların gökyüzündeki pozisyonunu çizmek ve SVG formatında görüntülemek için ise [star-charts](https://github.com/codebox/star-charts) isimli kütüphaneyi kullanıyor.

## Query Strings

Programı çağırırken kullanabileceğiniz parametreler aşağıda verilmiştir

| Parametre | Açıklama |
| ------ | ------ |
| date | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) formatında tarih. Verilmezse güncel tarihi alır. Örn.: 2017-07-07T12:00:00Z|
| lat | Enlem bilgisi. Varsayılan İstanbul'a ait: 41.015137 |
| lon | Boylam bilgisi. Varsayılan İstanbul'a ait: 28.979530 |
| elevation | Yükseklik bilgisi. Varsayılan: 0 |
| mag_min | Çizime dahil olacak en düşük yıldız parlaklığı. Parlaklık azaldıkça değer artar. Varsayılan: 4 |
| mag_max | Çizime dahil olacak en yüksek yıldız parlaklığı. Eksi değerler alabilir. Varsayılan: 0 |

### Çalışma Yöntemi

Gelen isteğe ait tarih ve konuma göre yıldızların pozisyonları EDB veritabanları ve pyephem kütüphanesi yardımıyla hesaplanır. Yıldızların pozisyonları hesaplandıktan sonra bu pozisyonlar star-charts kütüphanesinin istediği formata edb_converter ile çevrilir. İstenilen formata çevirildikten sonra star-charts kütüphanesi yardımıyla SVG dosyası oluşturulur ve gösterilir.
