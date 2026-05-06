import datetime as dt

DEALS = {"merger", "tender", "liquidation", "rights", "spin"}
REG_ALLOW = ("hsr", "hart-scott-rodino", "ftc", "doj", "department of justice", "cfius", "eu commission", "european commission", "samr", "state administration for market regulation")
REG_NONE = ("none required", "no regulatory approvals required", "not subject to regulatory clearance", "no governmental consents required")
FIN_ALLOW = ("debt commitment", "equity financing", "bridge loan", "senior secured", "committed financing", "no financing condition", "not subject to financing condition")
FIN_NONE = ("none required", "no financing condition", "not subject to financing condition")

def _has(value, phrases):
    text = value.lower() if isinstance(value, str) else ""
    return any(p in text for p in phrases)

def compute_confidence(extracted: dict) -> int:
    score = 20 if extracted.get("deal_type") in DEALS else 0
    cash = extracted.get("consideration_per_share_cash_or_null")
    stock = extracted.get("consideration_per_share_stock_ratio_or_null")
    if (isinstance(cash, (int, float)) and not isinstance(cash, bool)) or (isinstance(stock, str) and stock.strip()):
        score += 20
    try:
        filed = dt.date.fromisoformat(extracted.get("filed_date", ""))
        close = dt.date.fromisoformat(extracted.get("expected_close_date", ""))
        score += 20 if 0 <= (close - filed).days <= 366 else 0
    except Exception:
        pass
    if _has(extracted.get("regulatory_agency_named_or_none_explicit"), REG_ALLOW + REG_NONE):
        score += 20
    if _has(extracted.get("financing_source_named_or_none_explicit"), FIN_ALLOW + FIN_NONE):
        score += 20
    return score
