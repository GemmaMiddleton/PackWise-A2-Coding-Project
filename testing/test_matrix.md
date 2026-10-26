# PackWise Test Matrix

| Test | Duration | Day | Night | Occasions | Walking | Expected behaviour |
|---|---:|---|---|---|---|---|
| 1 | 3 | hot | warm | beach | low | Lightweight clothing, swimwear and sandals |
| 2 | 5 | mild | cool | dinner | moderate | Light layers, dinner clothing and comfortable sneakers |
| 3 | 10 | cold | cold | formal | high | Warm layers, coat, formal outfit and supportive footwear |
| 4 | 8 | warm | cool | beach, dinner, nightlife | high | Recommendations combined from all three occasions |
| 5 | banana | — | — | — | — | Reject trip duration and ask again |
| 6 | 0 | — | — | — | — | Reject trip duration and ask again |
| 7 | 5 | freezing-ish | — | — | — | Reject unsupported weather value |
| 8 | 14 | mild | cold | casual, formal | high | Larger quantities, evening warmth and walking footwear |
| 9 | 2 | hot | hot | casual | low | Minimal list without unnecessary layers |
| 10 | 21 | cold | cold | dinner, formal | high | Stress-test quantities and combined recommendation rules |

## Suggested Test Recording

For each test, record:

1. Expected behaviour
2. Actual behaviour
3. Problem identified, if any
4. Change made
5. Retest result

Add screenshots to `testing/screenshots/`.

## Screenshot Evidence

- [Multi-occasion test](screenshots/test_multi_occasion.png)
- [Cold/formal contrasting test](screenshots/test_cold_formal.png)
- [Invalid-input validation test](screenshots/test_invalid_input.png)
