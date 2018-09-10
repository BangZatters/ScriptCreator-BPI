#!/usr/bin/python

gxddp = "\033[93;1m<=[$] Script Deface Cretor By Mr.GxDDP [$]=>"

print gxddp
print "\033[92;1mTeam = BangZat PhiSingeRs InDoNeSia"
title = raw_input("\033[91;1mTitle / Judul : ")
titlem = raw_input("\033[92;1mTitle =>> Bentuk Ketikkan =>> Pertama : ")
titlem2 = raw_input("\033[93;1mTitle =>> Bentuk Ketikkan =>> Kedua : ")
icon = raw_input("\033[94;1mLink Gambar (Icon) : ")
nick = raw_input("\033[95;1mNick : ")
linkgmbr = raw_input("\033[96;1mlink gambar (Tengah) : ")
team = raw_input("\033[97;1mTeam Lu : ")
sebab = raw_input("\033[91;1mSebab Situs Kena Deface (marquee) : ")
print "\033[92;1mMasukkan Warna Textnya =>> Contoh = red / Pakai Code Warna"
colorm = raw_input("\033[93;1mMasukkan : ")
print "\033[94;1mPesan || Gunakan <br> Untuk Pesan Selanjutnya"
pesan = raw_input("\033[95;1mMasukkan : ")
print "\033[96;1mMasukkan Warna Textnya =>> Contoh = red / Pakai Code Warna"
colorp = raw_input("\033[97;1mMasukkan : ")
musik = raw_input("\033[91;1mCode Youtube (MUSIK) : ")
print "\033[92;1mSedang Proses Pembuatan"

#Proses Pembuatan
fo = open("script.html","w")

messagescript1 = """<html>
<head>
        <title>"""

messagescript2 = title

messagescript3 = """</title><script type="text/javascript">     var adfly_id = 19400118; l    var popunder_frequency_delay = 0; </script> <link rel="shorcut icon" href=" """

messagescript4 = icon

messagescript5 = """ "><script type='text/javascript'>
//<![CDATA[
msg = " """

messagescript6 = titlem2

messagescript7 = """ ";
msg = " """

messagescript8 = titlem


messagescript9 = """ " + msg;pos = 0;
function scrollMSG() {
document.title = (pos, msg.length) + msg.substring(0, pos); pos++;
if (pos > msg.length) pos = 0
window.setTimeout("scrollMSG()",80);
}
scrollMSG();
//]]></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css">
<link href="https://fonts.googleapis.com/css?family=Jolly+Lodger" rel="stylesheet" type="text/css" />
<br><iframe width="0%" height="0" scrolling="no" frameborder="no" allow="autoplay" src=" """

messagescript10 = musik

messagescript11 = """ "></iframe>
<style type="text/css">
@import url(http://fonts.googleapis.com/css?family=Iceland);
@import url(http://fonts.googleapis.com/css?family=Josefin+Slab);
body { background: #254A00; color: brown; font-family :'Iceland'; background-color: #000000; background-size: 100%; background-repeat:no-repeat; background-attachment: fixed; background-size: cover; background-position:center; }
.container {
        position:relative;
        margin:50px auto;
        max-width:800px;
        height:auto;
        border:2px solid #fff;
        padding:30px;
        box-sizing: border-box;
}

.transparent{
 background:rgba(31, 255, 28, 0.9);
 width: 100%;
 height:270px;
 padding:10px;
 margin:0px auto;
 color:#fff;
}

.transparent-box{
 background:rgba(46, 0, 102, 0.9);
 width: 100%;
 height:720px;
 padding:10px;
 margin:0px auto;
 color:#fff;
}
* {margin:0; padding:0;}

 nav {
 margin:auto;
 text-align: center;
 width: 100%;
 font-family: arial;
 }
 nav ul {
 background:#37988e;
 padding: 0 20px;
 list-style: none;
 position: relative;
 display: inline-table;
 width: 100%;
 }
 nav ul li{
 float:left;
 }

 nav ul li:hover{
 background:#d68d9a;
 }

 nav ul li:hover a{
 color:#000;
 }

 nav ul li a{
 display: block;
 padding: 25px;
 color: #fff;
 text-decoration: none;
</style>
<div style="position: fixed; top: 75px; left: -225px; width: 600px; padding: 10px; font-size: 24px; text-align: center; color: red; font-family: 'trebuchet ms', verdana, arial, sans-serif;transform: rotate(-45deg);transform-origin: 50% 0px;-o-transform: rotate(-45deg); -o-transform-origin: 50% 0px;-moz-transform: rotate(-45deg); -moz-transform-origin: 50% 0px; -webkit-transform: rotate(-45deg); -webkit-transform-origin: 50% 0px; background-color: Transparent; border: 1px solid rgb(170, 170, 170); z-index: 9999; opacity: 0.5;"><a style="text-decoration:none;color:#58FAF4;">"""

messagescript12 = nick

messagescript13 = """</a></div>
<center>
<font style="-webkit-text-stroke: 1px white;" size="20" color="blue" face="Jolly Lodger"  >"""

messagescript14 = nick

messagescript15 = """</font>
<br>
        <br>
<center><img src=" """

messagescript16 = linkgmbr

messagescript17 = """ "</center><br>
<br><center>

        <br><center>
<font style="-webkit-text-stroke: 1px red;" size="20" color="white" face="Jolly Lodger"  >Team : """

messagescript18 = team

messagescript19 = """</font></center>

<font style="-webkit-text-stroke: 1px blue;" size="15" color="white" face="Iceland"> Sebab Situs TerDeface</font><marquee behavior="scroll" style="background:rgb(0,0,0); text-align:center; border-top: 1px solid white; border-bottom: 1px solid #58FAF4"><font style="-webkit-text-stroke: 1px """

messagescript20 = colorm

messagescript21 = """;" color="white" size="6" face="Iceland">"""

messagescript22 = sebab

messagescript23 = """</marquee>

<br>
</div>
</form><center><script language="JavaScript">
var text=" """

messagescript24 = pesan

messagescript25 = """ ";
var delay=100000000;
var currentChar=1;
var destination="[none]";
function type()
{
//if (document.all)
{
var dest=document.getElementById(destination);
if (dest)// && dest.innerHTML)
{
dest.innerHTML=text.substr(0, currentChar)+"<blink> </blink>";
currentChar++;
if (currentChar>text.length)
{
currentChar=1;
setTimeout("type()", 50000000);
}
else
{
setTimeout("type()", delay);
}
}
}
}
function startTyping(textParam, delayParam, destinationParam)
{
text=textParam;
delay=delayParam;
currentChar=1;
destination=destinationParam;
type();
}
</script>
<b><div id="B4n9Z4tt3r5" style="font: 41px arial; color:"""

messagescript26 = colorp

messagescript27 = """; background:#000000;border-radius:5px;margin: 0px;padding:5px 10px 5px 10px;"></div></b>
<script language="JavaScript">
javascript:startTyping(text, 50, "B4n9Z4tt3r5");
</script></center><br><center><font style="-webkit-text-stroke: 1px Yellow;" color="White" size="20" face="Jolly Lodger">Hacked By """

messagescript28 = nick

messagescript29 = """</font></center>
<script>alert('Hacked By """

messagescript30 = nick

messagescript31 = """');</script>
<script>alert('Team : """

messagescript32 = team

messagescript33 = """');</script>"""


fo.write(messagescript1)
fo.write(messagescript2)
fo.write(messagescript3)
fo.write(messagescript4)
fo.write(messagescript5)
fo.write(messagescript6)
fo.write(messagescript7)
fo.write(messagescript8)
fo.write(messagescript9)
fo.write(messagescript10)
fo.write(messagescript11)
fo.write(messagescript12)
fo.write(messagescript13)
fo.write(messagescript14)
fo.write(messagescript15)
fo.write(messagescript16)
fo.write(messagescript17)
fo.write(messagescript18)
fo.write(messagescript19)
fo.write(messagescript20)
fo.write(messagescript21)
fo.write(messagescript22)
fo.write(messagescript23)
fo.write(messagescript24)
fo.write(messagescript25)
fo.write(messagescript26)
fo.write(messagescript27)
fo.write(messagescript28)
fo.write(messagescript29)
fo.write(messagescript30)
fo.write(messagescript31)
fo.write(messagescript32)
fo.write(messagescript33)

#Selesai Pembuatan

fo.close()
