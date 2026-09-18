# -*- coding: utf-8 -*-
"""Language registry: the seven supported languages and every display name
used by the generators.

English is the source language; every table below must have an ``en`` entry
and falls back to it when a translation is missing.  ``LANGS`` is a fixed
list (never derived from a set) so that generated output is reproducible.
"""

LANGS = ["en", "zh", "ja", "ko", "de", "fr", "es"]

# Native names, used in language switchers and README navigation.
LANG_LABEL = {
    "en": "English",
    "zh": "\u7b80\u4f53\u4e2d\u6587",
    "ja": "\u65e5\u672c\u8a9e",
    "ko": "\ud55c\uad6d\uc5b4",
    "de": "Deutsch",
    "fr": "Fran\u00e7ais",
    "es": "Espa\u00f1ol",
}

# BCP 47 tags for the HTML `lang` attribute.
LANG_TAG = {
    "en": "en", "zh": "zh-CN", "ja": "ja", "ko": "ko",
    "de": "de", "fr": "fr", "es": "es",
}

# Translation fields that live inline in every record's frontmatter.
TRANS_LANGS = ["zh", "ja", "ko", "de", "fr", "es"]


def name(table, key, lang):
    """Look up ``table[key][lang]`` with an English fallback."""
    row = table.get(key) or {}
    return row.get(lang) or row.get("en") or key


TYPE_NAME = {
    "IPI": {
        "en": "Indirect prompt injection",
        "zh": "\u95f4\u63a5\u63d0\u793a\u6ce8\u5165",
        "ja": "\u9593\u63a5\u30d7\u30ed\u30f3\u30d7\u30c8\u30a4\u30f3\u30b8\u30a7\u30af\u30b7\u30e7\u30f3",
        "ko": "\uac04\uc811 \ud504\ub86c\ud504\ud2b8 \uc778\uc81d\uc158",
        "de": "Indirekte Prompt-Injection",
        "fr": "Injection indirecte de prompt",
        "es": "Inyecci\u00f3n indirecta de prompt",
    },
    "EXFIL": {
        "en": "Data exfiltration",
        "zh": "\u6570\u636e\u5916\u6cc4",
        "ja": "\u30c7\u30fc\u30bf\u5916\u90e8\u9001\u4fe1",
        "ko": "\ub370\uc774\ud130 \uc720\ucd9c",
        "de": "Datenabfluss",
        "fr": "Exfiltration de donn\u00e9es",
        "es": "Exfiltraci\u00f3n de datos",
    },
    "SUPPLY": {
        "en": "Supply-chain poisoning",
        "zh": "\u4f9b\u5e94\u94fe\u6295\u6bd2",
        "ja": "\u30b5\u30d7\u30e9\u30a4\u30c1\u30a7\u30fc\u30f3\u6c5a\u67d3",
        "ko": "\uacf5\uae09\ub9dd \uc624\uc5fc",
        "de": "Supply-Chain-Vergiftung",
        "fr": "Empoisonnement de la cha\u00eene d'approvisionnement",
        "es": "Envenenamiento de la cadena de suministro",
    },
    "MCP": {
        "en": "MCP & tool-chain",
        "zh": "MCP / \u5de5\u5177\u94fe",
        "ja": "MCP\u30fb\u30c4\u30fc\u30eb\u30c1\u30a7\u30fc\u30f3",
        "ko": "MCP\u00b7\ud234\uccb4\uc778",
        "de": "MCP & Toolchain",
        "fr": "MCP et cha\u00eene d'outils",
        "es": "MCP y cadena de herramientas",
    },
    "SANDBOX": {
        "en": "Sandbox escape",
        "zh": "\u6c99\u7bb1\u9003\u9038",
        "ja": "\u30b5\u30f3\u30c9\u30dc\u30c3\u30af\u30b9\u8131\u51fa",
        "ko": "\uc0cc\ub4dc\ubc15\uc2a4 \ud0c8\ucd9c",
        "de": "Sandbox-Escape",
        "fr": "\u00c9vasion de bac \u00e0 sable",
        "es": "Escape de sandbox",
    },
    "ROGUE": {
        "en": "Rogue agent action",
        "zh": "agent \u81ea\u4e3b\u7834\u574f",
        "ja": "\u30a8\u30fc\u30b8\u30a7\u30f3\u30c8\u306e\u66b4\u8d70\u884c\u70ba",
        "ko": "\uc5d0\uc774\uc804\ud2b8 \uc790\uc728 \ud30c\uad34 \ud589\uc704",
        "de": "Entgleisung eines Agenten",
        "fr": "Action autonome d'agent",
        "es": "Acci\u00f3n aut\u00f3noma del agente",
    },
    "WEAPON": {
        "en": "Agent used as a weapon",
        "zh": "agent \u88ab\u7528\u4f5c\u653b\u51fb\u5de5\u5177",
        "ja": "\u653b\u6483\u30c4\u30fc\u30eb\u3068\u3057\u3066\u306e\u30a8\u30fc\u30b8\u30a7\u30f3\u30c8",
        "ko": "\uc5d0\uc774\uc804\ud2b8\uc758 \uacf5\uaca9 \ub3c4\uad6c\ud654",
        "de": "Agent als Angriffswerkzeug",
        "fr": "Agent utilis\u00e9 comme arme",
        "es": "Agente usado como arma",
    },
    "INFRA": {
        "en": "Agent infrastructure exposure",
        "zh": "agent \u57fa\u7840\u8bbe\u65bd\u66b4\u9732",
        "ja": "\u30a8\u30fc\u30b8\u30a7\u30f3\u30c8\u57fa\u76e4\u306e\u8d85\u9732",
        "ko": "\uc5d0\uc774\uc804\ud2b8 \uc778\ud504\ub77c \ub178\ucd9c",
        "de": "Exposition der Agenten-Infrastruktur",
        "fr": "Exposition de l'infrastructure d'agents",
        "es": "Exposici\u00f3n de infraestructura de agentes",
    },
    "CRED": {
        "en": "Credential abuse",
        "zh": "\u51ed\u636e\u6ee5\u7528",
        "ja": "\u8a8d\u8a3c\u60c5\u5831\u306e\u60aa\u7528",
        "ko": "\uc790\uaca9 \uc99d\uba85 \uc545\uc6a9",
        "de": "Missbrauch von Zugangsdaten",
        "fr": "Abus d'identifiants",
        "es": "Abuso de credenciales",
    },
    "EVAL": {
        "en": "Evaluation-environment breakout",
        "zh": "\u8bc4\u6d4b\u73af\u5883\u8d8a\u754c",
        "ja": "\u8a55\u4fa1\u74b0\u5883\u304b\u3089\u306e\u9038\u8131",
        "ko": "\ud3c9\uac00 \ud658\uacbd \uc774\ud0c8",
        "de": "Ausbruch aus der Evaluierungsumgebung",
        "fr": "\u00c9vasion de l'environnement d'\u00e9valuation",
        "es": "Escape del entorno de evaluaci\u00f3n",
    },
    "GOV": {
        "en": "Governance & policy",
        "zh": "\u6cbb\u7406 / \u76d1\u7ba1",
        "ja": "\u30ac\u30d0\u30ca\u30f3\u30b9\u30fb\u653f\u7b56",
        "ko": "\uac70\ubc84\ub10c\uc2a4\u00b7\uc815\ucc45",
        "de": "Governance & Regulierung",
        "fr": "Gouvernance et politiques",
        "es": "Gobernanza y pol\u00edticas",
    },
    "OTHER": {
        "en": "Other",
        "zh": "\u5176\u4ed6",
        "ja": "\u305d\u306e\u4ed6",
        "ko": "\uae30\ud0c0",
        "de": "Sonstiges",
        "fr": "Autre",
        "es": "Otros",
    },
}

REGION_NAME = {
    "GLOBAL": {"en": "Global", "zh": "\u5168\u7403", "ja": "\u30b0\u30ed\u30fc\u30d0\u30eb",
               "ko": "\uc804 \uc138\uacc4", "de": "Global", "fr": "Mondial", "es": "Global"},
    "US": {"en": "United States", "zh": "\u7f8e\u56fd", "ja": "\u30a2\u30e1\u30ea\u30ab",
           "ko": "\ubbf8\uad6d", "de": "Vereinigte Staaten", "fr": "\u00c9tats-Unis", "es": "Estados Unidos"},
    "EU": {"en": "Europe", "zh": "\u6b27\u6d32", "ja": "\u6b27\u5dde",
           "ko": "\uc720\ub7fd", "de": "Europa", "fr": "Europe", "es": "Europa"},
    "UK": {"en": "United Kingdom", "zh": "\u82f1\u56fd", "ja": "\u30a4\u30ae\u30ea\u30b9",
           "ko": "\uc601\uad6d", "de": "Vereinigtes K\u00f6nigreich", "fr": "Royaume-Uni", "es": "Reino Unido"},
    "JP": {"en": "Japan", "zh": "\u65e5\u672c", "ja": "\u65e5\u672c",
           "ko": "\uc77c\ubcf8", "de": "Japan", "fr": "Japon", "es": "Jap\u00f3n"},
    "KR": {"en": "South Korea", "zh": "\u97e9\u56fd", "ja": "\u97d3\u56fd",
           "ko": "\ud55c\uad6d", "de": "S\u00fcdkorea", "fr": "Cor\u00e9e du Sud", "es": "Corea del Sur"},
    "CN": {"en": "China", "zh": "\u4e2d\u56fd", "ja": "\u4e2d\u56fd",
           "ko": "\uc911\uad6d", "de": "China", "fr": "Chine", "es": "China"},
    "TW": {"en": "Taiwan", "zh": "\u53f0\u6e7e", "ja": "\u53f0\u6e7e",
           "ko": "\ub300\ub9cc", "de": "Taiwan", "fr": "Ta\u00efwan", "es": "Taiw\u00e1n"},
    "HK": {"en": "Hong Kong", "zh": "\u9999\u6e2f", "ja": "\u9999\u6e2f",
           "ko": "\ud64d\ucf69", "de": "Hongkong", "fr": "Hong Kong", "es": "Hong Kong"},
    "SG": {"en": "Singapore", "zh": "\u65b0\u52a0\u5761", "ja": "\u30b7\u30f3\u30ac\u30dd\u30fc\u30eb",
           "ko": "\uc2f1\uac00\ud3ec\ub974", "de": "Singapur", "fr": "Singapour", "es": "Singapur"},
    "AU": {"en": "Australia", "zh": "\u6fb3\u5927\u5229\u4e9a", "ja": "\u30aa\u30fc\u30b9\u30c8\u30e9\u30ea\u30a2",
           "ko": "\ud638\uc8fc", "de": "Australien", "fr": "Australie", "es": "Australia"},
    "LATAM": {"en": "Latin America", "zh": "\u62c9\u7f8e", "ja": "\u30e9\u30c6\u30f3\u30a2\u30e1\u30ea\u30ab",
              "ko": "\ub77c\ud2f4\uc544\uba54\ub9ac\uce74", "de": "Lateinamerika",
              "fr": "Am\u00e9rique latine", "es": "Latinoam\u00e9rica"},
    "SEA": {"en": "Southeast Asia", "zh": "\u4e1c\u5357\u4e9a", "ja": "\u6771\u5357\u30a2\u30b8\u30a2",
            "ko": "\ub3d9\ub0a8\uc544\uc2dc\uc544", "de": "S\u00fcdostasien",
            "fr": "Asie du Sud-Est", "es": "Sudeste asi\u00e1tico"},
    "APAC": {"en": "Asia-Pacific", "zh": "\u4e9a\u592a", "ja": "\u30a2\u30b8\u30a2\u592a\u5e73\u6d0b",
             "ko": "\uc544\uc2dc\uc544\ud0dc\ud3c9\uc591", "de": "Asien-Pazifik",
             "fr": "Asie-Pacifique", "es": "Asia-Pac\u00edfico"},
    "MX": {"en": "Mexico", "zh": "\u58a8\u897f\u54e5", "ja": "\u30e1\u30ad\u30b7\u30b3",
           "ko": "\uba55\uc2dc\ucf54", "de": "Mexiko", "fr": "Mexique", "es": "M\u00e9xico"},
    "BR": {"en": "Brazil", "zh": "\u5df4\u897f", "ja": "\u30d6\u30e9\u30b8\u30eb",
           "ko": "\ube0c\ub77c\uc9c8", "de": "Brasilien", "fr": "Br\u00e9sil", "es": "Brasil"},
    "TH": {"en": "Thailand", "zh": "\u6cf0\u56fd", "ja": "\u30bf\u30a4",
           "ko": "\ud0dc\uad6d", "de": "Thailand", "fr": "Tha\u00eflande", "es": "Tailandia"},
    "IL": {"en": "Israel", "zh": "\u4ee5\u8272\u5217", "ja": "\u30a4\u30b9\u30e9\u30a8\u30eb",
           "ko": "\uc774\uc2a4\ub77c\uc5d8", "de": "Israel", "fr": "Isra\u00ebl", "es": "Israel"},
    "IN": {"en": "India", "zh": "\u5370\u5ea6", "ja": "\u30a4\u30f3\u30c9",
           "ko": "\uc778\ub3c4", "de": "Indien", "fr": "Inde", "es": "India"},
    "DE": {"en": "Germany", "zh": "\u5fb7\u56fd", "ja": "\u30c9\u30a4\u30c4",
           "ko": "\ub3c5\uc77c", "de": "Deutschland", "fr": "Allemagne", "es": "Alemania"},
    "FR": {"en": "France", "zh": "\u6cd5\u56fd", "ja": "\u30d5\u30e9\u30f3\u30b9",
           "ko": "\ud504\ub791\uc2a4", "de": "Frankreich", "fr": "France", "es": "Francia"},
    "NL": {"en": "Netherlands", "zh": "\u8377\u5170", "ja": "\u30aa\u30e9\u30f3\u30c0",
           "ko": "\ub124\ub35c\ub780\ub4dc", "de": "Niederlande", "fr": "Pays-Bas", "es": "Pa\u00edses Bajos"},
    "CA": {"en": "Canada", "zh": "\u52a0\u62ff\u5927", "ja": "\u30ab\u30ca\u30c0",
           "ko": "\uce90\ub098\ub2e4", "de": "Kanada", "fr": "Canada", "es": "Canad\u00e1"},
    "RU": {"en": "Russia", "zh": "\u4fc4\u7f57\u65af", "ja": "\u30ed\u30b7\u30a2",
           "ko": "\ub7ec\uc2dc\uc544", "de": "Russland", "fr": "Russie", "es": "Rusia"},
    "KP": {"en": "North Korea", "zh": "\u671d\u9c9c", "ja": "\u5317\u671d\u9bae",
           "ko": "\ubd81\ud55c", "de": "Nordkorea", "fr": "Cor\u00e9e du Nord", "es": "Corea del Norte"},
    "IR": {"en": "Iran", "zh": "\u4f0a\u6717", "ja": "\u30a4\u30e9\u30f3",
           "ko": "\uc774\ub780", "de": "Iran", "fr": "Iran", "es": "Ir\u00e1n"},
    "MENA": {"en": "Middle East & North Africa", "zh": "\u4e2d\u4e1c\u5317\u975e",
             "ja": "\u4e2d\u6771\u30fb\u5317\u30a2\u30d5\u30ea\u30ab", "ko": "\uc911\ub3d9\u00b7\ubd81\uc544\ud504\ub9ac\uce74",
             "de": "Nahost & Nordafrika", "fr": "Moyen-Orient et Afrique du Nord",
             "es": "Oriente Medio y Norte de \u00c1frica"},
    "AFRICA": {"en": "Africa", "zh": "\u975e\u6d32", "ja": "\u30a2\u30d5\u30ea\u30ab",
               "ko": "\uc544\ud504\ub9ac\uce74", "de": "Afrika", "fr": "Afrique", "es": "\u00c1frica"},
}

SEV_NAME = {
    "critical": {"en": "Critical", "zh": "\u4e25\u91cd", "ja": "\u91cd\u5927",
                 "ko": "\uc2ec\uac01", "de": "Kritisch", "fr": "Critique", "es": "Cr\u00edtico"},
    "high": {"en": "High", "zh": "\u9ad8", "ja": "\u9ad8", "ko": "\ub192\uc74c",
             "de": "Hoch", "fr": "\u00c9lev\u00e9", "es": "Alto"},
    "medium": {"en": "Medium", "zh": "\u4e2d", "ja": "\u4e2d", "ko": "\uc911\uac04",
               "de": "Mittel", "fr": "Moyen", "es": "Medio"},
    "low": {"en": "Low", "zh": "\u4f4e", "ja": "\u4f4e", "ko": "\ub0ae\uc74c",
            "de": "Niedrig", "fr": "Faible", "es": "Bajo"},
    "info": {"en": "Info", "zh": "\u4fe1\u606f", "ja": "\u60c5\u5831", "ko": "\uc815\ubcf4",
             "de": "Information", "fr": "Information", "es": "Informativo"},
}

KIND_NAME = {
    "incident": {"en": "Incident", "zh": "\u771f\u5b9e\u4e8b\u6545", "ja": "\u5b9f\u969b\u306e\u30a4\u30f3\u30b7\u30c7\u30f3\u30c8",
                 "ko": "\uc2e4\uc81c \uc0ac\uace0", "de": "Vorfall", "fr": "Incident", "es": "Incidente"},
    "vulnerability": {"en": "Vulnerability disclosure", "zh": "\u6f0f\u6d1e\u62ab\u9732",
                      "ja": "\u8106\u5f31\u6027\u306e\u516c\u958b", "ko": "\ucde8\uc57d\uc810 \uacf5\uac1c",
                      "de": "Schwachstellen-Offenlegung", "fr": "Divulgation de vuln\u00e9rabilit\u00e9",
                      "es": "Divulgaci\u00f3n de vulnerabilidad"},
    "research": {"en": "Research demo", "zh": "\u7814\u7a76\u6f14\u793a", "ja": "\u7814\u7a76\u30c7\u30e2",
                 "ko": "\uc5f0\uad6c \uc2dc\uc5f0", "de": "Forschungsdemo", "fr": "D\u00e9monstration de recherche",
                 "es": "Demostraci\u00f3n de investigaci\u00f3n"},
    "report": {"en": "Threat report", "zh": "\u5a01\u80c1\u60c5\u62a5\u62a5\u544a",
               "ja": "\u8105\u5a01\u30a4\u30f3\u30c6\u30ea\u30b8\u30a7\u30f3\u30b9\u5831\u544a",
               "ko": "\uc704\ud611 \uc778\ud154\ub9ac\uc804\uc2a4 \ubcf4\uace0\uc11c",
               "de": "Bedrohungsbericht", "fr": "Rapport de menace", "es": "Informe de amenazas"},
    "policy": {"en": "Policy & regulation", "zh": "\u653f\u7b56 / \u76d1\u7ba1",
               "ja": "\u653f\u7b56\u30fb\u898f\u5236", "ko": "\uc815\ucc45\u00b7\uaddc\uc81c",
               "de": "Politik & Regulierung", "fr": "Politique et r\u00e9glementation",
               "es": "Pol\u00edtica y regulaci\u00f3n"},
}

AI_NAME = {
    "confirmed": {"en": "Confirmed", "zh": "\u5df2\u786e\u8ba4", "ja": "\u78ba\u8a8d\u6e08\u307f",
                  "ko": "\ud655\uc778\ub428", "de": "Best\u00e4tigt", "fr": "Confirm\u00e9", "es": "Confirmado"},
    "unverified": {"en": "Unverified", "zh": "\u672a\u8bc1\u5b9e", "ja": "\u672a\u78ba\u8a8d",
                   "ko": "\ubbf8\ud655\uc778", "de": "Unbest\u00e4tigt", "fr": "Non v\u00e9rifi\u00e9", "es": "Sin verificar"},
    "disputed": {"en": "Disputed", "zh": "\u6709\u4e89\u8bae", "ja": "\u4e89\u3044\u3042\u308a",
                 "ko": "\ubd84\uc7c1 \uc911", "de": "Umstritten", "fr": "Contest\u00e9", "es": "En disputa"},
    "not-applicable": {"en": "Not applicable", "zh": "\u4e0d\u9002\u7528", "ja": "\u8a72\u5f53\u306a\u3057",
                       "ko": "\ud574\ub2f9 \uc5c6\uc74c", "de": "Nicht zutreffend", "fr": "Non applicable",
                       "es": "No aplicable"},
}

# Strings used by generated Markdown pages (monthly indexes, topic/region
# tables).  English-only pages use the "en" entry directly.
LABELS = {
    "en": {
        "date": "Date", "record": "Record", "type": "Type", "severity": "Severity",
        "confidence": "Confidence", "harm": "Real harm", "month_records": "Records this month",
        "all_records": "All records", "records": "records", "by_severity": "by severity",
        "index_total": "**{n}** records across **{m}** months.",
        "index_head": ["Month", "Records", "critical", "high", "with real harm"],
        "index_total_row": "Total",
        "legend": "\u2605 = `critical` \u00b7 \u26a0\ufe0f = disputed facts or attribution \u00b7 "
                  "real harm: \u2705 confirmed victim / \u2014 none / \u00b7 not applicable "
                  "(policy and intelligence reports)",
        "nav_all": "All records", "nav_types": "By type",
        "harm_yes": "Yes", "harm_no": "No", "harm_na": "n/a",
    },
    "zh": {
        "date": "\u65e5\u671f", "record": "\u4e8b\u4ef6", "type": "\u7c7b\u578b",
        "severity": "\u4e25\u91cd\u5ea6", "confidence": "\u53ef\u4fe1\u5ea6",
        "harm": "\u771f\u5b9e\u4f24\u5bb3", "month_records": "\u672c\u6708\u6761\u76ee",
        "all_records": "\u5168\u90e8\u6761\u76ee", "records": "\u6761", "by_severity": "\u6309\u4e25\u91cd\u5ea6",
        "index_total": "\u5171 **{n}** \u6761\uff0c\u8986\u76d6 **{m}** \u4e2a\u6708\u3002",
        "index_head": ["\u6708\u4efd", "\u6761\u76ee", "critical", "high", "\u771f\u5b9e\u4f24\u5bb3"],
        "index_total_row": "\u5408\u8ba1",
        "legend": "\u2605 = `critical` \u00b7 \u26a0\ufe0f = \u4e8b\u5b9e\u6216\u5f52\u56e0\u5b58\u5728\u4e89\u8bae \u00b7 "
                  "\u771f\u5b9e\u4f24\u5bb3 \u2705 \u6709\u786e\u8ba4\u53d7\u5bb3\u65b9 / \u2014 \u65e0 / \u00b7 "
                  "\u4e0d\u9002\u7528\uff08\u653f\u7b56\u4e0e\u60c5\u62a5\u62a5\u544a\uff09",
        "nav_all": "\u5168\u5e93\u7d22\u5f15", "nav_types": "\u6309\u7c7b\u578b",
        "harm_yes": "\u662f", "harm_no": "\u5426", "harm_na": "\u4e0d\u9002\u7528",
    },
    "ja": {
        "date": "\u65e5\u4ed8", "record": "\u30ec\u30b3\u30fc\u30c9", "type": "\u7a2e\u5225",
        "severity": "\u6df1\u523b\u5ea6", "confidence": "\u4fe1\u983c\u5ea6",
        "harm": "\u5b9f\u5bb3", "month_records": "\u4eca\u6708\u306e\u30ec\u30b3\u30fc\u30c9",
        "all_records": "\u5168\u30ec\u30b3\u30fc\u30c9", "records": "\u4ef6", "by_severity": "\u6df1\u523b\u5ea6\u5225",
        "index_total": "\u5168 **{n}** \u4ef6\u3001**{m}** \u30f6\u6708\u5206\u3002",
        "index_head": ["\u6708", "\u4ef6\u6570", "critical", "high", "\u5b9f\u5bb3\u3042\u308a"],
        "index_total_row": "\u5408\u8a08",
        "legend": "\u2605 = `critical` \u00b7 \u26a0\ufe0f = \u4e8b\u5b9f\u307e\u305f\u306f\u5e30\u5c5e\u306b\u4e89\u3044\u3042\u308a \u00b7 "
                  "\u5b9f\u5bb3\uff1a\u2705 \u88ab\u5bb3\u8005\u78ba\u5b9a / \u2014 \u306a\u3057 / \u00b7 "
                  "\u8a72\u5f53\u306a\u3057\uff08\u653f\u7b56\u30fb\u60c5\u5831\u30ec\u30dd\u30fc\u30c8\uff09",
        "nav_all": "\u5168\u30ec\u30b3\u30fc\u30c9", "nav_types": "\u7a2e\u5225\u5225",
        "harm_yes": "\u3042\u308a", "harm_no": "\u306a\u3057", "harm_na": "\u8a72\u5f53\u306a\u3057",
    },
    "ko": {
        "date": "\ub0a0\uc9dc", "record": "\ub808\ucf54\ub4dc", "type": "\uc720\ud615",
        "severity": "\uc2ec\uac01\ub3c4", "confidence": "\uc2e0\ub8b0\ub3c4",
        "harm": "\uc2e4\uc81c \ud53c\ud574", "month_records": "\uc774\ubc88 \ub2ec \ub808\ucf54\ub4dc",
        "all_records": "\uc804\uccb4 \ub808\ucf54\ub4dc", "records": "\uac74", "by_severity": "\uc2ec\uac01\ub3c4\ubcc4",
        "index_total": "\ucd1d **{n}**\uac74, **{m}**\uac1c\uc6d4 \ubd84\ub7c9.",
        "index_head": ["\uc6d4", "\uac74\uc218", "critical", "high", "\uc2e4\uc81c \ud53c\ud574"],
        "index_total_row": "\ud569\uacc4",
        "legend": "\u2605 = `critical` \u00b7 \u26a0\ufe0f = \uc0ac\uc2e4 \ub610\ub294 \uadc0\uc18d\uc5d0 \ub17c\ub780 \uc788\uc74c \u00b7 "
                  "\uc2e4\uc81c \ud53c\ud574: \u2705 \ud53c\ud574\uc790 \ud655\uc778 / \u2014 \uc5c6\uc74c / \u00b7 "
                  "\ud574\ub2f9 \uc5c6\uc74c(\uc815\ucc45\u00b7\uc815\ubcf4 \ubcf4\uace0\uc11c)",
        "nav_all": "\uc804\uccb4 \ub808\ucf54\ub4dc", "nav_types": "\uc720\ud615\ubcc4",
        "harm_yes": "\uc608", "harm_no": "\uc544\ub2c8\uc624", "harm_na": "\ud574\ub2f9 \uc5c6\uc74c",
    },
    "de": {
        "date": "Datum", "record": "Eintrag", "type": "Typ", "severity": "Schweregrad",
        "confidence": "Verl\u00e4sslichkeit", "harm": "Echter Schaden", "month_records": "Eintr\u00e4ge dieses Monats",
        "all_records": "Alle Eintr\u00e4ge", "records": "Eintr\u00e4ge", "by_severity": "nach Schweregrad",
        "index_total": "**{n}** Eintr\u00e4ge \u00fcber **{m}** Monate.",
        "index_head": ["Monat", "Eintr\u00e4ge", "critical", "high", "mit echtem Schaden"],
        "index_total_row": "Gesamt",
        "legend": "\u2605 = `critical` \u00b7 \u26a0\ufe0f = umstrittene Fakten oder Zuordnung \u00b7 "
                  "Echter Schaden: \u2705 best\u00e4tigtes Opfer / \u2014 keiner / \u00b7 nicht zutreffend "
                  "(Politik- und Geheimdienstberichte)",
        "nav_all": "Alle Eintr\u00e4ge", "nav_types": "Nach Typ",
        "harm_yes": "Ja", "harm_no": "Nein", "harm_na": "nicht zutreffend",
    },
    "fr": {
        "date": "Date", "record": "Entr\u00e9e", "type": "Type", "severity": "Gravit\u00e9",
        "confidence": "Fiabilit\u00e9", "harm": "Pr\u00e9judice r\u00e9el", "month_records": "Entr\u00e9es du mois",
        "all_records": "Toutes les entr\u00e9es", "records": "entr\u00e9es", "by_severity": "par gravit\u00e9",
        "index_total": "**{n}** entr\u00e9es sur **{m}** mois.",
        "index_head": ["Mois", "Entr\u00e9es", "critical", "high", "pr\u00e9judice r\u00e9el"],
        "index_total_row": "Total",
        "legend": "\u2605 = `critical` \u00b7 \u26a0\ufe0f = faits ou attribution contest\u00e9s \u00b7 "
                  "Pr\u00e9judice r\u00e9el : \u2705 victime confirm\u00e9e / \u2014 aucun / \u00b7 non applicable "
                  "(rapports politiques et de renseignement)",
        "nav_all": "Toutes les entr\u00e9es", "nav_types": "Par type",
        "harm_yes": "Oui", "harm_no": "Non", "harm_na": "non applicable",
    },
    "es": {
        "date": "Fecha", "record": "Registro", "type": "Tipo", "severity": "Gravedad",
        "confidence": "Fiabilidad", "harm": "Da\u00f1o real", "month_records": "Registros del mes",
        "all_records": "Todos los registros", "records": "registros", "by_severity": "por gravedad",
        "index_total": "**{n}** registros en **{m}** meses.",
        "index_head": ["Mes", "Registros", "critical", "high", "con da\u00f1o real"],
        "index_total_row": "Total",
        "legend": "\u2605 = `critical` \u00b7 \u26a0\ufe0f = hechos o atribuci\u00f3n en disputa \u00b7 "
                  "Da\u00f1o real: \u2705 v\u00edctima confirmada / \u2014 ninguno / \u00b7 no aplicable "
                  "(informes pol\u00edticos y de inteligencia)",
        "nav_all": "Todos los registros", "nav_types": "Por tipo",
        "harm_yes": "S\u00ed", "harm_no": "No", "harm_na": "no aplicable",
    },
}
