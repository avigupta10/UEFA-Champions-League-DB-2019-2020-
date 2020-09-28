# Generated by Django 3.1.1 on 2020-09-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChampionsLeague', '0016_auto_20200917_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='imgsrc',
            field=models.CharField(choices=[('<img alt="Bandera España" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/esp.png"/>', '<img alt="Bandera España" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/esp.png"/>'), ('<img alt="Bandera Chile" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/chi.png"/>', '<img alt="Bandera Chile" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/chi.png"/>'), ('<img alt="Bandera Colombia" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/col.png"/>', '<img alt="Bandera Colombia" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/col.png"/>'), ('<img alt="Bandera México" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/mex.png"/>', '<img alt="Bandera México" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/mex.png"/>'), ('<img alt="Bandera USA" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/usa.png"/>', '<img alt="Bandera USA" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/usa.png"/>'), ('<img alt="Bandera Argentina" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/arg.png"/>', '<img alt="Bandera Argentina" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/arg.png"/>'), ('<img alt="Bandera Perú" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/per.png"/>', '<img alt="Bandera Perú" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/per.png"/>'), ('<img alt="Bandera América" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/america.png"/>', '<img alt="Bandera América" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/america.png"/>'), ('<img alt="Bandera English" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/gbr.png"/>', '<img alt="Bandera English" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/gbr.png"/>'), ('<img alt="Bandera عربي" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/arb.png"/>', '<img alt="Bandera عربي" class="" src="//as01.epimg.net/img/comunes/fotos/fichas/paises/84_56/arb.png"/>'), ('<img alt="Photo of Lewandowski" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/l/lew/large/19319.png"/>', '<img alt="Photo of Lewandowski" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/l/lew/large/19319.png"/>'), ('<img alt="Badge/Flag Bayern" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/170.png"/>', '<img alt="Badge/Flag Bayern" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/170.png"/>'), ('<img alt="Photo of Erling Braut Haaland" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/e/erl/large/46369.png"/>', '<img alt="Photo of Erling Braut Haaland" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/e/erl/large/46369.png"/>'), ('<img alt="Badge/Flag B. Dortmund" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/87.png"/>', '<img alt="Badge/Flag B. Dortmund" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/87.png"/>'), ('<img alt="Photo of Serge Gnabry" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/ser/large/20737.png"/>', '<img alt="Photo of Serge Gnabry" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/ser/large/20737.png"/>'), ('<img alt="Badge/Flag Bayern" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/170.png"/>', '<img alt="Badge/Flag Bayern" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/170.png"/>'), ('<img alt="Photo of Sterling" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/ste/large/21357.png"/>', '<img alt="Photo of Sterling" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/ste/large/21357.png"/>'), ('<img alt="Badge/Flag M. City" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/66.png"/>', '<img alt="Badge/Flag M. City" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/66.png"/>'), ('<img alt="Photo of Depay" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/d/dep/large/21564.png"/>', '<img alt="Photo of Depay" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/d/dep/large/21564.png"/>'), ('<img alt="Badge/Flag Lyon" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/106.png"/>', '<img alt="Badge/Flag Lyon" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/106.png"/>'), ('<img alt="Photo of Kane" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/k/kan/large/20771.png"/>', '<img alt="Photo of Kane" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/k/kan/large/20771.png"/>'), ('<img alt="Badge/Flag Tottenham" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/72.png"/>', '<img alt="Badge/Flag Tottenham" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/72.png"/>'), ('<img alt="Photo of Mertens" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/mer/large/19804.png"/>', '<img alt="Photo of Mertens" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/mer/large/19804.png"/>'), ('<img alt="Badge/Flag Napoli" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/28.png"/>', '<img alt="Badge/Flag Napoli" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/28.png"/>'), ('<img alt="Photo of Gabriel Jesus" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/g/gab/large/37013.png"/>', '<img alt="Photo of Gabriel Jesus" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/g/gab/large/37013.png"/>'), ('<img alt="Badge/Flag M. City" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/66.png"/>', '<img alt="Badge/Flag M. City" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/66.png"/>'), ('<img alt="Photo of Josip Ilicic" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/j/jos/large/20952.png"/>', '<img alt="Photo of Josip Ilicic" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/j/jos/large/20952.png"/>'), ('<img alt="Badge/Flag Atalanta" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/21.png"/>', '<img alt="Badge/Flag Atalanta" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/21.png"/>'), ('<img alt="Photo of Kylian Mbappe" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/k/kyl/large/33539.png"/>', '<img alt="Photo of Kylian Mbappe" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/k/kyl/large/33539.png"/>'), ('<img alt="Badge/Flag PSG" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/49.png"/>', '<img alt="Badge/Flag PSG" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/49.png"/>'), ('<img alt="Photo of Icardi" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/i/ica/large/20961.png"/>', '<img alt="Photo of Icardi" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/i/ica/large/20961.png"/>'), ('<img alt="Badge/Flag PSG" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/49.png"/>', '<img alt="Badge/Flag PSG" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/49.png"/>'), ('<img alt="Photo of Benzema" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/b/ben/large/15784.png"/>', '<img alt="Photo of Benzema" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/b/ben/large/15784.png"/>'), ('<img alt="Badge/Flag Real Madrid" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/1.png"/>', '<img alt="Badge/Flag Real Madrid" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/1.png"/>'), ('<img alt="Photo of Luis Suárez" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/l/lui/large/18478.png"/>', '<img alt="Photo of Luis Suárez" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/l/lui/large/18478.png"/>'), ('<img alt="Badge/Flag Barcelona" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/3.png"/>', '<img alt="Badge/Flag Barcelona" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/3.png"/>'), ('<img alt="Photo of Heung-Min Son" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/son/large/20434.png"/>', '<img alt="Photo of Heung-Min Son" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/son/large/20434.png"/>'), ('<img alt="Badge/Flag Tottenham" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/72.png"/>', '<img alt="Badge/Flag Tottenham" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/72.png"/>'), ('<img alt="Photo of Lautaro Martínez" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/l/lau/large/34156.png"/>', '<img alt="Photo of Lautaro Martínez" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/l/lau/large/34156.png"/>'), ('<img alt="Badge/Flag Inter" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/35.png"/>', '<img alt="Badge/Flag Inter" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/35.png"/>'), ('<img alt="Photo of Rodrygo" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/r/rod/large/40471.png"/>', '<img alt="Photo of Rodrygo" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/r/rod/large/40471.png"/>'), ('<img alt="Badge/Flag Real Madrid" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/1.png"/>', '<img alt="Badge/Flag Real Madrid" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/1.png"/>'), ('<img alt="Photo of Mislav Orsic" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/silueta-generica-large.png"/>', '<img alt="Photo of Mislav Orsic" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/silueta-generica-large.png"/>'), ('<img alt="Badge/Flag D. Zagreb" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/324.png"/>', '<img alt="Badge/Flag D. Zagreb" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/324.png"/>'), ('<img alt="Photo of Salah" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/sal/large/21766.png"/>', '<img alt="Photo of Salah" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/sal/large/21766.png"/>'), ('<img alt="Badge/Flag Liverpool" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/65.png"/>', '<img alt="Badge/Flag Liverpool" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/65.png"/>'), ('<img alt="Photo of Forsberg" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/f/for/large/26182.png"/>', '<img alt="Photo of Forsberg" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/f/for/large/26182.png"/>'), ('<img alt="Badge/Flag RB Leipzig" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/4281.png"/>', '<img alt="Badge/Flag RB Leipzig" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/4281.png"/>'), ('<img alt="Photo of Müller" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/mul/large/18302.png"/>', '<img alt="Photo of Müller" src="//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/mul/large/18302.png"/>'), ('<img alt="Badge/Flag Bayern" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/170.png"/>', '<img alt="Badge/Flag Bayern" src="//as01.epimg.net/img/comunes/fotos/fichas/equipos/small/2x/170.png"/>')], max_length=200, null=True),
        ),
    ]
