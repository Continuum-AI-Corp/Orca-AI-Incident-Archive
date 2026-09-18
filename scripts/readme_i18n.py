# -*- coding: utf-8 -*-
"""Localized copy for the README sections that scripts/build.py regenerates.

The root README.md is English; the translations live in docs/i18n/, hence the
depth-2 relative path prefix (``up``).  Only the content between
<!-- BEGIN:xxx --> markers is generated - everything else is hand-written.
"""

README_L10N = {
    # ------------------------------------------------------------- English
    "README.md": dict(
        lang="en", up="",
        badges=["records", "months", "critical", "with real harm", "primary sources", "license"],
        thesis=(
            "Coverage runs from **2025-01** to **{last}** \u2014 {total} records of AI agent security "
            "events arranged month by month, plus one precursor traceable to {first}. "
            "Each record is a single Markdown file with a YAML header, an attack-chain diagram "
            "and **at least one primary source you can click**. "
            "Of the {total}, only **{harm} have a confirmed victim**."),
        months_year="**{y}** ({n} records)",
        months_foot="<sub>`n` = records that month, \u2605 = of which `critical`</sub>",
        crit_head=["Date", "Record", "Type", "Region"],
        crit_lead=(
            "Any of three triggers: \u2460 **confirmed** damage reaching multiple organisations, a "
            "government, critical infrastructure or a supply-chain worm; \u2461 a first-of-its-kind "
            "capability milestone with real victims; \u2462 research that **overturns a widely deployed "
            "defence** \u2014 `real_harm: false` in that case, {cnr} of these. "
            "Full criteria in [{up}taxonomy/severity.md]({up}taxonomy/severity.md)."),
        qual_head=["", ""],
        qual=[("Source links", "{links} links across {urls} unique URLs"),
              ("Records with no source", "**0** \u2014 no source, no entry"),
              ("Grade A (primary source)", "{ga}"),
              ("Flagged as disputed", "{disp}"),
              ("Verification rounds", "4")],
        cite="{total} records, 2025-01 to {lastm}; {harm} with confirmed real-world harm",
        footer="Built {build} \u00b7 {total} records \u00b7 {months} months",
    ),
    # ------------------------------------------------------------- 简体中文
    "docs/i18n/README.zh-CN.md": dict(
        lang="zh", up="../../",
        badges=["条目", "覆盖月份", "严重", "真实伤害", "一手来源", "授权"],
        thesis=(
            "收录范围从 **2025-01** 到 **{last}**，按月整理 {total} 条与 AI agent 有关的安全事件"
            "（另含 1 条可追到 {first} 的前序事件）。"
            "每条一个 Markdown 文件，带 YAML frontmatter、攻击链示意图和**至少一条可点开的来源**。"
            "{total} 条里只有 **{harm} 条**有确认的受害方。"),
        months_year="**{y}**（{n} 条）",
        months_foot="<sub>`n` = 当月条目数，★ = 其中 `critical` 的条数</sub>",
        crit_head=["日期", "事件", "类型", "地区"],
        crit_lead=(
            "三个触发条件任一：① **确认的**真实损害达到多组织 / 政府 / 关键基础设施 / 供应链蠕虫级别；"
            "② 属首次出现且有真实受害方的能力里程碑；③ **推翻了一项已被广泛部署的防护假设**的研究实证"
            "——此时 `real_harm: false`，共 {cnr} 条。"
            "完整口径见 [{up}taxonomy/severity.md]({up}taxonomy/severity.md)。"),
        qual_head=["", ""],
        qual=[("来源链接", "{links} 条，{urls} 个唯一 URL"),
              ("无来源条目", "**0** —— 没有来源的条目不进库"),
              ("可信度 A（一手源）", "{ga} 条"),
              ("标记为争议", "{disp} 条"),
              ("复核轮次", "4 轮")],
        cite="{total} 条，2025-01 至 {lastm}；{harm} 条有确认的真实伤害",
        footer="构建于 {build} · {total} 条 · {months} 个月",
    ),
    # ------------------------------------------------------------- 日本語
    "docs/i18n/README.ja.md": dict(
        lang="ja", up="../../",
        badges=["件数", "対象月数", "重大", "実害あり", "一次情報源", "ライセンス"],
        thesis=(
            "収録範囲は **2025-01** から **{last}** まで。AI エージェントに関わるセキュリティ事象 "
            "{total} 件を月単位で整理しています（ほかに {first} まで遡れる前史 1 件）。"
            "各レコードは YAML ヘッダー、攻撃連鎖図、そして**クリックできる一次情報源を必ず 1 つ以上**"
            "持つ Markdown ファイルです。{total} 件のうち、確認された被害者がいるのは **{harm} 件**だけです。"),
        months_year="**{y}年**（{n} 件）",
        months_foot="<sub>`n` = その月の件数、★ = うち `critical` の件数</sub>",
        crit_head=["日付", "レコード", "種別", "地域"],
        crit_lead=(
            "次のいずれかで `critical` とします。① **確認された**被害が複数組織・政府・重要インフラ・"
            "サプライチェーンワームの規模に達したもの。② 実被害を伴う初の能力マイルストーン。"
            "③ **広く展開された防御の前提を覆した**研究（この場合 `real_harm: false`、{cnr} 件）。"
            "詳細は [{up}taxonomy/severity.md]({up}taxonomy/severity.md)。"),
        qual_head=["", ""],
        qual=[("情報源リンク", "{links} 件 / ユニーク URL {urls} 件"),
              ("情報源なしのレコード", "**0** — 情報源がなければ収録しない"),
              ("評価 A（一次情報源）", "{ga} 件"),
              ("争いありとしてマーク", "{disp} 件"),
              ("検証回数", "4 回")],
        cite="{total} 件、2025-01〜{lastm}、うち {harm} 件に確認された実害",
        footer="ビルド {build} · {total} 件 · {months} ヶ月",
    ),
    # ------------------------------------------------------------- 한국어
    "docs/i18n/README.ko.md": dict(
        lang="ko", up="../../",
        badges=["레코드", "대상 개월", "심각", "실제 피해", "1차 출처", "라이선스"],
        thesis=(
            "수록 범위는 **2025-01**부터 **{last}**까지입니다. AI 에이전트와 관련된 보안 사건 "
            "{total}건을 월별로 정리했습니다({first}까지 거슬러 올라가는 선행 사건 1건 포함). "
            "각 레코드는 YAML 헤더, 공격 체인 도식, 그리고 **클릭할 수 있는 1차 출처 최소 1개**를 "
            "갖춘 Markdown 파일입니다. {total}건 중 확인된 피해자가 있는 것은 **{harm}건**뿐입니다."),
        months_year="**{y}년**({n}건)",
        months_foot="<sub>`n` = 해당 월 건수, ★ = 그중 `critical` 건수</sub>",
        crit_head=["날짜", "레코드", "유형", "지역"],
        crit_lead=(
            "세 가지 조건 중 하나라도 충족하면 `critical` 입니다. ① **확인된** 피해가 다수 조직·정부·"
            "핵심 인프라·공급망 웜 규모에 이른 경우. ② 실제 피해자가 있는 최초의 역량 이정표. "
            "③ **널리 배포된 방어 전제를 뒤엎었는지**를 입증한 연구(이 경우 `real_harm: false`, {cnr}건). "
            "전체 기준은 [{up}taxonomy/severity.md]({up}taxonomy/severity.md)."),
        qual_head=["", ""],
        qual=[("출처 링크", "{links}개 / 고유 URL {urls}개"),
              ("출처 없는 레코드", "**0** — 출처가 없으면 수록하지 않음"),
              ("등급 A(1차 출처)", "{ga}건"),
              ("분쟁 표시", "{disp}건"),
              ("검증 회차", "4회")],
        cite="{total}건, 2025-01~{lastm}, {harm}건은 확인된 실제 피해",
        footer="빌드 {build} · {total}건 · {months}개월",
    ),
    # ------------------------------------------------------------- Deutsch
    "docs/i18n/README.de.md": dict(
        lang="de", up="../../",
        badges=["Einträge", "Monate", "kritisch", "mit echtem Schaden",
                "Primärquellen", "Lizenz"],
        thesis=(
            "Die Abdeckung reicht von **2025-01** bis **{last}** \u2014 {total} Einträge zu "
            "Sicherheitsvorfällen mit KI-Agenten, Monat für Monat, dazu ein Vorläufer bis "
            "zurück zu {first}. Jeder Eintrag ist eine einzelne Markdown-Datei mit YAML-Kopf, "
            "Angriffsketten-Diagramm und **mindestens einer anklickbaren Primärquelle**. "
            "Von den {total} Einträgen haben nur **{harm} ein bestätigtes Opfer**."),
        months_year="**{y}** ({n} Einträge)",
        months_foot="<sub>`n` = Einträge des Monats, ★ = davon `critical`</sub>",
        crit_head=["Datum", "Eintrag", "Typ", "Region"],
        crit_lead=(
            "Einer von drei Auslösern genügt: \u2460 **bestätigter** Schaden, der mehrere "
            "Organisationen, eine Regierung, kritische Infrastruktur oder einen "
            "Supply-Chain-Wurm erreicht; \u2461 ein erstmaliger Fähigkeits-Meilenstein mit realen "
            "Opfern; \u2462 Forschung, die **eine weit verbreitete Verteidigungsannahme "
            "widerlegt** \u2014 dann `real_harm: false`, {cnr} Fälle. "
            "Vollständige Kriterien in [{up}taxonomy/severity.md]({up}taxonomy/severity.md)."),
        qual_head=["", ""],
        qual=[("Quell-Links", "{links} Links aus {urls} eindeutigen URLs"),
              ("Einträge ohne Quelle", "**0** \u2014 keine Quelle, kein Eintrag"),
              ("Grad A (Primärquelle)", "{ga}"),
              ("Als umstritten markiert", "{disp}"),
              ("Verifikationsrunden", "4")],
        cite="{total} Einträge, 2025-01 bis {lastm}; {harm} mit bestätigtem realen Schaden",
        footer="Erstellt am {build} \u00b7 {total} Einträge \u00b7 {months} Monate",
    ),
    # ------------------------------------------------------------- Français
    "docs/i18n/README.fr.md": dict(
        lang="fr", up="../../",
        badges=["entrées", "mois", "critiques", "préjudice réel",
                "sources primaires", "licence"],
        thesis=(
            "La couverture va de **2025-01** à **{last}** \u2014 {total} entrées d'événements de "
            "sécurité liés aux agents IA, mois par mois, plus un précurseur remontant à {first}. "
            "Chaque entrée est un fichier Markdown unique avec un en-tête YAML, un schéma de "
            "chaîne d'attaque et **au moins une source primaire cliquable**. "
            "Sur ces {total} entrées, seules **{harm} ont une victime confirmée**."),
        months_year="**{y}** ({n} entrées)",
        months_foot="<sub>`n` = entrées du mois, ★ = dont `critical`</sub>",
        crit_head=["Date", "Entrée", "Type", "Région"],
        crit_lead=(
            "L'un de ces trois déclencheurs suffit : \u2460 des dommages **confirmés** touchant "
            "plusieurs organisations, un gouvernement, une infrastructure critique ou un ver de "
            "chaîne d'approvisionnement ; \u2461 un jalon de capacité inédit avec de vraies "
            "victimes ; \u2462 une recherche qui **renverse une défense largement déployée** "
            "\u2014 dans ce cas `real_harm: false`, {cnr} cas. "
            "Critères complets dans [{up}taxonomy/severity.md]({up}taxonomy/severity.md)."),
        qual_head=["", ""],
        qual=[("Liens sources", "{links} liens sur {urls} URL uniques"),
              ("Entrées sans source", "**0** \u2014 pas de source, pas d'entrée"),
              ("Grade A (source primaire)", "{ga}"),
              ("Marquées comme contestées", "{disp}"),
              ("Cycles de vérification", "4")],
        cite="{total} entrées, de 2025-01 à {lastm} ; {harm} avec préjudice réel confirmé",
        footer="Généré le {build} \u00b7 {total} entrées \u00b7 {months} mois",
    ),
    # ------------------------------------------------------------- Español
    "docs/i18n/README.es.md": dict(
        lang="es", up="../../",
        badges=["registros", "meses", "críticos", "con daño real",
                "fuentes primarias", "licencia"],
        thesis=(
            "La cobertura va de **2025-01** a **{last}**: {total} registros de incidentes de "
            "seguridad relacionados con agentes de IA, mes a mes, más un precursor que se "
            "remonta a {first}. Cada registro es un único archivo Markdown con cabecera YAML, "
            "diagrama de cadena de ataque y **al menos una fuente primaria en la que se puede "
            "hacer clic**. De los {total}, solo **{harm} tienen una víctima confirmada**."),
        months_year="**{y}** ({n} registros)",
        months_foot="<sub>`n` = registros del mes, ★ = de ellos `critical`</sub>",
        crit_head=["Fecha", "Registro", "Tipo", "Región"],
        crit_lead=(
            "Basta con uno de estos tres desencadenantes: \u2460 daño **confirmado** que alcanza a "
            "varias organizaciones, un gobierno, infraestructura crítica o un gusano de cadena de "
            "suministro; \u2461 un hito de capacidad inédito con víctimas reales; \u2462 investigación "
            "que **refuta una defensa ampliamente desplegada** \u2014 en ese caso `real_harm: false`, "
            "{cnr} casos. Criterios completos en [{up}taxonomy/severity.md]({up}taxonomy/severity.md)."),
        qual_head=["", ""],
        qual=[("Enlaces de fuentes", "{links} enlaces de {urls} URL únicas"),
              ("Registros sin fuente", "**0** \u2014 sin fuente no hay registro"),
              ("Grado A (fuente primaria)", "{ga}"),
              ("Marcados como en disputa", "{disp}"),
              ("Rondas de verificación", "4")],
        cite="{total} registros, de 2025-01 a {lastm}; {harm} con daño real confirmado",
        footer="Generado el {build} \u00b7 {total} registros \u00b7 {months} meses",
    ),
}
