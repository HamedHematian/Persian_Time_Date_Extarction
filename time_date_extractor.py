def time_marker_extractor(input_sentence):
  import re
  def farsi_year_map(year):
    if int(year) > 1 and int(year) < 100:
      return '13' + year
    else:
      return year

  def en_num_2_fa(num):
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
      '9': '۹',
    }

    new_num = ''
    for digit in num:
      new_num += num_dic[digit]
    return new_num

  def fa_num_2_en(num):
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
      '۹': '9',
    }

    new_num = ''
    for digit in num:
      new_num += num_dic[digit]
    return new_num

  def isEnglish(s):
    s = str(s)
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

  def zerofill_day_month(string):
    string = str(string)
    if len(string) == 1:
      return '0' + string
    elif len(string) == 2:
      return string

  def zerofill_year(string):
    string = str(string)
    str_len = 4 - len(string)
    return '0' * str_len + string



  def rule_1_mapping(day, month, year, type_):
    y = year
    if type_ == 'fa':
      try:
        m = farsi_months_1.index(month) + 1
      except:
        m = farsi_months_2.index(month) + 1
    elif type_ == 'gh':
      try:
        m = ghamari_months_1.index(month) + 1
      except:
        m = ghamari_months_2.index(month) + 1
    elif type_ == 'ml':
      try:
        m = miladi_months_1.index(month) + 1
      except:
        m = miladi_months_2.index(month) + 1
    d = day

    if not isEnglish(y):
      y = fa_num_2_en(y)
    if not isEnglish(m):
      m = fa_num_2_en(m)
    if not isEnglish(d):
      d = fa_num_2_en(d)
    
    d = zerofill_day_month(d)
    m = zerofill_day_month(m)
    y = zerofill_year(y)

    if type_ == 'fa':
      return y + '/' + m + '/' + d
    elif type_ == 'gh':
      return y + '/' + m + '/' + d + 'ه.ق'
    else:
      return d + '/' + m + '/' + y

  def rule_2_mapping(day, month, year, type_):
    y = year
    if type_ == 'fa':
      try:
        m = farsi_months_1.index(month) + 1
      except:
        m = farsi_months_2.index(month) + 1
    elif type_ == 'gh':
      try:
        m = ghamari_months_1.index(month) + 1
      except:
        m = ghamari_months_2.index(month) + 1
    elif type_ == 'ml':
      try:
        m = miladi_months_1.index(month) + 1
      except:
        m = miladi_months_2.index(month) + 1

    try:
      d = days_raw_1.index(day) + 1
    except:
      try:
        d = days_raw_2.index(day) + 1
      except:
        try:
          d = days_m_1.index(day) + 1
        except:
          d = days_m_2.index(day) + 1


    if not isEnglish(y):
      y = fa_num_2_en(y)
    if not isEnglish(m):
      m = fa_num_2_en(m)
    if not isEnglish(d):
      d = fa_num_2_en(d)

    d = zerofill_day_month(d)
    m = zerofill_day_month(m)
    y = zerofill_year(y)

    if type_ == 'fa':
      return y + '/' + m + '/' + d
    elif type_ == 'gh':
      return y + '/' + m + '/' + d + 'ه.ق'
    else:
      return d + '/' + m + '/' + y

  def rule_3_mapping(day, month, year, type_):
    y = year
    m = months_min.index(month) + 1
    try:
      d = days_min_1.index(day) + 1
    except:
      d = days_min_2.index(day) + 1

    if not isEnglish(y):
      y = fa_num_2_en(y)
    if not isEnglish(m):
      m = fa_num_2_en(m)
    if not isEnglish(d):
      d = fa_num_2_en(d)

    d = zerofill_day_month(d)
    m = zerofill_day_month(m)
    y = zerofill_year(y)

    if type_ == 'fa':
      return y + '/' + m + '/' + d
    elif type_ == 'gh':
      return y + '/' + m + '/' + d + 'ه.ق'
    else:
      return d + '/' + m + '/' + y

  def rule_4_mapping(day, month, year, type_):
    y = year
    if type_ == 'fa':
      try:
        m = farsi_months_1.index(month) + 1
      except:
        m = farsi_months_2.index(month) + 1
    elif type_ == 'gh':
      try:
        m = ghamari_months_1.index(month) + 1
      except:
        m = ghamari_months_2.index(month) + 1
    elif type_ == 'ml':
      try:
        m = miladi_months_1.index(month) + 1
      except:
        m = miladi_months_2.index(month) + 1
    try:
      d = days_min_1.index(day) + 1
    except:
      d = days_min_2.index(day) + 1

    if not isEnglish(y):
      y = fa_num_2_en(y)
    if not isEnglish(m):
      m = fa_num_2_en(m)
    if not isEnglish(d):
      d = fa_num_2_en(d)

    d = zerofill_day_month(d)
    m = zerofill_day_month(m)
    y = zerofill_year(y)

    if type_ == 'fa':
      return y + '/' + m + '/' + d
    elif type_ == 'gh':
      return y + '/' + m + '/' + d + 'ه.ق'
    else:
      return d + '/' + m + '/' + y

  def rule_5_mapping(day, month, year, type_):
    y = year
    m = month
    d = day
    if not isEnglish(y):
      y = fa_num_2_en(y)
    if not isEnglish(m):
      m = fa_num_2_en(m)
    if not isEnglish(d):
      d = fa_num_2_en(d)

    d = zerofill_day_month(d)
    m = zerofill_day_month(m)
    y = zerofill_year(y)

    if type_ == 'fa':
      return y + '/' + m + '/' + d
    elif type_ == 'gh':
      return y + '/' + m + '/' + d + 'ه.ق'
    else:
      return d + '/' + m + '/' + y

  days_m_1 = ['اول','دوم','سوم','چهارم','پنجم','ششم','هفتم','هشتم','نهم','دهم','یازدهم','دوازدهم','سیزدهم','چهاردهم','پانزدهم','شانزدهم','هفدهم','هجدهم','نوزدهم','بیستم','بیست‌و‌یکم','بیست‌و‌دوم','بیست‌و‌سوم','بیست‌و‌چهارم','بیست‌و‌پنجم','بیست‌و‌ششم','بیست‌و‌هفتم','بیست‌و‌هشتم','بیست‌و‌نهم','سی‌ام','سی‌و‌یکم']
  days_m_2 = ['اول','دوم','سوم','چهارم','پنجم','ششم','هفتم','هشتم','نهم','دهم','یازدهم','دوازدهم','سیزدهم','چهاردهم','پانزدهم','شانزدهم','هفدهم','هژدهم','نوزدهم','بیستم','بیست و یکم','بیست و دوم','بیست و سوم','بیست و چهارم','بیست و پنجم','بیست و ششم','بیست و هفتم','بیست و هشتم','بیست و نهم','سی ام','سی و یکم']
  days_raw_1 = ['یک','دو','سه','چهار','پنج','شش','هفت','هشت','نه','ده','یازده','دوازده','سیزده','چهارده','پانزده','شانزده','هفده','هجده','نوزده','بیست','بیست‌و‌یک','بیست‌و‌دو','بیست‌و‌سه','بیست‌و‌چهار','بیست‌و‌پنج','بیست‌و‌شش','بیست‌و‌هفت','بیست‌و‌هشت','بیست‌و‌نه','سی‌','سی‌و‌یک']
  days_raw_2 = ['یک','دو','سه','چهار','پنج','شش','هفت','هشت','نه','ده','یازده','دوازده','سیزده','چهارده','پانزده','شانزده','هفده','هژده','نوزده','بیست','بیست و یک','بیست و دو','بیست و سه','بیست و چهار','بیست و پنج','بیست و شش','بیست و هفت','بیست و هشت','بیست و نه','سی‌','سی و یک']
  days_min_1 = [w + 'ین' for w in days_m_1]
  days_min_2 = [w + 'ین' for w in days_m_2]

  year_1000 = ['هزار']
  year_100 = ['نهصد','هشتصد','هفتصد','ششصد','پانصد','چهارصد','سیصد','دویست','صد']
  year_20_90 = ['نود','هشتاد','هفتاد','شصت','پنجاه','چهل','سی','بیست']
  year_10 = ['نوزده','هجده','هفده','شانزده','پازده','چهارده','سیزده','دوازده','یازده']
  year = ['ده','نه','هست','هفت','شش','پنج','چهار','سه','دو','یک']

  re_year_1000 = '(?:' + '|'.join(year_1000) + ')'
  re_year_100 = '(?:' + '|'.join(year_100) + ')'
  re_year_20_90 = '(?:' + '|'.join(year_20_90) + ')'
  re_year_10 = '(?:' + '|'.join(year_10) + ')'
  re_year = '(?:' + '|'.join(year) + ')'



  farsi_months_1 = ['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']
  farsi_months_2 = ['فروردین','اردی‌بهشت','خرداد','تیر','مرداد','شهریور','مهر','ابان','اذر','دی','بهمن','اسفند']
  ghamari_months_1 = ['محرم','صفر','ربیع‌الاول','ربیع‌الثانی','جمادی‌الاول','جمادی‌الثانی','رجب','شعبان','رمضان','شوال','ذیقعده','ذیحجه']
  ghamari_months_2 = ['محرم','صفر','ربیع الاول','ربیع الثانی','جمادی الاول','جمادی الثانی','رجب','شعبان','رمضان','شوال','ذوالقعده','ذوالحجه']
  miladi_months_1 = ['ژانویه','فبریه','مارس','آپریل','مه','جوئن','جولای','آگوست','سپتامبر','اکتبر','نوامبر','دسامبر']
  miladi_months_2 = ['ژانویه','فوریه','مارس','آوریل','می','ژوئن','ژولای','آگست','سپتامبر','اکتبر','نوامبر','دسامبر']

  rules = []
  months_min = days_min_1[:12]

  re_farsi_months = '(' + '|'.join(farsi_months_1 + farsi_months_2) + ')'
  re_ghamari_months = '(' + '|'.join(ghamari_months_1 + ghamari_months_2) + ')'
  re_miladi_months = '(' + '|'.join(miladi_months_1 + miladi_months_2) + ')'

  re_months_min = '(' + '|'.join(months_min) + ')'
  re_days = '(' + '|'.join(days_m_1 + days_raw_1 + days_m_2 + days_raw_2) + ')'
  re_days_min = '(' + '|'.join(days_min_1 + days_min_2) + ')'
  shamsi_year_pattern = '([۱][۰-۴][۰-۹][.-۹]|[۰-۹][۰-۹][.-۹]|[۰-۹][.-۹]|[۰-۹][۰-۹]|[1][0-4][0-9][0-9]|[0-9][0-9][0-9]|[0-9][0-9]|[0-9])'
  miladi_year_pattern = '([1][5-9][0-9][0-9]|[2][0-1][0-9][0-9]|[۱][۵-۹][۰-۹][۰-۹]|[۲][۰-۱][۰-۹][۰-۹])'
  month_pattern = '([1][0-2]|[0-9]|[0][0-9]|[۱][۰-۲]|[۰-۹]|[۰][۰-۹])'
  day_pattern = '([1-3][0-9]|[0][0-9]|[0-9]|[۱-۳][۰-۹]|[۰-۹]|[۰][۰-۹])'
  rules = []

  rule_1_farsi = '(?P<fa_1>' + r'(?:([۰۱۲۳۴۵۶۷۸۹0123456789]+)(?: )?)' + re_farsi_months  + '(?: ماه)?' + '(?: سال){0,1}' + '(?: )?' + shamsi_year_pattern + ')'
  rule_2_farsi = '(?P<fa_2>' + re_days + '(?: ماه)?' + '(?: )?' + re_farsi_months + '(?: ماه)?' + '(?: سال){0,1}' + '(?: )?' + shamsi_year_pattern + ')'
  rule_3_farsi = '(?P<fa_3>' + re_days_min + '(?: روز)' + '(?: از){0,1}' + ' ' + re_months_min + '(?: ماه)' + '(?: از){0,1}' \
  + '(?: سال){0,1}' + ' ' + shamsi_year_pattern + '(?: (?:هجری|هجری شمسی))?' + ')'
  rule_4_farsi = '(?P<fa_4>' + re_days_min + '(?: روز)' + '(?: از){0,1}' + '(?: ماه){0,1}' + ' ' + re_farsi_months + '(?: از){0,1}' + '(?: سال){0,1}' + ' ' + shamsi_year_pattern + ')'
  rule_5_farsi = '(?P<fa_5>' + '\D' + shamsi_year_pattern + '(?:/|-|_)' + month_pattern + '(?:/|-|_)' + day_pattern + '\D' + '(?: شمسی|هجری شمسی)?' + ')'

  rule_1_ghamari = '(?P<gh_1>' + r'(?:([۰۱۲۳۴۵۶۷۸۹0123456789]+)(?: )?)' + re_ghamari_months + '(?: ماه){0,1}' + '(?: سال){0,1}' + '(?: )?' + shamsi_year_pattern + ')'
  rule_2_ghamari = '(?P<gh_2>' + re_days + '(?: ماه)?' + ' ' + re_ghamari_months + '(?: ماه)?' + '(?: سال){0,1}' + ' ' + shamsi_year_pattern + ')'
  rule_3_ghamari = '(?P<gh_3>' + re_days_min + '(?: روز)' + '(?: از){0,1}' + ' ' + re_months_min + '(?: ماه)' + '(?: از){0,1}' \
  + '(?: سال){0,1}' + ' ' + shamsi_year_pattern + '(?: (?:قمری|هجری قمری))' + ')'
  rule_4_ghamari = '(?P<gh_4>' + re_days_min + '(?: روز)' + '(?: از){0,1}' + '(?: ماه){0,1}' + ' ' + re_ghamari_months + '(?: از){0,1}' + '(?: سال){0,1}' + ' ' + shamsi_year_pattern + ')'
  rule_5_ghamari = '(?P<gh_5>' + shamsi_year_pattern + '(?:/|-|_)' + month_pattern + '(?:/|-|_)' + day_pattern + ' قمری' + ')'

  rule_1_miladi = '(?P<ml_1>' + r'(?:([۰۱۲۳۴۵۶۷۸۹0123456789]+)(?: )?)' + re_miladi_months + '(?: ماه){0,1}' + '(?: سال){0,1}' + '(?: )?' + miladi_year_pattern + ')'
  rule_2_miladi = '(?P<ml_2>' + re_days + '(?: ماه)?' + ' ' + re_miladi_months + '(?: ماه)?' + '(?: سال){0,1}' + ' ' + miladi_year_pattern + ')'
  rule_3_miladi = '(?P<ml_3>' + re_days_min + '(?: روز)' + '(?: از){0,1}' + ' ' + re_months_min + '(?: ماه)' + '(?: از){0,1}' \
  + '(?: سال){0,1}' + ' ' + miladi_year_pattern + ')'
  rule_4_miladi = '(?P<ml_4>' + re_days_min + '(?: روز)' + '(?: از){0,1}' + '(?: ماه){0,1}' + ' ' + re_miladi_months + '(?: از){0,1}' + '(?: سال){0,1}' + ' ' + miladi_year_pattern + ')'
  rule_5_miladi = '(?P<ml_5>' + day_pattern + '(?:/|-|_)' + month_pattern + '(?:/|-|_)' + miladi_year_pattern + '(?: میلادی)?' + ')'

  rules = rule_1_farsi + '|' + rule_2_farsi + '|' + rule_3_farsi + '|' + rule_4_farsi + '|' + rule_5_farsi + '|' + \
          rule_1_ghamari + '|' + rule_2_ghamari + '|' + rule_3_ghamari + '|' + rule_4_ghamari + '|' + rule_5_ghamari + '|' + \
          rule_1_miladi + '|' + rule_2_miladi + '|' + rule_3_miladi + '|' + rule_4_miladi + '|' + rule_5_miladi

  pattern = re.compile(rules)
  matches = re.finditer(pattern, input_sentence)
  found_list = []
  for match in matches:
    groups = match.groups()
    if groups[0] is not None:
      raw_string = groups[0]
      A = farsi_year_map(groups[3])
      string = rule_1_mapping(groups[1],groups[2],A,'fa')
    elif groups[4] is not None:
      raw_string = groups[4]
      A = farsi_year_map(groups[7])
      string = rule_2_mapping(groups[5],groups[6],A,'fa')
    elif groups[8] is not None:
      raw_string = groups[8]
      A = farsi_year_map(groups[11])
      string = rule_3_mapping(groups[9],groups[10],A,'fa')
    elif groups[12] is not None:
      raw_string = groups[12]
      A = farsi_year_map(groups[15])
      string = rule_4_mapping(groups[13],groups[14],A,'fa')
    elif groups[16] is not None:
      raw_string = groups[16]
      A = farsi_year_map(groups[17])
      string = rule_5_mapping(groups[19],groups[18],A,'fa')
    elif groups[20] is not None:
      raw_string = groups[20]
      string = rule_1_mapping(groups[21],groups[22],groups[23],'gh')
    elif groups[24] is not None:
      raw_string = groups[24]
      string = rule_2_mapping(groups[25],groups[26],groups[27],'gh')
    elif groups[28] is not None:
      raw_string = groups[28]
      string = rule_3_mapping(groups[29],groups[30],groups[31],'gh')
    elif groups[32] is not None:
      raw_string = groups[32]
      string = rule_4_mapping(groups[33],groups[34],groups[35],'gh')
    elif groups[36] is not None:
      raw_string = groups[36]
      string = rule_5_mapping(groups[39],groups[38],groups[37],'gh')
    elif groups[40] is not None:
      raw_string = groups[40]
      string = rule_1_mapping(groups[41],groups[42],groups[43],'ml')
    elif groups[44] is not None:
      raw_string = groups[44]
      string = rule_2_mapping(groups[45],groups[46],groups[47],'ml')
    elif groups[48] is not None:
      raw_string = groups[48]
      string = rule_3_mapping(groups[49],groups[50],groups[51],'ml')
    elif groups[52] is not None:
      raw_string = groups[52]
      string = rule_4_mapping(groups[53],groups[54],groups[55],'ml')
    elif groups[56] is not None:
      raw_string = groups[56]
      string = rule_5_mapping(groups[57],groups[58],groups[59],'ml')

    found_list.append({
        'phrase': raw_string.strip(),
        'value': string
    })

  return found_list
  

