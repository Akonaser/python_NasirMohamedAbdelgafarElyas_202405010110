# Test Report – Tutorials 1 to 5

**Tester:** Nasir Mohamed Abdelgafar Elyas (202405010110)
**Date:** 26 Nov 2026
**Method:** Black-box testing. Each program was run with the tutorial's sample input, boundary values, and invalid input (letters, empty input, negative numbers, out-of-range values, `nan` / `inf`). Week 7 was also tested with `pytest`.

## Summary

| Tutorial | Folder | Defects found | Status after fixes |
|---|---|:---:|---|
| 1 – Movie theater admission | `tutorial_1` | 1 | ✅ All tests pass |
| 2 – Student average calculator | `week_3` | 4 | ✅ All tests pass |
| 3 – Café bill calculator | `Tutorial_3` | 2 | ✅ All tests pass |
| 4 – FoodExpress (pytest) | `week_7` | 1 | ✅ 6/6 pytest pass |
| 5 – Food delivery receipt | `week_8` | 3 | ✅ All tests pass |

Every program still produces **exactly** the sample output from its tutorial sheet.

---

## Defects Found and Fixed

Severity: **High** = program crashes · **Medium** = wrong or invalid result accepted · **Low** = poor input handling

| ID | Tutorial | Input | Before fix | Expected | Severity | Fix |
|---|---|---|---|---|---|---|
| D1 | 2 | `abc` or empty as a mark | **Crash:** `ValueError` | Ask again | High | Added `get_mark()` with `try/except` |
| D2 | 2 | Mark `150` or `-20` | Accepted, average 76.67 | Reject (marks are 0–100) | Medium | `get_mark()` checks `0 <= mark <= 100` |
| D3 | 2 | Mark `nan` | Average `nan`, result FAIL | Reject | Medium | Range check also rejects `nan` |
| D4 | 2 | Continue? `yes` | Program ended | Continue | Low | Keep only the first letter: `.lower()[:1]` |
| D5 | 3 | Empty customer name | Receipt with a blank name | Ask again | Low | Loop until the name isn't empty |
| D6 | 3 | 0 coffee, 0 tea, 0 sandwich | Receipt for RM 0.00 | Reject the empty order | Low | Ask again if the total quantity is 0 |
| D7 | 4 | Price `nan` / `inf` | `Total Payment = RM nan` / `RM inf` | `"invalid price"` | Medium | `math.isfinite()` check in `calculate_total()` and 2 new test asserts |
| D8 | 5 | Price `inf` | `TOTAL : RM inf` | Reject | Medium | `math.isfinite()` check in `read_positive()` |
| D9 | 5 | Qty 1, price RM 0.30 | Lines show 0.30 + 0.01 but **TOTAL 0.32** | Lines add up to the total | Medium | Round the service charge to 2 d.p. before adding |
| D10 | 5 | Empty customer name | Receipt with a blank name | Ask again | Low | Loop until the name isn't empty |
| D11 | 1 | Age `500` | Accepted | Reject unrealistic ages | Low | Age must be 0–120 |

### D9 in detail (rounding)

The receipt printed each line rounded to 2 decimal places, but worked out the total from the **unrounded** values. So the printed lines didn't always add up to the printed total:

```
Subtotal : RM 0.30
Service Charge (5%) : RM 0.01      <- 0.015 shown as 0.01
Delivery Charge : RM 0.00
TOTAL    : RM 0.32                 <- but 0.30 + 0.01 = 0.31
```

An automated check over 10,000 combinations of quantity and price found **302** receipts that didn't add up. After rounding the service charge before adding it to the total, a check of **20,000** receipts (with and without delivery) found **0** mismatches.

---

## Tests That Passed First Time

| Tutorial | Test |
|---|---|
| 1 | Sample cases, boundary ages 12 and 13, age `abc` / `-5` / `12.5` rejected, generated truth table |
| 2 | Sample marks (70.00 PASS, 45.00 FAIL), boundary 50.00 = PASS, capital `Y` continues |
| 3 | Sheet sample (Bobby → **RM 67.50**), quantity `-1` / `abc` / `2.5` rejected |
| 4 | Totals 20, 30, 100, 10, invalid price, invalid quantity, letters rejected in `main.py` |
| 5 | Sheet sample (izzad → **RM 11.30**), invalid food / quantity / price / Y-N rejected, lower-case input accepted |

## Regression Results (after fixes)

| Tutorial | Result |
|---|---|
| 1 | Sample output unchanged · age `500` rejected |
| 2 | Empty, `abc`, `150` and `nan` rejected, then valid marks give 70.00 PASS · `yes` continues · 100/0/50 gives 50.00 PASS |
| 3 | Sample → RM 67.50 · empty name and empty order rejected |
| 4 | `pytest`: **6 passed** · `nan` / `inf` rejected in `main.py` |
| 5 | Sample → RM 11.30 · `inf` / `nan` rejected · 0 rounding mismatches across 20,000 receipts |

## Notes

- Interactive programs keep asking until they get valid input. When a test script sends only invalid input, the program waits for more and stops with `EOFError` once the script runs out of input. That is expected, not a crash in normal use.
- Week 3: the template line `quiz_1 = float(input(...))` became `quiz_1 = get_mark(...)`, because validation needs a `try/except` around the conversion. `get_mark()` still uses `float(input(...))` inside it.
