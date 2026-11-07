# Data Mining: Decision Tree and K-means

Two Python programs demonstrating classification and clustering.

- **decision_tree.py** — Uses ID3 to predict planet habitability from Size and Orbit using 800 observations. Displays entropy, information gain, predictions, and saves a drawing as `decision_tree.svg`.
- **k_means.py** — Performs three K-means iterations with K=2, starting with centroids 4 and 11. Displays distances, cluster assignments, and updated means.

**Requirements:** Python 3. No additional libraries needed.

**Run from the folder containing the files:**

```bash
python decision_tree.py
python k_means.py
```

**Results:** Big/Far and Small/Near planets are predicted habitable. After K-means iteration 3, the updated centroids are **7** and **25**.
