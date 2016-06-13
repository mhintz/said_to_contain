import string
import os
import sys
import time
from random import random, randint, randrange
from faker import Factory
from dragonmapper import hanzi
from names_db import filipino_first_names, filipino_last_names

def random_thresholds(thresholds):
  rnum = random()
  for idx, thr in enumerate(thresholds):
    if rnum < thr:
      return idx
  return len(thresholds)

def rand_from(names):
  return names[randrange(len(names))]

class filipino_name:
  def first_name_male(self):
    possible_names = [
      rand_from(filipino_first_names),
      fake_uk.first_name_male(),
      fake_spain.first_name_male(),
    ]
    return rand_from(possible_names)

  def last_name(self):
    return rand_from(filipino_last_names)

  def last_name_male(self):
    return rand_from(filipino_last_names)

class simp_chinese_name:
  def first_name(self):
    return hanzi.to_pinyin(fake_simp_china.first_name()).title()

  def first_name_male(self):
    return hanzi.to_pinyin(fake_simp_china.first_name_male()).title()

  def last_name(self):
    return hanzi.to_pinyin(fake_simp_china.last_name()).title()

  def last_name_male(self):
    return hanzi.to_pinyin(fake_simp_china.last_name()).title()

fake_bulgarian = Factory.create('bg_BG')
fake_czech = Factory.create('cs_CZ')
fake_german = Factory.create('de_DE')
fake_danish = Factory.create('dk_DK')
fake_greek = Factory.create('el_GR')
fake_australia = Factory.create('en_AU')
fake_canada = Factory.create('en_CA')
fake_uk = Factory.create('en_GB')
fake_us = Factory.create('en_US')
fake_spain = Factory.create('es_ES')
fake_mexico = Factory.create('es_MX')
fake_iran = Factory.create('fa_IR')
fake_finland = Factory.create('fi_FI')
fake_french = Factory.create('fr_FR')
fake_hindi = Factory.create('hi_IN')
fake_croatian = Factory.create('hr_HR')
fake_italian = Factory.create('it_IT')
fake_japanese = Factory.create('ja_JP')
fake_korean = Factory.create('ko_KR')
fake_lithuanian = Factory.create('lt_LT')
fake_latvian = Factory.create('lv_LV')
fake_nepali = Factory.create('ne_NP')
fake_dutch = Factory.create('nl_NL')
fake_norwegian = Factory.create('no_NO')
fake_polish = Factory.create('pl_PL')
fake_brazilian = Factory.create('pt_BR')
fake_portugal = Factory.create('pt_PT')
fake_russian = Factory.create('ru_RU')
fake_slovene = Factory.create('sl_SI')
fake_swedish = Factory.create('sv_SE')
fake_turkish = Factory.create('tr_TR')
fake_simp_china = Factory.create('zh_CN')
fake_trad_china = Factory.create('zh_TW')
fake_filipino = filipino_name()
fake_chinese_pinyin_stub = simp_chinese_name()

person_spacer = '<span class="personspace"> </span>'
nbsp = '&nbsp'

def name_both(name_gen):
  return lambda: name_gen.first_name() + nbsp + name_gen.last_name()

def name_male(name_gen):
  return lambda: name_gen.first_name_male() + nbsp + name_gen.last_name_male()

def gen_chinese_names(count, linebreak=True):
  genname = lambda x: nbsp.join(list(fake_simp_china.name()))
  joiner = '<br/>' if linebreak else ''
  return joiner.join(map(genname, range(count)))

def gen_chinese_male_names(count, linebreak=True):
  genname = lambda x: nbsp.join(list(fake_simp_china.name_male()))
  joiner = '<br/>' if linebreak else ''
  return joiner.join(map(genname, range(count)))

def gen_congolese_male_names(count):
  genname = lambda x: rand_from([fake_uk, fake_french]).first_name_male() + nbsp + rand_from([fake_uk, fake_french]).last_name()
  return person_spacer.join(map(genname, range(count)))

def gen_rand_names(name_gen, count):
  return person_spacer.join(map(lambda i: name_gen(), range(count)))

def rand_captain_name():
  name_gen = [
    fake_bulgarian,
    fake_russian,
    fake_dutch,
    fake_uk,
    fake_danish,
    fake_slovene,
    fake_german,
  ][random_thresholds([0.3, 0.55, 0.65, 0.75, 0.8, 0.9])]
  return name_male(name_gen)()

def rand_crew_member():
  name_gen = [
    fake_korean,
    fake_japanese,
    fake_chinese_pinyin_stub,
    fake_portugal,
    fake_hindi,
    fake_spain,
    fake_filipino,
    fake_bulgarian,
  ][random_thresholds([0.05, 0.08, 0.26, 0.32, 0.39, 0.48, 0.93])]
  return name_male(name_gen)()

def gen_ship_crew():
  return gen_rand_names(rand_crew_member, randint(15, 19))

def gen_ship_name():
  return rand_from(["Miss ", "Spirit of ", "Cap ", "HMS ", "", "", ""]) + rand_from([fake_uk, fake_spain]).first_name()

def gen_ship(route):
  return { "name": gen_ship_name(), "flag": rand_from(["Panama", "Liberia", "Marshall Islands", "Bahamas"]), "company": rand_from(["CMA", "COSCO", "CSC", "Maersk"]), "captain": rand_captain_name(), "crew": gen_ship_crew(), "route": route }

ship_template = string.Template("""\
h2 $route
    h3 Name
    p.centered $name ($company, registered in $flag)
    h3 Captain
    p.centered $captain
    h3 Crew
    p $crew
""")

def rand_ship(route):
  return ship_template.substitute(gen_ship(route))

template_variables = {
  "chiniron": gen_chinese_male_names(46, False),
  "chinironrail": gen_chinese_male_names(4, False),

  "aussilicon": gen_rand_names(name_male(fake_australia), 24),
  "ship1": rand_ship("Australia to China"),

  "ausiron": gen_rand_names(name_male(fake_australia), 20),
  "ship2": rand_ship("Australia to China"),

  "indotin": gen_rand_names(name_male(fake_filipino), 11),
  "ship3": rand_ship("Indonesia to China"),

  "congocoltan": gen_congolese_male_names(35),
  "ship4": rand_ship("DR Congo to Japan"),

  "austantalum": gen_rand_names(name_male(fake_australia), 35),
  "ship5": rand_ship("Australia to Japan"),

  "ausalu": gen_rand_names(name_male(fake_australia), 21),
  "ship6": rand_ship("Australia to China"),

  "argentinalithium": gen_rand_names(name_male(fake_mexico), 12),
  "ship7": rand_ship("Argentina to Taiwan"),

  "chileancopper": gen_rand_names(name_male(fake_mexico), 42),
  "ship8": rand_ship("Chile to China"),

  "russiantungsten": gen_rand_names(name_male(fake_russian), 13),
  "ship9": rand_ship("Russia to China"),

  "congocobalt": gen_congolese_male_names(3),
  "ship10": rand_ship("DR Congo to China"),

  "perugold": gen_rand_names(name_male(fake_mexico), 3),
  "ship11": rand_ship("Peru to China"),

  "aussilver": gen_rand_names(name_male(fake_australia), 2),
  "ship12": rand_ship("Australia to China"),

  "rusnickel": gen_rand_names(name_male(fake_russian), 12),
  "ship13": rand_ship("Russia to China"),

  "brazilneodym": gen_rand_names(name_male(fake_brazilian), 3),
  "ship14": rand_ship("Brazil to China"),

  "chinprasedym": gen_chinese_male_names(1, False),
  "chinrailpraseodym": gen_chinese_male_names(3, False),

  "turkboron": gen_rand_names(name_male(fake_turkish), 1),
  "ship15": rand_ship("Turkey to China"),

  "chindyspros": gen_chinese_male_names(1, False),
  "chinraildyspros": gen_chinese_male_names(8, False),

  "canpotash": gen_rand_names(name_male(fake_canada), 13),
  "ship16": rand_ship("Canada to China"),

  "chinindium": gen_chinese_male_names(1, False),

  "chinrareearth": gen_chinese_male_names(32, False),

  "chinsteelwork": gen_chinese_male_names(30, False),
  "chinsteelrail": gen_chinese_male_names(10, False),

  "amereleceng": gen_rand_names(name_both(fake_us), 100),
  "amerproddesign": gen_rand_names(name_both(fake_us), 40),
  "amermarketers": gen_rand_names(name_both(fake_us), 20),

  "sonyfac": gen_rand_names(name_both(fake_japanese), 30),
  "ship17": rand_ship("Japan to China"),

  "sharpfac": gen_rand_names(name_both(fake_japanese), 30),
  "ship18": rand_ship("Japan to China"),

  "fingerprintfac": gen_rand_names(name_both(fake_trad_china), 7),
  "ship19": rand_ship("Taiwan to China"),

  "inductorfac": gen_rand_names(name_both(fake_japanese), 10),
  "ship20": rand_ship("Japan to China"),

  "toshibafac": gen_rand_names(name_both(fake_japanese), 20),
  "ship21": rand_ship("Japan to China"),

  "samsungfac": gen_rand_names(name_both(fake_korean), 150),
  "ship23": rand_ship("Korea to China"),

  "foxconnworkers": gen_chinese_names(2200),
  "foxconnfloorboss": gen_chinese_names(110),
  "foxconnmanagers": gen_rand_names(name_male(fake_chinese_pinyin_stub), 10),
  "foxconnexec": gen_rand_names(name_male(fake_chinese_pinyin_stub), 1),
  "ship22": rand_ship("China to Rotterdam"),

  "dutchworkers": gen_rand_names(name_male(fake_dutch), 4),
  "germanriver": gen_rand_names(name_male(fake_german), 3),
  "swisstrain": gen_rand_names(name_both(fake_german), 1),
  "swissaplstock": gen_rand_names(name_both(fake_german), 1),
  "swisstelcom": gen_rand_names(name_both(fake_german), 1),
  "swissaplsales": gen_rand_names(name_male(fake_german), 2),
  "americancredit": gen_rand_names(name_both(fake_us), 1),
}

output_template = string.Template("""\
doctype html
html
  head
    title iPhone - Credits
    meta(charset="UTF-8")
    meta(http-equiv="X-UA-Compatible" content="IE=edge")
    meta(name="viewport" content="width=device-width,initial-scale=1")
    link(href='https://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300|Open+Sans:300', rel='stylesheet', type='text/css')
    style(type="text/css").
      body {
        font-size: 10px;
        font-family: "Source Sans Pro", Helvetica, sans-serif;
        font-weight: 200;
        background-color: black;
        color: white;
        margin: 0em 4em;
        padding: 0;
      }
      h1, h2, h3 {
        text-align: center;
        font-weight: inherit;
      }
      h1 {
        font-size: 8em;
        margin: 2em 0 0;
      }
      h2 {
        font-size: 3em;
        margin: 3em 0 1em;
      }
      .subheader {
        font-size: 3.3em;
        margin: 1em 0 11em;
      }
      h3 {
        font-size: 2.2em;
        margin: 1em 0 1em;
      }
      p {
        font-size: 1.7em;
        text-align: center;
      }
      p.centered {
        text-align: center;
      }
      .bigtopspace {
        margin-top: 10em;
      }
      .personspace {
        margin-left: 1.2em;
      }
      .chinesenames {
        column-width: 3.3em;
        text-align: right;
      }
    script(src="https://cdnjs.cloudflare.com/ajax/libs/gsap/1.18.5/TweenLite.min.js")
    script(type="text/javascript").
      window.onmousemove = function(e) {
        e.preventDefault();
        e.stopPropagation();
      };

      var windowPos = {
        pos: 0
      }

      window.onload = function() {
        console.log('window loaded');
        TweenLite.to(windowPos, {
          pos: window.innerHeight,
          duration: 10,
          onUpdate: function() {
            window.scrollTo(0, windowPos.pos)
          }
        });
      }
  body
    h1 iPhone

    h2.subheader A Short List of Credits

    h2 Chinese Iron Miners
    p.chinesenames $chiniron

    h2 Chinese Rail Workers (iron Shipping)
    p.chinesenames $chinironrail

    h2 Australian Silicon Miners
    p $aussilicon

    $ship1

    h2 Australian Iron Miners
    p $ausiron

    $ship2

    h2 Indonesian Tin Miners
    p $indotin

    $ship3

    h2 Congolese Coltan Miners
    p $congocoltan

    $ship4

    h2 Australian Tantalum Miners
    p $austantalum

    $ship5

    h2 Australian Aluminum Miners
    p $ausalu

    $ship6

    h2 Argentinian Lithium Miners
    p $argentinalithium

    $ship7

    h2 Chilean Copper Miners
    p $chileancopper

    $ship8

    h2 Russian Tungsten Miners
    p $russiantungsten

    $ship9

    h2 Congolese Cobalt Miners
    p $congocobalt

    $ship10

    h2 Peruvian Gold Miners
    p $perugold

    $ship11

    h2 Australian Silver Miners
    p $aussilver

    $ship12

    h2 Russian Nickel Miners
    p $rusnickel

    $ship13

    h2 Brazilian Neodymium Miners
    p $brazilneodym

    $ship14

    h2 Chinese Praseodymium Miner
    p $chinprasedym

    h2 Chinese Rail Workers (praseodymium Shipment)
    p $chinrailpraseodym

    h2 Turkish Boron Miner
    p $turkboron

    $ship15

    h2 Chinese Dysprosium Miner
    p $chindyspros

    h2 Chinese Rail Workers (dysprosium Shipment)
    p $chinraildyspros

    h2 Canadian Potash Miners
    p $canpotash

    $ship16

    h2 Chinese Indium Miner
    p $chinindium

    h2 Chinese Miners Of Assorted Rare Earths
    p $chinrareearth

    h2 Chinese Steel Workers
    p $chinsteelwork

    h2 Chinese Rail Workers (steel Shipment)
    p $chinsteelrail

    h2 American Electronic Engineers (100,000 Emails)
    p $amereleceng

    h2 American Product Designers (40,000 Emails)
    p $amerproddesign

    h2 American Marketers (30,000 Emails)
    p $amermarketers

    h2 Chief Design Officer (1,000 Emails)
    p.centered Jony Ive
    
    h2 Sony Factory Workers: Isight Camera
    p $sonyfac

    $ship17

    h2 Sharp Factory Workers: Retina Screen
    p $sharpfac

    $ship18

    h2 Taiwanese Factory Workers: Fingerprint Sensor
    p $fingerprintfac

    $ship19

    h2 Japanese Factory Workers: Inductor Coils
    p $inductorfac

    $ship20

    h2 Toshiba Factory Workers: Memory
    p $toshibafac

    $ship21

    h2 Samsung Factory Workers: A5 Processor
    p $samsungfac

    $ship23

    h2 Foxconn Factory Assembly Line Workers
    p.chinesenames $foxconnworkers
    h2 Foxconn Factory Floor Bosses
    p.chinesenames $foxconnfloorboss
    h2 Foxconn Factory Managers
    p $foxconnmanagers
    h2 Foxconn Factory Executive
    p $foxconnexec

    $ship22

    h2 Dutch Dock Workers
    p $dutchworkers

    h2 German River Barge Drivers
    p $germanriver

    h2 Swiss Train Conductor
    p.centered $swisstrain
    h2 Swiss Apple Store Stock Manager
    p.centered $swissaplstock
    h2 Swiss Telecoms Employee
    p.centered $swisstelcom
    h2 Swiss Apple Store Salesmen
    p.centered $swissaplsales

    h2 American Credit Card Company Customer Service Employee
    p.centered $americancredit

    h2 Purchaser
    p.centered Mark Hintz
    
    p.centered.bigtopspace This production is a work of fiction. Any resemblance to other personages, real or imagined, express or implied, is purely coincidental
""")

with open(os.path.dirname(os.path.realpath(__file__)) + "/iphone_credits.jade", "w+") as outputfile:
  outputfile.write(output_template.substitute(template_variables))
