#!/usr/bin/env python3
"""Generates the EN+TR legal pages. Run: python3 build.py"""
import os
UPDATED = {"en": "October 1, 2026", "tr": "1 Ekim 2026"}
BASE = "https://batuayhan.github.io/foodsymptomdetective-legal/"
CSS = """*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.7;color:#1a1a1a;background:#fff;padding:24px 20px 64px;max-width:680px;margin:0 auto;-webkit-font-smoothing:antialiased}
h1{font-size:26px;margin-bottom:6px;color:#111}.upd{font-size:14px;color:#666;margin-bottom:24px}
h2{font-size:19px;margin:30px 0 10px;color:#222}p{font-size:15px;margin-bottom:14px;color:#333}
ul{margin:8px 0 14px 20px;font-size:15px;color:#333}li{margin-bottom:6px}a{color:#2563eb}
.box{background:#f0f7ff;border-left:4px solid #3b82f6;padding:14px 16px;margin:16px 0;border-radius:4px}.box p{margin:0;font-size:14px;color:#1e3a5f}
.warn{background:#fef9ee;border-left-color:#f59e0b}.warn p{color:#78350f}
nav{display:flex;justify-content:space-between;gap:12px;font-size:14px;margin-bottom:20px;flex-wrap:wrap}
.lang a{font-weight:600}
@media (prefers-color-scheme:dark){body{background:#121212;color:#e8e8e8}h1,h2{color:#fff}p,ul{color:#d0d0d0}.upd{color:#999}a{color:#7ab0ff}.box{background:#16263d}.box p{color:#cfe0f7}.warn{background:#33280f}.warn p{color:#f5dcae}}"""

def box(t, w=False): return f'<div class="box{" warn" if w else ""}"><p>{t}</p></div>'
def sec(h, *parts): return f"<h2>{h}</h2>\n" + "\n".join(parts)
def p(t): return f"<p>{t}</p>"
def ul(*i): return "<ul>" + "".join(f"<li>{x}</li>" for x in i) + "</ul>"

PRIV = {"en": ("Privacy Policy", [
 p('Food Symptom Detective ("the App", "we") is an offline-first food and symptom tracker. This policy explains what is stored, what leaves your device and why.'),
 box("<b>Key point:</b> the food, symptom and wellness entries you create are stored on your device. We do not run servers that receive them, and we have no user accounts."),
 sec("1. Data you enter", p("You can log the following in the App:"), ul("Meals, foods and ingredients", "Symptoms, severity, timing and notes", "Wellness details such as stress, sleep, hydration, exercise, medication and menstrual cycle information"), p("This may be sensitive health-related information. It is kept in the App's local database on your device and is not uploaded by us.")),
 sec("2. Where data is stored", ul("Local on-device storage only (SQLite), inside the App's sandbox.", "No sign-up or account is required, and we cannot see, recover or restore your entries.", "Uninstalling the App deletes its data. You can also delete entries or clear data inside the App.", "If you use the in-app export or report feature, the file is created on your device and goes only where you choose to share it.")),
 sec("3. Information collected by service providers",
  p("The App uses the following third-party services. None of them receives your food, symptom or wellness entries."),
  ul("<b>RevenueCat</b> — manages subscriptions and purchase status. Purchases are processed by Apple's App Store or Google Play. RevenueCat receives an anonymous app user ID and purchase/subscription status. See <a href=\"https://www.revenuecat.com/privacy\">revenuecat.com/privacy</a>.",
     "<b>Apple App Store / Google Play</b> — process payments under their own terms and privacy policies. We never see your payment card details.",
     "<b>Google Firebase Analytics and Crashlytics</b> — provide anonymous usage statistics and crash reports (for example which screens or features are used, counts of items logged, meal type, severity level, purchase events, and technical device/app information such as OS version and crash traces). These services use a random app-instance identifier and do not receive your name or e-mail. In a small number of events a food name used in the elimination feature may be included. See <a href=\"https://firebase.google.com/support/privacy\">firebase.google.com/support/privacy</a>."),
  p("We do not use advertising SDKs, do not sell personal information and do not use the data for advertising.")),
 sec("4. Notifications", p("Reminders are scheduled locally on your device. You can switch them off in the App or in your device settings.")),
 sec("5. Not medical advice", box("Food Symptom Detective does not diagnose, treat or give medical advice. It shows patterns in the information you enter, which are not a medical conclusion. Talk to a qualified healthcare professional about symptoms, diet changes or medical decisions.", True)),
 sec("6. Security", p("Your entries rely on your device's protections (device encryption, passcode or biometrics, app sandboxing). Keep your device secured and backed up; we cannot restore data for you.")),
 sec("7. Children", p("The App is not directed to children under 13 and we do not knowingly collect their personal information.")),
 sec("8. Your rights", p("Because your entries stay on your device, you can access, edit, export and delete them in the App. For data handled by the services in section 3 (EEA/UK GDPR, California CCPA, Turkish KVKK No. 6698 or other laws) you may contact us to ask about, correct or delete the related information, and you may complain to your local data protection authority.")),
 sec("9. Changes", p("We may update this policy; the date above shows the latest version. Material changes will be reflected in the App or on this page.")),
 sec("10. Contact", p('<a href="mailto:privacy@foodsymptomdetective.com">privacy@foodsymptomdetective.com</a>')),
]), "tr": ("Gizlilik Politikası", [
 p('Food Symptom Detective ("Uygulama", "biz"), çevrimdışı çalışmayı esas alan bir yiyecek ve semptom takip uygulamasıdır. Bu politika neyin saklandığını, neyin cihazınızdan çıktığını ve nedenini açıklar.'),
 box("<b>Önemli:</b> oluşturduğunuz yiyecek, semptom ve sağlık/yaşam tarzı kayıtları cihazınızda saklanır. Bunları alan bir sunucu işletmiyoruz ve kullanıcı hesabı yoktur."),
 sec("1. Girdiğiniz veriler", p("Uygulamada şunları kaydedebilirsiniz:"), ul("Öğünler, yiyecekler ve içerikler", "Semptomlar, şiddeti, zamanı ve notlar", "Stres, uyku, su tüketimi, egzersiz, ilaç ve adet döngüsü gibi iyi oluş bilgileri"), p("Bunlar hassas sağlık verisi sayılabilir. Uygulamanın cihazınızdaki yerel veritabanında tutulur ve tarafımızdan yüklenmez.")),
 sec("2. Veriler nerede saklanır", ul("Yalnızca cihaz üzerinde yerel olarak (SQLite), uygulamanın korumalı alanında.", "Üyelik veya hesap gerekmez; kayıtlarınızı göremez, kurtaramaz veya geri yükleyemeyiz.", "Uygulamayı silmek verilerini siler. Uygulama içinden tek tek kayıtları veya tüm verileri de silebilirsiniz.", "Uygulama içi dışa aktarma/rapor özelliğini kullanırsanız dosya cihazınızda oluşturulur ve yalnızca paylaşmayı seçtiğiniz yere gider.")),
 sec("3. Hizmet sağlayıcıların topladığı bilgiler",
  p("Uygulama aşağıdaki üçüncü taraf hizmetleri kullanır. Hiçbiri yiyecek, semptom veya iyi oluş kayıtlarınızı almaz."),
  ul("<b>RevenueCat</b> — abonelikleri ve satın alma durumunu yönetir. Ödemeler Apple App Store veya Google Play üzerinden işlenir. RevenueCat anonim bir uygulama kullanıcı kimliği ile satın alma/abonelik durumunu alır. Bkz. <a href=\"https://www.revenuecat.com/privacy\">revenuecat.com/privacy</a>.",
     "<b>Apple App Store / Google Play</b> — ödemeleri kendi şartları ve gizlilik politikalarıyla işler. Kart bilgilerinizi hiçbir zaman görmeyiz.",
     "<b>Google Firebase Analytics ve Crashlytics</b> — anonim kullanım istatistikleri ve çökme raporları sağlar (örneğin hangi ekran veya özelliklerin kullanıldığı, kaydedilen öğe sayıları, öğün türü, şiddet düzeyi, satın alma olayları ile işletim sistemi sürümü ve çökme izi gibi teknik bilgiler). Bu hizmetler rastgele bir uygulama örneği kimliği kullanır; adınızı veya e-postanızı almaz. Az sayıda olayda eliminasyon özelliğinde kullanılan bir besin adı yer alabilir. Bkz. <a href=\"https://firebase.google.com/support/privacy\">firebase.google.com/support/privacy</a>."),
  p("Reklam SDK'sı kullanmıyoruz, kişisel bilgileri satmıyoruz ve verileri reklam amacıyla kullanmıyoruz.")),
 sec("4. Bildirimler", p("Hatırlatmalar cihazınızda yerel olarak planlanır. Uygulamadan veya cihaz ayarlarından kapatabilirsiniz.")),
 sec("5. Tıbbi tavsiye değildir", box("Food Symptom Detective teşhis koymaz, tedavi etmez ve tıbbi tavsiye vermez. Girdiğiniz bilgilerdeki örüntüleri gösterir; bunlar tıbbi bir sonuç değildir. Semptomlarınız, beslenme değişiklikleriniz veya tıbbi kararlarınız için yetkili bir sağlık uzmanına danışın.", True)),
 sec("6. Güvenlik", p("Kayıtlarınız cihazınızın korumalarına (cihaz şifrelemesi, parola veya biyometri, uygulama yalıtımı) dayanır. Cihazınızı güvende tutun ve yedekleyin; verilerinizi sizin için geri getiremeyiz.")),
 sec("7. Çocuklar", p("Uygulama 13 yaş altı çocuklara yönelik değildir ve onların kişisel bilgilerini bilerek toplamayız.")),
 sec("8. Haklarınız", p("Kayıtlarınız cihazınızda kaldığı için bunlara Uygulama içinden erişebilir, düzenleyebilir, dışa aktarabilir ve silebilirsiniz. 3. bölümdeki hizmetlerce işlenen veriler için (AEA/BK GDPR, Kaliforniya CCPA, 6698 sayılı KVKK veya diğer mevzuat) bizimle iletişime geçerek ilgili bilgileri sorabilir, düzeltilmesini veya silinmesini isteyebilir ve yerel veri koruma kurumuna şikâyette bulunabilirsiniz.")),
 sec("9. Değişiklikler", p("Bu politikayı güncelleyebiliriz; yukarıdaki tarih son sürümü gösterir.")),
 sec("10. İletişim", p('<a href="mailto:privacy@foodsymptomdetective.com">privacy@foodsymptomdetective.com</a>')),
])}

TERMS = {"en": ("Terms of Service", [
 p('These Terms govern your use of the Food Symptom Detective mobile app ("the App"). By using the App you agree to them. If you do not agree, please do not use the App.'),
 sec("1. Not medical advice", box("Food Symptom Detective is a personal tracking tool. It does not diagnose, treat or give medical advice, and it does not replace a healthcare professional.", True), ul("Patterns shown are based only on what you enter and are informational.", "Do not delay or disregard professional advice because of something in the App.", "In an emergency, contact your local emergency services.")),
 sec("2. The service", p("The App lets you log foods, symptoms and wellness factors and view patterns. It is offline-first: your entries are stored on your device (see the Privacy Policy).")),
 sec("3. Subscriptions and payments", ul("Premium features are offered as auto-renewable subscriptions, purchased and billed through your Apple ID or Google Play account. Purchases are processed by Apple/Google, with subscription status managed through RevenueCat.", "Prices are shown in the App before you buy. A free trial, if offered, converts to a paid subscription unless cancelled at least 24 hours before it ends.", "Subscriptions renew automatically until cancelled. Cancel in iOS Settings → Apple ID → Subscriptions, or Google Play → Payments &amp; subscriptions → Subscriptions.", "Refunds are handled by Apple or Google under their policies.")),
 sec("4. Your responsibilities", ul("Enter information as accurately as you can; the quality of patterns depends on it.", "Keep your device secure and backed up; uninstalling the App deletes its data.", "Use the App for personal, non-commercial purposes only and do not tamper with or reverse-engineer it.")),
 sec("5. Your data", p("You keep ownership of what you enter. Our handling of information is described in the Privacy Policy.")),
 sec("6. Intellectual property", p("The App, its design and code belong to us. You receive a limited, non-exclusive, non-transferable, revocable licence to use it personally.")),
 sec("7. Disclaimer and liability", p('The App is provided "as is" and "as available". To the extent permitted by law, we do not guarantee that patterns are accurate or complete, we are not liable for health decisions made from the App or for indirect or consequential damages, and our total liability is limited to the amount you paid for the App in the previous 12 months. Nothing here limits rights you have under mandatory consumer-protection law.')),
 sec("8. Changes and termination", p("We may update these Terms or suspend access for misuse. Continued use after an update means you accept it. You can stop at any time by uninstalling.")),
 sec("9. Contact", p('<a href="mailto:support@foodsymptomdetective.com">support@foodsymptomdetective.com</a>')),
]), "tr": ("Kullanım Koşulları", [
 p('Bu Koşullar, Food Symptom Detective mobil uygulamasını ("Uygulama") kullanımınızı düzenler. Uygulamayı kullanarak bunları kabul etmiş olursunuz. Kabul etmiyorsanız lütfen kullanmayın.'),
 sec("1. Tıbbi tavsiye değildir", box("Food Symptom Detective kişisel bir takip aracıdır. Teşhis koymaz, tedavi etmez, tıbbi tavsiye vermez ve bir sağlık uzmanının yerini tutmaz.", True), ul("Gösterilen örüntüler yalnızca sizin girdiğiniz bilgilere dayanır ve bilgilendirme amaçlıdır.", "Uygulamadaki bir şey nedeniyle profesyonel tavsiyeyi geciktirmeyin veya göz ardı etmeyin.", "Acil durumda yerel acil hizmetlerle iletişime geçin.")),
 sec("2. Hizmet", p("Uygulama yiyecek, semptom ve iyi oluş faktörlerini kaydetmenizi ve örüntüleri görmenizi sağlar. Çevrimdışı çalışmayı esas alır: kayıtlarınız cihazınızda saklanır (bkz. Gizlilik Politikası).")),
 sec("3. Abonelik ve ödemeler", ul("Premium özellikler, Apple Kimliğiniz veya Google Play hesabınız üzerinden satın alınan ve faturalandırılan otomatik yenilenen aboneliklerle sunulur. Ödemeleri Apple/Google işler; abonelik durumu RevenueCat ile yönetilir.", "Fiyatlar satın almadan önce Uygulamada gösterilir. Varsa ücretsiz deneme, bitiminden en az 24 saat önce iptal edilmezse ücretli aboneliğe dönüşür.", "Abonelikler iptal edilene kadar otomatik yenilenir. iOS Ayarlar → Apple Kimliği → Abonelikler veya Google Play → Ödemeler ve abonelikler → Abonelikler bölümünden iptal edebilirsiniz.", "İadeler Apple veya Google tarafından kendi politikalarına göre yürütülür.")),
 sec("4. Sorumluluklarınız", ul("Bilgileri mümkün olduğunca doğru girin; örüntülerin kalitesi buna bağlıdır.", "Cihazınızı güvende tutun ve yedekleyin; Uygulamayı silmek verilerini siler.", "Uygulamayı yalnızca kişisel, ticari olmayan amaçla kullanın; kurcalamayın veya tersine mühendislik yapmayın.")),
 sec("5. Verileriniz", p("Girdiğiniz verilerin sahibi sizsiniz. Bilgilerin nasıl işlendiği Gizlilik Politikasında açıklanmıştır.")),
 sec("6. Fikri mülkiyet", p("Uygulama, tasarımı ve kodu bize aittir. Size kişisel kullanım için sınırlı, münhasır olmayan, devredilemez ve geri alınabilir bir lisans verilir.")),
 sec("7. Sorumluluk reddi", p('Uygulama "olduğu gibi" ve "mevcut haliyle" sunulur. Yasaların izin verdiği ölçüde; örüntülerin doğru veya eksiksiz olduğunu garanti etmeyiz, Uygulamadan hareketle verilen sağlık kararlarından veya dolaylı/sonuç olarak doğan zararlardan sorumlu değiliz ve toplam sorumluluğumuz son 12 ayda Uygulama için ödediğiniz tutarla sınırlıdır. Bu hükümler, emredici tüketici koruma mevzuatından doğan haklarınızı sınırlamaz.')),
 sec("8. Değişiklik ve fesih", p("Bu Koşulları güncelleyebilir veya kötüye kullanım halinde erişimi askıya alabiliriz. Güncellemeden sonra kullanmaya devam etmeniz kabul anlamına gelir. İstediğiniz zaman Uygulamayı silerek bırakabilirsiniz.")),
 sec("9. İletişim", p('<a href="mailto:support@foodsymptomdetective.com">support@foodsymptomdetective.com</a>')),
])}

L = {"en": dict(home="Home", other="Türkçe", priv="Privacy Policy", terms="Terms of Service", upd="Last updated", lc="en"),
     "tr": dict(home="Ana sayfa", other="English", priv="Gizlilik Politikası", terms="Kullanım Koşulları", upd="Son güncelleme", lc="tr")}

def path(lang, name): return (f"tr/{name}.html" if lang == "tr" else f"{name}.html")
def page(lang, name, data):
    title, body = data[lang]
    o = "en" if lang == "tr" else "tr"
    prefix = "../" if lang == "tr" else ""
    other_href = ("../" if lang == "tr" else "tr/") + f"{name}.html" + ("?lang=en" if lang == "tr" else "")
    # EN page: auto-redirect Turkish devices to /tr/ unless ?lang=en was chosen
    redirect = ""
    if lang == "en":
        redirect = ("<script>try{var q=location.search.indexOf('lang=en')>-1;if(q){sessionStorage.setItem('fsdlang','en')}"
                    "var l=(navigator.languages&&navigator.languages[0])||navigator.language||'';"
                    f"if(!q&&sessionStorage.getItem('fsdlang')!=='en'&&/^tr/i.test(l)){{location.replace('tr/{name}.html')}}}}catch(e){{}}</script>")
    else:
        redirect = "<script>try{sessionStorage.setItem('fsdlang','tr')}catch(e){}</script>"
    alt = f'<link rel="alternate" hreflang="en" href="{BASE}{name}.html"><link rel="alternate" hreflang="tr" href="{BASE}tr/{name}.html"><link rel="alternate" hreflang="x-default" href="{BASE}{name}.html">'
    nav_other = "terms" if name == "privacy" else "privacy"
    return f'''<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} - Food Symptom Detective</title>{alt}
{redirect}
<style>{CSS}</style></head><body>
<nav><a href="{prefix}index.html">{L[lang]["home"]}</a><span><a href="{nav_other}.html">{L[lang]["terms"] if name=="privacy" else L[lang]["priv"]}</a></span><span class="lang"><a href="{other_href}" hreflang="{o}" lang="{o}">{L[lang]["other"]}</a></span></nav>
<h1>{title}</h1><p class="upd">{L[lang]["upd"]}: {UPDATED[lang]}</p>
{chr(10).join(body)}
</body></html>
'''

def index(lang):
    o = "en" if lang == "tr" else "tr"
    prefix = "../" if lang == "tr" else ""
    redirect = ("<script>try{var q=location.search.indexOf('lang=en')>-1;if(q){sessionStorage.setItem('fsdlang','en')}"
                "var l=(navigator.languages&&navigator.languages[0])||navigator.language||'';"
                "if(!q&&sessionStorage.getItem('fsdlang')!=='en'&&/^tr/i.test(l)){location.replace('tr/')}}catch(e){}</script>") if lang == "en" else ""
    t = "Legal" if lang == "en" else "Yasal Belgeler"
    other_href = ("../" if lang == "tr" else "tr/") + ("?lang=en" if lang == "tr" else "")
    return f'''<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Food Symptom Detective - {t}</title>
<link rel="alternate" hreflang="en" href="{BASE}"><link rel="alternate" hreflang="tr" href="{BASE}tr/">
{redirect}
<style>{CSS}</style></head><body>
<nav><span></span><span class="lang"><a href="{other_href}" hreflang="{o}" lang="{o}">{L[lang]["other"]}</a></span></nav>
<h1>Food Symptom Detective</h1><p class="upd">{t}</p>
<ul><li><a href="privacy.html">{L[lang]["priv"]}</a></li><li><a href="terms.html">{L[lang]["terms"]}</a></li></ul>
</body></html>
'''

os.makedirs("tr", exist_ok=True)
for lang in ("en", "tr"):
    d = "" if lang == "en" else "tr/"
    open(d + "index.html", "w").write(index(lang))
    open(d + "privacy.html", "w").write(page(lang, "privacy", PRIV))
    open(d + "terms.html", "w").write(page(lang, "terms", TERMS))
