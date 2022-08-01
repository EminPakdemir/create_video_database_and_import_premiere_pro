#languages:Turkish and English
import os
import glob
from pathlib import Path
import sqlite3  # pip install db-sqlite3
import platform
from pymediainfo import MediaInfo  # pip3 install pymediainfo

while True:
    print("""
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            +                                                      +
            +            VIDEO DOSYA FORMATLARI İÇİN               +
            +                 DATABASE OLUŞTURMA                   +
            +                                                      +
            +                      ver 1.0                         +
            +                                                      +
            +              Developed by Emin Pakdemir              +
            +                eminpakdemir@gmail.com                +
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++   
        """)
    # TODO MEDYA FORMATLARINI SIRALAYALIM
    MEDIA_TYPES_LIST = ["*.mp4", "*.mov", "*.mpg", "*.mts", "*.flv", "*.mxf", "*.MP4", "*.MOV", "*.MP4", "*.MPG",
                        "*.MTS", "*.FLV", "*.MXF"]
    # media_types = ["*"]   for all file types

    print("----------------------------------")
    print("MEDYA FORMATLARI")

    for i, media_type in enumerate(MEDIA_TYPES_LIST):
        print("*", i + 1, "=", media_type)


    # TODO MEDYA FORMATLARINI SEÇMEK İÇİN SORU SORUYORUZ
    try:
        soru1 = input("""
            => Yukarıdaki hangi medya türleri için database-veritabanı oluşturmak istiyorsunuz?:
            Birden çok seçenek seçebilirsiniz. 
            Lütfen 1,2,3,4,5 şeklinde yazınız. :
            """)
        print("----------------------------------")

        cevap1 = soru1.split(",")

        # TODO SECİLEN MEDYA FORMATLARINI SIRALAYALIM

        SECILEN_MEDYA_FORMATLARI = []



        for cevap in cevap1:
            SECILEN_MEDYA_FORMATLARI.append(MEDIA_TYPES_LIST[int(cevap) - 1])

        print("=>", SECILEN_MEDYA_FORMATLARI, "medya türlerini seçtiniz.")

        # TODO KAÇ TANE ALT KLASÖRDE ARAMA-TARAMA YAPACAĞIMIZI SORUYORUZ.
        try:
            soru2 = input("""
                        => En  fazla kaç tane alt klasörde tarama yapılsın?
                        Max:10 Alt Klasör taranır.
    
                        0 = Ana dizin
                        1 = Ana dizin ve ana dizindeki klasörler içindekiler
                        2 = Ana dizin ve ana dizindeki klasörler ve bunların içindekiler
                        .
                        .
                        .
                        . Değer giriniz: 
                        """)
            print("----------------------------------")
            cevap2 = int(soru2)

            find_files = []

            if 0 == cevap2:
                for type in SECILEN_MEDYA_FORMATLARI:
                    ALT_KLASOR_0 = glob.glob(f"{type}")
                    find_files += ALT_KLASOR_0

                # print(find_files)

            if 1 == cevap2:
                for type in SECILEN_MEDYA_FORMATLARI:
                    ALT_KLASOR_0 = glob.glob(f"{type}")
                    find_files += ALT_KLASOR_0

                    ALT_KLASOR_1 = glob.glob(f"*/{type}")
                    find_files += ALT_KLASOR_1
                # print(find_files)

            if 2 == cevap2:
                for type in SECILEN_MEDYA_FORMATLARI:
                    ALT_KLASOR_0 = glob.glob(f"{type}")
                    find_files += ALT_KLASOR_0

                    ALT_KLASOR_1 = glob.glob(f"*/{type}")
                    find_files += ALT_KLASOR_1

                    ALT_KLASOR_2 = glob.glob(f"*/*/{type}")
                    find_files += ALT_KLASOR_2

                # print(find_files)

            if 3 == cevap2:
                for type in SECILEN_MEDYA_FORMATLARI:
                    ALT_KLASOR_0 = glob.glob(f"{type}")
                    find_files += ALT_KLASOR_0

                    ALT_KLASOR_1 = glob.glob(f"*/{type}")
                    find_files += ALT_KLASOR_1

                    ALT_KLASOR_2 = glob.glob(f"*/*/{type}")
                    find_files += ALT_KLASOR_2

                    ALT_KLASOR_3 = glob.glob(f"*/*/*/{type}")
                    find_files += ALT_KLASOR_3
                # print(find_files)

            if 4 == cevap2:
                for type in SECILEN_MEDYA_FORMATLARI:
                    ALT_KLASOR_0 = glob.glob(f"{type}")
                    find_files += ALT_KLASOR_0

                    ALT_KLASOR_1 = glob.glob(f"*/{type}")
                    find_files += ALT_KLASOR_1

                    ALT_KLASOR_2 = glob.glob(f"*/*/{type}")
                    find_files += ALT_KLASOR_2

                    ALT_KLASOR_3 = glob.glob(f"*/*/*/{type}")
                    find_files += ALT_KLASOR_3

                    ALT_KLASOR_4 = glob.glob(f"*/*/*/*/{type}")
                    find_files += ALT_KLASOR_4
                # print(find_files)

            if 5 == cevap2:
                for type in SECILEN_MEDYA_FORMATLARI:
                    ALT_KLASOR_0 = glob.glob(f"{type}")
                    find_files += ALT_KLASOR_0

                    ALT_KLASOR_1 = glob.glob(f"*/{type}")
                    find_files += ALT_KLASOR_1

                    ALT_KLASOR_2 = glob.glob(f"*/*/{type}")
                    find_files += ALT_KLASOR_2

                    ALT_KLASOR_3 = glob.glob(f"*/*/*/{type}")
                    find_files += ALT_KLASOR_3

                    ALT_KLASOR_4 = glob.glob(f"*/*/*/*/{type}")
                    find_files += ALT_KLASOR_4

                    ALT_KLASOR_5 = glob.glob(f"*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_5
                # print(find_files)

            if 6 == cevap2:
                for type in SECILEN_MEDYA_FORMATLARI:
                    ALT_KLASOR_0 = glob.glob(f"{type}")
                    find_files += ALT_KLASOR_0

                    ALT_KLASOR_1 = glob.glob(f"*/{type}")
                    find_files += ALT_KLASOR_1

                    ALT_KLASOR_2 = glob.glob(f"*/*/{type}")
                    find_files += ALT_KLASOR_2

                    ALT_KLASOR_3 = glob.glob(f"*/*/*/{type}")
                    find_files += ALT_KLASOR_3

                    ALT_KLASOR_4 = glob.glob(f"*/*/*/*/{type}")
                    find_files += ALT_KLASOR_4

                    ALT_KLASOR_5 = glob.glob(f"*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_5

                    ALT_KLASOR_6 = glob.glob(f"*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_6
                # print(find_files)

            if 7 == cevap2:
                for type in SECILEN_MEDYA_FORMATLARI:
                    ALT_KLASOR_0 = glob.glob(f"{type}")
                    find_files += ALT_KLASOR_0

                    ALT_KLASOR_1 = glob.glob(f"*/{type}")
                    find_files += ALT_KLASOR_1

                    ALT_KLASOR_2 = glob.glob(f"*/*/{type}")
                    find_files += ALT_KLASOR_2

                    ALT_KLASOR_3 = glob.glob(f"*/*/*/{type}")
                    find_files += ALT_KLASOR_3

                    ALT_KLASOR_4 = glob.glob(f"*/*/*/*/{type}")
                    find_files += ALT_KLASOR_4

                    ALT_KLASOR_5 = glob.glob(f"*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_5

                    ALT_KLASOR_6 = glob.glob(f"*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_6

                    ALT_KLASOR_7 = glob.glob(f"*/*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_7
                # print(find_files)

            if 8 == cevap2:
                for type in SECILEN_MEDYA_FORMATLARI:
                    ALT_KLASOR_0 = glob.glob(f"{type}")
                    find_files += ALT_KLASOR_0

                    ALT_KLASOR_1 = glob.glob(f"*/{type}")
                    find_files += ALT_KLASOR_1

                    ALT_KLASOR_2 = glob.glob(f"*/*/{type}")
                    find_files += ALT_KLASOR_2

                    ALT_KLASOR_3 = glob.glob(f"*/*/*/{type}")
                    find_files += ALT_KLASOR_3

                    ALT_KLASOR_4 = glob.glob(f"*/*/*/*/{type}")
                    find_files += ALT_KLASOR_4

                    ALT_KLASOR_5 = glob.glob(f"*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_5

                    ALT_KLASOR_6 = glob.glob(f"*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_6

                    ALT_KLASOR_7 = glob.glob(f"*/*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_7

                    ALT_KLASOR_8 = glob.glob(f"*/*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_8
                # print(find_files)

            if 9 == cevap2:
                for type in SECILEN_MEDYA_FORMATLARI:
                    ALT_KLASOR_0 = glob.glob(f"{type}")
                    find_files += ALT_KLASOR_0

                    ALT_KLASOR_1 = glob.glob(f"*/{type}")
                    find_files += ALT_KLASOR_1

                    ALT_KLASOR_2 = glob.glob(f"*/*/{type}")
                    find_files += ALT_KLASOR_2

                    ALT_KLASOR_3 = glob.glob(f"*/*/*/{type}")
                    find_files += ALT_KLASOR_3

                    ALT_KLASOR_4 = glob.glob(f"*/*/*/*/{type}")
                    find_files += ALT_KLASOR_4

                    ALT_KLASOR_5 = glob.glob(f"*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_5

                    ALT_KLASOR_6 = glob.glob(f"*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_6

                    ALT_KLASOR_7 = glob.glob(f"*/*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_7

                    ALT_KLASOR_7 = glob.glob(f"*/*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_7

                    ALT_KLASOR_8 = glob.glob(f"*/*/*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_8

                    ALT_KLASOR_9 = glob.glob(f"*/*/*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_9
                # print(find_files)

            if 10 == cevap2:
                for type in SECILEN_MEDYA_FORMATLARI:
                    ALT_KLASOR_0 = glob.glob(f"{type}")
                    find_files += ALT_KLASOR_0

                    ALT_KLASOR_1 = glob.glob(f"*/{type}")
                    find_files += ALT_KLASOR_1

                    ALT_KLASOR_2 = glob.glob(f"*/*/{type}")
                    find_files += ALT_KLASOR_2

                    ALT_KLASOR_3 = glob.glob(f"*/*/*/{type}")
                    find_files += ALT_KLASOR_3

                    ALT_KLASOR_4 = glob.glob(f"*/*/*/*/{type}")
                    find_files += ALT_KLASOR_4

                    ALT_KLASOR_5 = glob.glob(f"*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_5

                    ALT_KLASOR_6 = glob.glob(f"*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_6

                    ALT_KLASOR_7 = glob.glob(f"*/*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_7

                    ALT_KLASOR_8 = glob.glob(f"*/*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_8

                    ALT_KLASOR_9 = glob.glob(f"*/*/*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_9

                    ALT_KLASOR_10 = glob.glob(f"*/*/*/*/*/*/*/*/*/*/{type}")
                    find_files += ALT_KLASOR_10
                # print(find_files)

            # print(find_files)

            con = sqlite3.connect("database_.db")
            cursor = con.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS videos (
            Created_ID  INT,
            File_name TEXT,
            Resolution TEXT,
            Frame_rate TEXT,
            Codec_format TEXT,
            Duration TEXT,
            File_size TEXT,
            File_name_with_file_type TEXT,
            Path_from_content_root TEXT,
            Absolute_full_path TEXT)""")

            created_id = 1
            for i in find_files:
                # TODO ONLY FILE NAMES PRINT
                # print(Path(i).stem)  # .stem dosya uzantısını vermiyor   .name dosya uzantısını veriyor.
                try:

                    # TODO MEDIA FILE INFOS
                    media_info = MediaInfo.parse(f"{i}")

                    width = media_info.video_tracks[0].width
                    height = media_info.video_tracks[0].height
                    resolution = f"{width}x{height}"

                    frame_rate = media_info.video_tracks[0].frame_rate
                    codec_format = media_info.video_tracks[0].format
                    duration = media_info.video_tracks[0].other_duration[4]
                    file_size = round(media_info.general_tracks[
                                          0].file_size / 1024 / 1024)  # mega byte için /1024/1024 . Çıkan sayıyı round() ile yuvarlıyoruz.
                    # print("Resolution  :", resolution)
                    # print("Frame Rate  :", frame_rate)
                    # print("Codec Format:", codec_format)
                    # print("Duration    :", duration)
                    # print("File Size :", file_size, "mb")
                    # Resolution 1920x1080
                    # Frame Rate: 25.000
                    # Format: AVC
                    # Duration: 00:00:01:14
                except IndexError:
                    media_info = MediaInfo.parse(f"{i}")
                    width = "yok"
                    height = "yok"
                    resolution = "yok"

                    frame_rate = "yok"
                    codec_format = "yok"
                    duration = "yok"
                    file_size = "yok"



                # TODO ONLY FILE NAMES AND .FILE TYPE PRINT
                print(i)

                # TODO PATH FROM CONTENT ROOT PRINT
                # print(i)
                # TODO FULL PATH - ABSOLUTE PATH WINDOWS PRINT
                plt = platform.system()

                if plt == "Windows":
                    full_path = os.getcwd() + "\\" + i

                elif plt == "Darwin":
                    full_path = os.getcwd() + "/" + i

                # print(full_path)
                cursor.execute(
                f"""INSERT INTO videos VALUES ("{created_id}","{Path(i).stem}","{resolution}", "{frame_rate} fps", "{codec_format}", "{duration}","{file_size} mb","{Path(i).name}","{i}","{full_path}")""")
                # print("\n")
                created_id += 1
            con.commit()
            con.close()
        except:
            print("\n=> Lütfen geçerli bir seçenek giriniz! soru2\n")
    except:
        print("=> Lütfen geçerli bir seçenek giriniz! soru1")
