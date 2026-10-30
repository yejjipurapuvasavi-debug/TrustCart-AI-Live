from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT

CATALOGUE = ROOT / "catalogue.csv"
POLICY = ROOT / "policy.md"

DEV_QUESTIONS = ROOT / "questions_dev.csv"
DEV_TRUTH = ROOT / "questions_dev_truth.jsonl"
TEST_QUESTIONS = ROOT / "questions_test.csv"

REQUIRED_COLUMNS = {
    "product_id", "title", "brand", "category", "sub_category",
    "description", "attributes", "price_inr", "mrp_inr",
    "stock_status", "rating", "review_count",
}

VALID_STOCK = {"in_stock", "low_stock", "out_of_stock"}
