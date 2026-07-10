# -*- coding: utf-8 -*-
import os
from data import (
    JOURNAL_ARTICLES, BOOK_CHAPTERS, OTHER_PUBLICATIONS, INVITED_TALKS,
    CONFERENCE_PRESENTATIONS, MEDIA, RESEARCH_AREAS, SOFTWARE,
    TEACHING_COURSES, TEACHING_AWARDS, APPOINTMENTS_CURRENT,
    APPOINTMENTS_PREVIOUS, SELECTED_GRANTS, PUBLICATION_LINKS, TALK_LINKS,
)

SITE = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html", "Home"),
    ("publications.html", "Publications"),
    ("talks.html", "Public Lectures"),
    ("software.html", "Software"),
    ("teaching.html", "Teaching"),
    ("media.html", "Media"),
    ("contact.html", "Contact"),
]

# Visibility & credit settings, per the intake form (both left checked = on).
PARAMS_MYSITE_CREDIT = True
PARAMS_MYSITE_DISCOVERY = True


def head(title, active, description):
    marker = (
        '\n  <meta name="mysite-directory" content="garyking.org/mysite">'
        if PARAMS_MYSITE_DISCOVERY else ""
    )
    nav_items = "\n".join(
        '        <li><a href="{href}"{cls}>{label}</a></li>'.format(
            href=href,
            cls=' class="active"' if href == active else "",
            label=label,
        )
        for href, label in NAV
    )
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Nicholas B. King</title>
  <meta name="description" content="{description}">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="assets/css/style.css">{marker}
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <nav class="navbar" aria-label="Primary">
      <a class="brand" href="index.html">Nicholas B. King</a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">&#9776;</button>
      <ul class="nav-links">
{nav_items}
      </ul>
    </nav>
  </header>
  <main id="main">
""".format(title=title, description=description, marker=marker, nav_items=nav_items)


def footer():
    credit = (
        '\n    <div class="footer-credit">Created using '
        '<a href="https://garyking.org/mysite">GaryKing.org/mysite</a></div>'
        if PARAMS_MYSITE_CREDIT else ""
    )
    return """  </main>
  <footer class="site-footer">
    <div class="container footer-inner">
      <div>
        <strong>Nicholas B. King</strong><br>
        Associate Professor, McGill University<br>
        <a href="mailto:Nicholas.king@mcgill.ca">Nicholas.king@mcgill.ca</a>
      </div>
      <ul class="footer-nav">
""" + "\n".join(
        '        <li><a href="{href}">{label}</a></li>'.format(href=h, label=l)
        for h, l in NAV
    ) + """
      </ul>
    </div>{credit}
  </footer>
  <script src="assets/js/main.js"></script>
</body>
</html>
""".format(credit=credit)


def write_page(filename, title, description, body):
    html = head(title, filename, description) + body + footer()
    with open(os.path.join(SITE, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)


# ---------------------------------------------------------------- index.html

HOMEPAGE_RESEARCH = [
    {
        "title": "A large language model-based tool for identifying relationships to industry in research on the carcinogenicity of benzene, cobalt, and aspartame",
        "authors": "DeBono N, Amar V, Hardy H, Schubauer-Berigan M, Ruths D, King NB.",
        "venue": "<em>Environmental Health</em> 24:64 (2025)",
        "description": "A proof-of concept paper introducing InfluenceMapper, a large language model-based tool that identifies extracts and analyzes disclosure information in scientific papers. InfluenceMapper is applied to a sample of 2046 papers to assess industry sponsorship and relationships in research on the carcinogenicity of benzene, cobalt, and aspartame.",
        "url": "https://doi.org/10.1186/s12940-025-01223-1",
    },
    {
        "title": "How global is global health research? A large-scale analysis of trends in authorship",
        "authors": "Dimitris MC, Gittings M, King NB.",
        "venue": "<em>BMJ Global Health</em> 6:e003758 (2021)",
        "description": "A large-scale analysis of over 786,000 publications examining how well researchers affiliated with low- and middle-income countries are represented in global health research, and how this has changed over time.",
        "url": "https://doi.org/10.1136/bmjgh-2020-003758",
    },
    {
        "title": "Harm Reduction: A Misnomer",
        "authors": "King NB.",
        "venue": "<em>Health Care Analysis</em> 28:324&ndash;334 (2020)",
        "description": "Harm reduction programs are usually justified on the utilitarian grounds that they aim to reduce the net harms of a behavior. In this paper, I contend that (1) the original intent and moral imperatives that guide harm reduction programs are not utilitarian; (2) the practical implementation of harm reduction programs is not, and probably cannot be, utilitarian; and (3) the continued justification of harm reduction on utilitarian grounds is untenable and may itself cause harm.",
        "url": "https://doi.org/10.1007/s10728-020-00413-x",
    },
]


def build_index():
    research_html = []
    for r in HOMEPAGE_RESEARCH:
        research_html.append("""        <div class="research-box">
          <h3><a href="{url}" target="_blank" rel="noopener">{title}</a></h3>
          <p class="research-meta">{authors} {venue}</p>
          <p>{description}</p>
        </div>""".format(
            url=r["url"], title=r["title"], authors=r["authors"],
            venue=r["venue"], description=r["description"],
        ))
    research_html = "\n".join(research_html)

    body = """    <section class="hero container">
      <div class="hero-grid">
        <div class="hero-left">
          <div class="hero-photo">
            <img src="images/headshot-full.jpg" alt="Portrait of Nicholas B. King" width="240" height="300">
          </div>
          <h1>Nicholas B. King</h1>

          <p class="position-block">
            <strong>Associate Professor</strong><br>
            Department of Equity, Ethics, and Policy<br>
            Max Bell School of Public Policy<br>
            McGill University
          </p>
          <p class="position-block">
            <strong>Associate Director</strong><br>
            Trottier Institute for Science and Public Policy
          </p>

          <div class="button-row">
            <a class="btn btn-secondary" href="files/King_CV_2026.pdf">CV</a>
            <a class="btn btn-secondary" href="mailto:Nicholas.king@mcgill.ca">Contact</a>
            <a class="btn btn-secondary" href="https://scholar.google.ca/citations?user=LWgI4HgAAAAJ&amp;hl=en" target="_blank" rel="noopener">Google Scholar</a>
          </div>

          <h2 class="section-title">About Me</h2>
          <p>I study how evidence, expertise, and value judgments shape public health and public
          policy, and how these tools can be manipulated and may encode assumptions that go
          unexamined. My early research examined the history and politics of emerging infectious
          disease and biosecurity. I have since turned my attention to the measurement and framing
          of health inequalities, the ethics of harm reduction and opioid policy, and, most
          recently, the use of machine learning and large language models to improve scientific
          transparency. I teach courses on artificial intelligence and public policy, evidence and
          expertise in policy, and public health ethics at McGill University. In my spare time I
          play the bass, compose music, go rock climbing, and take pictures. I&rsquo;m also
          learning to play the drums.</p>
        </div>

        <div class="hero-right">
          <h2 class="section-title">Research</h2>
{research_html}
        </div>
      </div>
    </section>
""".format(research_html=research_html)
    write_page(
        "index.html",
        "Home",
        "Nicholas B. King is an Associate Professor at McGill University working on public health policy, ethics, health inequalities, and AI in public policy.",
        body,
    )


# ---------------------------------------------------------------- publications.html

def build_publications():
    def pub_items(entries, tab):
        out = []
        for year, html in entries:
            url = PUBLICATION_LINKS.get(html)
            link_html = (
                ' <a class="read-link" href="{url}" target="_blank" rel="noopener">Read online &rarr;</a>'.format(url=url)
                if url else ""
            )
            out.append(
                '        <li class="pub-item" data-tab="{tab}" data-year="{year}">'
                '<span class="pub-year">{year}</span>{html}{link_html}</li>'.format(
                    tab=tab, year=year, html=html, link_html=link_html
                )
            )
        return "\n".join(out)

    all_items = (
        pub_items(JOURNAL_ARTICLES, "articles")
        + "\n"
        + pub_items(BOOK_CHAPTERS, "chapters")
        + "\n"
        + pub_items(OTHER_PUBLICATIONS, "other")
    )
    total = len(JOURNAL_ARTICLES) + len(BOOK_CHAPTERS) + len(OTHER_PUBLICATIONS)

    body = """    <section class="block container" style="padding-top:48px;">
      <h1>Publications</h1>
      <p style="color:var(--color-muted);">{total} publications. Filter by type below.</p>

      <div class="tab-strip">
        <button class="tab-btn active" data-tab="all">All</button>
        <button class="tab-btn" data-tab="articles">Journal Articles</button>
        <button class="tab-btn" data-tab="chapters">Book Chapters</button>
        <button class="tab-btn" data-tab="other">Other</button>
      </div>
      <p class="result-count">{total} of {total} results</p>

      <ul class="pub-list">
{items}
      </ul>
    </section>
""".format(total=total, items=all_items)
    write_page(
        "publications.html",
        "Publications",
        "Full list of peer-reviewed journal articles, book chapters, and other publications by Nicholas B. King.",
        body,
    )


# ---------------------------------------------------------------- talks.html

PUBLIC_LECTURES = [
    ("Defining freedom in the time of COVID", "https://www.youtube.com/watch?v=p98ex_FeMWA"),
    ("Weaponizing Uncertainty During the COVID-19 Pandemic", "https://www.youtube.com/watch?v=gZxu9fg1iYU"),
    ("Health Disparities Amid the COVID-19 Pandemic", "https://www.mcgill.ca/maxbellschool/article/policy-challenges-during-pandemic-video/video-health-disparities-amid-covid-19-pandemic"),
    ("Evidence and Uncertainty During the COVID-19 Pandemic", "https://www.mcgill.ca/maxbellschool/article/briefing-evidence-and-uncertainty-during-covid-19-pandemic"),
]


def build_talks():
    items = "\n".join(
        '        <li><a href="{url}" target="_blank" rel="noopener">{title}</a></li>'.format(url=url, title=title)
        for title, url in PUBLIC_LECTURES
    )

    body = """    <section class="block container" style="padding-top:48px;">
      <h1>Public Lectures</h1>
      <ul class="plain-list">
{items}
      </ul>
    </section>
""".format(items=items)
    write_page(
        "talks.html",
        "Public Lectures",
        "Public lectures and recorded talks by Nicholas B. King on public health ethics, health inequalities, and the COVID-19 pandemic.",
        body,
    )


# ---------------------------------------------------------------- software.html

def build_software():
    cards = []
    for s in SOFTWARE:
        links = "".join(
            '<li>{label}: {val}</li>'.format(label=l, val=v) for l, v in s["links"]
        )
        cards.append("""      <div class="card">
        <h2 style="margin-top:0;">{name}</h2>
        <p style="color:var(--color-clay); font-weight:600;">{tagline}</p>
        <p>{description}</p>
        <ul style="color:var(--color-muted); font-size:0.9rem;">{links}</ul>
      </div>""".format(name=s["name"], tagline=s["tagline"], description=s["description"], links=links))

    body = """    <section class="block container" style="padding-top:48px;">
      <h1>Software</h1>
      {cards}
    </section>
""".format(cards="\n".join(cards))
    write_page(
        "software.html",
        "Software",
        "Software projects by Nicholas B. King, including InfluenceMapper.",
        body,
    )


# ---------------------------------------------------------------- teaching.html

def build_teaching():
    course_rows = "\n".join(
        '        <tr><td>{c}<br><span style="color:var(--color-muted);">{l}</span></td><td>{y}</td></tr>'.format(c=c, l=l, y=y)
        for c, l, y in TEACHING_COURSES
        if "McGill" in l
    )
    award_rows = "\n".join(
        '        <tr><td>{a}</td><td>{y}</td></tr>'.format(a=a, y=y)
        for y, a in TEACHING_AWARDS
    )
    body = """    <section class="block container" style="padding-top:48px;">
      <h1>Teaching</h1>

      <h2 class="section-title">Courses taught</h2>
      <table class="plain">
        <tbody>
{courses}
        </tbody>
      </table>

      <h2 class="section-title">Teaching awards</h2>
      <table class="plain">
        <tbody>
{awards}
        </tbody>
      </table>
    </section>
""".format(courses=course_rows, awards=award_rows)
    write_page(
        "teaching.html",
        "Teaching",
        "Courses taught and teaching awards received by Nicholas B. King at McGill University and Case Western Reserve University.",
        body,
    )


# ---------------------------------------------------------------- contact.html

def build_contact():
    body = """    <section class="block container" style="padding-top:48px;">
      <h1>Contact</h1>
      <p>Email: <a href="mailto:Nicholas.king@mcgill.ca">Nicholas.king@mcgill.ca</a></p>
      <p>Department of Equity, Ethics &amp; Policy<br>
      Faculty of Medicine and Health Sciences<br>
      McGill University<br>
      Montreal, Quebec, Canada</p>
    </section>
"""
    write_page(
        "contact.html",
        "Contact",
        "Contact information for Nicholas B. King, Associate Professor at McGill University.",
        body,
    )


# ---------------------------------------------------------------- media.html

def build_media():
    rows = []
    for y, t, v, url in MEDIA:
        if url:
            title_html = '<a href="{url}" target="_blank" rel="noopener">{title}</a>'.format(url=url, title=t)
        else:
            title_html = t
        rows.append(
            '        <tr><td>{title_html}</td><td>{venue}</td><td>{year}</td></tr>'.format(
                title_html=title_html, venue=v, year=y
            )
        )
    rows = "\n".join(rows)
    body = """    <section class="block container" style="padding-top:48px;">
      <h1>Media</h1>
      <p style="color:var(--color-muted);">Selected media coverage and appearances.</p>
      <table class="plain">
        <tbody>
{rows}
        </tbody>
      </table>
    </section>
""".format(rows=rows)
    write_page(
        "media.html",
        "Media",
        "Selected media coverage of Nicholas B. King's research and commentary.",
        body,
    )


if __name__ == "__main__":
    build_index()
    build_publications()
    build_talks()
    build_software()
    build_teaching()
    build_contact()
    build_media()
    print("Build complete.")
