# MyWatchlist
Deployment link : [link](https://yotugas1.herokuapp.com/mywatchlist/)

# Perbedaan JSON, XML, dan HTML
* JSON (_JavaScript Object Notation_) : adalah format yang secara sintaks identik dengan kode untuk membuat objek JavaScript. JSON diturunkan dari syntax _JavaScript Object Notation_. JSON biasanya digunakan untuk pertukaran atau transfer data (data delivery) karena data dapat disimpan dalam bentuk array.
* XML (_Extensible Markup Language_)  : adalah format berbasis teks sederhana yang digunakan untuk mendeskripsikan data. XML mirip dengan JSON, digunakan untuk delivery data. Dalam menyimpan data, XML memiliki format yang mirip dengan HTML menjadikannya mudah untuk dibaca dibanding JSON.
* HTML (_Hyper Text Markup Language_) : adalah suatu _markup language_. HTML digunakan untuk membuat halaman web dan aplikasi web. Dibandingkan dengan JSON dan XML yang digunakan untuk data delivery, HTML digunakan untuk menampilkan data. HTML disebut _markup language_ karena penggunaan tag dalam mendefinisikan struktur dari suatu halaman web.

# Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform
Data delivery adalah hal yang sangat penting karena dalam implementasi sebuah platform seringkali terjadi pertukaran data antara clients dengan server. Data delivery juga yang dapat membuat data-data dalam server ditampilkan di sisi _frontend_.

# Langkah-langkah implementasi Tugas 3
1. Membuat aplikasi Django baru bernama mywatchlist dengan command berikut:

```shell
python manage.py startapp mywatchlist
```

2. Menambahkan patch mywatchlist pada direktori project_django pada file settings.py dan pada file urls.py

```shell
INSTALLED_APPS = [
    ...
    'mywatchlist',
]
```

```shell
urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
]

```

3. Membuat class watchlist pada file models.py yang ada pada direktory mywatchlist yang menerima parameter models.Model 

```shell
class watchlist(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    deskripsi = models.TextField()
```

4. Membuat folder baru bernama fixtures dalam folder mywatchlist, kemudian membuat file bernama "initial_watchlist_data.json" lalu menambahkan 10 data awal sebagai objek models

5. Melakukan migrasi skema model ke database Django lokal dengan menjalankan perintah berikut:

```shell
python manage.py makemigrations
```

```shell
python manage.py migrate
```

6. Memasukkan data yang terdapat pada initial_mywatchlist_data.json ke database Django lokal:

```shell
python manage.py loaddata initial_watchlist_data.json
```

7. Membuat file html yang ingin ditampilkan
8. Menambahkan fungsi-fungsi untuk menampilkan data dalam format HTML, JSON, dan XML pada file views.py yang berada di folder mywatchlist
9. Membuat routing dengan cara menambahkan urlpatterns pada file urls.py di folder mywatchlist:
```shell
urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]
```
10. Menambahkan Class dan fungsi pada test.py yang berguna sebagai unit test
11. Menambahkan isi Procfile
```shell
release: sh -c 'python manage.py migrate && python manage.py loaddata initial_mywatchlist_data.json'
web: gunicorn project_django.wsgi --log-file -
```
12. Push ke github
# Postman
## HTML
![Screenshot 2022-09-22 024401](https://user-images.githubusercontent.com/112576463/191647653-575b6adf-48af-41e1-9b9e-8a1afbd83c65.png)


## JSON
![Screenshot 2022-09-22 024503](https://user-images.githubusercontent.com/112576463/191647961-ec7be309-68c2-49c1-b220-b6f0da60c340.png)


## XML
![Screenshot 2022-09-22 024443](https://user-images.githubusercontent.com/112576463/191647992-65990e5e-4028-413a-a697-0e085cd67898.png)
