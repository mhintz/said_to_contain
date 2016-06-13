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

outputfile = open(os.path.dirname(os.path.realpath(__file__)) + "/iphone_credits.jade", "w+")

def write(something):
  outputfile.write(something)

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

def name_both(name_gen):
  return lambda: name_gen.first_name() + ' ' + name_gen.last_name()

def male_name(name_gen):
  return lambda: name_gen.first_name_male() + ' ' + name_gen.last_name()

def rand_chinese():
  return hanzi.to_pinyin(' '.join(list(fake_simp_china.name())))

def gen_rand_names(name_gen, count):
  return ' '.join(map(lambda i: name_gen(), range(count)))

def rand_captain_name():
  return [
    fake_bulgarian,
    fake_russian,
    fake_dutch,
    fake_uk,
    fake_danish,
    fake_slovene,
  ][random_thresholds([0.3, 0.75, 0.81, 0.9, 0.95])].name_male()

def rand_crew_member():
  name_gen = [
    fake_korean,
    fake_japanese,
    fake_simp_china,
    fake_portugal,
    fake_hindi,
    fake_spain,
    fake_filipino,
    fake_bulgarian,
  ][random_thresholds([0.05, 0.1, 0.35, 0.4, 0.45, 0.5, 0.92])]
  return male_name(name_gen)

def gen_ship_crew():
  return { "captain": rand_captain_name(), "crew": list(map(lambda _: rand_crew_member(), range(randint(15, 19)))) }

def gen_ship_name():
  return rand_from(["Maersk", "Spirit of", "Cap"]) + " " + rand_from([fake_uk, fake_spain]).first_name()

def gen_ship():
  return { "name": gen_ship_name(), "flag": rand_from(["Panama", "Liberia", "Marshall Islands", "Bahamas"]), "crew": gen_ship_crew() }

def print_ship(theship):
  ship_template = string.Template("""

  """)
  return 

# 46 Chinese iron miners
# 4 Chinese rail workers
# 24 Australian silicon miners
# 1 ship Australia > China
# 20 Australian iron miners
# 1 ship Australia > China
# 11 Indonesian tin miners
# 1 ship - Indonesia > China
# 35 Congolese coltan miners
# 1 ship DR Congo > Japan
# 35 Australian tantalum miners
# 1 ship Australia > Japan
# 21 Australian aluminum miners
# 1 ship Australia > China
# 12 Argentinian lithium miners
# 1 ship Argentina > Taiwan
# 42 Chilean copper miners
# 1 ship Chile > China
# 13 Russian tungsten miners
# 1 ship Russia > China
# 3 Congolese cobalt miners
# 1 ship DR Congo > China
# 3 Peruvian gold miners
# 1 ship Peru > China
# 2 Australian silver miners
# 1 ship Australia > China
# 12 Russian nickel miners
# 1 ship Russia > China
# 3 Brazilian neodymium miners
# 1 ship Brazil > China
# 1 Chinese praseodymium miner
# 3 Chinese rail workers
# 1 Turkish boron miner
# 1 ship Turkey > China
# 1 Chinese dysprosium miner
# 8 Chinese rail workers
# 6 Canadian Potash miners
# 1 ship Canada > China
# 1 Chinese indium miner
# 8 Chinese miners of assorted rare earths
# 30 Chinese steel workers
# 10 Chinese rail workers - steel shipping
# 30 Japanese Sony factory workers: iSight camera
# 1 ship Japan > China
# 30 Japanese Sharp factory workers: retina screen
# 1 ship Japan > China
# 7 Taiwanese factory workers: fingerprint sensor
# 1 ship Taiwan > China
# 10 Japanese factory workers: inductor coils
# 1 ship Japan > China
# 20 Japanese Toshiba factory workers: memory
# 1 ship Japan > China
# 2200 Chinese Foxconn factory assembly line workers
# 110 Chinese Foxconn factory floor bosses
# 10 Chinese Foxconn factory managers
# 1 Chinese Foxconn factory executive

# 100 American electronic engineers (100,000 emails)
# 40 American product designers (40,000 emails)
# 20 American marketers (30,000 emails)

# 1 ship China > Rotterdam
# 4 Dutch dock workers
# 3 German river barge drivers
# 1 Swiss train conductor
# 1 Swiss Apple store stock manager
# 1 Swiss telecoms employee
# 2 Swiss Apple store salesmen
# 1 American credit card company customer service employee

# for i in range(20):
# print(gen_rand_names(name_both(fake_us), 20))

template_variables = {
  
}

output_template = string.Template("""\
doctype html
html(lang="en")
  head
    title iPhone - Credits
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
      h1, h2 {
        text-align: center;
        font-weight: inherit;
      }
      h1 {
        font-size: 8em;
        margin: 2em 0 6em;
      }
      h2 {
        font-size: 3em;
        margin: 3em 0 1em;
      }
      p {
        font-size: 1.8em;
        text-align: justify;
      }
      p.centered {
        text-align: center;
      }
      .bigtopspace {
        margin-top: 10em;
      }
  body
    h1 iPhone
    h2 Chief Design Officer (1,000 Emails)
    p.centered Jony Ive
    h2 Purchaser
    p.centered Mark Hintz
    p.centered.bigtopspace.
      This production is a work of fiction. Any resemblance to other personages, real or imagined, express or implied, is purely coincidental
""")

write(output_template.substitute(template_variables))
