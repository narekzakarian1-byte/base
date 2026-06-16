#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Hexagon service pages from structured content (shared shell)."""
import os, html

OUT = os.path.join(os.path.dirname(__file__), "uslugi")
os.makedirs(OUT, exist_ok=True)

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')
TICK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l4 4 10-10"/></svg>')
TICK_THIN = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
             'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l4 4 10-10"/></svg>')
CHEVRON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
           'stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>')
CLOCK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">'
         '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>')
USERS = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">'
         '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/>'
         '<circle cx="17" cy="9" r="2.2"/><path d="M16 14.2c2.3.4 4 2.4 4 4.8"/></svg>')

NAV_LINKS = [
    ("consulting.html", "Hexagon Consulting", "Трансформация под ключ"),
    ("acceleration.html", "Hexagon Acceleration", "Сопровождение внедрения"),
    ("strategy-board.html", "Hexagon Strategy Board", "Стратегическое партнёрство"),
    ("fast-results.html", "Hexagon Fast Results", "Быстрые спринты"),
]

def nav(active):
    items = ""
    for href, title, sub in NAV_LINKS:
        items += (f'<a href="{href}"><div class="nm-title">{title}</div>'
                  f'<div class="nm-sub">{sub}</div></a>')
    return f'''<header class="nav">
    <div class="nav-inner">
      <a class="brand" href="../index.html" aria-label="Hexagon Consulting">
        <span class="hex-mark" aria-hidden="true">
          <svg viewBox="0 0 40 40" width="38" height="38" fill="none">
            <path d="M20 2 L35 11 L35 29 L20 38 L5 29 L5 11 Z" stroke="url(#hg)" stroke-width="1.6"/>
            <path d="M20 11 L28 15.5 L28 24.5 L20 29 L12 24.5 L12 15.5 Z" stroke="url(#hg)" stroke-width="1.2" opacity="0.6"/>
            <defs><linearGradient id="hg" x1="5" y1="2" x2="35" y2="38" gradientUnits="userSpaceOnUse">
              <stop stop-color="#E6B84E"/><stop offset="1" stop-color="#A9760E"/></linearGradient></defs>
          </svg>
        </span>
        <span class="brand-name">HEXAGON<span>.</span></span>
      </a>
      <nav class="nav-links" aria-label="Главное меню">
        <div class="nav-item">
          <a class="nav-link" href="../index.html#formats">Услуги</a>
          <div class="nav-menu">{items}</div>
        </div>
        <a class="nav-link" href="../index.html#solution">Методология</a>
        <a class="nav-link" href="../index.html#cases">Кейсы</a>
        <a class="nav-link" href="../index.html#trust">О нас</a>
      </nav>
      <a class="btn btn-gold btn-sm nav-cta-desktop" href="../index.html#contact">Запрос консультации {ARROW}</a>
      <button class="nav-toggle" aria-label="Открыть меню">
        <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
  </header>
  <div class="drawer" aria-hidden="true">
    <button class="drawer-close" aria-label="Закрыть меню">
      <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
    <a href="consulting.html">Hexagon Consulting</a>
    <a href="acceleration.html">Hexagon Acceleration</a>
    <a href="strategy-board.html">Hexagon Strategy Board</a>
    <a href="fast-results.html">Hexagon Fast Results</a>
    <a class="btn btn-gold btn-block" href="../index.html#contact">Запрос консультации</a>
  </div>'''

def footer():
    return '''<footer class="footer">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <a class="brand" href="../index.html" style="margin-bottom:18px;">
            <span class="hex-mark" aria-hidden="true">
              <svg viewBox="0 0 40 40" width="34" height="34" fill="none">
                <path d="M20 2 L35 11 L35 29 L20 38 L5 29 L5 11 Z" stroke="url(#hg2)" stroke-width="1.6"/>
                <defs><linearGradient id="hg2" x1="5" y1="2" x2="35" y2="38" gradientUnits="userSpaceOnUse"><stop stop-color="#E6B84E"/><stop offset="1" stop-color="#A9760E"/></linearGradient></defs>
              </svg>
            </span>
            <span class="brand-name">HEXAGON<span>.</span></span>
          </a>
          <p style="font-size:14px;color:var(--text-soft);max-width:34ch;">Стратегический партнёр компаний по управляемому росту. Меритократическая архитектура управления — Hexagon Management.</p>
        </div>
        <div>
          <h5>Услуги</h5>
          <a href="consulting.html">Hexagon Consulting</a>
          <a href="acceleration.html">Hexagon Acceleration</a>
          <a href="strategy-board.html">Hexagon Strategy Board</a>
          <a href="fast-results.html">Hexagon Fast Results</a>
        </div>
        <div>
          <h5>Компания</h5>
          <a href="../index.html#solution">Методология</a>
          <a href="../index.html#cases">Кейсы</a>
          <a href="../index.html#trust">О нас</a>
          <a href="../index.html#contact">Контакты</a>
        </div>
        <div>
          <h5>Связаться</h5>
          <a href="mailto:hello@hexagon.consulting">hello@hexagon.consulting</a>
          <a href="tel:+74950000000">+7 (495) 000-00-00</a>
          <a href="../index.html#contact">Запрос консультации</a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span data-year>2026</span> Hexagon Consulting. Все права защищены.</span>
        <span>Москва · Дубай · Алматы</span>
      </div>
    </div>
  </footer>'''

def svc_card(i, s):
    gives = "".join(f'<li><span class="tick">{TICK}</span>{html.escape(g)}</li>' for g in s["gives"])
    return f'''<article class="card svc reveal">
        <div class="svc-left">
          <span class="svc-num">{i:02d}</span>
          <h2>{html.escape(s["title"])}</h2>
          <p class="svc-what">{html.escape(s["what"])}</p>
          <div class="svc-meta">
            <span class="row">{USERS}{html.escape(s["who"])}</span>
            <span class="row">{CLOCK}Срок: {html.escape(s["term"])}</span>
          </div>
        </div>
        <div class="svc-right">
          <div class="gives-h">Что это даёт</div>
          <ul class="gives">{gives}</ul>
        </div>
      </article>'''

def page(fname, eyebrow, h1, intro, services, note=None):
    cards = "\n      ".join(svc_card(i + 1, s) for i, s in enumerate(services))
    note_html = (f'<p style="text-align:center;margin-top:30px;font-size:13.5px;color:var(--muted);">{html.escape(note)}</p>'
                 if note else "")
    doc = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(h1)} — Hexagon Consulting</title>
  <meta name="description" content="{html.escape(intro)}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/css/styles.css" />
</head>
<body class="bg-base">
  <div class="hex-field" aria-hidden="true"></div>
  {nav(fname)}

  <section class="subhero">
    <div class="glow glow-gold" style="width:480px;height:480px;top:-140px;right:-120px;" aria-hidden="true"></div>
    <div class="wrap">
      <nav class="crumbs reveal" aria-label="Хлебные крошки">
        <a href="../index.html">Главная</a>{CHEVRON}<a href="../index.html#formats">Услуги</a>{CHEVRON}<span>{html.escape(h1)}</span>
      </nav>
      <span class="eyebrow reveal">{html.escape(eyebrow)}</span>
      <h1 class="reveal reveal-d1" style="margin-top:18px;">{html.escape(h1)}</h1>
      <p class="lead reveal reveal-d2">{html.escape(intro)}</p>
      <div class="badge-line reveal reveal-d2">
        <span class="pill">{CLOCK}Гибкие сроки</span>
        <span class="pill">{USERS}Под ваш масштаб</span>
        <span class="pill">{TICK_THIN}Конкретный результат</span>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:40px;">
    <div class="wrap">
      <div class="svc-list">
      {cards}
      </div>
      {note_html}
    </div>
  </section>

  <section class="section" id="contact" style="padding-top:20px;">
    <div class="wrap">
      <div class="cta-final reveal">
        <span class="eyebrow" style="color:var(--gold-bright);justify-content:center;">Первый шаг</span>
        <h2 class="h2" style="margin-top:18px;">Обсудим вашу задачу?</h2>
        <p class="lead">Запросите консультацию и бесплатную экспресс-диагностику уровня управленческой зрелости вашей компании. Вы поймёте, где узкое место роста — и с чего начать.</p>
        <div style="margin-top:30px;display:flex;justify-content:center;">
          <a class="btn btn-gold" href="mailto:hello@hexagon.consulting">Запросить консультацию {ARROW}</a>
        </div>
        <p class="fine">Это займёт 30 минут. Без обязательств.</p>
      </div>
    </div>
  </section>

  {footer()}
  <script src="../assets/js/main.js"></script>
</body>
</html>
'''
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote", fname)


# ---------------- CONTENT ----------------

consulting = [
    {"title": "Продуктовое управление и стратегия", "who": "Средний и крупный бизнес", "term": "4–8 месяцев",
     "what": "Выстраиваем систему, в которой продукты развиваются от реальных болей клиента, а не от интуиции собственника. Гипотезы тестируются быстро и дёшево, а масштабируются только те, что подтвердили спрос.",
     "gives": ["Новые продукты выходят на рынок быстрее и с понятной экономикой",
               "Решения по продукту принимаются на данных, а не на мнениях",
               "Снижается стоимость ошибки: дорогие запуски заменяются дешёвыми проверками гипотез",
               "Продуктовая линейка перестаёт «промахиваться» мимо клиента",
               "Рост перестаёт зависеть от ручного участия собственника"]},
    {"title": "Корпоративное предпринимательство и внутренний рынок", "who": "Средний и крупный бизнес", "term": "5–10 месяцев",
     "what": "Превращаем менеджеров в «наёмных предпринимателей» с собственными мини-бизнесами, отдельными P&L и предпринимательской мотивацией. Между подразделениями выстраивается внутренний рынок с трансфертным ценообразованием.",
     "gives": ["Лидеры зарабатывают от реального бизнес-результата, а не от выполнения задач",
               "Внутренний рынок убирает «дотационные» подразделения и обнажает реальную эффективность",
               "Инициатива и ответственность растут без давления сверху",
               "Компания получает десятки точек роста вместо одной — на собственнике",
               "Сильнейшие лидеры остаются и растут вместе с бизнесом"]},
    {"title": "Стратегия развития и экспансии компании", "who": "Средний и крупный бизнес", "term": "3–6 месяцев",
     "what": "Определяем уникальное конкурентное преимущество компании и собираем стратегию роста вокруг ценности для клиента. Формируем дорожную карту экспансии, которую можно воспроизводить год за годом.",
     "gives": ["Чёткое понимание, за счёт чего компания выигрывает на рынке",
               "Стратегия, очищенная от бюрократического шума и «планов ради планов»",
               "Управляемая экспансия без потери прибыльности",
               "Приоритеты, на которые реально опирается команда в ежедневных решениях",
               "Рост, который не упирается в потолок текущей модели управления"]},
    {"title": "Построение дебюрократизированной оргструктуры", "who": "Средний и крупный бизнес", "term": "3–6 месяцев",
     "what": "Перестраиваем структуру под скорость и результат: убираем лишние уровни согласований, ненужные регламенты и узкие места. Полномочия и ресурсы получают те, кто создаёт наибольший вклад.",
     "gives": ["Решения принимаются быстрее и ближе к месту, где есть информация",
               "Сокращаются управленческие расходы и стоимость согласований",
               "Прозрачная ответственность вместо размытой",
               "Команды перестают «буксовать» в ожидании одобрений",
               "Структура масштабируется без потери управляемости"]},
    {"title": "Performance Management и целеполагание (OKR/cOKR)", "who": "Малый, средний и крупный бизнес", "term": "3–5 месяцев",
     "what": "Внедряем OKR/cOKR и контур контроля, который объединяет стратегию компании и интересы команд в единую систему целей. Развитие бизнеса становится личным интересом каждого лидера.",
     "gives": ["Цели команд напрямую связаны со стратегическими приоритетами",
               "Прозрачные метрики, по которым компания сверяется регулярно",
               "Снижается потребность в ручном контроле собственника",
               "Мотивация привязана к реальному результату, а не к активности",
               "Видно, какие инициативы двигают бизнес, а какие — нет"]},
    {"title": "Оптимизация бизнес-процессов и операционная эффективность", "who": "Малый, средний и крупный бизнес", "term": "3–6 месяцев",
     "what": "Делаем процессы «живыми» — выстроенными под скорость и результат, без лишней бюрократии. Дорогие, затянутые и буксующие процессы заменяются на эффективные.",
     "gives": ["Больше результата при меньшем числе действий",
               "Снижается себестоимость обслуживания бизнес-процессов",
               "Цифровизация перестаёт «буксовать» и начинает окупаться",
               "Высвобождается время команды на развитие, а не на рутину",
               "Рост маржинальности за счёт операционной эффективности"]},
]

acceleration = [
    {"title": "Полная акселерация по Hexagon Management", "who": "Средний и крупный бизнес", "term": "6–12 месяцев",
     "what": "Сопровождаем и обучаем лидеров компании развитию своих команд по полному циклу Hexagon Management. В контур входит большинство лидеров и их команды.",
     "gives": ["Лидеры осваивают методологию на собственных задачах, а не в теории",
               "Внедрение идёт силами самой команды — и остаётся после нас",
               "Конкретные бизнес-результаты на горизонте программы, а не «знания»",
               "Единый управленческий язык во всей компании",
               "Снижается зависимость от внешних консультантов в будущем"]},
    {"title": "Программа корпоративного предпринимательства", "who": "Средний и крупный бизнес", "term": "4–9 месяцев",
     "what": "Развиваем в компании корпоративное предпринимательство через обучение и акселерацию выбранных лидеров и их продуктов, с фокусом на эффективное продуктовое управление.",
     "gives": ["Лидеры учатся управлять продуктом как собственным бизнесом",
               "Появляются предприниматели внутри компании, а не исполнители",
               "Продукты получают владельцев, отвечающих за P&L",
               "Растёт скорость и качество запуска новых продуктов",
               "Формируется кадровый резерв сильных управленцев"]},
    {"title": "Акселерация внутренних стартапов и новых продуктов", "who": "Малый, средний и крупный бизнес", "term": "3–6 месяцев",
     "what": "Запускаем новые продукты и направления внутри компании по модернизированной методологии Lean Startup как компонента Hexagon Management.",
     "gives": ["Новые продукты проверяются дёшево до крупных вложений",
               "Сокращается time-to-market: от идеи до первых денег быстрее",
               "Отсев слабых гипотез до того, как они «съели» бюджет",
               "Системный конвейер новых продуктов вместо разовых попыток",
               "Рост выручки за счёт расширения продуктового портфеля"]},
]

strategy = [
    {"title": "Стратегический трекинг собственника / CEO", "who": "Малый, средний и крупный бизнес", "term": "регулярный, от 3 месяцев",
     "what": "Регулярная работа один на один с собственником или CEO: помогаем держать фокус на стратегических приоритетах, принимать ключевые решения и не утонуть в операционке.",
     "gives": ["Взгляд на бизнес со стороны от партнёра с опытом трансформаций",
               "Стратегические решения принимаются быстрее и увереннее",
               "Собственник выходит из операционки без потери контроля",
               "Приоритеты не размываются под потоком текущих задач",
               "Минимальное вовлечение команды — максимальный эффект на верхнем уровне"]},
    {"title": "Стратегический трекинг Совета лидеров", "who": "Средний и крупный бизнес", "term": "регулярный, от 4 месяцев",
     "what": "Сопровождаем команду топов: помогаем наладить коммуникацию, выстроить систему метрик и совместное принятие стратегических решений.",
     "gives": ["Топ-команда работает как единый орган управления, а не набор отделов",
               "Прозрачные метрики и регулярная сверка по целям",
               "Решения принимаются командой, а не спускаются сверху",
               "Снижается нагрузка на собственника как «единственное звено»",
               "Синхронизация стратегии и ежедневных действий лидеров"]},
    {"title": "Внешний департамент Strategy & Operations", "who": "Средний и крупный бизнес", "term": "регулярный, от 6 месяцев",
     "what": "Интегрируемся в компанию как внешний департамент стратегии и операций: берём на себя стратегическую функцию там, где у компании ещё нет своей сильной команды.",
     "gives": ["Полноценная стратегическая функция без найма дорогой команды",
               "Стратегия не только формулируется, но и доводится до исполнения",
               "Гибкое масштабирование вовлечения под задачи компании",
               "Доступ к методологии и экспертизе уровня крупных консалтингов",
               "Постепенная передача функции внутренней команде"]},
]

fast = [
    {"title": "CustDev Sprint — Customer Discovery", "who": "Малый, средний и крупный бизнес", "term": "2–4 недели",
     "what": "Глубинное исследование клиентов: выясняем, какую боль на самом деле решает ваш продукт и за что клиент готов платить.",
     "gives": ["Понимание реальной ценности продукта вместо догадок",
               "Список подтверждённых болей и потребностей клиента",
               "Основа для пересборки оффера и продуктовой линейки",
               "Снижение риска вкладываться не в то, что нужно рынку",
               "Часто — неожиданные точки роста, видимые только из интервью"]},
    {"title": "Market Intelligence Sprint", "who": "Малый, средний и крупный бизнес", "term": "2–4 недели",
     "what": "Быстрый анализ рынка, конкурентов и сегментов: где компания сейчас, где свободные ниши и за счёт чего можно расти.",
     "gives": ["Карта рынка и конкурентного поля без «воды»",
               "Сегменты с наибольшим потенциалом роста",
               "Понимание реального конкурентного преимущества",
               "Аргументы для приоритизации направлений",
               "База для стратегической сессии и решений по экспансии"]},
    {"title": "Strategic Session Sprint", "who": "Малый, средний и крупный бизнес", "term": "1–3 недели",
     "what": "Стратегическая сессия с топ-командой: определяем драйверы роста, приоритеты и решения, фиксируем roadmap на ближайший горизонт.",
     "gives": ["Согласованная стратегия и приоритеты у всей команды",
               "Конкретные решения и дорожная карта на выходе",
               "Синхронизация топов вокруг общих целей",
               "Снятие внутренних конфликтов по направлениям развития",
               "Готовый план, с которым можно работать с понедельника"]},
    {"title": "Growth Sprint — CJM, Value Proposition, Product Strategy", "who": "Малый, средний и крупный бизнес", "term": "3–5 недель",
     "what": "Единый быстрый формат для рывка в росте, внутри которого выбирается фокус: путь клиента (CJM), ценностное предложение и оффер или продуктовая стратегия.",
     "gives": ["Один фокусный спринт вместо трёх разрозненных проектов",
               "Переработанный оффер или карта пути клиента под реальные данные",
               "Чёткий приоритет: куда вкладывать ресурсы для роста",
               "Быстрая проверка гипотез без долгой трансформации",
               "Конкретные артефакты на выходе, готовые к внедрению"]},
    {"title": "Management Architecture Audit Sprint", "who": "Малый, средний и крупный бизнес", "term": "1–2 недели",
     "what": "Экспресс-диагностика управленческого контура: где компанию тормозит модель управления, а не рынок. Карта узких мест и точек роста.",
     "gives": ["Объективная оценка управленческой зрелости компании",
               "Список главных ограничителей роста с приоритетами",
               "Понимание, с чего начинать изменения и что даст быстрый эффект",
               "Аргументированный план дальнейшей трансформации",
               "Точка отсчёта, к которой можно вернуться и измерить прогресс"]},
    {"title": "Motivation & Incentives Quick Design", "who": "Малый, средний и крупный бизнес", "term": "1–3 недели",
     "what": "Быстрый дизайн системы мотивации под конкретную цель или управленческий контур: привязываем вознаграждение к реальному результату.",
     "gives": ["Мотивация, которая двигает нужные бизнес-метрики",
               "Прозрачные правила вместо «ручного» премирования",
               "Снижение перекосов, когда платят за активность, а не результат",
               "Удержание и рост сильных лидеров",
               "Готовая к внедрению модель, а не теоретическая схема"]},
    {"title": "Business Simulation / Strategic Game", "who": "Средний и крупный бизнес", "term": "1–2 недели",
     "what": "Стратегическая деловая игра с реальными решениями и артефактами на выходе. Команда проживает сценарии развития бизнеса в безопасной среде.",
     "gives": ["Команда учится принимать стратегические решения на практике",
               "Выявляются скрытые конфликты и узкие места в управлении",
               "Конкретные решения и артефакты, а не просто «тимбилдинг»",
               "Общий управленческий язык и опыт совместных решений",
               "Безопасная проверка стратегий до применения в реальном бизнесе"]},
    {"title": "Personal Strategy Consultation", "who": "Малый, средний и крупный бизнес", "term": "разовый формат",
     "what": "Персональная стратегическая консультация один на один с экспертом по вашей конкретной бизнес-задаче.",
     "gives": ["Взгляд со стороны на вашу ситуацию от практика трансформаций",
               "Конкретные варианты решения вашей задачи",
               "Приоритеты и первые шаги без долгого проекта",
               "Быстрый вход в методологию Hexagon Management",
               "Понимание, какой формат работы подойдёт дальше"]},
]

page("consulting.html", "Трансформация и стратегирование под ключ", "Hexagon Consulting",
     "Полное внедрение Hexagon Management для максимального результата. При этом каждый компонент имеет самостоятельную ценность и может внедряться отдельно.",
     consulting,
     note="Полная трансформация включает все продукты блоков Hexagon Acceleration, Strategy Board и Fast Results.")

page("acceleration.html", "Сопровождение вашего внедрения", "Hexagon Acceleration",
     "Помогаем компании вырасти через программы акселерации по Hexagon Management: сопровождаем и обучаем лидеров и команды методологии с достижением конкретных результатов по бизнесу.",
     acceleration)

page("strategy-board.html", "Стратегическое партнёрство с минимальной трансформацией", "Hexagon Strategy Board",
     "Входим в контур управления компании и стимулируем рост через комфортные форматы — от стратегического трекинга ключевых стейкхолдеров до интеграции как внешний департамент стратегии.",
     strategy)

page("fast-results.html", "Быстрые форматы с конкретным результатом", "Hexagon Fast Results",
     "Короткие спринты для точечных задач. Можно брать по отдельности или собирать в пакет под конкретную цель.",
     fast)

print("Done.")
