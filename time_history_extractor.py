import re
import json


class history_extractor:

  def __init__(self):
    self.days_m_1 = ['اول','دوم','سوم','چهارم','پنجم','ششم','هفتم','هشتم','نهم','دهم','یازدهم','دوازدهم','سیزدهم','چهاردهم','پانزدهم','شانزدهم','هفدهم','هجدهم','نوزدهم','بیستم','بیست‌و‌یکم','بیست‌و‌دوم','بیست‌و‌سوم','بیست‌و‌چهارم','بیست‌و‌پنجم','بیست‌و‌ششم','بیست‌و‌هفتم','بیست‌و‌هشتم','بیست‌و‌نهم','سی‌ام','سی‌و‌یکم']
    self.days_m_2 = ['اول','دوم','سوم','چهارم','پنجم','ششم','هفتم','هشتم','نهم','دهم','یازدهم','دوازدهم','سیزدهم','چهاردهم','پانزدهم','شانزدهم','هفدهم','هیجدهم','نوزدهم','بیستم','بیست و یکم','بیست و دوم','بیست و سوم','بیست و چهارم','بیست و پنجم','بیست و ششم','بیست و هفتم','بیست و هشتم','بیست و نهم','سی ام','سی و یکم']
    self.days_raw_1 = ['یک','دو','سه','چهار','پنج','شش','هفت','هشت','نه','ده','یازده','دوازده','سیزده','چهارده','پانزده','شانزده','هفده','هجده','نوزده','بیست','بیست‌و‌یک','بیست‌و‌دو','بیست‌و‌سه','بیست‌و‌چهار','بیست‌و‌پنج','بیست‌و‌شش','بیست‌و‌هفت','بیست‌و‌هشت','بیست‌و‌نه','سی‌','سی‌و‌یک']
    self.days_raw_2 = ['یک','دو','سه','چهار','پنج','شش','هفت','هشت','نه','ده','یازده','دوازده','سیزده','چهارده','پانزده','شانزده','هفده','هژده','نوزده','بیست','بیست و یک','بیست و دو','بیست و سه','بیست و چهار','بیست و پنج','بیست و شش','بیست و هفت','بیست و هشت','بیست و نه','سی','سی و یک']
    self.days_min_1 = [w + 'ین' for w in self.days_m_1]
    self.days_min_2 = [w + 'ین' for w in self.days_m_2]
    self.farsi_months_1 = ['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']
    self.farsi_months_2 = ['فروردین','اردی‌بهشت','خرداد','تیر','مرداد','شهریور','مهر','ابان','اذر','دی','بهمن','اسفند']
    self.ghamari_months_1 = ['محرم','صفر','ربیع‌الاول','ربیع‌الثانی','جمادی‌الاول','جمادی‌الثانی','رجب','شعبان','رمضان','شوال','ذیقعده','ذیحجه']
    self.ghamari_months_2 = ['محرم','صفر','ربیع الاول','ربیع الثانی','جمادی الاول','جمادی الثانی','رجب','شعبان','رمضان','شوال','ذوالقعده','ذوالحجه']
    self.miladi_months_1 = ['ژانویه','فبریه','مارس','آپریل','مه','جوئن','جولای','آگوست','سپتامبر','اکتبر','نوامبر','دسامبر']
    self.miladi_months_2 = ['ژانویه','فوریه','مارس','آوریل','می','ژوئن','ژولای','آگست','سپتامبر','اکتبر','نوامبر','دسامبر']
    self.miladi_months_3 = ['ژانبیه','فوریه','مارس','اوریل','می','ژوئن','ژولای','آگست','سپتامبر','اکتبر','نوامبر','دسامبر']
    self.miladi_months_4 = ['ژانویه','فوریه','مارس','اپریل','می','ژوئن','ژولای','آگست','سپتامبر','اکتبر','نوامبر','دسامبر']
    self.months_min = self.days_min_1[:12]
    self.re_farsi_months = '(' + '|'.join(self.farsi_months_1 + self.farsi_months_2) + ')'
    self.re_ghamari_months = '(' + '|'.join(self.ghamari_months_1 + self.ghamari_months_2) + ')'
    self.re_miladi_months = '(' + '|'.join(self.miladi_months_1 + self.miladi_months_2 + self.miladi_months_3 + self.miladi_months_4) + ')'
    self.re_months_min = '(' + '|'.join(self.months_min) + ')'
    self.re_days = '(' + '|'.join(self.days_m_1 + self.days_raw_1 + self.days_m_2 + self.days_raw_2) + ')'
    self.re_days_min = '(' + '|'.join(self.days_min_1 + self.days_min_2) + ')'
    self.shamsi_year_pattern = '([۱][۰-۴][۰-۹][.-۹]|[۰-۹][۰-۹][.-۹]|[۰-۹][.-۹]|[۰-۹][۰-۹]|[1][0-4][0-9][0-9]|[0-9][0-9][0-9]|[0-9][0-9]|[0-9])'
    self.miladi_year_pattern = '([1][5-9][0-9][0-9]|[2][0-1][0-9][0-9]|[۱][۵-۹][۰-۹][۰-۹]|[۲][۰-۱][۰-۹][۰-۹])'
    self.month_pattern = '([1][0-2]|[0-9]|[0][0-9]|[۱][۰-۲]|[۰-۹]|[۰][۰-۹])'
    self.day_pattern = '([1-3][0-9]|[0][0-9]|[0-9]|[۱-۳][۰-۹]|[۰-۹]|[۰][۰-۹])'
    self.rules()

  def farsi_year_map(self, year):
    if int(year) > 1 and int(year) < 100:
      return '13' + year
    else:
      return year

  def en_num_2_fa(self, num):
    num = str(num)
    num_dic = {
      '0': '۰',
      '1': '۱',
      '2': '۲',
      '3': '۳',
      '4': '۴',
      '5': '۵',
      '6': '۶',
      '7': '۷',
      '8': '۸',
      '9': '۹'}
    new_num = ''
    for digit in num:
      new_num += num_dic[digit]
    return new_num

  def fa_num_2_en(self, num):
    num = str(num)
    num_dic = {
      '۰': '0',
      '۱': '1',
      '۲': '2',
      '۳': '3',
      '۴': '4',
      '۵': '5',
      '۶': '6',
      '۷': '7',
      '۸': '8',
      '۹': '9'}
    new_num = ''
    for digit in num:
      new_num += num_dic[digit]
    return new_num

  def isEnglish(self, s):
    s = str(s)
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

  def zerofill_day_month(self, string):
    string = str(string)
    if len(string) == 1:
      return '0' + string
    elif len(string) == 2:
      return string

  def zerofill_year(self, string):
    string = str(string)
    str_len = 4 - len(string)
    return '0' * str_len + string

  def stringify(self, y, m, d, type_):
    if not self.isEnglish(y):
      y = self.fa_num_2_en(y)
    if not self.isEnglish(m):
      m = self.fa_num_2_en(m)
    if not self.isEnglish(d):
      d = self.fa_num_2_en(d)
    # zero filling of days, monts and years   
    d = self.zerofill_day_month(d)
    m = self.zerofill_day_month(m)
    y = self.zerofill_year(y)
    if type_ == 'fa':
      return y + '/' + m + '/' + d
    elif type_ == 'gh':
      return y + '/' + m + '/' + d + 'ه.ق'
    else:
      return d + '/' + m + '/' + y

  def month_mapping(self, month, type_):
    if type_ == 'fa':
      try:
        m = self.farsi_months_1.index(month) + 1
      except:
        m = self.farsi_months_2.index(month) + 1
    elif type_ == 'gh':
      try:
        m = self.ghamari_months_1.index(month) + 1
      except:
        m = self.ghamari_months_2.index(month) + 1
    elif type_ == 'ml':
      try:
        m = self.miladi_months_1.index(month) + 1
      except:
        try:
          m = self.miladi_months_2.index(month) + 1
        except:
          try:
            m = self.miladi_months_3.index(month) + 1
          except:
            m = self.miladi_months_4.index(month) + 1
    return m
    
  def day_min_mapping(self, day):
    try:
      d = self.days_min_1.index(day) + 1
    except:
      d = self.days_min_2.index(day) + 1
    return d

  def day_mapping(self, day):
    try:
      d = self.days_raw_1.index(day) + 1
    except:
      try:
        d = self.days_raw_2.index(day) + 1
      except:
        try:
          d = self.days_m_1.index(day) + 1
        except:
          d = self.days_m_2.index(day) + 1
    return d

  def rule_1_mapping(self, day, month, year, type_):
    y = year
    m = self.month_mapping(month, type_)
    d = day
    return self.stringify(y, m, d, type_)

  def rule_2_mapping(self, day, month, year, type_):
    y = year
    m = self.month_mapping(month, type_)
    d = self.day_mapping(day)
    return self.stringify(y, m, d, type_)
  
  def rule_3_mapping(self, day, month, year, type_):
    y = year
    m = self.months_min.index(month) + 1
    d = self.day_min_mapping(day)
    return self.stringify(y, m, d, type_)

  def rule_4_mapping(self, day, month, year, type_):
    y = year
    # find numeric version of month
    m = self.month_mapping(month, type_)
    # find numeric version of day  
    d = self.day_min_mapping(day)
    return self.stringify(y, m, d, type_)

  def rule_5_mapping(self, day, month, year, type_):
    return day + '/' + month + '/' + year
  
  def rules(self):
    # shamsi rules
    self.rule_1_farsi = '(?P<fa_1>' + r'(?:([۰۱۲۳۴۵۶۷۸۹0123456789]+)(?: )?)' + self.re_farsi_months  + '(?: ماه)?' + '(?: سال){0,1}' + '(?: )?' + self.shamsi_year_pattern + ')'
    self.rule_2_farsi = '(?P<fa_2>' + self.re_days + '(?: ماه)?' + '(?: )?' + self.re_farsi_months + '(?: ماه)?' + '(?: سال){0,1}' + '(?: )?' + self.shamsi_year_pattern + ')'
    self.rule_3_farsi = '(?P<fa_3>' + self.re_days_min + '(?: روز)' + '(?: از){0,1}' + ' ' + self.re_months_min + '(?: ماه)' + '(?: از){0,1}' \
    + '(?: سال){0,1}' + ' ' + self.shamsi_year_pattern + '(?: (?:هجری|هجری شمسی))?' + ')'
    self.rule_4_farsi = '(?P<fa_4>' + self.re_days_min + '(?: روز)' + '(?: از){0,1}' + '(?: ماه){0,1}' + '(?: ){0,1}' + self.re_farsi_months + '(?: از){0,1}' + '(?: سال){0,1}' + ' ' + self.shamsi_year_pattern + ')'
    self.rule_5_farsi = '(?P<fa_5>' + '\D' + self.shamsi_year_pattern + '(?:\\|\/|-|_|\.)' + self.month_pattern + '(?:\\|\/|-|_|\.)' + self.day_pattern + '\D' + '(?: شمسی|هجری شمسی)?' + ')'
    # ghamari rules
    self.rule_1_ghamari = '(?P<gh_1>' + r'(?:([۰۱۲۳۴۵۶۷۸۹0123456789]+)(?: )?)' + self.re_ghamari_months + '(?: ماه){0,1}' + '(?: سال){0,1}' + '(?: )?' + self.shamsi_year_pattern + ')'
    self.rule_2_ghamari = '(?P<gh_2>' + self.re_days + '(?: ماه)?' + ' ' + self.re_ghamari_months + '(?: ماه)?' + '(?: سال){0,1}' + '(?: ){0,1}' + self.shamsi_year_pattern + ')'
    self.rule_3_ghamari = '(?P<gh_3>' + self.re_days_min + '(?: روز)' + '(?: از){0,1}' + ' ' + self.re_months_min + '(?: ماه)' + '(?: از){0,1}' \
    + '(?: سال){0,1}' + ' ' + self.shamsi_year_pattern + '(?: (?:قمری|هجری قمری))' + ')'
    self.rule_4_ghamari = '(?P<gh_4>' + self.re_days_min + '(?: روز)' + '(?: از){0,1}' + '(?: ماه){0,1}' + ' ' + self.re_ghamari_months + '(?: از){0,1}' + '(?: سال){0,1}' + '(?: ){0,1}' + self.shamsi_year_pattern + ')'
    self.rule_5_ghamari = '(?P<gh_5>' + self.shamsi_year_pattern + '(?:\|/|-|_|\.)' + self.month_pattern + '(?:\|/|-|_|\.)' + self.day_pattern + ' قمری' + ')'
    # miladi rules
    self.rule_1_miladi = '(?P<ml_1>' + r'(?:([۰۱۲۳۴۵۶۷۸۹0123456789]+)(?: )?)' + self.re_miladi_months + '(?: ماه){0,1}' + '(?: سال){0,1}' + '(?: )?' + self.miladi_year_pattern + ')'
    self.rule_2_miladi = '(?P<ml_2>' + self.re_days + '(?: ماه)?' + ' ' + self.re_miladi_months + '(?: ماه)?' + '(?: سال){0,1}' + ' ' + self.miladi_year_pattern + ')'
    self.rule_3_miladi = '(?P<ml_3>' + self.re_days_min + '(?: روز)' + '(?: از){0,1}' + ' ' + self.re_months_min + '(?: ماه)' + '(?: از){0,1}' \
    + '(?: سال){0,1}' + ' ' + self.miladi_year_pattern + ')'
    self.rule_4_miladi = '(?P<ml_4>' + self.re_days_min + '(?: روز)' + '(?: از){0,1}' + '(?: ماه){0,1}' + ' ' + self.re_miladi_months + '(?: از){0,1}' + '(?: سال){0,1}' + ' ' + self.miladi_year_pattern + ')'
    self.rule_5_miladi = '((\d{1,4})[/.-](\d{1,2})[/.-](\d{1,4}))'
    # combining all rules
    self.rules = self.rule_1_farsi + '|' + self.rule_2_farsi + '|' + self.rule_3_farsi + '|' + self.rule_4_farsi + '|' + self.rule_5_farsi + '|' + \
            self.rule_1_ghamari + '|' + self.rule_2_ghamari + '|' + self.rule_3_ghamari + '|' + self.rule_4_ghamari + '|' + self.rule_5_ghamari + '|' + \
            self.rule_1_miladi + '|' + self.rule_2_miladi + '|' + self.rule_3_miladi + '|' + self.rule_4_miladi + '|' + self.rule_5_miladi
    self.pattern = re.compile(self.rules)

  def find(self, input_sentence):
    matches = re.finditer(self.pattern, input_sentence)
    found_list = []
    for match in matches:
      try:
        groups = match.groups()
        if groups[0] is not None:
          raw_string = groups[0]
          A = self.farsi_year_map(groups[3])
          string = self.rule_1_mapping(groups[1],groups[2],A,'fa')
        elif groups[4] is not None:
          raw_string = groups[4]
          A = self.farsi_year_map(groups[7])
          string = self.rule_2_mapping(groups[5],groups[6],A,'fa')
        elif groups[8] is not None:
          raw_string = groups[8]
          A = self.farsi_year_map(groups[11])
          string = self.rule_3_mapping(groups[9],groups[10],A,'fa')
        elif groups[12] is not None:
          raw_string = groups[12]
          A = self.farsi_year_map(groups[15])
          string = self.rule_4_mapping(groups[13],groups[14],A,'fa')
        elif groups[16] is not None:
          raw_string = groups[16]
          A = self.farsi_year_map(groups[17])
          string = self.rule_5_mapping(groups[19],groups[18],A,'fa')
        elif groups[20] is not None:
          raw_string = groups[20]
          string = self.rule_1_mapping(groups[21],groups[22],groups[23],'gh')
        elif groups[24] is not None:
          raw_string = groups[24]
          string = self.rule_2_mapping(groups[25],groups[26],groups[27],'gh')
        elif groups[28] is not None:
          raw_string = groups[28]
          string = self.rule_3_mapping(groups[29],groups[30],groups[31],'gh')
        elif groups[32] is not None:
          raw_string = groups[32]
          string = self.rule_4_mapping(groups[33],groups[34],groups[35],'gh')
        elif groups[36] is not None:
          raw_string = groups[36]
          string = self.rule_5_mapping(groups[39],groups[38],groups[37],'gh')
        elif groups[40] is not None:
          raw_string = groups[40]
          string = self.rule_1_mapping(groups[41],groups[42],groups[43],'ml')
        elif groups[44] is not None:
          raw_string = groups[44]
          string = self.rule_2_mapping(groups[45],groups[46],groups[47],'ml')
        elif groups[48] is not None:
          raw_string = groups[48]
          string = self.rule_3_mapping(groups[49],groups[50],groups[51],'ml')
        elif groups[52] is not None:
          raw_string = groups[52]
          string = self.rule_4_mapping(groups[53],groups[54],groups[55],'ml')
        elif groups[56] is not None:
          raw_string = groups[56]
          string = self.rule_5_mapping(groups[57],groups[58],groups[59],'ml')
        found_list.append({
            'phrase': raw_string.strip(),
            'value': string})
      except:
        pass
    return found_list


