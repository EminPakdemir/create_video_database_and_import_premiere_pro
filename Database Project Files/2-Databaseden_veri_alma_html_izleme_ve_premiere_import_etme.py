#!/usr/bin/env python3
# coding: utf-8
import glob
import sqlite3  # pip install db-sqlite3
import pymiere  # pip install pymiere
import os
import platform
import time
import subprocess

while True:
    ALL_DATABASE_DB_LIST = glob.glob("*.db")

    print("----------------------------------")
    for i, database in enumerate(ALL_DATABASE_DB_LIST):
        print("*", i + 1, "=", database)
    print("----------------------------------")

    try:
        soru1 = int(input("=> Yukarıdaki hangi database içinde çalışma yapacaksınız?:"))
        print("----------------------------------")

        print("=>", ALL_DATABASE_DB_LIST[soru1 - 1], "seçtiniz.")

        con = sqlite3.connect(f"{ALL_DATABASE_DB_LIST[soru1 - 1]}")
        cursor = con.cursor()

        # cursor.execute("SELECT * FROM videos")  # TÜM DATABASE ÇEKMEK İÇİN
        # data = cursor.fetchall()
        # for i in data:
        #     print(i)

        print("""
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            +                                                          +
            +           DATABASE'DEN FİLTRELENEN VERİLER İÇİN          +
            +              HTML İZLEME SAYFASI OLUŞTURMA               +
            +                           VE                             +
            +    ADOBE PREMIERE PRO 2020-2022 İÇERİSİNE IMPORT ETME    +
            +                                                          +
            +          Birden çok ID numarası girebilmek için          +
            +          lütfen 1,2,3,4,12,16 şeklinde yazınız.          +
            +               Max 483 Adet ID yazabilirsiniz.             +
            +                                                          +
            +                        ver 1.0                           +
            +                                                          +
            +              Developed by Emin Pakdemir                  +
            +                eminpakdemir@gmail.com                    +
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   
        """)
        soru2 = input("=> Veri tabanında filtrelemek ve izlemek istediğiniz ID numaralarını giriniz:")
        ID_LISTE = soru2.split(",")

        SIFIRLAR_LISTESI = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
                            ]  # 501 Adet boş ID listesi girildi.
        ID_LISTE.extend(SIFIRLAR_LISTESI)

        cursor.execute(f"""SELECT
        Created_Id,Resolution, File_name,  Absolute_full_path
        FROM videos WHERE
        Created_Id='{ID_LISTE[0]}' OR
        Created_Id='{ID_LISTE[1]}' OR
        Created_Id='{ID_LISTE[2]}' OR
        Created_Id='{ID_LISTE[3]}' OR
        Created_Id='{ID_LISTE[4]}' OR
        Created_Id='{ID_LISTE[5]}' OR
        Created_Id='{ID_LISTE[6]}' OR
        Created_Id='{ID_LISTE[7]}' OR
        Created_Id='{ID_LISTE[8]}' OR
        Created_Id='{ID_LISTE[9]}' OR
        Created_Id='{ID_LISTE[10]}' OR
        Created_Id='{ID_LISTE[11]}' OR
        Created_Id='{ID_LISTE[12]}' OR
        Created_Id='{ID_LISTE[13]}' OR
        Created_Id='{ID_LISTE[14]}' OR
        Created_Id='{ID_LISTE[15]}' OR
        Created_Id='{ID_LISTE[16]}' OR
        Created_Id='{ID_LISTE[17]}' OR
        Created_Id='{ID_LISTE[18]}' OR
        Created_Id='{ID_LISTE[19]}' OR
        Created_Id='{ID_LISTE[20]}' OR
        Created_Id='{ID_LISTE[21]}' OR
        Created_Id='{ID_LISTE[22]}' OR
        Created_Id='{ID_LISTE[23]}' OR
        Created_Id='{ID_LISTE[24]}' OR
        Created_Id='{ID_LISTE[25]}' OR
        Created_Id='{ID_LISTE[26]}' OR
        Created_Id='{ID_LISTE[27]}' OR
        Created_Id='{ID_LISTE[28]}' OR
        Created_Id='{ID_LISTE[29]}' OR
        Created_Id='{ID_LISTE[30]}' OR
        Created_Id='{ID_LISTE[31]}' OR
        Created_Id='{ID_LISTE[32]}' OR
        Created_Id='{ID_LISTE[33]}' OR
        Created_Id='{ID_LISTE[34]}' OR
        Created_Id='{ID_LISTE[35]}' OR
        Created_Id='{ID_LISTE[36]}' OR
        Created_Id='{ID_LISTE[37]}' OR
        Created_Id='{ID_LISTE[38]}' OR
        Created_Id='{ID_LISTE[39]}' OR
        Created_Id='{ID_LISTE[40]}' OR
        Created_Id='{ID_LISTE[41]}' OR
        Created_Id='{ID_LISTE[42]}' OR
        Created_Id='{ID_LISTE[43]}' OR
        Created_Id='{ID_LISTE[44]}' OR
        Created_Id='{ID_LISTE[45]}' OR
        Created_Id='{ID_LISTE[46]}' OR
        Created_Id='{ID_LISTE[47]}' OR
        Created_Id='{ID_LISTE[48]}' OR
        Created_Id='{ID_LISTE[49]}' OR
        Created_Id='{ID_LISTE[50]}' OR
        Created_Id='{ID_LISTE[51]}' OR
        Created_Id='{ID_LISTE[52]}' OR
        Created_Id='{ID_LISTE[53]}' OR
        Created_Id='{ID_LISTE[54]}' OR
        Created_Id='{ID_LISTE[55]}' OR
        Created_Id='{ID_LISTE[56]}' OR
        Created_Id='{ID_LISTE[57]}' OR
        Created_Id='{ID_LISTE[58]}' OR
        Created_Id='{ID_LISTE[59]}' OR
        Created_Id='{ID_LISTE[60]}' OR
        Created_Id='{ID_LISTE[61]}' OR
        Created_Id='{ID_LISTE[62]}' OR
        Created_Id='{ID_LISTE[63]}' OR
        Created_Id='{ID_LISTE[64]}' OR
        Created_Id='{ID_LISTE[65]}' OR
        Created_Id='{ID_LISTE[66]}' OR
        Created_Id='{ID_LISTE[67]}' OR
        Created_Id='{ID_LISTE[68]}' OR
        Created_Id='{ID_LISTE[69]}' OR
        Created_Id='{ID_LISTE[70]}' OR
        Created_Id='{ID_LISTE[71]}' OR
        Created_Id='{ID_LISTE[72]}' OR
        Created_Id='{ID_LISTE[73]}' OR
        Created_Id='{ID_LISTE[74]}' OR
        Created_Id='{ID_LISTE[75]}' OR
        Created_Id='{ID_LISTE[76]}' OR
        Created_Id='{ID_LISTE[77]}' OR
        Created_Id='{ID_LISTE[78]}' OR
        Created_Id='{ID_LISTE[79]}' OR
        Created_Id='{ID_LISTE[80]}' OR
        Created_Id='{ID_LISTE[81]}' OR
        Created_Id='{ID_LISTE[82]}' OR
        Created_Id='{ID_LISTE[83]}' OR
        Created_Id='{ID_LISTE[84]}' OR
        Created_Id='{ID_LISTE[85]}' OR
        Created_Id='{ID_LISTE[86]}' OR
        Created_Id='{ID_LISTE[87]}' OR
        Created_Id='{ID_LISTE[88]}' OR
        Created_Id='{ID_LISTE[89]}' OR
        Created_Id='{ID_LISTE[90]}' OR
        Created_Id='{ID_LISTE[91]}' OR
        Created_Id='{ID_LISTE[92]}' OR
        Created_Id='{ID_LISTE[93]}' OR
        Created_Id='{ID_LISTE[94]}' OR
        Created_Id='{ID_LISTE[95]}' OR
        Created_Id='{ID_LISTE[96]}' OR
        Created_Id='{ID_LISTE[97]}' OR
        Created_Id='{ID_LISTE[98]}' OR
        Created_Id='{ID_LISTE[99]}' OR
        Created_Id='{ID_LISTE[100]}' OR
        Created_Id='{ID_LISTE[101]}' OR
        Created_Id='{ID_LISTE[102]}' OR
        Created_Id='{ID_LISTE[103]}' OR
        Created_Id='{ID_LISTE[104]}' OR
        Created_Id='{ID_LISTE[105]}' OR
        Created_Id='{ID_LISTE[106]}' OR
        Created_Id='{ID_LISTE[107]}' OR
        Created_Id='{ID_LISTE[108]}' OR
        Created_Id='{ID_LISTE[109]}' OR
        Created_Id='{ID_LISTE[110]}' OR
        Created_Id='{ID_LISTE[111]}' OR
        Created_Id='{ID_LISTE[112]}' OR
        Created_Id='{ID_LISTE[113]}' OR
        Created_Id='{ID_LISTE[114]}' OR
        Created_Id='{ID_LISTE[115]}' OR
        Created_Id='{ID_LISTE[116]}' OR
        Created_Id='{ID_LISTE[117]}' OR
        Created_Id='{ID_LISTE[118]}' OR
        Created_Id='{ID_LISTE[119]}' OR
        Created_Id='{ID_LISTE[120]}' OR
        Created_Id='{ID_LISTE[121]}' OR
        Created_Id='{ID_LISTE[122]}' OR
        Created_Id='{ID_LISTE[123]}' OR
        Created_Id='{ID_LISTE[124]}' OR
        Created_Id='{ID_LISTE[125]}' OR
        Created_Id='{ID_LISTE[126]}' OR
        Created_Id='{ID_LISTE[127]}' OR
        Created_Id='{ID_LISTE[128]}' OR
        Created_Id='{ID_LISTE[129]}' OR
        Created_Id='{ID_LISTE[130]}' OR
        Created_Id='{ID_LISTE[131]}' OR
        Created_Id='{ID_LISTE[132]}' OR
        Created_Id='{ID_LISTE[133]}' OR
        Created_Id='{ID_LISTE[134]}' OR
        Created_Id='{ID_LISTE[135]}' OR
        Created_Id='{ID_LISTE[136]}' OR
        Created_Id='{ID_LISTE[137]}' OR
        Created_Id='{ID_LISTE[138]}' OR
        Created_Id='{ID_LISTE[139]}' OR
        Created_Id='{ID_LISTE[140]}' OR
        Created_Id='{ID_LISTE[141]}' OR
        Created_Id='{ID_LISTE[142]}' OR
        Created_Id='{ID_LISTE[143]}' OR
        Created_Id='{ID_LISTE[144]}' OR
        Created_Id='{ID_LISTE[145]}' OR
        Created_Id='{ID_LISTE[146]}' OR
        Created_Id='{ID_LISTE[147]}' OR
        Created_Id='{ID_LISTE[148]}' OR
        Created_Id='{ID_LISTE[149]}' OR
        Created_Id='{ID_LISTE[150]}' OR
        Created_Id='{ID_LISTE[151]}' OR
        Created_Id='{ID_LISTE[152]}' OR
        Created_Id='{ID_LISTE[153]}' OR
        Created_Id='{ID_LISTE[154]}' OR
        Created_Id='{ID_LISTE[155]}' OR
        Created_Id='{ID_LISTE[156]}' OR
        Created_Id='{ID_LISTE[157]}' OR
        Created_Id='{ID_LISTE[158]}' OR
        Created_Id='{ID_LISTE[159]}' OR
        Created_Id='{ID_LISTE[160]}' OR
        Created_Id='{ID_LISTE[161]}' OR
        Created_Id='{ID_LISTE[162]}' OR
        Created_Id='{ID_LISTE[163]}' OR
        Created_Id='{ID_LISTE[164]}' OR
        Created_Id='{ID_LISTE[165]}' OR
        Created_Id='{ID_LISTE[166]}' OR
        Created_Id='{ID_LISTE[167]}' OR
        Created_Id='{ID_LISTE[168]}' OR
        Created_Id='{ID_LISTE[169]}' OR
        Created_Id='{ID_LISTE[170]}' OR
        Created_Id='{ID_LISTE[171]}' OR
        Created_Id='{ID_LISTE[172]}' OR
        Created_Id='{ID_LISTE[173]}' OR
        Created_Id='{ID_LISTE[174]}' OR
        Created_Id='{ID_LISTE[175]}' OR
        Created_Id='{ID_LISTE[176]}' OR
        Created_Id='{ID_LISTE[177]}' OR
        Created_Id='{ID_LISTE[178]}' OR
        Created_Id='{ID_LISTE[179]}' OR
        Created_Id='{ID_LISTE[180]}' OR
        Created_Id='{ID_LISTE[181]}' OR
        Created_Id='{ID_LISTE[182]}' OR
        Created_Id='{ID_LISTE[183]}' OR
        Created_Id='{ID_LISTE[184]}' OR
        Created_Id='{ID_LISTE[185]}' OR
        Created_Id='{ID_LISTE[186]}' OR
        Created_Id='{ID_LISTE[187]}' OR
        Created_Id='{ID_LISTE[188]}' OR
        Created_Id='{ID_LISTE[189]}' OR
        Created_Id='{ID_LISTE[190]}' OR
        Created_Id='{ID_LISTE[191]}' OR
        Created_Id='{ID_LISTE[192]}' OR
        Created_Id='{ID_LISTE[193]}' OR
        Created_Id='{ID_LISTE[194]}' OR
        Created_Id='{ID_LISTE[195]}' OR
        Created_Id='{ID_LISTE[196]}' OR
        Created_Id='{ID_LISTE[197]}' OR
        Created_Id='{ID_LISTE[198]}' OR
        Created_Id='{ID_LISTE[199]}' OR
        Created_Id='{ID_LISTE[200]}' OR
        Created_Id='{ID_LISTE[201]}' OR
        Created_Id='{ID_LISTE[202]}' OR
        Created_Id='{ID_LISTE[203]}' OR
        Created_Id='{ID_LISTE[204]}' OR
        Created_Id='{ID_LISTE[205]}' OR
        Created_Id='{ID_LISTE[206]}' OR
        Created_Id='{ID_LISTE[207]}' OR
        Created_Id='{ID_LISTE[208]}' OR
        Created_Id='{ID_LISTE[209]}' OR
        Created_Id='{ID_LISTE[210]}' OR
        Created_Id='{ID_LISTE[211]}' OR
        Created_Id='{ID_LISTE[212]}' OR
        Created_Id='{ID_LISTE[213]}' OR
        Created_Id='{ID_LISTE[214]}' OR
        Created_Id='{ID_LISTE[215]}' OR
        Created_Id='{ID_LISTE[216]}' OR
        Created_Id='{ID_LISTE[217]}' OR
        Created_Id='{ID_LISTE[218]}' OR
        Created_Id='{ID_LISTE[219]}' OR
        Created_Id='{ID_LISTE[220]}' OR
        Created_Id='{ID_LISTE[221]}' OR
        Created_Id='{ID_LISTE[222]}' OR
        Created_Id='{ID_LISTE[223]}' OR
        Created_Id='{ID_LISTE[224]}' OR
        Created_Id='{ID_LISTE[225]}' OR
        Created_Id='{ID_LISTE[226]}' OR
        Created_Id='{ID_LISTE[227]}' OR
        Created_Id='{ID_LISTE[228]}' OR
        Created_Id='{ID_LISTE[229]}' OR
        Created_Id='{ID_LISTE[230]}' OR
        Created_Id='{ID_LISTE[231]}' OR
        Created_Id='{ID_LISTE[232]}' OR
        Created_Id='{ID_LISTE[233]}' OR
        Created_Id='{ID_LISTE[234]}' OR
        Created_Id='{ID_LISTE[235]}' OR
        Created_Id='{ID_LISTE[236]}' OR
        Created_Id='{ID_LISTE[237]}' OR
        Created_Id='{ID_LISTE[238]}' OR
        Created_Id='{ID_LISTE[239]}' OR
        Created_Id='{ID_LISTE[240]}' OR
        Created_Id='{ID_LISTE[241]}' OR
        Created_Id='{ID_LISTE[242]}' OR
        Created_Id='{ID_LISTE[243]}' OR
        Created_Id='{ID_LISTE[244]}' OR
        Created_Id='{ID_LISTE[245]}' OR
        Created_Id='{ID_LISTE[246]}' OR
        Created_Id='{ID_LISTE[247]}' OR
        Created_Id='{ID_LISTE[248]}' OR
        Created_Id='{ID_LISTE[249]}' OR
        Created_Id='{ID_LISTE[250]}' OR
        Created_Id='{ID_LISTE[251]}' OR
        Created_Id='{ID_LISTE[252]}' OR
        Created_Id='{ID_LISTE[253]}' OR
        Created_Id='{ID_LISTE[254]}' OR
        Created_Id='{ID_LISTE[255]}' OR
        Created_Id='{ID_LISTE[256]}' OR
        Created_Id='{ID_LISTE[257]}' OR
        Created_Id='{ID_LISTE[258]}' OR
        Created_Id='{ID_LISTE[259]}' OR
        Created_Id='{ID_LISTE[260]}' OR
        Created_Id='{ID_LISTE[261]}' OR
        Created_Id='{ID_LISTE[262]}' OR
        Created_Id='{ID_LISTE[263]}' OR
        Created_Id='{ID_LISTE[264]}' OR
        Created_Id='{ID_LISTE[265]}' OR
        Created_Id='{ID_LISTE[266]}' OR
        Created_Id='{ID_LISTE[267]}' OR
        Created_Id='{ID_LISTE[268]}' OR
        Created_Id='{ID_LISTE[269]}' OR
        Created_Id='{ID_LISTE[270]}' OR
        Created_Id='{ID_LISTE[271]}' OR
        Created_Id='{ID_LISTE[272]}' OR
        Created_Id='{ID_LISTE[273]}' OR
        Created_Id='{ID_LISTE[274]}' OR
        Created_Id='{ID_LISTE[275]}' OR
        Created_Id='{ID_LISTE[276]}' OR
        Created_Id='{ID_LISTE[277]}' OR
        Created_Id='{ID_LISTE[278]}' OR
        Created_Id='{ID_LISTE[279]}' OR
        Created_Id='{ID_LISTE[280]}' OR
        Created_Id='{ID_LISTE[281]}' OR
        Created_Id='{ID_LISTE[282]}' OR
        Created_Id='{ID_LISTE[283]}' OR
        Created_Id='{ID_LISTE[284]}' OR
        Created_Id='{ID_LISTE[285]}' OR
        Created_Id='{ID_LISTE[286]}' OR
        Created_Id='{ID_LISTE[287]}' OR
        Created_Id='{ID_LISTE[288]}' OR
        Created_Id='{ID_LISTE[289]}' OR
        Created_Id='{ID_LISTE[290]}' OR
        Created_Id='{ID_LISTE[291]}' OR
        Created_Id='{ID_LISTE[292]}' OR
        Created_Id='{ID_LISTE[293]}' OR
        Created_Id='{ID_LISTE[294]}' OR
        Created_Id='{ID_LISTE[295]}' OR
        Created_Id='{ID_LISTE[296]}' OR
        Created_Id='{ID_LISTE[297]}' OR
        Created_Id='{ID_LISTE[298]}' OR
        Created_Id='{ID_LISTE[299]}' OR
        Created_Id='{ID_LISTE[300]}' OR
        Created_Id='{ID_LISTE[301]}' OR
        Created_Id='{ID_LISTE[302]}' OR
        Created_Id='{ID_LISTE[303]}' OR
        Created_Id='{ID_LISTE[304]}' OR
        Created_Id='{ID_LISTE[305]}' OR
        Created_Id='{ID_LISTE[306]}' OR
        Created_Id='{ID_LISTE[307]}' OR
        Created_Id='{ID_LISTE[308]}' OR
        Created_Id='{ID_LISTE[309]}' OR
        Created_Id='{ID_LISTE[310]}' OR
        Created_Id='{ID_LISTE[311]}' OR
        Created_Id='{ID_LISTE[312]}' OR
        Created_Id='{ID_LISTE[313]}' OR
        Created_Id='{ID_LISTE[314]}' OR
        Created_Id='{ID_LISTE[315]}' OR
        Created_Id='{ID_LISTE[316]}' OR
        Created_Id='{ID_LISTE[317]}' OR
        Created_Id='{ID_LISTE[318]}' OR
        Created_Id='{ID_LISTE[319]}' OR
        Created_Id='{ID_LISTE[320]}' OR
        Created_Id='{ID_LISTE[321]}' OR
        Created_Id='{ID_LISTE[322]}' OR
        Created_Id='{ID_LISTE[323]}' OR
        Created_Id='{ID_LISTE[324]}' OR
        Created_Id='{ID_LISTE[325]}' OR
        Created_Id='{ID_LISTE[326]}' OR
        Created_Id='{ID_LISTE[327]}' OR
        Created_Id='{ID_LISTE[328]}' OR
        Created_Id='{ID_LISTE[329]}' OR
        Created_Id='{ID_LISTE[330]}' OR
        Created_Id='{ID_LISTE[331]}' OR
        Created_Id='{ID_LISTE[332]}' OR
        Created_Id='{ID_LISTE[333]}' OR
        Created_Id='{ID_LISTE[334]}' OR
        Created_Id='{ID_LISTE[335]}' OR
        Created_Id='{ID_LISTE[336]}' OR
        Created_Id='{ID_LISTE[337]}' OR
        Created_Id='{ID_LISTE[338]}' OR
        Created_Id='{ID_LISTE[339]}' OR
        Created_Id='{ID_LISTE[340]}' OR
        Created_Id='{ID_LISTE[341]}' OR
        Created_Id='{ID_LISTE[342]}' OR
        Created_Id='{ID_LISTE[343]}' OR
        Created_Id='{ID_LISTE[344]}' OR
        Created_Id='{ID_LISTE[345]}' OR
        Created_Id='{ID_LISTE[346]}' OR
        Created_Id='{ID_LISTE[347]}' OR
        Created_Id='{ID_LISTE[348]}' OR
        Created_Id='{ID_LISTE[349]}' OR
        Created_Id='{ID_LISTE[350]}' OR
        Created_Id='{ID_LISTE[351]}' OR
        Created_Id='{ID_LISTE[352]}' OR
        Created_Id='{ID_LISTE[353]}' OR
        Created_Id='{ID_LISTE[354]}' OR
        Created_Id='{ID_LISTE[355]}' OR
        Created_Id='{ID_LISTE[356]}' OR
        Created_Id='{ID_LISTE[357]}' OR
        Created_Id='{ID_LISTE[358]}' OR
        Created_Id='{ID_LISTE[359]}' OR
        Created_Id='{ID_LISTE[360]}' OR
        Created_Id='{ID_LISTE[361]}' OR
        Created_Id='{ID_LISTE[362]}' OR
        Created_Id='{ID_LISTE[363]}' OR
        Created_Id='{ID_LISTE[364]}' OR
        Created_Id='{ID_LISTE[365]}' OR
        Created_Id='{ID_LISTE[366]}' OR
        Created_Id='{ID_LISTE[367]}' OR
        Created_Id='{ID_LISTE[368]}' OR
        Created_Id='{ID_LISTE[369]}' OR
        Created_Id='{ID_LISTE[370]}' OR
        Created_Id='{ID_LISTE[371]}' OR
        Created_Id='{ID_LISTE[372]}' OR
        Created_Id='{ID_LISTE[373]}' OR
        Created_Id='{ID_LISTE[374]}' OR
        Created_Id='{ID_LISTE[375]}' OR
        Created_Id='{ID_LISTE[376]}' OR
        Created_Id='{ID_LISTE[377]}' OR
        Created_Id='{ID_LISTE[378]}' OR
        Created_Id='{ID_LISTE[379]}' OR
        Created_Id='{ID_LISTE[380]}' OR
        Created_Id='{ID_LISTE[381]}' OR
        Created_Id='{ID_LISTE[382]}' OR
        Created_Id='{ID_LISTE[383]}' OR
        Created_Id='{ID_LISTE[384]}' OR
        Created_Id='{ID_LISTE[385]}' OR
        Created_Id='{ID_LISTE[386]}' OR
        Created_Id='{ID_LISTE[387]}' OR
        Created_Id='{ID_LISTE[388]}' OR
        Created_Id='{ID_LISTE[389]}' OR
        Created_Id='{ID_LISTE[390]}' OR
        Created_Id='{ID_LISTE[391]}' OR
        Created_Id='{ID_LISTE[392]}' OR
        Created_Id='{ID_LISTE[393]}' OR
        Created_Id='{ID_LISTE[394]}' OR
        Created_Id='{ID_LISTE[395]}' OR
        Created_Id='{ID_LISTE[396]}' OR
        Created_Id='{ID_LISTE[397]}' OR
        Created_Id='{ID_LISTE[398]}' OR
        Created_Id='{ID_LISTE[399]}' OR
        Created_Id='{ID_LISTE[400]}' OR
        Created_Id='{ID_LISTE[401]}' OR
        Created_Id='{ID_LISTE[402]}' OR
        Created_Id='{ID_LISTE[403]}' OR
        Created_Id='{ID_LISTE[404]}' OR
        Created_Id='{ID_LISTE[405]}' OR
        Created_Id='{ID_LISTE[406]}' OR
        Created_Id='{ID_LISTE[407]}' OR
        Created_Id='{ID_LISTE[408]}' OR
        Created_Id='{ID_LISTE[409]}' OR
        Created_Id='{ID_LISTE[410]}' OR
        Created_Id='{ID_LISTE[411]}' OR
        Created_Id='{ID_LISTE[412]}' OR
        Created_Id='{ID_LISTE[413]}' OR
        Created_Id='{ID_LISTE[414]}' OR
        Created_Id='{ID_LISTE[415]}' OR
        Created_Id='{ID_LISTE[416]}' OR
        Created_Id='{ID_LISTE[417]}' OR
        Created_Id='{ID_LISTE[418]}' OR
        Created_Id='{ID_LISTE[419]}' OR
        Created_Id='{ID_LISTE[420]}' OR
        Created_Id='{ID_LISTE[421]}' OR
        Created_Id='{ID_LISTE[422]}' OR
        Created_Id='{ID_LISTE[423]}' OR
        Created_Id='{ID_LISTE[424]}' OR
        Created_Id='{ID_LISTE[425]}' OR
        Created_Id='{ID_LISTE[426]}' OR
        Created_Id='{ID_LISTE[427]}' OR
        Created_Id='{ID_LISTE[428]}' OR
        Created_Id='{ID_LISTE[429]}' OR
        Created_Id='{ID_LISTE[430]}' OR
        Created_Id='{ID_LISTE[431]}' OR
        Created_Id='{ID_LISTE[432]}' OR
        Created_Id='{ID_LISTE[433]}' OR
        Created_Id='{ID_LISTE[434]}' OR
        Created_Id='{ID_LISTE[435]}' OR
        Created_Id='{ID_LISTE[436]}' OR
        Created_Id='{ID_LISTE[437]}' OR
        Created_Id='{ID_LISTE[438]}' OR
        Created_Id='{ID_LISTE[439]}' OR
        Created_Id='{ID_LISTE[440]}' OR
        Created_Id='{ID_LISTE[441]}' OR
        Created_Id='{ID_LISTE[442]}' OR
        Created_Id='{ID_LISTE[443]}' OR
        Created_Id='{ID_LISTE[444]}' OR
        Created_Id='{ID_LISTE[445]}' OR
        Created_Id='{ID_LISTE[446]}' OR
        Created_Id='{ID_LISTE[447]}' OR
        Created_Id='{ID_LISTE[448]}' OR
        Created_Id='{ID_LISTE[449]}' OR
        Created_Id='{ID_LISTE[450]}' OR
        Created_Id='{ID_LISTE[451]}' OR
        Created_Id='{ID_LISTE[452]}' OR
        Created_Id='{ID_LISTE[453]}' OR
        Created_Id='{ID_LISTE[454]}' OR
        Created_Id='{ID_LISTE[455]}' OR
        Created_Id='{ID_LISTE[456]}' OR
        Created_Id='{ID_LISTE[457]}' OR
        Created_Id='{ID_LISTE[458]}' OR
        Created_Id='{ID_LISTE[459]}' OR
        Created_Id='{ID_LISTE[460]}' OR
        Created_Id='{ID_LISTE[461]}' OR
        Created_Id='{ID_LISTE[462]}' OR
        Created_Id='{ID_LISTE[463]}' OR
        Created_Id='{ID_LISTE[464]}' OR
        Created_Id='{ID_LISTE[465]}' OR
        Created_Id='{ID_LISTE[466]}' OR
        Created_Id='{ID_LISTE[467]}' OR
        Created_Id='{ID_LISTE[468]}' OR
        Created_Id='{ID_LISTE[469]}' OR
        Created_Id='{ID_LISTE[470]}' OR
        Created_Id='{ID_LISTE[471]}' OR
        Created_Id='{ID_LISTE[472]}' OR
        Created_Id='{ID_LISTE[473]}' OR
        Created_Id='{ID_LISTE[474]}' OR
        Created_Id='{ID_LISTE[475]}' OR
        Created_Id='{ID_LISTE[476]}' OR
        Created_Id='{ID_LISTE[477]}' OR
        Created_Id='{ID_LISTE[478]}' OR
        Created_Id='{ID_LISTE[479]}' OR
        Created_Id='{ID_LISTE[480]}' OR
        Created_Id='{ID_LISTE[481]}' OR
        Created_Id='{ID_LISTE[482]}'
        
                                
                        """)  # SEÇİLİ SATIRLARI ÇEKMEK İÇİN
        data = cursor.fetchall()
        print("=>", len(data), "Adet ID listelendi.")

        # TODO: WRITE HTML FILE FOR QUICK VIEWS #############
        fieldset_css = """fieldset{width: 500px;margin:11px;padding:2px;border-width:1px;border: 1px solid #00000014;}"""
        display_css = """#block_container{display: flex;justify-content: center;flex-wrap: wrap; align-items: start;}"""
        import_font_css = """@import url('https://fonts.googleapis.com/css2?family=Roboto+Flex:opsz@8..144&family=Roboto:wght@300;400;500&display=swap');"""
        font_family_css_p = """p {font-family: 'Roboto Flex', sans-serif;margin: 5px 7px;padding: 1px;}"""
        font_family_css_others = """h1, h2, h3, h4, h5 {font-weight:500;font-family: 'Roboto', sans-serif;padding: 7px;}"""
        legend_css = """legend {color:#ffffff;background: #036299;border-width: 1px;font-family: 'Roboto Flex', sans-serif; padding:2px;}"""

        html_document_type_open_codes = f"""
        <!DOCTYPE html> 
        <html> 
        <body style="background: #f9f9f9">
        <h1 style="text-align:center;">{len(data)} Adet ID listelendi.</h1>
        <style>
            
            
            {import_font_css}
            {font_family_css_p}  
            {font_family_css_others}
            {display_css}
            {fieldset_css}
            {legend_css}
        
        
        </style>
        <div id="block_container">
        """
        html_document_type_close_codes = f"""
        </div>
        </body> 
        </html>
        """
        f = open("filtrelenen_videolari_hizli_izle.html", "w", encoding='utf-8')
        f = open("filtrelenen_videolari_hizli_izle.html", "a", encoding='utf-8')
        f.write(html_document_type_open_codes)

        for i in data:
            # TODO FOR HTML VİEW FOR DÖNGÜSÜ

            f = open("filtrelenen_videolari_hizli_izle.html", "a", encoding='utf-8')
            f.write(f"""
            <fieldset>
                <legend><p>ID {i[0]}  | {i[2]}</p></legend>
                <video width="600px" controls="controls"><source src="{i[3]}" type="video/mp4"></video>
            </fieldset>
            """)

        f = open("filtrelenen_videolari_hizli_izle.html", "a", encoding='utf-8')
        f.write(html_document_type_close_codes)
        f.close()
        con.close()  # close DATABASE

        print("\n => TEBRİKLER!\n => Html izlemesi başarıyla gerçekleştirildi.\n")

        # #####################################################

        print("""
            ++++++++++++++++++++++++++++++++++++++++++++++++++++
            +                                                  +
            +        PREMIERE PRO IMPORT FILTERED FILES        +
            +                                                  +
            ++++++++++++++++++++++++++++++++++++++++++++++++++++
        """)
        while True:
            soru3 = str(input("=> Filtrelenen dosyaları Premiere Pro'ya aktarmak ister misiniz? y/n/yes/no/YES/NO:"))

            if soru3 == "y" or soru3 == "Y" or soru3 == "yes" or soru3 == "YES":
                from Macos_and_Win_auto_project_ver3_function import ProjeOlustur

                plt = platform.system()

                if plt == "Windows":

                    tasklistesi = subprocess.Popen('TASKLIST', stdout=subprocess.PIPE).stdout.readlines()
                    type(tasklistesi)
                    c = str(list(tasklistesi)).find("b'Adobe Premiere Pro.exe")

                    if c == -1:
                        ProjeOlustur()

                elif plt == "Darwin":

                    tasklistesi = subprocess.Popen(["ps", "-axc"], stdout=subprocess.PIPE).stdout.readlines()
                    type(tasklistesi)
                    c = str(list(tasklistesi)).find(
                        "Adobe Premiere Pro 2020")  # ÖNEMLİ!!! MACOSX'TE VERSİYON NUMARASI VAR. Eğer güncellenirse buradaki değer değişritilmesi gerekir.

                    if c == -1:
                        ProjeOlustur()
                n = 1
                for i in data:


                    success = pymiere.objects.app.project.importFiles(
                        [i[3]],  # can import a list of media
                        suppressUI=True,
                        targetBin=pymiere.objects.app.project.rootItem,
                        importAsNumberedStills=False
                    )
                    print(n, ") => ", i[3], ": IMPORTED")

                    n+=1
                pymiere.objects.app.project.save()

                con.close()  # close DATABASE
                soru4 = str(input("""\n\n
                --------------------------------------------------------------------
                |                            THE END                                |
                |    Tüm işlemler bitti. En başa dönmek için ENTER'a basınız.       | 
                --------------------------------------------------------------------
                """))
                break

            if soru3 == "n" or soru3 == "N" or soru3 == "no" or soru3 == "NO":
                con.close()  # close DATABASE
                soru4 = str(input("""\n\n
                --------------------------------------------------------------------
                |                            THE END                                |
                |    Tüm işlemler bitti. En başa dönmek için ENTER'a basınız.       | 
                --------------------------------------------------------------------
                """))

                break
            else:
                print("=>", "\nLütfen geçerli bir seçenek giriniz!2\n")
    except:
        print("\n=> Lütfen geçerli bir seçenek giriniz!1\n")
