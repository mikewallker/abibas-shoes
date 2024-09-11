-Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. buat direktori baru untuk projek beserta instalasi-instalasi awal
2. hubungkan dengan repositori remote github
3. buat aplikasi dengan nama main
4. membuat model pada aplikasi main, dengan inisiasi awal 3 atribut wajib
5. melakukan migrasi model agar struktur tabel database ter-update
6. membuat template html
7. menghubungkan view dengan template
8. routing projek (mengatur URL tingkat proyek)
9. membuat routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
10. deploy ke pws(belum karena webnya bermasalah)



-Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jadi saat client memulai request ke web menggunakan url(rute url diatur oleh urls.py dan menampilkan view yang bersesuaian), request tersebut akan diteruskan ke framework Django. Pertama-tama, views.py akan mengambil request tersebut, lalu dia akan menjadi perantara antara model dan template html. Model berisi logika yang mengatur hubungan antara aplikasi dengan database. Data-data tersebut dihubungkan ke template html melalui views. Template html mengatur tampilan antarmuka pengguna. Pada akhirnya, django akan memberi respon berupa web page kepada web (internet) yang akan diteruskan ke client (laptop pengguna).

Model: Menyimpan data dan logika aplikasi.
View: Menampilkan data dari model dan menghubungkannya dengan template.
Template(html): Menentukan tampilan antarmuka pengguna.
Urls: Mencocokkan URL permintaan dengan view yang sesuai.

-Jelaskan fungsi git dalam pengembangan perangkat lunak!
git berfungsi sebagai sistem kontrol versi untuk menyimpan, mengelola, dan berbagi source code secara efisien dan kolaboratif. Dengan git, kita bisa melakukan perubahan code dengan aman karena kita bisa membuat beberapa branch untuk projek kita, jika kita melakukan suatu kesalahan maka kesalahan itu hanya berdampak pada 1 branch saja. 


-Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
dengan memakai django, kita dapat membuat aplikasi secara cepat tanpa harus melakukan banyak langkah manual. Selain itu, django memiliki dokumentasi yang lengkap. Karena django populer, banyak komunitas yang akan membantu kita dalam menyelesaikan masalah-masalah yang muncul. Selain itu, django adalah framework yang fleksibel.

-Mengapa model pada Django disebut sebagai ORM?
karena dengan menggunakan django, source code kita bisa berinteraksi dengan struktur database, sesuai kepanjangannya (Object-relational mapper)



