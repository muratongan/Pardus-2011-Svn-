package net.zemberek.yapi.kok;

import net.zemberek.yapi.HarfDizisi;
import net.zemberek.yapi.ek.Ek;

import java.util.HashSet;
import java.util.Set;

/**
 * Koke ilskin ozel durumu ifade eder. kok ozel durumlarinin farkli ozlelikleri
 * bu sinifta belirtilir. Dogrudan uretilmez, once Uretici ic sinifi olusturulmasi gerekir.
 */
public class KokOzelDurumu {

    /**
     * tip  bilgisi bu ozel duruma iliskin cesitli kimlik bilgilerini tasir.
     * onegin ozel durumun adi, indeksi, ek dizisi gibi.
     * dile gore farkli tip gerceklemeleri mevcttur.
     */
    private KokOzelDurumTipi tip;

    /**
     * bazi ozel durumlar sadece bazi eklerin koke eklenmesi ile olusur. Bu listede
     * bu ekler yer alir.
     */
    protected Set<Ek> gelebilecekEkler = new HashSet<Ek>();

    /**
     * Eger ozel durum kokun yapisini bozuyorsa true.
     */
    protected boolean yapiBozucu = false;

    /**
     * bazi ozel durumlarin olusmasi mevburi degildir. ornegin turkiye turkceisnde
     * "icerlerde" ve "icerilerde" kelimeleri dogru kabul edilir. Eger ozel durum
     * bu sekilde ise secimlik=true olur.
     */
    protected boolean secimlik = false;

    /**
     * Ek kisitlayici ozel durumlar genellikle kokun yapisini bozmaktansa kendisinden sonra
     * bazei eklerin gelmesini engeller.
     */
    protected boolean ekKisitlayici = false;

    /**
     * Cogu kok bozucu ozel durum sadece kendisinden sonra sesli ile baslayan
     * bir ekin glmesi ile olusur. but bayrak bu tyur ozel durumlar icin true olur.
     */
    protected boolean sesliEkIleOlusur = false;

    /**
     * bu sinif KokOzelDurumu uretimi icin kullanilir. Bu sinif sayesinde
     * hem verilere dogrudan setter erisimi kisitlanir hem de esnek ilklnedirme saglanir.
     */
    public static class Uretici {

        private Set<Ek> gelebilecekEkler = new HashSet<Ek>();
        private boolean sesliEkIleOlusur = false;
        private boolean yapiBozucu = false;
        private boolean secimlik = false;
        private boolean ekKisitlayici = false;
        private KokOzelDurumTipi tip;

        public Uretici(KokOzelDurumTipi tip) {
            this.tip = tip;
        }

        public Uretici gelebilecekEkler(Set<Ek> ekler) {
            this.gelebilecekEkler = ekler;
            return this;
        }

        public Uretici sesliEkIleOlusur(boolean deger) {
            this.sesliEkIleOlusur = deger;
            return this;
        }

        public Uretici yapiBozucu(boolean yapiBozucu) {
            this.yapiBozucu = yapiBozucu;
            return this;
        }

        public Uretici secimlik(boolean secimlik) {
            this.secimlik = secimlik;
            return this;
        }

        public Uretici ekKisitlayici(boolean ekKisitlayici) {
            this.ekKisitlayici = ekKisitlayici;
            return this;
        }

        public Uretici parametre(KokOzelDurumTipi tip) {
            this.tip = tip;
            return this;
        }

        public KokOzelDurumu uret() {
            return new KokOzelDurumu(this);
        }
    }

    /**
     * KokOzelDurumu uretici nesnesi uzerinden uretilir. dogrudan erisim yoktur.
     *
     * @param uretici
     */
    protected KokOzelDurumu(Uretici uretici) {
        this.gelebilecekEkler = uretici.gelebilecekEkler;
        this.sesliEkIleOlusur = uretici.sesliEkIleOlusur;
        this.yapiBozucu = uretici.yapiBozucu;
        this.secimlik = uretici.secimlik;
        this.ekKisitlayici = uretici.ekKisitlayici;
        this.tip = uretici.tip;
    }

    public boolean yapiBozucumu() {
        return yapiBozucu;
    }

    public boolean secimlikmi() {
        return secimlik;
    }

    public boolean seslikEkleolusurmu() {
        return sesliEkIleOlusur;
    }

    public Set geleibilecekEkler() {
        return gelebilecekEkler;
    }


    public boolean ekKisitlayiciMi() {
        return ekKisitlayici;
    }

    public int indeks() {
        return tip.indeks();
    }

    public String ad() {
        return tip.kisaAd();
    }

    public KokOzelDurumTipi tip() {
        return tip;
    }

    /**
     * giris ile gelen [dizi] harf dizisine ozel durumu uygular.
     * basit ziyaretci deseni (visitor pattern).
     *
     * @param dizi
     */
    public void uygula(HarfDizisi dizi) {
    }

    /**
     * Ozel durum giris parametresi olan ek'in bu ozel durumun olusmasina
     * izin verip vermeyeegi belirlenir.
     *
     * @param ek
     * @return gelen ek ile bu ozel durum olusabilirse true
     */
    public boolean olusabilirMi(Ek ek) {
        if (sesliEkIleOlusur && ek.sesliIleBaslayabilirMi())
            return true;
        return gelebilecekEkler.contains(ek);
    }

    /**
     * esitlik kiyaslamasi sadece tip indexi ve tip adina gore yapilir.
     *
     * @param o
     * @return ayni ise true.
     */
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        final KokOzelDurumu that = (KokOzelDurumu) o;
        if ((tip.indeks() == that.tip.indeks()) && tip.ad().equals(that.tip.ad()))
            return true;
        return false;

    }

    /**
     * sadece tip adi ve indeksine gore belirlenir.
     * @return hash code.
     */
    public int hashCode() {
        return tip.ad().hashCode() * tip.indeks();
    }
}
